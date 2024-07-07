# Documentation
- Class name: color_drop
- Category: Image Processing
- Output node: False
- Repo Ref: https://github.com/jags111/ComfyUI_Jags_VectorMagic

The node class handles image data by applying the colour discard effect to enhance the visual features of the input image through the flat colour spectra.

# Input types
## Required
- images
    - Entering images is essential for the operation of nodes as the basis for the colour discarding process.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
## Optional
- number_of_colors
    - This parameter affects the particle size of the colour pressure level effect, and the higher values lead to a more visible colour belt in the output.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- Image
    - The output is an image that uses the colour discard effect and shows the expected visual enhancement effect.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class color_drop:
    """
    This node provides a simple interface to apply PixelSort blur to the output image.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        """
        Input Types
        """
        return {'required': {'images': ('IMAGE',)}, 'optional': {'number_of_colors': ('INT', {'default': 2, 'min': 1, 'max': 4000, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('Image',)
    FUNCTION = 'flatten'
```