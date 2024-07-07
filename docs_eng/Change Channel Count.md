# Documentation
- Class name: ChangeChannelCount
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The ChangechannelCount node is designed to modify the number of channels for image lengths. It allows intelligent processing of different types of images, such as masks, RGBA and RGB, and conversions according to the specified type. This node plays a key role in image processing workflows that require channel operations to achieve compatibility or style.

# Input types
## Required
- image
    - The image parameter is the input length of the image data. It is vital because it is the primary data that the node will process. The operation of the node depends on the dimension and content of the image length, which directly influences the output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- kind
    - Kind parameter instructions apply to the type of channel conversion that enters the image length. It is vital because it determines the output format of the image channel. Depending on the specified channel conversion type, the kind parameter significantly alters the execution and final result of the node.
    - Comfy dtype: COMBO['mask', 'RGB', 'RGBA']
    - Python dtype: str

# Output types
- output_image
    - Output_image is the result of the channel conversion process. It is important because it represents the final output of the node, i.e. the number of images with a modified channel number according to the specified kind.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ChangeChannelCount:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'kind': (['mask', 'RGB', 'RGBA'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'change_channels'
    CATEGORY = 'Masquerade Nodes'

    def change_channels(self, image, kind):
        image_size = image.size()
        if kind == 'mask':
            return (tensor2mask(image),)
        elif kind == 'RGBA':
            return (tensor2rgba(image),)
        else:
            return (tensor2rgb(image),)
```