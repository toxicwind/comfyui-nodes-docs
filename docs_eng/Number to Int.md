# Documentation
- Class name: WAS_Number_To_Int
- Category: WAS Suite/Number/Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `number_to_int' method of the WAS_numer_To_Int node is designed to convert the number entered into their integer equivalents. It plays a key role in the pre-processing of data, by ensuring numerical consistency and promoting further numerical operations.

# Input types
## Required
- number
    - The " number " parameter is essential to the operation of the node because it is to be converted to an integer input. It is important because the accuracy and completeness of the conversion depends on the quality of the input.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float, str]

# Output types
- int_value
    - The 'int_value'output represents the integer conversion of the input number. It is important because it directly reflects the result of the primary function of the node and provides a consistent and usable format for the follow-up process.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Number_To_Int:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'number': ('NUMBER',)}}
    RETURN_TYPES = ('INT',)
    FUNCTION = 'number_to_int'
    CATEGORY = 'WAS Suite/Number/Operations'

    def number_to_int(self, number):
        return (int(number),)
```