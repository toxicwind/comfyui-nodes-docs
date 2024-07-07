# Documentation
- Class name: WAS_Mask_Dominant_Region
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The dominant_region method is designed to identify and isolate the most prominent areas in a given mask image. It processes the input image to highlight the maximum continuous area based on the specified threshold. This method is particularly applicable in applications that focus on the main themes or features in the image, such as image partitions or feature extraction tasks.

# Input types
## Required
- masks
    - The input mask parameter is essential for the operation of the node because it defines the image data to be processed. The node relies on this input to identify the dominant area in the image, making it a key component that directly affects node performance and results.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- threshold
    - Threshold parameters play an important role in determining the visibility of the stitches in the image. By adjusting the threshold values, the user can control the balance between the visibility of the stitches and the size of the result image, which is essential for applications that require seamless texture or pattern.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- MASKS
    - Output MASKS parameters represent processed image data, in which the main area is identified and isolated. This output is important because it provides the results of node operations that can be further used in downstream processes or applications.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Dominant_Region:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',), 'threshold': ('INT', {'default': 128, 'min': 0, 'max': 255, 'step': 1})}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'dominant_region'

    def dominant_region(self, masks, threshold=128):
        if masks.ndim > 3:
            regions = []
            for mask in masks:
                mask_pil = Image.fromarray(np.clip(255.0 * mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
                region_mask = self.WT.Masking.dominant_region(mask_pil, threshold)
                region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
                regions.append(region_tensor)
            regions_tensor = torch.cat(regions, dim=0)
            return (regions_tensor,)
        else:
            mask_pil = Image.fromarray(np.clip(255.0 * masks.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
            region_mask = self.WT.Masking.dominant_region(mask_pil, threshold)
            region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
            return (region_tensor,)
```