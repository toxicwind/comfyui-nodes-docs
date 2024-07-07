# Documentation
- Class name: WAS_Image_Aspect_Ratio
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `aspect'method of the WAS_Image_Aspect_Ratio node is designed to calculate and return multiple proportional expressions of the image. It determines whether the image is overscreened or overscreened and provides a common scale in simplified form. This node is essential for image operation and analysis tasks, and proportionality considerations are key.

# Input types
## Optional
- image
    - The 'image'parameter is an optional input that allows the width and height of an automatic derived image when node does not provide a visible size. When providing image lengths, it is essential for the ability of the node to accurately calculate the vertical ratio.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- width
    - The 'width' parameter is an optional number input that specifies the width of the image. When an image is not provided, it is used to calculate the vertical ratio with the 'height' parameter.
    - Comfy dtype: NUMBER
    - Python dtype: int
- height
    - The 'height' parameter is an optional number input that specifies the height of the image. Together with the 'width' parameter, it is necessary to determine the vertical ratio when the image length is not provided.
    - Comfy dtype: NUMBER
    - Python dtype: int

# Output types
- aspect_number
    - The 'aspect_number' output provides the original number vertical ratio of the image, which is calculated as the width divided by height.
    - Comfy dtype: NUMBER
    - Python dtype: float
- aspect_float
    - The `aspect_float' output is another expression of the vertical ratio and is divided by width by height, but returns as a number of floating points.
    - Comfy dtype: FLOAT
    - Python dtype: float
- is_landscape_bool
    - The `is_landscape_bool' output is a boolean value that indicates whether the image is in screen mode. For screen return 1, for screens or squares return 0.
    - Comfy dtype: NUMBER
    - Python dtype: int
- aspect_ratio_common
    - The "aspect_ratio_common' output, for example '16:9', is a common horizontal ratio of images in simplified form, derived from the maximum number of conventions of width and height.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str
- aspect_type
    - The `aspect_type' output describes the type of `landscape', `portrait' or `square', based on the calculated vertical ratio.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Aspect_Ratio:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}, 'optional': {'image': ('IMAGE',), 'width': ('NUMBER',), 'height': ('NUMBER',)}}
    RETURN_TYPES = ('NUMBER', 'FLOAT', 'NUMBER', TEXT_TYPE, TEXT_TYPE)
    RETURN_NAMES = ('aspect_number', 'aspect_float', 'is_landscape_bool', 'aspect_ratio_common', 'aspect_type')
    FUNCTION = 'aspect'
    CATEGORY = 'WAS Suite/Logic'

    def aspect(self, boolean=True, image=None, width=None, height=None):
        if width and height:
            width = width
            height = height
        elif image is not None:
            (width, height) = tensor2pil(image).size
        else:
            raise Exception('WAS_Image_Aspect_Ratio must have width and height provided if no image tensori supplied.')
        aspect_ratio = width / height
        aspect_type = 'landscape' if aspect_ratio > 1 else 'portrait' if aspect_ratio < 1 else 'square'
        landscape_bool = 0
        if aspect_type == 'landscape':
            landscape_bool = 1
        gcd = math.gcd(width, height)
        gcd_w = width // gcd
        gcd_h = height // gcd
        aspect_ratio_common = f'{gcd_w}:{gcd_h}'
        return (aspect_ratio, aspect_ratio, landscape_bool, aspect_ratio_common, aspect_type)
```