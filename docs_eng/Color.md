# Documentation
- Class name: ColorInput
- Category: ♾️Mixlab/Utils
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node facilitates the processing and extraction of input colour information and provides detailed analysis of colour components in a structured format.

# Input types
## Required
- color
    - Colour parameters are essential for the running of nodes, as they are the main source of data for colour analysis.
    - Comfy dtype: TCOLOR
    - Python dtype: Dict[str, Union[str, int]]

# Output types
- hex
    - Hexadecimal output represents a hexadecimal colour code and is a standard expression in web page and graphic design.
    - Comfy dtype: STRING
    - Python dtype: str
- r
    - r The output represents the red fraction of the colour, which contributes to the overall tone and saturation.
    - Comfy dtype: INT
    - Python dtype: int
- g
    - g The output represents the green fraction, which affects the middle tone of the colour.
    - Comfy dtype: INT
    - Python dtype: int
- b
    - b The output corresponds to the blue fraction and affects the coolness or heat of the colour.
    - Comfy dtype: INT
    - Python dtype: int
- a
    - a The output represents the alpha channel, indicating the level of transparency of the colour.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class ColorInput:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'color': ('TCOLOR',)}}
    RETURN_TYPES = ('STRING', 'INT', 'INT', 'INT', 'FLOAT')
    RETURN_NAMES = ('hex', 'r', 'g', 'b', 'a')
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Utils'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False, False, False, False, False)

    def run(self, color):
        h = color['hex']
        r = color['r']
        g = color['g']
        b = color['b']
        a = color['a']
        return (h, r, g, b, a)
```