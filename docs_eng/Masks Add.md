# Documentation
- Class name: WAS_Mask_Add
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_Add node is designed to perform a combination of two mask images. It is good at combining mask data to create a compound mask, which is essential in the image processing workflow that requires a layered mask. The node ensures that the result mask value is within the range of effectiveness and contributes to seamless integration of the mask layer.

# Input types
## Required
- masks_a
    - Parameters'masks_a' represent the first set of mask images that you want to add. It plays a key role in determining the initial state of the compound mask and influences the final outcome of the mask processing process.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- masks_b
    - The parameter'masks_b' is a second set of mask images integrated with'masks_a'. It is essential to create a full mask that contains the required features from two sets of masks.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- MASKS
    - The output 'MASKS' is the result of an addition operation performed at the node. It is a composite mask that contains the combination features of the input mask to be used for downstream image processing tasks.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Add:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks_a': ('MASK',), 'masks_b': ('MASK',)}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'add_masks'

    def add_masks(self, masks_a, masks_b):
        if masks_a.ndim > 2 and masks_b.ndim > 2:
            added_masks = masks_a + masks_b
        else:
            added_masks = torch.clamp(masks_a.unsqueeze(1) + masks_b.unsqueeze(1), 0, 255)
            added_masks = added_masks.squeeze(1)
        return (added_masks,)
```