# Documentation
- Class name: WAS_Mask_Minority_Region
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The miniority_region method is designed to process input masks and identify a few of them. By converting them to PIL images, it uses thresholds to separate different areas and then isolates the smallest ones. This method is particularly suitable for applications that focus on less visible or few areas in the image, for example in image partitioning or feature extraction tasks.

# Input types
## Required
- masks
    - Enter the mask parameter is essential for the MINORITY_region method, as it defines the interest range within the image. This parameter affects the way in which a few areas are identified and processed, and is essential for the accuracy of the result.
    - Comfy dtype: MASK
    - Python dtype: Union[torch.Tensor, List[torch.Tensor]]
## Optional
- threshold
    - The threshold parameter is used to determine the cut-off point between the different areas within the mask. It plays an important role in the miniority_region approach by influencing which areas are considered part of a small number of areas. The default is set at 128, allowing some flexibility in applying the threshold.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- MASKS
    - The MASKS output parameter represents a small number of areas processed from the input mask. It is a key output because it provides the final result of the Minority_region method, highlighting the less visible areas in the original image.
    - Comfy dtype: MASK
    - Python dtype: Tuple[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Minority_Region:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',), 'threshold': ('INT', {'default': 128, 'min': 0, 'max': 255, 'step': 1})}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'minority_region'

    def minority_region(self, masks, threshold=128):
        if masks.ndim > 3:
            regions = []
            for mask in masks:
                mask_np = np.clip(255.0 * mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
                pil_image = Image.fromarray(mask_np, mode='L')
                region_mask = self.WT.Masking.minority_region(pil_image, threshold)
                region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
                regions.append(region_tensor)
            regions_tensor = torch.cat(regions, dim=0)
            return (regions_tensor,)
        else:
            mask_np = np.clip(255.0 * masks.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
            pil_image = Image.fromarray(mask_np, mode='L')
            region_mask = self.WT.Masking.minority_region(pil_image, threshold)
            region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
            return (region_tensor,)
```