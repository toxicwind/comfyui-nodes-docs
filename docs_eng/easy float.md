# Documentation
- Class name: Float
- Category: EasyUse/Logic/Type
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

This node provides the basis for floating-point processing, focusing on the operation and calculation of small values within the specified accuracy.

# Input types
## Required
- value
    - The `value' parameter is essential for the operation of the node, which is an input small value for the operation or calculation of the node.
    - Comfy dtype: FLOAT
    - Python dtype: Union[Decimal, float, int]

# Output types
- float
    - Output `float' represents the result of the calculation or operation of the node, reflecting the values processed.
    - Comfy dtype: FLOAT
    - Python dtype: Union[Decimal, float]

# Usage tips
- Infra type: CPU

# Source code
```
class Float:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'value': ('FLOAT', {'default': 0, 'step': 0.01})}}
    RETURN_TYPES = ('FLOAT',)
    RETURN_NAMES = ('float',)
    FUNCTION = 'execute'
    CATEGORY = 'EasyUse/Logic/Type'

    def execute(self, value):
        return (value,)
```