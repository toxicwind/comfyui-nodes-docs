# Documentation
- Class name: WAS_Number_To_Float
- Category: WAS Suite/Number/Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Number_To_Float node is designed to convert the number entered into their floating-point equivalents. This node plays a vital role in the pre-processing of data for downstream operations by ensuring numerical consistency and compatibility.

# Input types
## Required
- number
    - The `number' parameter is essential for the operation of the node, because it is an input that will be converted to floating points. This conversion is important for maintaining numerical accuracy and promoting further mathematical calculations.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float, str]

# Output types
- float_number
    - The 'float_number'output is the result of the conversion process and provides a floating point for input numbers. This output is essential for any subsequent numerical analysis or operation that requires decimal accuracy.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Number_To_Float:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'number': ('NUMBER',)}}
    RETURN_TYPES = ('FLOAT',)
    FUNCTION = 'number_to_float'
    CATEGORY = 'WAS Suite/Number/Operations'

    def number_to_float(self, number):
        return (float(number),)
```