# Documentation
- Class name: WAS_Mask_Fill_Region
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_Fill_Region node is designed to handle image masking and fill the specified area, which is essential for applications involving image partitioning or area-based operations. It uses the capabilities of the WAS_Tools_Class to perform actual filling to ensure that the fill area is properly integrated into the mask. This node is particularly useful when it is necessary to create seamless textures or synthesizing maps where the continuity of the area is important.

# Input types
## Required
- masks
    - The'masks' parameter is the key input for the node, which defines the binary mask to be processed. It is essential for the execution of the node because it directly affects the filled area. The parameter expects a mask array, each of which corresponds to an area to be filled.
    - Comfy dtype: np.ndarray
    - Python dtype: numpy.ndarray

# Output types
- MASKS
    - The 'MASKS'output parameter represents the result of node operations, i.e. the array of areas filled in the mask. This output is important because it provides a processed mask that can be further analysed or rendered in various applications.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Fill_Region:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',)}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'fill_region'

    def fill_region(self, masks):
        if masks.ndim > 3:
            regions = []
            for mask in masks:
                mask_np = np.clip(255.0 * mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
                pil_image = Image.fromarray(mask_np, mode='L')
                region_mask = self.WT.Masking.fill_region(pil_image)
                region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
                regions.append(region_tensor)
            regions_tensor = torch.cat(regions, dim=0)
            return (regions_tensor,)
        else:
            mask_np = np.clip(255.0 * masks.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
            pil_image = Image.fromarray(mask_np, mode='L')
            region_mask = self.WT.Masking.fill_region(pil_image)
            region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
            return (region_tensor,)
```