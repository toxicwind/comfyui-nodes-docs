# Documentation
- Class name: WAS_Mask_Crop_Minority_Region
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_Crop_Minority_Region node is designed to process the loads that enter the image or represent the mask, and is intelligently cropping a few of the areas. This is particularly useful for focusing on the less prominent areas in the image for further analysis or processing. This node can handle individual mask and mask batches and fill the area that the user has specified.

# Input types
## Required
- masks
    - The input mask is the main input for this node, which can be a single mask or stack of multiple masks, representing the image area to be processed. The node will identify a few of these masks and perform the crop operation accordingly.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- padding
    - Padding parameters allow users to specify fills to be added around a few areas of the crop. This is useful for keeping context around the cropping area or for seamless integration with other image processing tasks.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- MASKS
    - The output of the nodes is a small number of areas that are cropped in the input mask. They can be used for further processing or analysis tasks.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Crop_Minority_Region:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',), 'padding': ('INT', {'default': 24, 'min': 0, 'max': 4096, 'step': 1})}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'crop_minority_region'

    def crop_minority_region(self, masks, padding=24):
        if masks.ndim > 3:
            regions = []
            for mask in masks:
                mask_pil = Image.fromarray(np.clip(255.0 * mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
                region_mask = self.WT.Masking.crop_minority_region(mask_pil, padding)
                region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
                regions.append(region_tensor)
            regions_tensor = torch.cat(regions, dim=0)
            return (regions_tensor,)
        else:
            mask_pil = Image.fromarray(np.clip(255.0 * masks.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
            region_mask = self.WT.Masking.crop_minority_region(mask_pil, padding)
            region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
            return (region_tensor,)
```