# Documentation
- Class name: FloatUnaryOperation
- Category: math/float
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The floatUnaryOperation node applies mathematical calculations to individual floating points and converts them to another floating point value. It is designed to process all monogonal calculations so that they are very flexible in the data processing process for mathematical calculations.

# Input types
## Required
- op
    - The parameter 'op' specifies the single-digit mathematical operation that you want to perform. It is vital because it determines the type of conversion that should be applied to input floating point values.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' indicates that the input float value will be applied to a single-digit operation. It is an essential part of the node operation because it is the subject of a mathematical change.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- result
    - The output'reult' provides the conversion float value after applying the specified one-dollar operation. It is important because it represents the mathematical calculations performed by the node.
    - Comfy dtype: float
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class FloatUnaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(FLOAT_UNARY_OPERATIONS.keys()),), 'a': DEFAULT_FLOAT}}
    RETURN_TYPES = ('FLOAT',)
    FUNCTION = 'op'
    CATEGORY = 'math/float'

    def op(self, op: str, a: float) -> tuple[float]:
        return (FLOAT_UNARY_OPERATIONS[op](a),)
```