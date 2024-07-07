# Documentation
- Class name: WAS_Mask_Batch_to_Single_Mask
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `mask_batch_to_mask' method is designed to handle a batch of masks and to extract individual masks based on a specified batch number. It is essential in a scenario where a specific mask needs to be obtained from a collection and facilitates the transition from batch to single instance operations.

# Input types
## Required
- masks
    - The `masks' parameter is the mass of masks that the node will process. It is vital because it forms the basis for node operations and determines the mask that will be considered for extraction.
    - Comfy dtype: MASK
    - Python dtype: List[Tuple[torch.Tensor, ...]]
## Optional
- batch_number
    - The 'batch_number'parameter specifies which mask load to draw from the batch. It is important because it determines the selection process within the node and ensures that the right mask is returned on the basis of the batch index.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- single_mask
    - The `single_mask' output represents a single mask load extracted from the batch. It is important because it is the main result of node operations and provides users with the specific mask they request.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Batch_to_Single_Mask:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',), 'batch_number': ('INT', {'default': 0, 'min': 0, 'max': 64, 'step': 1})}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'mask_batch_to_mask'
    CATEGORY = 'WAS Suite/Image/Masking'

    def mask_batch_to_mask(self, masks=[], batch_number=0):
        count = 0
        for _ in masks:
            if batch_number == count:
                tensor = masks[batch_number][0]
                return (tensor,)
            count += 1
        cstr(f'Batch number `{batch_number}` is not defined, returning last image').error.print()
        last_tensor = masks[-1][0]
        return (last_tensor,)
```