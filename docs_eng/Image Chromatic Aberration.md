# Documentation
- Class name: WAS_Image_Chromatic_Aberration
- Category: WAS Suite/Image/Filter
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Chromatic_Aberration node is designed to apply color differential effects to input images, simulations of optical phenomena that blur the image’s edge because the lens fails to focus all colours at the same point. Such effects can add a unique visual style to the image, which is usually used in photography and films to create specific aesthetic effects.

# Input types
## Required
- image
    - The image parameter is the core input of the node, representing the image that will apply the colour differential effect. The quality and properties of the image directly influence the final output and determine the range and appearance of the color differential.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- red_offset
    - The red_offset parameter allows adjustment of red channel deviations to create colour differential effects by moving the red fraction of the image. It is an important part of achieving the required visual loss.
    - Comfy dtype: INT
    - Python dtype: int
- green_offset
    - Green_offset parameters are used to fine-tune the contribution of green corridors to colour differentials. By adjusting this value, nodes control the blurring of greens in images.
    - Comfy dtype: INT
    - Python dtype: int
- blue_offset
    - The blue_offset parameter determines the shift of the blue channel in the colour differential. This is essential to controlling the spread of the blue in the false image.
    - Comfy dtype: INT
    - Python dtype: int
- intensity
    - Strength parameters control the intensity of colour differential effects. Higher values produce more obvious effects, while lower values produce more subtle distortions.
    - Comfy dtype: FLOAT
    - Python dtype: float
- fade_radius
    - The file_radius parameter defines the fade effect radius on the edge of the image. It helps to create a smooth transition between color differentials and unreal image centres.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The output image is the result of the application of the colour differential effect to the input image. It reflects the adjusted deflection and intensity and provides a creative version of the original image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Chromatic_Aberration:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'red_offset': ('INT', {'default': 2, 'min': -255, 'max': 255, 'step': 1}), 'green_offset': ('INT', {'default': -1, 'min': -255, 'max': 255, 'step': 1}), 'blue_offset': ('INT', {'default': 1, 'min': -255, 'max': 255, 'step': 1}), 'intensity': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'fade_radius': ('INT', {'default': 12, 'min': 0, 'max': 1024, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_chromatic_aberration'
    CATEGORY = 'WAS Suite/Image/Filter'

    def image_chromatic_aberration(self, image, red_offset=4, green_offset=2, blue_offset=0, intensity=1, fade_radius=12):
        return (pil2tensor(self.apply_chromatic_aberration(tensor2pil(image), red_offset, green_offset, blue_offset, intensity, fade_radius)),)

    def apply_chromatic_aberration(self, img, r_offset, g_offset, b_offset, intensity, fade_radius):

        def lingrad(size, direction, white_ratio):
            image = Image.new('RGB', size)
            draw = ImageDraw.Draw(image)
            if direction == 'vertical':
                black_end = size[1] - white_ratio
                range_start = 0
                range_end = size[1]
                range_step = 1
                for y in range(range_start, range_end, range_step):
                    color_ratio = y / size[1]
                    if y <= black_end:
                        color = (0, 0, 0)
                    else:
                        color_value = int((y - black_end) / (size[1] - black_end) * 255)
                        color = (color_value, color_value, color_value)
                    draw.line([(0, y), (size[0], y)], fill=color)
            elif direction == 'horizontal':
                black_end = size[0] - white_ratio
                range_start = 0
                range_end = size[0]
                range_step = 1
                for x in range(range_start, range_end, range_step):
                    color_ratio = x / size[0]
                    if x <= black_end:
                        color = (0, 0, 0)
                    else:
                        color_value = int((x - black_end) / (size[0] - black_end) * 255)
                        color = (color_value, color_value, color_value)
                    draw.line([(x, 0), (x, size[1])], fill=color)
            return image.convert('L')

        def create_fade_mask(size, fade_radius):
            mask = Image.new('L', size, 255)
            left = ImageOps.invert(lingrad(size, 'horizontal', int(fade_radius * 2)))
            right = left.copy().transpose(Image.FLIP_LEFT_RIGHT)
            top = ImageOps.invert(lingrad(size, 'vertical', int(fade_radius * 2)))
            bottom = top.copy().transpose(Image.FLIP_TOP_BOTTOM)
            mask = ImageChops.multiply(mask, left)
            mask = ImageChops.multiply(mask, right)
            mask = ImageChops.multiply(mask, top)
            mask = ImageChops.multiply(mask, bottom)
            mask = ImageChops.multiply(mask, mask)
            return mask
        (r, g, b) = img.split()
        r_offset_img = ImageChops.offset(r, r_offset, 0)
        g_offset_img = ImageChops.offset(g, 0, g_offset)
        b_offset_img = ImageChops.offset(b, 0, b_offset)
        merged = Image.merge('RGB', (r_offset_img, g_offset_img, b_offset_img))
        fade_mask = create_fade_mask(img.size, fade_radius)
        result = Image.composite(merged, img, fade_mask).convert('RGB')
        return result
```