# Documentation
- Class name: WLSH_SDXL_Resolutions
- Category: WLSH Nodes/number
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The `get_resources' method at the WTSH_SDXL_Resultions nodes is designed to process image resolution and directional data. It accepts a string of resolution and a directional indicator as input, converts the resolution to an integer value of width and altitude and adjusts the values according to the direction provided, ensuring that the correct width ratio of the image or view direction is maintained.

# Input types
## Required
- resolution
    - The resolution parameter is a string that specifies the size of the image in 'widthxheight' format. It is essential for determining the pixel size of the image and is used to calculate width and height values.
    - Comfy dtype: str
    - Python dtype: str
- direction
    - The 'direction' parameter indicates the direction of the image, which can be 'landscape' or 'portrait'. This parameter is essential for adjusting the width and height values to match the given direction.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- width
    - The 'width' output represents the width of the image after considering the 'direction' input. It is an integer value, reflecting the number of pixels on the horizontal axis of the image.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height'output corresponds to the image height of the adjusted direction. It is an integer number, which represents the number of pixels on the vertical axis of the image.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_SDXL_Resolutions:
    resolution = ['1024x1024', '1152x896', '1216x832', '1344x768', '1536x640']
    direction = ['landscape', 'portrait']

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'resolution': (s.resolution,), 'direction': (s.direction,)}}
    RETURN_TYPES = ('INT', 'INT')
    RETURN_NAMES = ('width', 'height')
    FUNCTION = 'get_resolutions'
    CATEGORY = 'WLSH Nodes/number'

    def get_resolutions(self, resolution, direction):
        (width, height) = resolution.split('x')
        width = int(width)
        height = int(height)
        if direction == 'portrait':
            (width, height) = (height, width)
        return (width, height)
```