# Documentation
- Class name: AddMask
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

AddMask node is designed to perform pixel-by-pixel additions to two binary masks. It is used to combine mask images in a way that preserves the integrity of the original mask while creating a new mask that represents their union.

# Input types
## Required
- mask1
    - The first mask to be added. It is a key component because it helps to create a cover of results and determines the area that will be included in the final combination mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- mask2
    - The second mask to be added. Like the first mask, it plays an important role in defining the output mask, where contributions are included in the combination result.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- mask
    - The output is a new binary mask, which is added to the input mask. It indicates a combination of two input maskes, indicating an overlap of two mask areas.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class AddMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask1': ('MASK',), 'mask2': ('MASK',)}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Operation'

    def doit(self, mask1, mask2):
        mask = add_masks(mask1, mask2)
        return (mask,)
```