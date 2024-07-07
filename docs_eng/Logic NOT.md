# Documentation
- Class name: WAS_Logical_NOT
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Legal_NOT node is designed to apply logical non-operational to Boolean input. It reverses the real value and provides a simple mechanism for denying the boolean conditions in the workflow. In the decision-making process, this node plays a key role when it is needed to reverse the boolean state.

# Input types
## Required
- boolean
    - The " boolean " parameter is the key input to the WAS_Logical_NOT node. It is a boolean value and node will be denied. The significance of this parameter is that it is capable of controlling the logical state of the subsequent operation, which is essential for the condition flow.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- result
    - WAS_Logical_NOT node's `Result' output represents the logic for entering a boolean value. Its importance is that it directly influences the logical process in the system and allows the construction of complex conditional statements.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Logical_NOT:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'boolean': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('BOOLEAN',)
    FUNCTION = 'do'
    CATEGORY = 'WAS Suite/Logic'

    def do(self, boolean):
        return (not boolean,)
```