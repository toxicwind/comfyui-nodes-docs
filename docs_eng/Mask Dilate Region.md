# Documentation
- Class name: WAS_Mask_Dilate_Region
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The dilaate_region method is designed to implement a morphological inflation of the mask for input masking and to expand the boundaries of the masked area. This process is critical to the need to enhance the edge of the mask or to create buffer zones in the masked area. By applying the overlap of the specified number of times, the method allows for the containment of the inflated range, thus providing a multifunctional tool for a variety of image-processing tasks involving masking operations.

# Input types
## Required
- masks
    - Input mask parameters are essential to the dilaate_region method because it defines the area to expand. This is a key component that directly affects the outcome of the expansion process. The mask should be provided in a format that the method can explain and process, usually as a stretch or numbery array.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- iterations
    - An iterative parameter determines the number of times an inflated operation is applied to the input mask. It is an optional parameter that allows users to control the degree of inflation, and more overlaps lead to more significant effects. This parameter is important for fine-tuning inflation to suit specific application needs.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- MASKS
    - The MASKS output parameter represents the result of the expansion process. It contains the inflated mask from the original input mask extension after a specified number of rotations. This output is very important because it is the main result of the dilate_region method and is used for further image processing or analysis.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Dilate_Region:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',), 'iterations': ('INT', {'default': 5, 'min': 1, 'max': 64, 'step': 1})}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'dilate_region'

    def dilate_region(self, masks, iterations=5):
        if masks.ndim > 3:
            regions = []
            for mask in masks:
                mask_np = np.clip(255.0 * mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
                pil_image = Image.fromarray(mask_np, mode='L')
                region_mask = self.WT.Masking.dilate_region(pil_image, iterations)
                region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
                regions.append(region_tensor)
            regions_tensor = torch.cat(regions, dim=0)
            return (regions_tensor,)
        else:
            mask_np = np.clip(255.0 * masks.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
            pil_image = Image.fromarray(mask_np, mode='L')
            region_mask = self.WT.Masking.dilate_region(pil_image, iterations)
            region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
            return (region_tensor,)
```