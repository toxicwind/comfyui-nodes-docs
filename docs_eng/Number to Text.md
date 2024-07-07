# Documentation
- Class name: WAS_Number_To_Text
- Category: WAS Suite/Number/Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

This node converts the number input into a text expression, making the number easier to understand and use by downstream nodes or applications.

# Input types
## Required
- number
    - The `number' parameter is essential for the operation of the node, as it is an input that will be converted to text. This is a sine qua non for the node to perform its main function.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float, complex]

# Output types
- text
    - Output 'text'means the text form of the input number, which is the result of the node conversion process.
    - Comfy dtype: TEXT
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Number_To_Text:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'number': ('NUMBER',)}}
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'number_to_text'
    CATEGORY = 'WAS Suite/Number/Operations'

    def number_to_text(self, number):
        return (str(number),)
```