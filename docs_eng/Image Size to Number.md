# Documentation
- Class name: WAS_Image_Size_To_Number
- Category: WAS Suite/Number/Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Size_To_Number node is designed to extract the size of the image and convert it to a value. It provides a direct method of obtaining the width and height of the image, in different formats, to facilitate further processing or analysis, which requires numeric dimensions information.

# Input types
## Required
- image
    - The image parameter is essential for the operation of the node, as it is the source of the extraction size. It directly influences the output of the node by determining the value of return.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or numpy.ndarray

# Output types
- width_num
    - Width_num represents the integer value of the image width. It is important because it provides a numerical measure of the image width that can be used for various purposes, such as resizing or layout calculations.
    - Comfy dtype: NUMBER
    - Python dtype: int
- height_num
    - The header_num indicates the integer value of the image height. It is essential for applications that need to know the vertical range of the image, such as printing or displaying adjustments.
    - Comfy dtype: NUMBER
    - Python dtype: int
- width_float
    - Width_float provides a floating point value for image width that allows for more accurate measurements and calculations when necessary.
    - Comfy dtype: FLOAT
    - Python dtype: float
- height_float
    - Height_float provides floating point values at image height, which are very useful for applications requiring high accuracy in vertical measurements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- width_int
    - Width_int is another integer expression of image width, providing interchangeable values that can be used with width_num for different applications.
    - Comfy dtype: INT
    - Python dtype: int
- height_int
    - Height_int is another integer value for image height, providing another value for applications that may be preferred or required for this particular format.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Size_To_Number:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',)}}
    RETURN_TYPES = ('NUMBER', 'NUMBER', 'FLOAT', 'FLOAT', 'INT', 'INT')
    RETURN_NAMES = ('width_num', 'height_num', 'width_float', 'height_float', 'width_int', 'height_int')
    FUNCTION = 'image_width_height'
    CATEGORY = 'WAS Suite/Number/Operations'

    def image_width_height(self, image):
        image = tensor2pil(image)
        if image.size:
            return (image.size[0], image.size[1], float(image.size[0]), float(image.size[1]), image.size[0], image.size[1])
        return (0, 0, 0, 0, 0, 0)
```