# Documentation
- Class name: WAS_Mask_To_Image
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_To_Image node is designed to convert mask data into image formats. It allows intelligent handling of various dimensions of mask input to ensure compatibility with different types of mask data. This node plays a key role in the conversion process, making the transition from mask expression to visual images seamless.

# Input types
## Required
- masks
    - The'masks' parameter is essential to the operation of the node because it defines the input mask data that needs to be converted to the image. The node execution has a significant impact because it directly affects the quality and expression of the output image.
    - Comfy dtype: MASK
    - Python dtype: Union[torch.Tensor, List[torch.Tensor]]

# Output types
- IMAGES
    - The 'IMAGES'output parameter represents the image data that is converted from the input mask. It is a key output because it marks the successful conversion of the mask data to a visual format that can be further processed or displayed.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_To_Image:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',)}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('IMAGES',)
    FUNCTION = 'mask_to_image'

    def mask_to_image(self, masks):
        if masks.ndim == 4:
            tensor = masks.permute(0, 2, 3, 1)
            tensor_rgb = torch.cat([tensor] * 3, dim=-1)
            return (tensor_rgb,)
        elif masks.ndim == 3:
            tensor = masks.unsqueeze(-1)
            tensor_rgb = torch.cat([tensor] * 3, dim=-1)
            return (tensor_rgb,)
        elif masks.ndim == 2:
            tensor = masks.unsqueeze(0).unsqueeze(-1)
            tensor_rgb = torch.cat([tensor] * 3, dim=-1)
            return (tensor_rgb,)
        else:
            cstr('Invalid input shape. Expected [N, C, H, W] or [H, W].').error.print()
            return masks
```