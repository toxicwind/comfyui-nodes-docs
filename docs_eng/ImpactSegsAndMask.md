# Documentation
- Class name: SegsBitwiseAndMask
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The `doit' method at SegsBitwise And Mask node provides for partitioning (segs) and masking by bits and operations, generating refined areas that contain only partition and mask overlaps. This operation is essential for applications that require precise space filtering, such as object testing in a medical image or in a specific area of the image.

# Input types
## Required
- segs
    - The'segs' parameter is the grouping of split objects that the node will process. It is essential to define the initial split that will be combined by bit with the operation and the mask. The quality and accuracy of the'segs' directly affect the results of the node operation.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
- mask
    - The'mask' parameter is a binary mask that filters the partitions provided by'segs'. It is a key component because it determines the partition areas that will be retained by bit and operation. The mask should be precisely defined to ensure the required filtering effect.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- result
    - The'redult' output is a condensed grouping that is filtered by bit and operation with the provided mask. It represents the final output of the node and contains only the partition area that meets the mask criteria.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[List[SEG], List[SEG]]

# Usage tips
- Infra type: CPU

# Source code
```
class SegsBitwiseAndMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',), 'mask': ('MASK',)}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Operation'

    def doit(self, segs, mask):
        return (core.segs_bitwise_and_mask(segs, mask),)
```