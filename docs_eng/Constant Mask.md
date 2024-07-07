# Documentation
- Class name: ConstantMask
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

Constant Mask node is designed to generate a mask with a uniform value in its dimensions. It provides flexibility to define the mask in large hours, which can be clearly defined, or by copying the size of the existing image, thus ensuring consistency in the data pre-processing process.

# Input types
## Required
- value
    - The parameter'value' specifies the constant value for filling the mask. It plays a key role in determining the homogeneity of the output mask and influences the subsequent processing of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- explicit_height
    - Parameter 'explicit_height' sets the height of the mask when it is not copied from the image. It is important to define the vertical dimensions of the mask.
    - Comfy dtype: INT
    - Python dtype: int
- explicit_width
    - Parameter 'explicit_width' sets the width of the mask when it is not copied from the image. It is essential to define the horizontal dimensions of the mask.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- copy_image_size
    - The parameter'copy_image_size' allows the mask to use the size of the image provided, avoiding the need to specify the obvious size.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor

# Output types
- result
    - The'redult' output is the generation mask that fills the specified constant value. It is important for applications that require a uniform mask for further image operations.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ConstantMask:
    """
    Creates a mask filled with a constant value. If copy_image_size is provided, the explicit_height and explicit_width parameters are ignored and the size of the given images will be used instead.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'value': ('FLOAT', {'default': 0.0, 'min': -8.0, 'max': 8.0, 'step': 0.01}), 'explicit_height': ('INT', {'default': 0, 'min': 0, 'max': VERY_BIG_SIZE, 'step': 1}), 'explicit_width': ('INT', {'default': 0, 'min': 0, 'max': VERY_BIG_SIZE, 'step': 1})}, 'optional': {'copy_image_size': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'constant_mask'
    CATEGORY = 'Masquerade Nodes'

    def constant_mask(self, value, explicit_height, explicit_width, copy_image_size=None):
        height = explicit_height
        width = explicit_width
        if copy_image_size is not None:
            size = copy_image_size.size()
            height = size[1]
            width = size[2]
        elif explicit_height == 0 or explicit_width == 0:
            height = 16
            width = 16
        result = torch.zeros([1, height, width])
        result[:, :, :] = value
        return (result,)
```