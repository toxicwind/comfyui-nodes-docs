# Documentation
- Class name: WAS_Boolean_Primitive
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `do'method for the WAS_Boolean_Primitive node is designed to process and return a boolean value. As the basic building block in the logical operation, it ensures the integrity of the boolean calculation in the workflow.

# Input types
## Required
- boolean
    - The " boolean " parameter is essential to the operation of the node because it directly affects the logical outcome of the do-do method. It is the main input that determines the node behaviour and the result boolean value.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- result
    - The “redault” output parameter represents the result of a boolean calculation executed by the do method. It is important because it provides the final boolean value after processing the input.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Boolean_Primitive:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'boolean': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('BOOLEAN',)
    FUNCTION = 'do'
    CATEGORY = 'WAS Suite/Logic'

    def do(self, boolean):
        return (boolean,)
```