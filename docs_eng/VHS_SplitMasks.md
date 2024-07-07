# Documentation
- Class name: SplitMasks
- Category: Video Helper Suite 🎥🅥🅗🅢/mask
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

SplitMaks node is intended to divide the given mask load into two different groups based on the specified index. It is used to divide the input data and allow for individual analysis or processing of each group. This node is essential for applications that require video masking, such as object tracking or split tasks.

# Input types
## Required
- mask
    - The parameter'mask' is the main input for the Splitmasks node, representing the video mask that is to be separated. It is vital because it determines the data that will be parted. The structure and content of the mask directly influence the operation of the node and the partition results.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- split_index
    - The parameter'split_index' defines the location where the input mask will be split. It plays a key role in determining the size of each result group in the split operation. The validity of the partition depends to a large extent on the appropriate selection of the index.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- MASK_A
    - Output 'MASK_A' is the first group to divide the mask. It is important because it allows separate processing or analysis of the initial segment of the video mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- A_count
    - The output 'A_count' provides the number of elements in the first group of partition masks and provides an understanding of the size of the initial segment.
    - Comfy dtype: INT
    - Python dtype: int
- MASK_B
    - The output 'MASK_B' corresponds to the second group of split masks, allowing different processing or checking of the subsequent segments of the video mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- B_count
    - The output 'B_count' indicates the number of elements in group 2 of the mask, highlighting the size of the latter segment.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SplitMasks:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'split_index': ('INT', {'default': 0, 'step': 1, 'min': BIGMIN, 'max': BIGMAX})}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢/mask'
    RETURN_TYPES = ('MASK', 'INT', 'MASK', 'INT')
    RETURN_NAMES = ('MASK_A', 'A_count', 'MASK_B', 'B_count')
    FUNCTION = 'split_masks'

    def split_masks(self, mask: Tensor, split_index: int):
        group_a = mask[:split_index]
        group_b = mask[split_index:]
        return (group_a, group_a.size(0), group_b, group_b.size(0))
```