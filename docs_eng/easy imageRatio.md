# Documentation
- Class name: imageRatio
- Category: EasyUse/Image
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node category is designed to process images and calculate the maximum convention number (GCD) of their size, thereby determining the width ratio between the integer and the floating point ratio. The purpose is to simplify the analysis of the image ratio so that it can be further processed or displayed.

# Input types
## Required
- image
    - The image parameter is essential for the node because it is the main input the size is analysed to calculate the width ratio. Without this input, the node cannot perform its intended function.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray

# Output types
- result
    - This output provides a calculated width ratio for the input image, including integer and floating point formats. It is important because it clearly illustrates the relationship between image sizes, which is very useful for various image processing tasks.
    - Comfy dtype: COMBO[INT, INT, FLOAT, FLOAT]
    - Python dtype: Tuple[int, int, float, float]
- ui
    - The `ui' output is a dictionary containing text information that provides a human readable summary of image width. This output is very useful for showing results in the user interface and enhances user experience by presenting data in an easily understandable format.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, str]

# Usage tips
- Infra type: CPU

# Source code
```
class imageRatio:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',)}}
    RETURN_TYPES = ('INT', 'INT', 'FLOAT', 'FLOAT')
    RETURN_NAMES = ('width_ratio_int', 'height_ratio_int', 'width_ratio_float', 'height_ratio_float')
    OUTPUT_NODE = True
    FUNCTION = 'image_ratio'
    CATEGORY = 'EasyUse/Image'

    def gcf(self, a, b):
        while b:
            (a, b) = (b, a % b)
        return a

    def image_ratio(self, image):
        (_, raw_H, raw_W, _) = image.shape
        width = raw_W
        height = raw_H
        ratio = self.gcf(width, height)
        if width is not None and height is not None:
            width_ratio = width // ratio
            height_ratio = height // ratio
            result = (width_ratio, height_ratio, width_ratio, height_ratio)
        else:
            width_ratio = 0
            height_ratio = 0
            result = (0, 0, 0.0, 0.0)
        text = f'Image Ratio is {str(width_ratio)}:{str(height_ratio)}'
        return {'ui': {'text': text}, 'result': result}
```