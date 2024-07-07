# Documentation
- Class name: WAS_Mask_Subtract
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_Masks method of the node of Mask_Subtract reduces two sets of masks by element, ensuring that the result falls within the range of valid pixel values. It is designed to facilitate operations that require the removal of another mask from one mask, such as in image processing or masking applications.

# Input types
## Required
- masks_a
    - The first set of masks is used for subtraction operations. This parameter is essential because it defines the basis from which the second set of masks will be subtracted.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- masks_b
    - The second mask will be subtracted from the first group. This parameter significantly influences the results of the operation.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- MASKS
    - The results of the two sets of masks are reduced and restricted to ensure valid pixel values.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Subtract:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks_a': ('MASK',), 'masks_b': ('MASK',)}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'subtract_masks'

    def subtract_masks(self, masks_a, masks_b):
        subtracted_masks = torch.clamp(masks_a - masks_b, 0, 255)
        return (subtracted_masks,)
```