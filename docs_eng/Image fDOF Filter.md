# Documentation
- Class name: WAS_Image_fDOF
- Category: WAS Suite/Image/Filter
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_fDOF node fdof_composite function is designed to apply deep view effects to images, enhancing visual focus on subjects by blurring the background. It achieves this effect by combining different image-processing techniques that apply to different models, such as simulation, Gausss or box blurry, and customizes through parameters such as radius and sample numbers.

# Input types
## Required
- image
    - The image parameter is essential for the operation of the node, because it is an input image that will apply the deep-view effect. It significantly influences the final result of the node implementation by identifying the visual content to be processed.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- depth
    - The depth parameters provide a depth map to determine the areas in the image that should be focused or blurred. It plays a key role in the implementation of the nodes by guiding the application of the deep effect.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- mode
    - Model parameters determine the type of blurry that is to be applied to the image. It is important because it determines the style of the deep effect and provides options such as simulation, Gaussian or box blurry.
    - Comfy dtype: COMBO['mock', 'gaussian', 'box']
    - Python dtype: str
- radius
    - The radius parameter defines the scope of the blurry effect, which is important for controlling the intensity of the view depth. It directly affects the appearance of the blurred area in the output image.
    - Comfy dtype: INT
    - Python dtype: int
- samples
    - The sample parameter specifies the number of fuzzy effect applications, which increases the fuzzy smoothness. It influences the execution of nodes by determining the level of detail in the final synthetic image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output_image
    - The output image parameter represents the final processing of the image using the deep effect. It is important because it is a direct result of node operations and reflects the creative intent of the filters applied.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_fDOF:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'depth': ('IMAGE',), 'mode': (['mock', 'gaussian', 'box'],), 'radius': ('INT', {'default': 8, 'min': 1, 'max': 128, 'step': 1}), 'samples': ('INT', {'default': 1, 'min': 1, 'max': 3, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'fdof_composite'
    CATEGORY = 'WAS Suite/Image/Filter'

    def fdof_composite(self, image, depth, radius, samples, mode):
        import cv2 as cv
        tensor_images = []
        for i in range(len(image)):
            if i <= len(image):
                img = tensor2pil(image[i])
            else:
                img = tensor2pil(image[-1])
            if i <= len(depth):
                dpth = tensor2pil(depth[i])
            else:
                dpth = tensor2pil(depth[-1])
            tensor_images.append(pil2tensor(self.portraitBlur(img, dpth, radius, samples, mode)))
        tensor_images = torch.cat(tensor_images, dim=0)
        return (tensor_images,)

    def portraitBlur(self, img, mask, radius, samples, mode='mock'):
        mask = mask.resize(img.size).convert('L')
        bimg: Optional[Image.Image] = None
        if mode == 'mock':
            bimg = medianFilter(img, radius, radius * 1500, 75)
        elif mode == 'gaussian':
            bimg = img.filter(ImageFilter.GaussianBlur(radius=radius))
        elif mode == 'box':
            bimg = img.filter(ImageFilter.BoxBlur(radius))
        else:
            return
        bimg.convert(img.mode)
        rimg: Optional[Image.Image] = None
        if samples > 1:
            for i in range(samples):
                if not rimg:
                    rimg = Image.composite(img, bimg, mask)
                else:
                    rimg = Image.composite(rimg, bimg, mask)
        else:
            rimg = Image.composite(img, bimg, mask).convert('RGB')
        return rimg
```