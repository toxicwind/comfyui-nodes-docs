# Documentation
- Class name: WAS_Image_Blank
- Category: WAS Suite/Image
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Blank node is designed to generate blank images with specified sizes and colours. It plays a key role in creating visual canvass for further image processing tasks. This node is essential for initializing images with the required size and colour properties, and can then operate on images or be used as a starting point for various image-related operations.

# Input types
## Required
- width
    - The `width' parameter defines the width of the blank image to be generated. This is a basic attribute that determines the horizontal range of the image. `width' is essential for setting the size of the image and influencing the overall composition and layout of any subsequent image processing.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height'parameter sets the vertical dimensions of the blank image. It is as important as width in defining the overall shape and structure of the image. This parameter ensures that the image is created with the required vertical range, which is important to align with other visual elements or to meet specific display requirements.
    - Comfy dtype: INT
    - Python dtype: int
- red
    - The `red' parameter specifies the strength of the red channel in the blank image. It is a key component in determining the color of the image as a whole. By adjusting the `red' value, the user can create images with a specific red shadow that can be used for various purposes, such as background colours or colour filters.
    - Comfy dtype: INT
    - Python dtype: int
- green
    - The `green' parameter controls the strength of the green channel in the image. It works with the red and blue parameters to produce the final colour of the blank image. The `green' value is important for achieving the required colour balance and tone, which may be essential for some design or visual needs.
    - Comfy dtype: INT
    - Python dtype: int
- blue
    - The `blue' parameter determines the strength of the blue channel and helps to form the overall colour of the blank image. It is an essential element of the colour mix, allowing users to fine-tune the colour of the image to meet specific visual or aesthetic standards.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The `IMAGE' output provides a blank image with a specified size and colour. It provides the base layer for any subsequent image operation or processing task. This output is important because it represents the main result of node functions and is prepared for downstream workflows.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Blank:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'width': ('INT', {'default': 512, 'min': 8, 'max': 4096, 'step': 1}), 'height': ('INT', {'default': 512, 'min': 8, 'max': 4096, 'step': 1}), 'red': ('INT', {'default': 255, 'min': 0, 'max': 255, 'step': 1}), 'green': ('INT', {'default': 255, 'min': 0, 'max': 255, 'step': 1}), 'blue': ('INT', {'default': 255, 'min': 0, 'max': 255, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'blank_image'
    CATEGORY = 'WAS Suite/Image'

    def blank_image(self, width, height, red, green, blue):
        width = width // 8 * 8
        height = height // 8 * 8
        blank = Image.new(mode='RGB', size=(width, height), color=(red, green, blue))
        return (pil2tensor(blank),)
```