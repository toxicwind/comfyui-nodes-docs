# Documentation
- Class name: SelectEveryNthMask
- Category: Video Helper Suite 🎥🅥🅗🅢/mask
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The `select_masks'method for SELECTEveryNthMasks node is designed to handle a series of masks by selecting every n mask from the input. This is essential for the application that requires further processing or analysis of the mask set. The node effectively filters the required mask to ensure that the output is the mask sequence at the specified interval.

# Input types
## Required
- mask
    - The parameter `mask'is the mask sequence that the node will process. It plays a central role in the operation of the node, as it is the main input that determines the subsequent output. The execution of the node and the resulting mask are directly influenced by the content and structure of the input mask sequence.
    - Comfy dtype: Tensor
    - Python dtype: torch.Tensor
- select_every_nth
    - The parameter `select_every_nth'determines the frequency of the mask to be selected from the input sequence. It is an important component of the node function because it determines the spacing of the mask selection. The output of the node is significantly influenced by this parameter because it controls the density of the returned mask sequence.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- MASK
    - Output `MASK'is a subset of the input mask based on the specified interval selection. It represents the filter sequence of the mask processed by the node according to the user's selection criteria. This output is important for downstream tasks that need to reduce the mask set in order to improve efficiency or specificity.
    - Comfy dtype: Tensor
    - Python dtype: torch.Tensor
- count
    - Output `count'provides the number of masks selected from the input sequence. This is an important information that demonstrates the efficiency of the selection process and can be used for further analysis or notification of subsequent steps in the workflow.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SelectEveryNthMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'select_every_nth': ('INT', {'default': 1, 'min': 1, 'max': BIGMAX, 'step': 1})}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢/mask'
    RETURN_TYPES = ('MASK', 'INT')
    RETURN_NAMES = ('MASK', 'count')
    FUNCTION = 'select_masks'

    def select_masks(self, mask: Tensor, select_every_nth: int):
        sub_mask = mask[0::select_every_nth]
        return (sub_mask, sub_mask.size(0))
```