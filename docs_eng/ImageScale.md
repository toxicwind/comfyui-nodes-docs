# Documentation
- Class name: ImageScale
- Category: image/upscaling
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ImageScale node is designed to increase the resolution of the digital image by various up-sampling methods. It provides a simple interface for users to zoom in the image by specifying a new size or maintaining a horizontal ratio. The node supports a range of upsampling algorithms that apply to different examples to achieve high-quality image magnification.

# Input types
## Required
- image
    - The image parameter is the input number image that the node will process. This is the basis, because all operation of the node revolves around increasing the resolution of the image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- upscale_method
    - The upperscale_method parameter determines the algorithm to be used to magnify the image. It is vital because it directly affects the quality and style of sampling.
    - Comfy dtype: STRING
    - Python dtype: str
- crop
    - The crop parameter defines whether and how to edit the image after sampling. It is essential to control the image's final construction.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- width
    - The width parameter specifies the new width of the zoom image. It is important because it determines one of the dimensions of the image that will be resized.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The header parameter specifies a new height for scaling the image. Its importance is to control the vertical dimensions of the output image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- upscaled_image
    - Upscaled_image is the output of the node, which represents the image that is magnified using the specified method. It is the result of node processing and the direct result of the sampling operation.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageScale:
    upscale_methods = ['nearest-exact', 'bilinear', 'area', 'bicubic', 'lanczos']
    crop_methods = ['disabled', 'center']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'upscale_method': (s.upscale_methods,), 'width': ('INT', {'default': 512, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1}), 'height': ('INT', {'default': 512, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1}), 'crop': (s.crop_methods,)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'upscale'
    CATEGORY = 'image/upscaling'

    def upscale(self, image, upscale_method, width, height, crop):
        if width == 0 and height == 0:
            s = image
        else:
            samples = image.movedim(-1, 1)
            if width == 0:
                width = max(1, round(samples.shape[3] * height / samples.shape[2]))
            elif height == 0:
                height = max(1, round(samples.shape[2] * width / samples.shape[3]))
            s = comfy.utils.common_upscale(samples, width, height, upscale_method, crop)
            s = s.movedim(1, -1)
        return (s,)
```