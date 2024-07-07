# Documentation
- Class name: ToBinaryMask
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

Tobinarymask node is designed to handle input masks by converting input masks into binary formats. It does so by applying threshold values to mask values, so that each pixel is classified as background or foreground. This is essential for tasks that require a clear distinction between different regions in the image, for example in image partitioning or target testing.

# Input types
## Required
- mask
    - The mask parameter is the key input for the Tobinary Mask node. It represents the initial mask from which the binary mask is derived. The quality and accuracy of the mask directly influences the output of the node and determines the accuracy of the split or target detection task.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- threshold
    - The threshold parameter is an optional input for determining the cut-off point for converting the mask value to a binary format. It plays an important role in the operation of the node, influencing the result by controlling the sensitivity of the binary classification. Higher thresholds lead to more conservative conversions, while lower thresholds lead to more radical conversions.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- binary_mask
    - The binary Mask output is the result of the Tobinary Mask node operation. It is the binary expression for the input mask, in which each pixel is assigned a value of 0 or 1, indicating the existence or absence of an interested feature. This output is essential for further analysis or processing of various computer visual applications.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ToBinaryMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'threshold': ('INT', {'default': 20, 'min': 1, 'max': 255})}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Operation'

    def doit(self, mask, threshold):
        mask = to_binary_mask(mask, threshold / 255.0)
        return (mask,)
```