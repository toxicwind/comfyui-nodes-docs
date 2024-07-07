# Documentation
- Class name: ImageColorToMask
- Category: mask
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ImageColorToMask node is designed to convert colour images into binary masks according to the colour specified. It highlights areas of interest by identifying pixels in the image that match the given colour and converting them into masks. The node plays a key role in applications that require colour-based masks, for example in target detection and partitioning.

# Input types
## Required
- image
    - The 'image'parameter is the input colour image that the node will process. It is the basic basis for node operations, because it is the source of the derivative mask. The contents of the image directly affect the accuracy and final output of the mask.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- color
    - The 'color' parameter defines the particular colour in which the image should be converted to a mask. It is a key parameter because it determines which pixels will be included in the final mask. The colour is specified in numerical format and allows the tone required for accurate positioning.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- mask
    - The'mask' output is a binary expression of the input image, in which the colour specified has been converted to a mask. It is important because it provides a clear division between the area of interest and the rest of the image that can be used for further analysis or processing.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ImageColorToMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'color': ('INT', {'default': 0, 'min': 0, 'max': 16777215, 'step': 1, 'display': 'color'})}}
    CATEGORY = 'mask'
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'image_to_mask'

    def image_to_mask(self, image, color):
        temp = (torch.clamp(image, 0, 1.0) * 255.0).round().to(torch.int)
        temp = torch.bitwise_left_shift(temp[:, :, :, 0], 16) + torch.bitwise_left_shift(temp[:, :, :, 1], 8) + temp[:, :, :, 2]
        mask = torch.where(temp == color, 255, 0).float()
        return (mask,)
```