# Documentation
- Class name: WAS_Integer_Place_Counter
- Category: WAS Suite/Integer
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

This node is intended to calculate the number of digits in an integer value. It serves as a basic tool for applications that require numeric operations, such as numerical analysis or data processing.

# Input types
## Required
- int_input
    - To determine the integer input of the number of digits. It is the main data element of the node operation, which directly influences the result.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- INT_PLACES
    - The output represents the number of digits in an integer number. It is important for applications that need to know the length of the number.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Integer_Place_Counter:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'int_input': ('INT', {'default': 0, 'min': 0, 'max': 10000000, 'step': 1})}}
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('INT_PLACES',)
    FUNCTION = 'count_places'
    CATEGORY = 'WAS Suite/Integer'

    def count_places(self, int_input):
        output = len(str(int_input))
        cstr('\nInteger Places Count: ' + str(output)).msg.print()
        return (output,)
```