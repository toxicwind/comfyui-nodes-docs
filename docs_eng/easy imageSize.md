# Documentation
- Class name: imageSize
- Category: EasyUse/Image
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node is designed to extract and provide the size of the image, focusing on width and height as key attributes. It serves as a basic tool in image processing, making possible further analysis and operation based on these parameters.

# Input types
## Required
- image
    - The image parameter is necessary because it is the source of the node derived width and height values. Without this input, node cannot perform its main function.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray

# Output types
- width_int
    - The width_int output represents the horizontal dimension of the image entered, providing key information for further image-related operations.
    - Comfy dtype: INT
    - Python dtype: int
- height_int
    - The header_int output represents the vertical dimension of the input image, which is essential for understanding the image structure and subsequent image processing tasks.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class imageSize:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',)}}
    RETURN_TYPES = ('INT', 'INT')
    RETURN_NAMES = ('width_int', 'height_int')
    OUTPUT_NODE = True
    FUNCTION = 'image_width_height'
    CATEGORY = 'EasyUse/Image'

    def image_width_height(self, image):
        (_, raw_H, raw_W, _) = image.shape
        width = raw_W
        height = raw_H
        if width is not None and height is not None:
            result = (width, height)
        else:
            result = (0, 0)
        return {'ui': {'text': 'Width: ' + str(width) + ' , Height: ' + str(height)}, 'result': result}
```