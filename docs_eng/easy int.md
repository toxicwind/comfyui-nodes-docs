# Documentation
- Class name: Int
- Category: EasyUse/Logic/Type
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

This node facilitates the operation of arithmetical operations by converting input into integer numbers, ensuring data integrity and type consistency in the calculation process.

# Input types
## Required
- value
    - The `value' parameter is essential because it is the main input for node operations. It influences node processing by determining the data to be converted into integer numbers.
    - Comfy dtype: INT
    - Python dtype: Union[int, float, str, Decimal]

# Output types
- int
    - Output of `int' represents the results of the integer conversion process, which is essential to ensure that the correct data type is used in subsequent operations.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class Int:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'value': ('INT', {'default': 0})}}
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('int',)
    FUNCTION = 'execute'
    CATEGORY = 'EasyUse/Logic/Type'

    def execute(self, value):
        return (value,)
```