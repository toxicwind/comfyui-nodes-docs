# Documentation
- Class name: FloatToNumber
- Category: math/conversion
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The FloatTonumer node is designed to convert floating point values into more common forms of numerical expression. It plays a key role in data type conversion, ensuring compatibility between different parts of the mathematical or computational workflow.

# Input types
## Required
- a
    - The 'a' parameter is a floating number that is intended for conversion. It is essential for the operation of the node, as it determines the type of input data to be converted.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- result
    - The'redult' output is a number that is converted from input float values. It marks a successful conversion from a given data type to a more common digital form.
    - Comfy dtype: NUMBER
    - Python dtype: number

# Usage tips
- Infra type: CPU

# Source code
```
class FloatToNumber:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'a': ('FLOAT', {'default': 0.0})}}
    RETURN_TYPES = ('NUMBER',)
    FUNCTION = 'op'
    CATEGORY = 'math/conversion'

    def op(self, a: float) -> tuple[number]:
        return (a,)
```