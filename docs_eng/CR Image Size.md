# Documentation
- Class name: CR_ImageSize
- Category: Comfyroll/Essential/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_ImageSize node is designed to adjust the size of the image. It provides the function to specify the width and height of the image and allows for magnification through a adjustable factor. In the image processing workflow that requires a size adjustment, this node is essential to ensure that the image meets the size required for further processing or display.

# Input types
## Required
- width
    - The `width' parameter is essential for defining the desired width of the image. It plays a key role in determining the final dimensions of the post-processed image. `width' sets the width ratio and overall appearance that directly influences the image.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height'parameter is used to set the vertical dimensions of the image. It is a key factor in controlling the size of the image's output and ensuring that it meets specific requirements or limitations. The 'height'value is important for maintaining the integrity of the image content.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- upscale_factor
    - The `upscale_factor' parameter is optional and is used to increase the size of the image. It is a multiplier that increases the original size proportionally and allows higher resolution output. This factor is particularly useful when enhancing image details or preparing images for larger monitors.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- Width
    - The `Width' output reflects the processing width of the image after applying the node resize function. It is important for downstream processes that rely on the exact size of the image.
    - Comfy dtype: INT
    - Python dtype: int
- Height
    - The `Height' output provides the height of the image processing, which is essential to maintain the expected width ratio and to ensure that the image is suitable for the given display area.
    - Comfy dtype: INT
    - Python dtype: int
- upscale_factor
    - `upscape_factor' output is the zoom factor applied to the image. It shows how much of the original size has been increased, which may be important for quality assessment or further image operations.
    - Comfy dtype: FLOAT
    - Python dtype: float
- show_help
    - The `show_help' output refers to the URL link to the node that describes the page. It is particularly useful for users seeking more information on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ImageSize:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 512, 'min': 64, 'max': 2048}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 2048}), 'upscale_factor': ('FLOAT', {'default': 1, 'min': 1, 'max': 2000})}}
    RETURN_TYPES = ('INT', 'INT', 'FLOAT', 'STRING')
    RETURN_NAMES = ('Width', 'Height', 'upscale_factor', 'show_help')
    FUNCTION = 'ImageSize'
    CATEGORY = icons.get('Comfyroll/Essential/Legacy')

    def ImageSize(self, width, height, upscale_factor):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Legacy-Nodes#cr-image-size'
        return (width, height, upscale_factor, show_help)
```