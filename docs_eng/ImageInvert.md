# Documentation
- Class name: ImageInvert
- Category: image
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ImageInvert node is designed to perform a basic image processing operation, i.e. an image inverse colour. It receives an image as input and exports an image corresponding to its inverse colour, in which the strength of pixels is reversed, reversing the visible and dark area of the image. The node plays a key role in various image analysis and enhancement tasks, providing a simple and effective method of visual contrast change.

# Input types
## Required
- image
    - An image parameter is essential for the ImageInvert node because it is the main input that determines the object of the operation. The node processes this image to produce an inverse version, making the image parameter central to the function and result of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- inverted_image
    - The inverse image output parameter represents the result of the image's inverse color treatment. It is important because it is the direct output of the main function of the node, showing the converted image with the inverted pixel strength.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageInvert:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'invert'
    CATEGORY = 'image'

    def invert(self, image):
        s = 1.0 - image
        return (s,)
```