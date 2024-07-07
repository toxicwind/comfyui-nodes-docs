# Documentation
- Class name: SegsBitwiseAndMaskForEach
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The `doit' method at SegsBitwise And MaskForEach node performs position and operation for each split mask and the given mask, thereby generating a detailed set of partition maskes. This operation is essential to filter out areas that are not needed during the partition process and to ensure that only interested areas are retained.

# Input types
## Required
- segs
    - The'segs' parameter represents the group of split objects to be processed by the node. It is essential for the operation of the node, as it determines the input data that will be performed by location and operation of the mask.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
- masks
    - The'masks' parameter is a volume that contains a mask to be applied to each partition. It plays an important role in the function of the node by defining the area to be included or excluded in the final partition output.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- output
    - The output of the 'doit' method is a group of elements containing the original split and a detailed list of split objects, each with a mask updated by bit and operation.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[SEG, List[SEG]]

# Usage tips
- Infra type: CPU

# Source code
```
class SegsBitwiseAndMaskForEach:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',), 'masks': ('MASK',)}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Operation'

    def doit(self, segs, masks):
        return (core.apply_mask_to_each_seg(segs, masks),)
```