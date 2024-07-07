# Documentation
- Class name: WAS_Mask_Erode_Region
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The erode_region method is designed to treat the boundaries of the masked area by applying corrosion effects. This method is particularly useful in image-processing tasks, such as removing noise or isolating different areas in the image. It operates by reducing the size of the masked area over time, thus creating a more smoother and clearer boundary. The corrosive level can be controlled by iterative parameters, allowing for fine-tuning effects.

# Input types
## Required
- masks
    - Enter the mask parameter is essential for the erode_region method because it defines the image range that will be subject to corrosion. This parameter directly affects the execution and outcome of the node and determines which parts of the image will be affected by the corrosion process.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- iterations
    - An iterative parameter is used to control the extent of the corrosion effect applied to the input mask. Higher values lead to more obvious corrosion and a more significant reduction in the size of the mask area. This parameter is essential for adjusting the intensity of the corrosion to achieve the required visual effect.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- MASKS
    - The MASKS output parameter represents the final mask after the application of the corrosion process. It is a key output because it reflects the final state of the area of the image after the corrosion and contains the information needed for further processing or analysis in the follow-up process.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Erode_Region:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',), 'iterations': ('INT', {'default': 5, 'min': 1, 'max': 64, 'step': 1})}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'erode_region'

    def erode_region(self, masks, iterations=5):
        if masks.ndim > 3:
            regions = []
            for mask in masks:
                mask_np = np.clip(255.0 * mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
                pil_image = Image.fromarray(mask_np, mode='L')
                region_mask = self.WT.Masking.erode_region(pil_image, iterations)
                region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
                regions.append(region_tensor)
            regions_tensor = torch.cat(regions, dim=0)
            return (regions_tensor,)
        else:
            mask_np = np.clip(255.0 * masks.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
            pil_image = Image.fromarray(mask_np, mode='L')
            region_mask = self.WT.Masking.erode_region(pil_image, iterations)
            region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
            return (region_tensor,)
```