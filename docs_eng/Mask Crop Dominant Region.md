# Documentation
- Class name: WAS_Mask_Crop_Dominant_Region
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The crop_dominant_region method is designed to handle the dominant area in the input mask and intelligently crop each mask. This is particularly useful for focusing on the most important part of the image, and for applications such as image summaries, object recognition and content perception image resizeing. This method applies filling to ensure that the cropping area is not too close to the edge, thus improving the quality of the result image.

# Input types
## Required
- masks
    - Enter the mask parameter is essential for the operation of the node because it defines the area of interest within the image. This parameter directly influences the output of the node and determines which parts of the image will be retained after the cropping process. The mask should be provided as a volume to ensure compatibility with the node's internal processing mechanism.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- padding
    - The padding parameter is used to specify the amount of space that will be left around the dominant area after the crop. It is essential to prevent the cropping area from being too close to the edge of the image, which may lead to more pleasant results. The default is set at 24, which reasonably balances the relationship between the focus on the dominant area and the preservation of the image context.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- MASKS
    - The output parameter MASKS represents the creation of a mask after the dominant area is cropped. It is a stretch containing the area of interest after cropping, which can be used for further image processing or analysis. The importance of this output is that it can provide a focused subset of the original image, which may increase the efficiency of the follow-up operation.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Crop_Dominant_Region:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',), 'padding': ('INT', {'default': 24, 'min': 0, 'max': 4096, 'step': 1})}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'crop_dominant_region'

    def crop_dominant_region(self, masks, padding=24):
        if masks.ndim > 3:
            regions = []
            for mask in masks:
                mask_pil = Image.fromarray(np.clip(255.0 * mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
                region_mask = self.WT.Masking.crop_dominant_region(mask_pil, padding)
                region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
                regions.append(region_tensor)
            regions_tensor = torch.cat(regions, dim=0)
            return (regions_tensor,)
        else:
            mask_pil = Image.fromarray(np.clip(255.0 * masks.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
            region_mask = self.WT.Masking.crop_dominant_region(mask_pil, padding)
            region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
            return (region_tensor,)
```