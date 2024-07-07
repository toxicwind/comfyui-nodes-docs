# Documentation
- Class name: NumberToFloat
- Category: math/conversion
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The NumberToFloat node is designed to convert input numbers into floating point formats. It plays a key role in ensuring accuracy and consistency in the computation of values between different data types.

# Input types
## Required
- a
    - The 'a'parameter is the input number for which the node is intended to convert to a floating point value. It is essential for the operation of the node, as it directly affects the value of the output.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float, str]

# Output types
- result
    - The'redult' output is the number of floating points converted from the input. It is important because it represents the end result of the main output and conversion process of the node.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class NumberToFloat:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'a': ('NUMBER', {'default': 0.0})}}
    RETURN_TYPES = ('FLOAT',)
    FUNCTION = 'op'
    CATEGORY = 'math/conversion'

    def op(self, a: number) -> tuple[float]:
        return (float(a),)
```