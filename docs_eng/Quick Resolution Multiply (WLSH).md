# Documentation
- Class name: WLSH_Res_Multiply
- Category: WLSH Nodes/number
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The WLSH_Res_Mulliply node is designed to perform multiplier operations for width and height, scaled according to the multipliers provided. It plays a crucial role in adjusting the size of images or similar geometric entities to ensure that the zoom factor is applied equally to both dimensions.

# Input types
## Required
- width
    - The `width' parameter represents the initial width of the entity to be scaled. It is essential for the operation of the node, as it determines the starting point of the multiplying process. Once the width is multiplied by a multiplier, the new width of the scaling is defined.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The `height' parameter represents the initial height of the pre-scaling entity. It is the key input for the node, as it determines the vertical dimension that will be influenced by the multiplier. The final height after the operation will reflect the height of the scaling.
    - Comfy dtype: INT
    - Python dtype: int
- multiplier
    - The'multiplier' parameter is the factor that the width and height will be scaled. It is a key component of the node because it directly affects the range of the scaling operation. The proper selection of the multiplier is essential to achieve the size required.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- width
    - The `width' output represents the contraction of the entity after the multiplication operation. It is important because it provides a new width measurement from the scaling process.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - 'Height'output indicates the height of the entity by multiplying. It is an important result of node operations, as it provides a new altimeter value after scaling.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Res_Multiply:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'width': ('INT', {'default': 512, 'min': 16, 'max': MAX_RESOLUTION, 'forceInput': True}), 'height': ('INT', {'default': 512, 'min': 16, 'max': MAX_RESOLUTION, 'forceInput': True}), 'multiplier': ('INT', {'default': 2, 'min': 1, 'max': 10000})}}
    RETURN_TYPES = ('INT', 'INT')
    RETURN_NAMES = ('width', 'height')
    FUNCTION = 'multiply'
    CATEGORY = 'WLSH Nodes/number'

    def multiply(self, width, height, multiplier):
        adj_width = width * multiplier
        adj_height = height * multiplier
        return (int(adj_width), int(adj_height))
```