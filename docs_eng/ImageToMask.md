# Documentation
- Class name: ImageToMask
- Category: mask
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ImageToMask node is designed to extract a specific colour channel from the input image, creating a mask that can be used for a variety of image processing tasks. It plays a key role in dividing and isolating particular features in the image, thus enabling more targeted analysis and operations.

# Input types
## Required
- image
    - The image parameter is the main input of the ImageToMask node. It is the source of the colour channel to form the mask. This parameter is vital because it determines the content and quality of the result mask.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- channel
    - Channel parameters specify the colour channel from which the image is extracted. It is a key input, as it determines the particular aspects of the image that will be represented in the mask. The selection of the channel can significantly influence the subsequent processing and analysis of the image.
    - Comfy dtype: COMBO['red', 'green', 'blue', 'alpha']
    - Python dtype: str

# Output types
- mask
    - A mask output is a single channel for entering the selected colour channel in the image. It provides a focused view of the selected channel information as a basis for further image operation and analysis.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageToMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['red', 'green', 'blue', 'alpha'],)}}
    CATEGORY = 'mask'
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'image_to_mask'

    def image_to_mask(self, image, channel):
        channels = ['red', 'green', 'blue', 'alpha']
        mask = image[:, :, :, channels.index(channel)]
        return (mask,)
```