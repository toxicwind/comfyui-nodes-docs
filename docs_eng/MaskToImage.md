# Documentation
- Class name: MaskToImage
- Category: mask
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The MaskToImage node is designed to convert binary mask data into colour image formats. It plays a key role in visualizing masked data, by converting them into images that are easier to interpret and understand. The node abstractes the complexity of the conversion process and focuses on generating user-friendly visual expressions of the ultimate goal.

# Input types
## Required
- mask
    - The `mask' parameter is essential for the MaskToImage node, as it represents the binary mask data that needs to be converted to images. The correct input of this parameter is essential for the node to perform its conversion function effectively, directly affecting the quality and accuracy of the images generated.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- result
    - The `result' output of the MaskToImage node is a colour image derived from the input mask. It marks the successful conversion of binary mask data to a visual format that can be used for further analysis or presentation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class MaskToImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',)}}
    CATEGORY = 'mask'
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'mask_to_image'

    def mask_to_image(self, mask):
        result = mask.reshape((-1, 1, mask.shape[-2], mask.shape[-1])).movedim(1, -1).expand(-1, -1, -1, 3)
        return (result,)
```