# Documentation
- Class name: INTConstant
- Category: KJNodes/constants
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

The INTConstant node is intended to provide a constant integer value in the network. When an operation requires a fixed integer, such as an index, a threshold or any scenario that requires a constant value, it is used. This node ensures that the value remains constant during implementation, providing a stable and predictable integer reference.

# Input types
## Required
- value
    - The `value' parameter is the core of the INTConstant node, which represents the constant integer to be exported. It plays a key role in node operations, as it defines the fixed integer value to be provided to the network. The significance of this parameter is that it provides consistent and constant integer references to the various computational tasks.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- value
    - The `value' output from INTConstant is the constant integer set as input. It serves as a reliable source of fixed integer numbers for downstream operations in the network, ensuring that the value remains constant and is not subject to external influence.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class INTConstant:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'value': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('value',)
    FUNCTION = 'get_value'
    CATEGORY = 'KJNodes/constants'

    def get_value(self, value):
        return (value,)
```