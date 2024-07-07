# Documentation
- Class name: FloatToInt
- Category: math/conversion
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The FloatToInt node is designed to convert floating points into their integer equivalents. It plays a crucial role in situations where an accurate small value is required to be converted to an integer, facilitating operations that require an integer input.

# Input types
## Required
- a
    - The 'a'parameter is the float number that is converted from node to integer. It is essential for the operation of node, as it directly affects output and determines the starting value of the conversion process.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- result
    - The'reult' output is an integer of input floats. It represents the result of the conversion process and provides an integer that can be used in subsequent integer-based calculations.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class FloatToInt:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'a': ('FLOAT', {'default': 0.0})}}
    RETURN_TYPES = ('INT',)
    FUNCTION = 'op'
    CATEGORY = 'math/conversion'

    def op(self, a: float) -> tuple[int]:
        return (int(a),)
```