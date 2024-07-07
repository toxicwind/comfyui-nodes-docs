# Documentation
- Class name: WLSH_Int_Multiply
- Category: WLSH Nodes/number
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The node performs an integer multiplier, which is a basic arithmetic operation that expands the given number by specified multipliers and facilitates a variety of mathematical and data-processing tasks in the workflow.

# Input types
## Required
- number
    - The `number' parameter is multiplied by the base integer value of `multiplier'. It is essential for the operation of the node, as it defines the initial value during the multiplication process.
    - Comfy dtype: INT
    - Python dtype: int
- multiplier
    - The `multiplier' parameter determines the multiplier of the `number' parameter. This is essential for the function of the node, as it determines the degree of magnification applied to the initial value.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- result
    - The results of the integer-multiplier operation are effectively demonstrated by the `result' output, which represents the multipliers of `number' and `multiplier'.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Int_Multiply:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'number': ('INT', {'default': 2, 'min': 1, 'max': 10000, 'forceInput': True}), 'multiplier': ('INT', {'default': 2, 'min': 1, 'max': 10000})}}
    RETURN_TYPES = ('INT',)
    FUNCTION = 'multiply'
    CATEGORY = 'WLSH Nodes/number'

    def multiply(self, number, multiplier):
        result = number * multiplier
        return (int(result),)
```