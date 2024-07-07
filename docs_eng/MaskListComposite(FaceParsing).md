# Documentation
- Class name: MaskListComposite
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The MaskListComposite node is designed to perform the specified logical or arithmetic operations for a series of binary masks. It sequences input masks and applies the selected operation to group them into individual result masks. This node plays a key role in tasks that require operation and combination of binary facial feature masks, such as feature extraction in the field of facial section cutting or facial resolution.

# Input types
## Required
- mask
    - The `mask' parameter is a binary mask assembly that is combined through the operation specified in the `option' parameter. It is essential for the function of the node, as it determines the input that will be subjected to logic or arithmetic operations.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- operation
    - The `option' parameter indicates the type of operation to perform on the input mask. It may be one of the `multiple', `add', `and', `or' or `xor', which significantly influences the final outcome of the masking process.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- result
    - The `redult' parameter is the output of the node, which represents the application of the configured mask on the input mask. It encapsulates the node process results and is essential for the follow-on task that relies on the synthetic mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class MaskListComposite:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mask': ('MASK', {}), 'operation': (['multiply', 'add', 'and', 'or', 'xor'],)}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, mask: Tensor, operation: str):
        mask_result = mask[0]
        for item in mask[1:]:
            if operation == 'multiply':
                mask_result = mask_result * item
            if operation == 'add':
                mask_result = mask_result + item
            if operation == 'and':
                mask_result = mask_result & item
            if operation == 'or':
                mask_result = mask_result | item
            if operation == 'xor':
                mask_result = mask_result ^ item
        return (mask_result.unsqueeze(0),)
```