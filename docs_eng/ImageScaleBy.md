# Documentation
- Class name: ImageScaleBy
- Category: image/upscaling
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ImageScaleBy node is designed to improve the resolution of the input image by applying a variety of up-sampling methods. It allows users to choose from a range of scaling techniques to achieve the desired results, focusing on improving the quality of the image as a whole without changing its original content.

# Input types
## Required
- image
    - The image parameter is essential for the operation of the node because it is the input that will be taken up. It directly affects the execution process and the quality of the image that will eventually be sampled.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- upscale_method
    - Upscale_method parameters determine the algorithm to be used for image sampling. They are essential for achieving the desired visual effects and performance.
    - Comfy dtype: STRING
    - Python dtype: str
- scale_by
    - The scale_by parameter defines the zoom factor of the image, which is the key determinant of the final image size. It significantly influences the execution and outcome of the node.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- upscaled_image
    - Upscaled_image output represents the outcome of the node process, showing the version of the input image after sampling using the selected method.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageScaleBy:
    upscale_methods = ['nearest-exact', 'bilinear', 'area', 'bicubic', 'lanczos']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'upscale_method': (s.upscale_methods,), 'scale_by': ('FLOAT', {'default': 1.0, 'min': 0.01, 'max': 8.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'upscale'
    CATEGORY = 'image/upscaling'

    def upscale(self, image, upscale_method, scale_by):
        samples = image.movedim(-1, 1)
        width = round(samples.shape[3] * scale_by)
        height = round(samples.shape[2] * scale_by)
        s = comfy.utils.common_upscale(samples, width, height, upscale_method, 'disabled')
        s = s.movedim(1, -1)
        return (s,)
```