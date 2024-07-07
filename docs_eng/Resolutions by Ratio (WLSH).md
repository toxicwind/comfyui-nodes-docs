# Documentation
- Class name: WLSH_Resolutions_by_Ratio
- Category: WLSH Nodes/number
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The WLSH_Resultions_by_Radio nodes' method is designed to calculate the width and height of the image based on the given width ratio, direction and shorter edge length. It first determines the scale from the width margin string and then calculates the width based on the short edge length and ratio. The method also considers the direction of the image and, if it is vertical, exchanges width and height. This node plays a key role in image processing and display settings, where width and direction are essential.

# Input types
## Required
- aspect
    - The parameter 'aspect' defines the width ratio of the image, which is essential for determining the correct size. It is a string that represents the scale, for example, '16:9'. In adjusting the image for a large hour, the width ratio is essential for maintaining the shape and proportion of the image.
    - Comfy dtype: STR
    - Python dtype: str
- direction
    - The parameter 'direction' specifies the direction of the image, which can be 'landscape' (horizontal) or 'portrait' (vertical). This parameter is important because it affects the calculation of width and height and ensures that the size is appropriate for the given direction.
    - Comfy dtype: STR
    - Python dtype: str
- shortside
    - The parameter'shortside' indicates the length of the shorter edge of the image. It is a key input because it directly affects calculations based on width and direction. This method ensures that the width is optimized for display or processing purposes.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- width
    - The output parameter'width' provides the width of the image calculated after considering the width ratio, direction and shorter edge length. It is important to ensure that the image is suitable for the required display or processing limits.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The output parameter 'height' provides the image height calculated after considering the width ratio, direction and shorter edge length. It plays an important role in maintaining the image ratio and ensuring that the display requirements are met.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Resolutions_by_Ratio:
    aspects = ['1:1', '6:5', '5:4', '4:3', '3:2', '16:10', '16:9', '21:9', '2:1', '3:1', '4:1']
    direction = ['landscape', 'portrait']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'aspect': (s.aspects,), 'direction': (s.direction,), 'shortside': ('INT', {'default': 512, 'min': 64, 'max': MAX_RESOLUTION, 'step': 64})}}
    RETURN_TYPES = ('INT', 'INT')
    RETURN_NAMES = ('width', 'height')
    FUNCTION = 'get_resolutions'
    CATEGORY = 'WLSH Nodes/number'

    def get_resolutions(self, aspect, direction, shortside):
        (x, y) = aspect.split(':')
        x = int(x)
        y = int(y)
        ratio = x / y
        width = int(shortside * ratio)
        width = width + 63 & -64
        height = shortside
        if direction == 'portrait':
            (width, height) = (height, width)
        return (width, height)
```