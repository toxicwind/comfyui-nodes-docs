# Documentation
- Class name: IntToFloat
- Category: math/conversion
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The IntToFloat node is designed to convert an integer value to its floating-point equivalent. It plays a key role in numerical calculations to ensure that data types are consistent when accurate results are needed, thereby ensuring the accuracy of calculations.

# Input types
## Required
- a
    - The parameter 'a' indicates the integer value to be converted to a floating point. It is essential for the operation of the node, as it determines the starting point of the conversion process.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- result
    - Output'reult' is the floating point for inputting an integer. It is important because it provides a converted value that can be used to calculate subsequent values.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class IntToFloat:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'a': ('INT', {'default': 0})}}
    RETURN_TYPES = ('FLOAT',)
    FUNCTION = 'op'
    CATEGORY = 'math/conversion'

    def op(self, a: int) -> tuple[float]:
        return (float(a),)
```