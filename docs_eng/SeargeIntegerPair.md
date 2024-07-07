# Documentation
- Class name: SeargeIntegerPair
- Category: Searge/_deprecated_/Integers
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node is designed to process and return integer logarithms and is a basic component of the workflow involved in numerical analysis or data operations.

# Input types
## Required
- value1
    - This is essential for the first integer in the middle and for the operation of the node, as it forms the basis for the numerical relationship.
    - Comfy dtype: INT
    - Python dtype: int
- value2
    - This second integer of the pair, together with the first value, completes the numeric set and influences the output of the nodes.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- value 1
    - The first element of the output array represents the initial integer value provided to the node.
    - Comfy dtype: INT
    - Python dtype: int
- value 2
    - The second element of the output array represents the second integer value provided to the node.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeIntegerPair:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'value1': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'value2': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('INT', 'INT')
    RETURN_NAMES = ('value 1', 'value 2')
    FUNCTION = 'get_value'
    CATEGORY = 'Searge/_deprecated_/Integers'

    def get_value(self, value1, value2):
        return (value1, value2)
```