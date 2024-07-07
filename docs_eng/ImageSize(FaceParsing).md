# Documentation
- Class name: ImageSize
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The ImageSize node is designed to extract and provide the size of the input image, especially its width and height. It is a basic component in the image processing workflow to ensure that the spatial properties of the image are understood and can be used in follow-up operations.

# Input types
## Required
- image
    - The image parameter is essential because it is an input image that will determine the size. It significantly influences the output of the node and determines the values of width and height that will be calculated and returned.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- width
    - Width output represents the spatial range of the image along its horizontal axis. This is the basic information for further image analysis and operation.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - High output corresponds to the spatial range of the image that follows its vertical axis. This measure is essential to understand the layout of the image and the subsequent image processing tasks.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class ImageSize:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE', {})}}
    RETURN_TYPES = ('INT', 'INT')
    RETURN_NAMES = ('width', 'height')
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, image: Tensor):
        w = image.shape[2]
        h = image.shape[1]
        return (w, h)
```