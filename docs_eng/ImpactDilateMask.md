# Documentation
- Class name: DilateMask
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The Dilate Mask node is designed to implement a morphological expansion of the binary mask and expand the boundary of the object for which the mask is intended. It is particularly appropriate for the task of severing the mask by increasing the size of the segment, which is very useful for object detection and fragmentation.

# Input types
## Required
- mask
    - The `mask' parameter is a binary mask that defines the area of interest in the image. It is essential for the process of expansion, because it determines which areas will be expanded. The quality of the inflation outcome depends largely on the accuracy of the input mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- dilation
    - The `dilation' parameter specifies the inflation to be applied to the mask. Positive values lead to an expansion of the margin of the mask, and negative values lead to a contraction. This parameter is essential for controlling the extent of the inflation effect.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- dilated_mask
    - `dilated_mask' output is the result of the application of the expansion operation to the input mask. It is a binary mask in which the foreground object has been expanded according to the specified inflation factor.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class DilateMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'dilation': ('INT', {'default': 10, 'min': -512, 'max': 512, 'step': 1})}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, mask, dilation):
        mask = core.dilate_mask(mask.numpy(), dilation)
        mask = torch.from_numpy(mask)
        mask = utils.make_3d_mask(mask)
        return (mask,)
```