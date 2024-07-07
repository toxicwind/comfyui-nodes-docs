# Documentation
- Class name: IntToBool
- Category: math/conversion
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The IntToBool node is intended to convert the integer value to a Boolean expression. Where the existence of the value is essential, it is a basic practical tool for abstracting the concept of true value from the numerical data. This node plays a key role in the data type conversion to ensure that the value is properly interpreted in the boolean context.

# Input types
## Required
- a
    - The parameter 'a' is the input integer that the node will process. It is essential for the operation of the node because it determines the boolean output according to whether the value is not zero. This parameter directly affects the execution of the node and the resulting boolean value.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- op
    - The 'op' output is a boolean value that indicates the true value of the integer. It is important because it provides a clear and direct explanation of the value input in the boolean context, which is usually necessary for further processing or decision-making in the system.
    - Comfy dtype: BOOL
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class IntToBool:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'a': ('INT', {'default': 0})}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/conversion'

    def op(self, a: int) -> tuple[bool]:
        return (a != 0,)
```