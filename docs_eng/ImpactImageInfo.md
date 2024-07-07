# Documentation
- Class name: ImpactImageInfo
- Category: ImpactPack/Logic/_for_test
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImpactImageInfo method is designed to provide critical image information. It is essential to understand the dimensions and structure of the image data set, which are essential for downstream processing and analysis tasks. It conveys abstractly the ability to extract and return the batch size, height, width and number of channels to enter the image.

# Input types
## Required
- value
    - The `value' parameter is the input image data processed by the node. Its function is fundamental because it directly affects output information about the size of the image. This parameter is essential for the execution of the node because it is the basis for determining the volume size, height, width and number of channels.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- batch
    - The `batch' parameter indicates the number of images processed in a single batch. It is important because it indicates the volume of data processed in a single batch, which is important for optimizing the calculation of resources and understanding the scope of analysis.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height'parameter indicates the vertical dimension of the input image. It is a key factor in determining the spatial resolution and is essential for the purpose of the image's manipulation and display.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The `width' parameter indicates the horizontal dimension of the input image. It plays a key role in the overall image resolution and is essential to ensure the correct width ratio and display format.
    - Comfy dtype: INT
    - Python dtype: int
- channel
    - The 'channel' parameter refers to the number of colour fractions in the image, usually three for the RGB image. It is a determining factor for the depth of the colour and is essential for the colour processing and image enhancement tasks.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactImageInfo:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'value': ('IMAGE',)}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic/_for_test'
    RETURN_TYPES = ('INT', 'INT', 'INT', 'INT')
    RETURN_NAMES = ('batch', 'height', 'width', 'channel')

    def doit(self, value):
        return (value.shape[0], value.shape[1], value.shape[2], value.shape[3])
```