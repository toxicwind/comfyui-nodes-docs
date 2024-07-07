# Documentation
- Class name: SeargeIntegerMath
- Category: Searge/_deprecated_/Integers
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node implements integer algorithms according to the choice of the user and facilitates the processing and conversion of whole data within the system.

# Input types
## Required
- op
    - The operational parameters determine the arithmetic function to be applied and are the cornerstone of the node calculation process.
    - Comfy dtype: COMBO[SeargeIntegerMath.OPERATIONS]
    - Python dtype: str
- a
    - The parameter `a' represents the first number of operations in the integer calculation and plays a crucial role in determining the results of the calculation.
    - Comfy dtype: INT
    - Python dtype: int
- b
    - The parameter `b' is the second number of operations performed by multiplying and dividing, which has a significant impact on the final result.
    - Comfy dtype: INT
    - Python dtype: int
- c
    - The parameter'c' is the third number of operations in addition and subtraction operations that affect the overall calculation.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- result
    - The output'reult' shows the calculation value after the application of the selected arithmetic and represents the final result of the node function.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeIntegerMath:
    OPERATIONS = ['a * b + c', 'a + c', 'a - c', 'a * b', 'a / b']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'op': (SeargeIntegerMath.OPERATIONS, {'default': 'a * b + c'}), 'a': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'b': ('INT', {'default': 1, 'min': 0, 'max': 18446744073709551615}), 'c': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('result',)
    FUNCTION = 'get_value'
    CATEGORY = 'Searge/_deprecated_/Integers'

    def get_value(self, op, a, b, c):
        res = 0
        if op == 'a * b + c':
            res = a * b + c
        elif op == 'a + c':
            res = a + c
        elif op == 'a - c':
            res = a - c
        elif op == 'a * b':
            res = a * b
        elif op == 'a / b':
            res = a // b
        return (int(res),)
```