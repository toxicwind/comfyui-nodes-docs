# Documentation
- Class name: CR_IntegerToString
- Category: Comfyroll/Utils/Conversion
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_IntegerToString node is designed to transform the whole value seamlessly into the corresponding string expression. In a scenario where numerical data are to be interpreted or displayed in text format, this conversion process is essential. The node plays a key role in data operation and conversion tasks to ensure that the conversion from value to text form is accurate and reliable.

# Input types
## Required
- int_
    - The 'int_'parameter is the core input of the node, representing the whole value that needs to be converted to a string. Its conversion is essential for the operation of the node, as it directly affects the output and the subsequent processing of data.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- STRING
    - The `STRING' output parameter represents the string form in which an integer is entered. It is the main result of the node conversion process and marks the successful conversion of numerical data into a human readable format.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The'show_help' output provides a URL link to the document for further help. It is a useful resource for users to seek more information about node functions and uses.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_IntegerToString:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'int_': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615, 'forceInput': True})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    FUNCTION = 'convert'
    CATEGORY = icons.get('Comfyroll/Utils/Conversion')

    def convert(self, int_):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Conversion-Nodes#cr-integer-to-string'
        return (f'{int_}', show_help)
```