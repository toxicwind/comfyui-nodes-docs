# Documentation
- Class name: WAS_Image_Direct_Occlusion
- Category: WAS Suite/Image/Filter
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Direct_Occlusion node is designed to process images and depth maps in order to create direct shielding effects that enhance the visual authenticity of images by simulating the interaction of light with objects. It identifies the light source and uses the shield on the basis of depth and colour differences to generate images with a more stereo look.

# Input types
## Required
- images
    - Entering the image parameter is essential for the operation of the node, as it is the main data source that generates the masking effect. It directly affects the end result by determining the visual content that will be processed to create the masking content.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- depth_images
    - The depth_images parameter provides the depth information necessary to calculate the mask effect. It is essential to determine how the light interacts according to the depth of the different parts of the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- strength
    - Strength parameters control the strength of the shielding effect. It is important because it allows users to fine-tune the visual effects of the final output by adjusting the level of shielding applied to the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- radius
    - The Radius parameter defines the impact area of each pixel when calculating the mask. It is important because it determines the range of shielding effects around each pixel and affects the overall texture and detail of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- specular_threshold
    - The specular_threshold parameter is used to identify the brightest areas in the image, which help to identify the light source. It plays a key role in determining which parts of the image will be considered as sources of light in the screen calculation.
    - Comfy dtype: INT
    - Python dtype: int
- colored_occlusion
    - The color_occlusion parameter determines whether to apply the masking effect to colour or greyscale effects. This selection affects the visual style that allows for more subtle or visible visual changes.
    - Comfy dtype: COMBO[True, False]
    - Python dtype: bool

# Output types
- composited_images
    - Composited_images output parameters represent the final image of the application of the direct masking effect. It is important because it is the main result of node processing and is used for further visualization or analysis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- ssdo_images
    - The ssdo_images output parameter provides a pre-synthesis image with a mask effect. It is useful for separate checking of the mask effects and for debugging purposes.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- ssdo_image_masks
    - The ssdo_image_masks output parameters include masks corresponding to the masked area in the image. These masks can be used for further image processing or to isolate the specific area of the shield effect.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- light_source_image_masks
    - Light_source_image_masks output parameters include masks that identify areas considered to be light sources in the image. These masks are essential to understand which parts of the image contribute to shielding effects.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class WAS_Image_Direct_Occlusion:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'depth_images': ('IMAGE',), 'strength': ('FLOAT', {'min': 0.0, 'max': 5.0, 'default': 1.0, 'step': 0.01}), 'radius': ('FLOAT', {'min': 0.01, 'max': 1024, 'default': 30, 'step': 0.01}), 'specular_threshold': ('INT', {'min': 0, 'max': 255, 'default': 128, 'step': 1}), 'colored_occlusion': (['True', 'False'],)}}
    RETURN_TYPES = ('IMAGE', 'IMAGE', 'IMAGE', 'IMAGE')
    RETURN_NAMES = ('composited_images', 'ssdo_images', 'ssdo_image_masks', 'light_source_image_masks')
    FUNCTION = 'direct_occlusion'
    CATEGORY = 'WAS Suite/Image/Filter'

    def direct_occlusion(self, images, depth_images, strength, radius, specular_threshold, colored_occlusion):
        composited = []
        occlusions = []
        occlusion_masks = []
        light_sources = []
        for (i, image) in enumerate(images):
            cstr(f'Processing SSDO image {i + 1}/{len(images)} ...').msg.print()
            (composited_image, occlusion_image, occlusion_mask, light_source) = self.create_direct_occlusion(tensor2pil(image), tensor2pil(depth_images[i if len(depth_images) >= i else -1]), strength=strength, radius=radius, threshold=specular_threshold, colored=True)
            composited.append(pil2tensor(composited_image))
            occlusions.append(pil2tensor(occlusion_image))
            occlusion_masks.append(pil2tensor(occlusion_mask))
            light_sources.append(pil2tensor(light_source))
        composited = torch.cat(composited, dim=0)
        occlusions = torch.cat(occlusions, dim=0)
        occlusion_masks = torch.cat(occlusion_masks, dim=0)
        light_sources = torch.cat(light_sources, dim=0)
        return (composited, occlusions, occlusion_masks, light_sources)

    def find_light_source(self, rgb_normalized, threshold):
        from skimage.measure import regionprops
        from skimage import measure
        rgb_uint8 = (rgb_normalized * 255).astype(np.uint8)
        rgb_to_grey = Image.fromarray(rgb_uint8, mode='RGB')
        dominant = self.dominant_region(rgb_to_grey, threshold)
        grayscale_image = np.array(dominant.convert('L'), dtype=np.float32) / 255.0
        regions = measure.label(grayscale_image > 0)
        if np.max(regions) > 0:
            region_sums = measure.regionprops(regions, intensity_image=grayscale_image)
            brightest_region = max(region_sums, key=lambda r: r.mean_intensity)
            (light_y, light_x) = brightest_region.centroid
            light_mask = (regions == brightest_region.label).astype(np.uint8)
            light_mask_cluster = light_mask
        else:
            (light_x, light_y) = (np.nan, np.nan)
            light_mask_cluster = np.zeros_like(dominant, dtype=np.uint8)
        return (light_mask_cluster, light_x, light_y)

    def dominant_region(self, image, threshold=128):
        from scipy.ndimage import label
        image = ImageOps.invert(image.convert('L'))
        binary_image = image.point(lambda x: 255 if x > threshold else 0, mode='1')
        (l, n) = label(np.array(binary_image))
        sizes = np.bincount(l.flatten())
        dominant = 0
        try:
            dominant = np.argmax(sizes[1:]) + 1
        except ValueError:
            pass
        dominant_region_mask = (l == dominant).astype(np.uint8) * 255
        result = Image.fromarray(dominant_region_mask, mode='L')
        return result.convert('RGB')

    def create_direct_occlusion(self, rgb_image, depth_image, strength=1.0, radius=10, threshold=200, colored=False):
        rgb_normalized = np.array(rgb_image, dtype=np.float32) / 255.0
        depth_normalized = np.array(depth_image, dtype=np.float32) / 255.0
        (height, width, _) = rgb_normalized.shape
        (light_mask, light_x, light_y) = self.find_light_source(rgb_normalized, threshold)
        occlusion_array = calculate_direct_occlusion_factor(rgb_normalized, depth_normalized, height, width, radius)
        occlusion_scaled = ((occlusion_array - np.min(occlusion_array)) / (np.max(occlusion_array) - np.min(occlusion_array)) * 255).astype(np.uint8)
        occlusion_image = Image.fromarray(occlusion_scaled, mode='L')
        occlusion_image = occlusion_image.filter(ImageFilter.GaussianBlur(radius=0.5))
        occlusion_image = occlusion_image.filter(ImageFilter.SMOOTH_MORE)
        if colored:
            occlusion_result = Image.composite(Image.new('RGB', rgb_image.size, (0, 0, 0)), rgb_image, occlusion_image)
            occlusion_result = ImageOps.autocontrast(occlusion_result, cutoff=(0, strength))
        else:
            occlusion_result = Image.blend(occlusion_image, occlusion_image, strength)
        light_image = ImageOps.invert(Image.fromarray(light_mask * 255, mode='L'))
        direct_occlusion_image = ImageChops.screen(rgb_image, occlusion_result.convert('RGB'))
        return (direct_occlusion_image, occlusion_result, occlusion_image, light_image)
```