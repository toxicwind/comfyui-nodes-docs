# Documentation
- Class name: WAS_Mask_Ceiling_Region
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_Ceiling_Region method is designed to process input masks and identify the top areas. Its working principle is to convert them to PIL images, to use ceiling effects to isolate the top areas, and then to convert the results back into a volume format suitable for further image processing tasks.

# Input types
## Required
- masks
    - Enter the mask parameter is essential for the ceiling_region method because it provides the original mask data that the node will process. This parameter directly influences the output of the node and determines which areas in the image are identified as the uppermost.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Output types
- MASKS
    - The MASKS output parameter represents the volume of the area processed from the input mask. This output is important because it is the result of node processing and is used for follow-up tasks in the image analysis process.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Ceiling_Region:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',)}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'ceiling_region'

    def ceiling_region(self, masks):
        if masks.ndim > 3:
            regions = []
            for mask in masks:
                mask_np = np.clip(255.0 * mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
                pil_image = Image.fromarray(mask_np, mode='L')
                region_mask = self.WT.Masking.ceiling_region(pil_image)
                region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
                regions.append(region_tensor)
            regions_tensor = torch.cat(regions, dim=0)
            return (regions_tensor,)
        else:
            mask_np = np.clip(255.0 * masks.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
            pil_image = Image.fromarray(mask_np, mode='L')
            region_mask = self.WT.Masking.ceiling_region(pil_image)
            region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
            return (region_tensor,)
```