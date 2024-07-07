# Documentation
- Class name: CR_FloatToString
- Category: Comfyroll/Utils/Conversion
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_FloatToString is designed to convert floating points into their string expression. This conversion is essential for various applications that require the display or processing of numerical data in text format. The node plays a central role in data pre-processing, and is used to generate reports, interface with systems that require text input, or integrates databases that store numerical data as strings.

# Input types
## Required
- float_
    - The 'float_' parameter is a float number, and the node converts it to a string. This is a basic input, because all operations of the node are around this value. The conversion process ensures that the value data can be used in the context in which the string format is required.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- STRING
    - The 'STRING' output provides a string for input float numbers. This output is important because it is the main result of node operations and allows users to use converted strings in subsequent processes or applications.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The'show_help' output is a URL string that points the user to the help document of the node. It is a convenient reference when the user requires additional information or guidance for the effective use of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_FloatToString:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'float_': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1000000.0, 'forceInput': True})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    FUNCTION = 'convert'
    CATEGORY = icons.get('Comfyroll/Utils/Conversion')

    def convert(self, float_):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Conversion-Nodes#cr-float-to-string'
        return (f'{float_}', show_help)
```