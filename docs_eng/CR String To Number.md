# Documentation
- Class name: CR_StringToNumber
- Category: Comfyroll/Utils/Conversion
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_StringToNumber node is designed to convert given strings into numerical formats, which can be integer or floating points. It handles numerical strings by providing rounding options, thus ensuring that the output meets specific requirements and providing flexibility.

# Input types
## Required
- text
    - The 'text' parameter is the string that needs to be converted to a number. It is the basic input for node operations, as it directly affects the conversion process and the final numerical result.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- round_integer
    - The `round_integer' parameter determines how the string is rounded to the integer if necessary. It can be set as a standard rounded round for `round', `round down' always pouring down, or `round up' always picking up, affecting the accuracy and accuracy of the integer output.
    - Comfy dtype: COMBO['round', 'round down', 'round up']
    - Python dtype: str

# Output types
- INT
    - The `INT' output represents a string that is converted into an integer number according to the specified rounding method. It is important for an application that requires an integer value.
    - Comfy dtype: INT
    - Python dtype: int
- FLOAT
    - The 'FLOAT' output is a string that converts to floating points. It retains the decimal accuracy of the original string and is very useful for applications that require precise values.
    - Comfy dtype: FLOAT
    - Python dtype: float
- show_help
    - The'show_help' output provides a URL link to a document for further help. It is particularly useful for users seeking to use nodes or solve problems.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_StringToNumber:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': False, 'default': 'text', 'forceInput': True}), 'round_integer': (['round', 'round down', 'round up'],)}}
    RETURN_TYPES = ('INT', 'FLOAT', 'STRING')
    RETURN_NAMES = ('INT', 'FLOAT', 'show_help')
    FUNCTION = 'convert'
    CATEGORY = icons.get('Comfyroll/Utils/Conversion')

    def convert(self, text, round_integer):
        if text.startswith('-') and text[1:].replace('.', '', 1).isdigit():
            float_out = -float(text[1:])
        elif text.replace('.', '', 1).isdigit():
            float_out = float(text)
        else:
            print(f'[Error] CR String To Number. Not a number.')
            return {}
        if round_integer == 'round up':
            if text.startswith('-'):
                int_out = int(float_out)
            else:
                int_out = int(float_out) + 1
        elif round_integer == 'round down':
            if text.startswith('-'):
                int_out = int(float_out) - 1
            else:
                int_out = int(float_out)
        else:
            int_out = round(float_out)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Conversion-Nodes#cr-string-to-number'
        return (int_out, float_out, show_help)
```