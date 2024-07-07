# Documentation
- Class name: CR_FloatToInteger
- Category: Comfyroll/Utils/Conversion
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_FloatToInteger node is designed to convert floating points into their integer equivalents. It plays a key role in data processing by ensuring consistency and compatibility of values in different computing tasks. This node is particularly useful when only the integer values are acceptable or necessary.

# Input types
## Required
- _float
    - _float parameters are essential for the operation of nodes because they are input floats that need to be converted into integer numbers. Their conversion is essential for all mathematical and logical operations that require integer input.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- INT
    - The INT output represents the integer conversion of input floats. It is important because it provides a discrete value that can be used in calculations that only integer values allow.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - Show_help output provides a URL link to a document for further help. It is a useful resource for users seeking more information about node functions and usages.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_FloatToInteger:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'_float': ('FLOAT', {'default': 0.0, 'forceInput': True, 'forceInput': True})}}
    RETURN_TYPES = ('INT', 'STRING')
    RETURN_NAMES = ('INT', 'show_help')
    FUNCTION = 'convert'
    CATEGORY = icons.get('Comfyroll/Utils/Conversion')

    def convert(self, _float):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Conversion-Nodes#cr-float-to-integer'
        return (int(_float), show_help)
```