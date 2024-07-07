# Documentation
- Class name: WAS_Mask_Arbitrary_Region
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The SAS_Mask_Arbitray_region method is designed to process input masks and generate loads of areas of interest according to the size and threshold parameters provided. This method is particularly suitable for applications that require the identification and extraction of specific areas in the image, such as image editing, analysis, or machine learning tasks involving regional focus.

# Input types
## Required
- masks
    - Input mask parameters are essential for the arbitry_region method, as they define the source from which the area of interest will be extracted. The quality and characteristics of the input mask directly influence the outcome of the area identification process.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- size
    - The size parameter determines the size of the area to be considered as an area of interest. It is a key factor in the methodology, as it directly affects the size of the extraction area.
    - Comfy dtype: INT
    - Python dtype: int
- threshold
    - The threshold parameter is used to set the sensitivity level of the area of interest in the input mask. It plays an important role in the accuracy of the extraction of the area.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- MASKS
    - The MASKS output parameter represents the volume of the area of interest extracted from the input mask. It is an important output because it provides the final result of the arbitry_region method, which can be further processed or analysed.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Arbitrary_Region:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',), 'size': ('INT', {'default': 256, 'min': 1, 'max': 4096, 'step': 1}), 'threshold': ('INT', {'default': 128, 'min': 0, 'max': 255, 'step': 1})}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'arbitrary_region'

    def arbitrary_region(self, masks, size=256, threshold=128):
        if masks.ndim > 3:
            regions = []
            for mask in masks:
                mask_np = np.clip(255.0 * mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
                pil_image = Image.fromarray(mask_np, mode='L')
                region_mask = self.WT.Masking.arbitrary_region(pil_image, size, threshold)
                region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
                regions.append(region_tensor)
            regions_tensor = torch.cat(regions, dim=0)
            return (regions_tensor,)
        else:
            mask_np = np.clip(255.0 * masks.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
            pil_image = Image.fromarray(mask_np, mode='L')
            region_mask = self.WT.Masking.arbitrary_region(pil_image, size, threshold)
            region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
            return (region_tensor,)
```