# Documentation
- Class name: FeatherMask
- Category: mask
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The Feither Mask node is designed to smoothly mix the edges of the given mask with the surrounding area. It does so by gradually adjusting the non-transparent pixels of the mask, thus creating a soft transition at the masked boundary, which is usually used in image processing and editing. This node is particularly useful when there is no visual desire to have a hard edge between the mask and the background.

# Input types
## Required
- mask
    - The `mask' parameter is a binary mass that defines the area of interest in the image. It is essential for the node, because it determines which parts of the image will be feathered. The dimension of the mask and its binary properties directly influence the process and final output.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
## Optional
- left
    - The `left' parameter specifies the number of pixels that start with the plume effect on the left side of the mask. It plays an important role in determining the width of the plume on the left side of the mask, thus influencing the overall visual result.
    - Comfy dtype: int
    - Python dtype: int
- top
    - The `top' parameter sets the number of pixels to be melted from the top edge of the mask. It is essential to control the height of the plume at the top of the mask, affecting the output of nodes.
    - Comfy dtype: int
    - Python dtype: int
- right
    - The 'right'parameter sets the number of pixels that will be feathered from the right side of the mask. It is a key factor in creating the width of the area on the right side of the mask, affecting the execution and final appearance of the node.
    - Comfy dtype: int
    - Python dtype: int
- bottom
    - The `bottom' parameter indicates the number of pixels to be gleaned from the bottom edge of the mask. It is essential to determine the height of the plume at the bottom of the mask, which significantly influences the outcome of the node.
    - Comfy dtype: int
    - Python dtype: int

# Output types
- feathered_mask
    - The 'feathered_mask' output is a volume that represents the original mask and carries a plume edge. It is the main result of node operations and provides a visual smooth transition between the masked and unshaded areas in the image.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class FeatherMask:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mask': ('MASK',), 'left': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1}), 'top': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1}), 'right': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1}), 'bottom': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1})}}
    CATEGORY = 'mask'
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'feather'

    def feather(self, mask, left, top, right, bottom):
        output = mask.reshape((-1, mask.shape[-2], mask.shape[-1])).clone()
        left = min(left, output.shape[-1])
        right = min(right, output.shape[-1])
        top = min(top, output.shape[-2])
        bottom = min(bottom, output.shape[-2])
        for x in range(left):
            feather_rate = (x + 1.0) / left
            output[:, :, x] *= feather_rate
        for x in range(right):
            feather_rate = (x + 1) / right
            output[:, :, -x] *= feather_rate
        for y in range(top):
            feather_rate = (y + 1) / top
            output[:, y, :] *= feather_rate
        for y in range(bottom):
            feather_rate = (y + 1) / bottom
            output[:, -y, :] *= feather_rate
        return (output,)
```