# Documentation
- Class name: WAS_Number_To_String
- Category: WAS Suite/Number/Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Numer_To_String node is designed to convert values into the corresponding string expression. This node plays a vital role in data pre-processing and conversion workflows, enabling numerical data to be integrated seamlessly into the system that requires text input.

# Input types
## Required
- number
    - The `number'parameter is essential for the operation of the node because it is the input value that needs to be converted to a string. It significantly influences the node by deciding the content of the output string.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float]

# Output types
- string
    - The `string' output parameter indicates the text form of the input number. It is important because it provides post-conversion data that can be used for various downstream applications or processes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Number_To_String:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'number': ('NUMBER',)}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'number_to_string'
    CATEGORY = 'WAS Suite/Number/Operations'

    def number_to_string(self, number):
        return (str(number),)
```