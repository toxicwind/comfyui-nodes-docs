# Documentation
- Class name: WAS_Mask_Smooth_Region
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_Smooth_Region node is designed to process input masks and apply smooth effects to their area. This is particularly useful for generating seamless textures or for preparing masks for further image processing tasks. The node uses Gaussian fuzzy to smooth the area within the mask, with the'sigma' parameter controlling the level of smoothness. The function of the node is optimized for individual mask and mask batches, ensuring flexibility and efficiency in various applications.

# Input types
## Required
- masks
    - The'masks' parameter is the key input for the node, which is expected to receive a mask or mask batch. This input directly affects the operation of the node because it determines the area to be smooth. The parameter is essential for the node to produce the desired output, affecting the seamlessness of the image of the final texture quality and the smoothing of the map.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- sigma
    - The'sigma' parameter defines the smoothness to be applied to the masked area. It is a floating point number that adjusts Gaussian's vague standard deviations, and higher values lead to a more obvious smoothing effect. This parameter is optional, but has a significant impact on the output of nodes, allowing users to control the appearance of smooth areas.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- MASKS
    - The 'MASKS'output provides a smooth mask or mask batch that can be obtained by applying the Gaussian fuzzy definition of the'sigma'parameter. This output is important because it represents node processed data that can be used for follow-up operations or as the final output generated as texture.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Smooth_Region:

    def __init__(self):
        self.WT = WAS_Tools_Class()

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',), 'sigma': ('FLOAT', {'default': 5.0, 'min': 0.0, 'max': 128.0, 'step': 0.1})}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'smooth_region'

    def smooth_region(self, masks, sigma=128):
        if masks.ndim > 3:
            regions = []
            for mask in masks:
                mask_np = np.clip(255.0 * mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
                pil_image = Image.fromarray(mask_np, mode='L')
                region_mask = self.WT.Masking.smooth_region(pil_image, sigma)
                region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
                regions.append(region_tensor)
            regions_tensor = torch.cat(regions, dim=0)
            return (regions_tensor,)
        else:
            mask_np = np.clip(255.0 * masks.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
            pil_image = Image.fromarray(mask_np, mode='L')
            region_mask = self.WT.Masking.smooth_region(pil_image, sigma)
            region_tensor = pil2mask(region_mask).unsqueeze(0).unsqueeze(1)
            return (region_tensor,)
```