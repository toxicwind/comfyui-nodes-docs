# Documentation
- Class name: ImageScaleToTotalPixels
- Category: image/upscaling
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ImageScaleToToralPixels node is designed to adjust the image to the number of total pixels specified. It provides a variety of magnification methods to ensure that image quality is maintained in the scaling process. The main objective of the node is to provide a simple and efficient way of zooming images for various applications, without affecting visual authenticity.

# Input types
## Required
- image
    - The image parameter is essential for the operation of the node because it is the input that the node will process. It is the raw data that will be magnified to the required total pixels, the quality of which directly influences the final output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- upscale_method
    - The upscale_method parameter determines how the image will be resized. It is essential to control the mass of the magnified image, allowing users to choose between different algorithms that may produce different results depending on the image content.
    - Comfy dtype: STRING
    - Python dtype: str
- megapixels
    - The megapixels parameter defines the target total pixel number for the magnifying image. It is a key factor in the scaling process and determines the final size of the image, i.e. its width and height.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- upscaled_image
    - The output upscaled_image represents the result of the scaling process. It is the main output of the node and contains images adjusted to the size of the total pixels, following the magnification method selected to maintain quality.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageScaleToTotalPixels:
    upscale_methods = ['nearest-exact', 'bilinear', 'area', 'bicubic', 'lanczos']
    crop_methods = ['disabled', 'center']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'upscale_method': (s.upscale_methods,), 'megapixels': ('FLOAT', {'default': 1.0, 'min': 0.01, 'max': 16.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'upscale'
    CATEGORY = 'image/upscaling'

    def upscale(self, image, upscale_method, megapixels):
        samples = image.movedim(-1, 1)
        total = int(megapixels * 1024 * 1024)
        scale_by = math.sqrt(total / (samples.shape[3] * samples.shape[2]))
        width = round(samples.shape[3] * scale_by)
        height = round(samples.shape[2] * scale_by)
        s = comfy.utils.common_upscale(samples, width, height, upscale_method, 'disabled')
        s = s.movedim(1, -1)
        return (s,)
```