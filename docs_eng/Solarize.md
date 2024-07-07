# Documentation
- Class name: Solarize
- Category: postprocessing/Color Adjustments
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

The node is designed to adjust the colour of the image by inverting a colour above a given threshold, providing a solarization effect that enhances visibility and contrast.

# Input types
## Required
- image
    - The image parameter is essential because it is the main input into the solarization process. It determines the source material that will be adjusted for colour.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- threshold
    - As the decision boundary of the solarization process, the threshold parameters determine which colours are reversed to enhance the contrast of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- solarized_image
    - The output is a solarized image that undergoes a color inversion process to increase its visual attractiveness and clarity.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class Solarize:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'solarize_image'
    CATEGORY = 'postprocessing/Color Adjustments'

    def solarize_image(self, image: torch.Tensor, threshold: float):
        solarized_image = torch.where(image > threshold, 1 - image, image)
        solarized_image = torch.clamp(solarized_image, 0, 1)
        return (solarized_image,)
```