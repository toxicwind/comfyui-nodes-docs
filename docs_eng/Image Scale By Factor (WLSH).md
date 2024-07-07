# Documentation
- Class name: WLSH_Image_Scale_By_Factor
- Category: WLSH Nodes/upscaling
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The WLSH_Image_Scale_By_Actor node method 'upscale' is designed to increase the size of the input image by specifying a factor. It supports a variety of magnification methods to maintain or improve the quality of the image during the magnification process. This node plays a key role in the image processing workflow that needs to magnify the image.

# Input types
## Required
- original
    - The 'origanal'parameter is the input image that needs to be scaled up. It is the core of the operation, because all operations of the node revolve around this image. The quality and content of the original image directly influences the output after the scaling.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- upscale_method
    - The 'upscale_method'parameter determines the algorithm to be used for scaling the image. It is essential for controlling the quality and properties of magnifying the image. Different methods can produce different results, and their selection can significantly affect the final appearance.
    - Comfy dtype: COMBO['nearest-exact', 'bilinear', 'area']
    - Python dtype: str
- factor
    - The 'factor'parameter defines the scale of the original image size multiplied by it. It is a key parameter, because it determines the ultimate size of the image to be magnified. The selection of factors will have a direct impact on the level of detail and overall dimensions.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- upscaled_image
    - The 'upscaled_image'output is the result of the magnification process, reflecting input images scaled up by the specified factor. It is important because it represents the direct result of node operations and is used for further processing or presentation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class WLSH_Image_Scale_By_Factor:
    upscale_methods = ['nearest-exact', 'bilinear', 'area']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'original': ('IMAGE',), 'upscale_method': (s.upscale_methods,), 'factor': ('FLOAT', {'default': 2.0, 'min': 0.1, 'max': 8.0, 'step': 0.1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'upscale'
    CATEGORY = 'WLSH Nodes/upscaling'

    def upscale(self, original, upscale_method, factor):
        old_width = original.shape[2]
        old_height = original.shape[1]
        new_width = int(old_width * factor)
        new_height = int(old_height * factor)
        print('Processing image with shape: ', old_width, 'x', old_height, 'to ', new_width, 'x', new_height)
        samples = original.movedim(-1, 1)
        s = comfy.utils.common_upscale(samples, new_width, new_height, upscale_method, crop='disabled')
        s = s.movedim(1, -1)
        return (s,)
```