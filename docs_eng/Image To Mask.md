# Documentation
- Class name: ImageToMask
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The ImageToMask node is designed to convert the input image to a mask. It provides a method for converting the image based on strength or alpha value, which helps to create binary or single-channel masks from input data, which are essential for various image processing tasks (e.g. partitions).

# Input types
## Required
- image
    - The image parameter is necessary because it is the main input to the node. It influences the node by determining the source of the mask to be generated. The image is expected to exist in a sheet format, and the node will process it to generate the required mask output.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- method
    - The methodological parameters determine the conversion strategy to be used at the node. It is important because it determines whether the mask is derived from strength or alpha, which in turn affects the properties of the final mask and the suitability for downstream applications.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- MASK
    - MASK output is a volume, representing the mask derived from the input image. It is a key output, because it is the direct result of the node conversion process that the converted image data are sealed in formats suitable for partitioning or other mask-based applications.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageToMask:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'method': (['intensity', 'alpha'],)}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'convert'
    CATEGORY = 'Masquerade Nodes'

    def convert(self, image, method):
        if method == 'intensity':
            if len(image.shape) > 3 and image.shape[3] == 4:
                image = tensor2rgb(image)
            return (tensor2mask(image),)
        else:
            return (tensor2rgba(image)[:, :, :, 0],)
```