# Documentation
- Class name: Vignette
- Category: postprocessing/Effects
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

The node applies the dizziness effect to the image, increasing the visual focus on the centre by gradually diluting the edges. It adjusts the intensity of the dizziness to the parameters defined by the user, allowing for fine control of aesthetic effects.

# Input types
## Required
- image
    - The image parameter is necessary because it is the main input to the node operation. It determines the object that will be applied to the dizziness effect, thus directly influencing the output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- a
    - The parameter 'a' controls the strength of the dizziness effect. It is essential for customizing aesthetic results according to user preferences, allowing different visual styles from subtle to dramatic.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output_image
    - The output image is the result of the application of the dizziness effect. It reflects the input image with the applied aesthetic adjustment and represents the main output of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class Vignette:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'a': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 10.0, 'step': 1.0})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'apply_vignette'
    CATEGORY = 'postprocessing/Effects'

    def apply_vignette(self, image: torch.Tensor, vignette: float):
        if vignette == 0:
            return (image,)
        (height, width, _) = image.shape[-3:]
        x = torch.linspace(-1, 1, width, device=image.device)
        y = torch.linspace(-1, 1, height, device=image.device)
        (X, Y) = torch.meshgrid(x, y, indexing='ij')
        radius = torch.sqrt(X ** 2 + Y ** 2)
        mapped_vignette_strength = 1.8 - (vignette - 1) * 0.1
        vignette = 1 - torch.clamp(radius / mapped_vignette_strength, 0, 1)
        vignette = vignette[..., None]
        vignette_image = torch.clamp(image * vignette, 0, 1)
        return (vignette_image,)
```