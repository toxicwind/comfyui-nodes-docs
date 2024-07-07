# Documentation
- Class name: Dissolve
- Category: postprocessing/Blends
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

Dissolve node is designed to mix two images seamlessly according to the specified solvency factor. It creates a smooth transition between two images by generating and using the point array pattern to determine the contribution of each image to the final output.

# Input types
## Required
- image1
    - Image1 is the first input image that you want to mix with the second image. It plays a vital role in the initial combination of the image that eventually mixes.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image2
    - Image2 is the second input image that you want to mix with the first image. The visual element will be combined with the element of Image1 to create the final output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- dissolve_factor
    - The solubility factor is a floating point value used to determine the ratio between image1 and image2. It affects the visibility of each image in the end result, showing only image1 at 0.0, and only image2 at 1.0.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- dissolve_image
    - The output of Dissolve node is a single image representing the result of using the specified solvency factor mix 1 and 2.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class Dissolve:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image1': ('IMAGE',), 'image2': ('IMAGE',), 'dissolve_factor': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'dissolve_images'
    CATEGORY = 'postprocessing/Blends'

    def dissolve_images(self, image1: torch.Tensor, image2: torch.Tensor, dissolve_factor: float):
        dither_pattern = torch.rand_like(image1)
        mask = (dither_pattern < dissolve_factor).float()
        dissolved_image = image1 * mask + image2 * (1 - mask)
        dissolved_image = torch.clamp(dissolved_image, 0, 1)
        return (dissolved_image,)
```