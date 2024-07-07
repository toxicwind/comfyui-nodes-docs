# Documentation
- Class name: MaskListToMaskBatch
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The MaskListToMaskBatch node is designed to integrate a series of mask images into a single batch load. It handles each mask in the list, ensuring that they are in a 3D format suitable for batch processing, and effectively handles individual and multiple masks. The node plays a key role in preparing the batch input data needed for downstream machine learning models.

# Input types
## Required
- mask
    - The'mask'parameter is a list of masked images processed by nodes. It is essential for the operation of nodes, as it directly affects the batch volume of output. Nodees handle this list by converting each mask to a 3D format (if required) and then grouping them into a single load for batch processing.
    - Comfy dtype: MASK
    - Python dtype: List[torch.Tensor]

# Output types
- mask_batch
    - The output of the MaskListToMaskBatch node is a single load representing a masked batch. This load is formatted to be compatible with the machine learning model for expected bulk input data and is important for the subsequent stages of model training or reasoning.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class MaskListToMaskBatch:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',)}}
    INPUT_IS_LIST = True
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Operation'

    def doit(self, mask):
        if len(mask) == 1:
            mask = make_3d_mask(mask[0])
            return (mask,)
        elif len(mask) > 1:
            mask1 = make_3d_mask(mask[0])
            for mask2 in mask[1:]:
                mask2 = make_3d_mask(mask2)
                if mask1.shape[1:] != mask2.shape[1:]:
                    mask2 = comfy.utils.common_upscale(mask2.movedim(-1, 1), mask1.shape[2], mask1.shape[1], 'lanczos', 'center').movedim(1, -1)
                mask1 = torch.cat((mask1, mask2), dim=0)
            return (mask1,)
        else:
            empty_mask = torch.zeros((1, 64, 64), dtype=torch.float32, device='cpu').unsqueeze(0)
            return (empty_mask,)
```