# Documentation
- Class name: SubtractMask
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method at SubtractMask node performs subtraction operations for two mask images, providing the result mask that represents the difference between the input. It is intended to be the basic operation in the image processing workflow, in which certain areas of the image need to be removed or added.

# Input types
## Required
- mask1
    - The first mask for subtraction operations. It plays a crucial role in determining the result mask because it defines the initial state of the mask from which the second mask will be subtracted.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- mask2
    - The second mask to be subtracted from the first mask. Its importance is to change the content of the first mask so as to produce the ultimate mask that reflects the subtraction effect.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- mask
    - The output mask is the result of a subtraction operation between two input maskes. It indicates the remaining area after the first mask is subtracted from the second mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class SubtractMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask1': ('MASK',), 'mask2': ('MASK',)}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Operation'

    def doit(self, mask1, mask2):
        mask = subtract_masks(mask1, mask2)
        return (mask,)
```