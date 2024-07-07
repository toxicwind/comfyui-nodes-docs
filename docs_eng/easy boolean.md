# Documentation
- Class name: Boolean
- Category: EasyUse/Logic/Type
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node class covers the logic of handling the boolean values, making it possible to perform the basic operation and conversion of the logical data processing.

# Input types
## Required
- value
    - The `value' parameter is essential because it determines the input of the Boolean operation. It is the basic element for applying node logic and directly influences the results of node execution.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- boolean
    - Outputs the result of a boolean operation performed by 'boolean' on the node. This is a key data segment that can be used for further logical decision-making or as a condition in the workflow.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class Boolean:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'value': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('BOOLEAN',)
    RETURN_NAMES = ('boolean',)
    FUNCTION = 'execute'
    CATEGORY = 'EasyUse/Logic/Type'

    def execute(self, value):
        return (value,)
```