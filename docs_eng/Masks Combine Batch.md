# Documentation
- Class name: WAS_Mask_Combine_Batch
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_Combine_Batch node is designed to combine multiple mask images into a single, seamless mask. This is particularly useful for applications that need further processing or visualization. The node receives a batch of masks and exports a combination mask that retains the basic features in the input mask.

# Input types
## Required
- masks
    - Enter the parameter'masks' is the list of mask images to be combined. It plays a key role in the operation of the node, because the quality and resolution of the output mask depends directly on the input mask. The mask should be processed in compatible formats.
    - Comfy dtype: List[Image]
    - Python dtype: List[PIL.Image.Image]

# Output types
- combined_mask
    - The 'combined_mask' output is the result of a combination of input masks. It is a single image that represents the collective coverage of all input masks and applies to applications such as image partitions or masks in visual effects.
    - Comfy dtype: Image
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Combine_Batch:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',)}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'combine_masks'

    def combine_masks(self, masks):
        combined_mask = torch.sum(torch.stack([mask.unsqueeze(0) for mask in masks], dim=0), dim=0)
        combined_mask = torch.clamp(combined_mask, 0, 1)
        return (combined_mask,)
```