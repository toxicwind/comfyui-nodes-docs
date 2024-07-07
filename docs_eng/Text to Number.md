# Documentation
- Class name: WAS_Text_To_Number
- Category: WAS Suite/Text/Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

This node converts text data to values to enable further processing and analysis in numerical format.

# Input types
## Required
- text
    - Text parameters are necessary, providing raw text data that needs to be converted to digital format. It is the main input that determines node output.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- NUMBER
    - Output is the value of the input text, which may be an integer or floating point, depending on the content of the text.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_To_Number:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False})}}
    RETURN_TYPES = ('NUMBER',)
    FUNCTION = 'text_to_number'
    CATEGORY = 'WAS Suite/Text/Operations'

    def text_to_number(self, text):
        if text.replace('.', '').isnumeric():
            number = float(text)
        else:
            number = int(text)
        return (number,)
```