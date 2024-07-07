# Documentation
- Class name: WAS_Mask_Combine
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_Combine node is designed to merge multiple mask images into a single, coherent mask. It effectively combines input masks that can be used for various applications, such as image processing, graphic design and visual effects. The node ensures that the merged mask retains the basic features of the individual mask, making it a multifunctional tool to enhance visual content.

# Input types
## Required
- mask_a
    - The first mask to be combined with the other mask. It plays a key role in determining the initial properties of the combined mask.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image.Image or numpy.ndarray
- mask_b
    - A second mask to merge with the first mask. It helps to eventually mask the overall composition of the mask.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image.Image or numpy.ndarray
## Optional
- mask_c
    - The optional additional mask could be included in the grouping process to further refine the final mask.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image.Image or numpy.ndarray
- mask_d
    - Another optional mask could be provided to the combination to increase its complexity and detail.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image.Image or numpy.ndarray
- mask_e
    - An additional optional mask could be used to add more layers to the combination mask and enhance its visual elements.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image.Image or numpy.ndarray
- mask_f
    - The last optional mask can be integrated into the creation of a detailed and complex combination mask.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image.Image or numpy.ndarray

# Output types
- combined_mask
    - All input mask combinations produce the final mask. It is a single mask containing the visual data of the input mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Combine:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mask_a': ('MASK',), 'mask_b': ('MASK',)}, 'optional': {'mask_c': ('MASK',), 'mask_d': ('MASK',), 'mask_e': ('MASK',), 'mask_f': ('MASK',)}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'combine_masks'

    def combine_masks(self, mask_a, mask_b, mask_c=None, mask_d=None, mask_e=None, mask_f=None):
        masks = [mask_a, mask_b]
        if mask_c:
            masks.append(mask_c)
        if mask_d:
            masks.append(mask_d)
        if mask_e:
            masks.append(mask_e)
        if mask_f:
            masks.append(mask_f)
        combined_mask = torch.sum(torch.stack(masks, dim=0), dim=0)
        combined_mask = torch.clamp(combined_mask, 0, 1)
        return (combined_mask,)
```