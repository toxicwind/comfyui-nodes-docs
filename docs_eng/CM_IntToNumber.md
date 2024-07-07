# Documentation
- Class name: IntToNumber
- Category: math/conversion
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

This node converts integer input into a digital format suitable for further processing, emphasizing the importance of data type conversion in the computational workflow.

# Input types
## Required
- a
    - The parameter 'a' is a key input that provides an integer value for the node. The correct input is essential for the node to accurately execute the conversion and impact final result.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- result
    - The output of the node is in the form of an integer numeric expression that is essential for the subsequent operation of the numerical data required.
    - Comfy dtype: NUMBER
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class IntToNumber:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'a': ('INT', {'default': 0})}}
    RETURN_TYPES = ('NUMBER',)
    FUNCTION = 'op'
    CATEGORY = 'math/conversion'

    def op(self, a: int) -> tuple[number]:
        return (a,)
```