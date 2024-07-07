# Documentation
- Class name: WAS_Mask_Threshold_Region
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_Threshold_Region node is designed to distinguish between areas in the image by using a threshold to process image masks. It uses a black and white threshold to create a binary mask, which can be divided by the strength of pixels. This node is essential for image partitioning, target detection, and any application that requires a division of image areas based on colour or brightness levels.

# Input types
## Required
- masks
    - Input mask is the main source of node operations. They are used to generate a threshold range within the image. This parameter is critical, as all functions of the node revolve around the manipulation and analysis of these masks.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- black_threshold
    - Black_threshold parameters define the strength threshold of pixels that are considered to belong to the black area. It plays an important role in determining whether the image is divided into different areas according to colour intensity.
    - Comfy dtype: INT
    - Python dtype: int
- white_threshold
    - The white_threshold parameter is used to define the upper limit of the intensity values of the pixels that are considered to belong to the white area. It is an important parameter for controlling the partition process and determining the white area in the image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- MASKS
    - MASKS output consists of image masks that are processed after applying thresholds. This output is important because it represents the final segment of the image that is entered according to the specified thresholds.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Threshold_Region:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',), 'black_threshold': ('INT', {'default': 75, 'min': 0, 'max': 255, 'step': 1}), 'white_threshold': ('INT', {'default': 175, 'min': 0, 'max': 255, 'step': 1})}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'threshold_region'

    def threshold_region(self, masks, black_threshold=75, white_threshold=255):
        if masks.ndim > 3:
            regions = []
            for mask in masks:
                mask_np = np.clip(255.0 * mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
                pil_image = Image.fromarray(mask_np, mode='L')
                region_mask = self.WT.Masking.threshold_region(pil_image, black_threshold, white_threshold)
                region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
                regions.append(region_tensor)
            regions_tensor = torch.cat(regions, dim=0)
            return (regions_tensor,)
        else:
            mask_np = np.clip(255.0 * masks.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
            pil_image = Image.fromarray(mask_np, mode='L')
            region_mask = self.WT.Masking.threshold_region(pil_image, black_threshold, white_threshold)
            region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
            return (region_tensor,)
```