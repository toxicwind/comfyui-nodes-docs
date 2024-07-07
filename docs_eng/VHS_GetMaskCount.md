# Documentation
- Class name: GetMaskCount
- Category: Video Helper Suite 🎥🅥🅗🅢/mask
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The GetMaskCount node is designed to process and calculate the number of masks that exist in given video frames. It plays a key role in video analysis by providing a direct method to determine the number of masks, which is essential for various applications in video processing, such as target detection or task partitioning.

# Input types
## Required
- mask
    - The `mask'parameter is essential for the GetMaskCount node, because it represents a video frame containing the number of numbers to be counted. The importance of the node is that the function depends entirely on the input mask to perform its counting operations.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- count
    - The `account' output parameter represents the total number of masks identified in the input frame. It is important because it directly reflects the results of node operations and provides a quantitative measure of the presence of the mask.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class GetMaskCount:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',)}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢/mask'
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('count',)
    FUNCTION = 'count_input'

    def count_input(self, mask: Tensor):
        return (mask.size(0),)
```