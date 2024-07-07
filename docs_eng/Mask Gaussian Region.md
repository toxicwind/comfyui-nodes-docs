# Documentation
- Class name: WAS_Mask_Gaussian_Region
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_Gaussian_Region method is very useful for smooth transitions in the image area by using the Gaussian fuzzy effect to handle input masks. This method enhances the visual quality of texture by reducing the visible seams to apply to applications that require seamless textures, such as game development and 3D modelling.

# Input types
## Required
- masks
    - Enter the mask parameter is essential for the operation of the node because it defines the image range that will experience the Gaussian fuzzy effect. This parameter directly influences the texture process and determines the smoothness and continuity of the image generated.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- radius
    - The radius parameter determines the degree of hyperbolicness that should be applied to the input mask. The larger radius leads to a more obvious blur effect, which can be used to create a softer transition between different areas of the image. This parameter is essential to fine-tune the visual appearance of the final texture.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- MASKS
    - The MASKS output provides an application of the Gaussian fuzzy treated image mask. This output is important because it represents the end result of node operations that can be used for further image processing tasks or integration into larger workflows.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Gaussian_Region:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',), 'radius': ('FLOAT', {'default': 5.0, 'min': 0.0, 'max': 1024, 'step': 0.1})}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'gaussian_region'

    def gaussian_region(self, masks, radius=5.0):
        if masks.ndim > 3:
            regions = []
            for mask in masks:
                mask_np = np.clip(255.0 * mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
                pil_image = Image.fromarray(mask_np, mode='L')
                region_mask = self.WT.Masking.gaussian_region(pil_image, radius)
                region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
                regions.append(region_tensor)
            regions_tensor = torch.cat(regions, dim=0)
            return (regions_tensor,)
        else:
            mask_np = np.clip(255.0 * masks.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
            pil_image = Image.fromarray(mask_np, mode='L')
            region_mask = self.WT.Masking.gaussian_region(pil_image, radius)
            region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
            return (region_tensor,)
```