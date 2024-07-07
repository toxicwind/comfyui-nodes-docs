# Documentation
- Class name: Vec4ToScalarBinaryOperation
- Category: math/vec4
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec4ScalBinaryOperation node is designed to perform binary calculations for two four-dimensional vectors (Vec4), resulting in a metric value. It encapsulates the mathematical logic, abstractly complex, and provides a visual interface for a vector-based calculation.

# Input types
## Required
- op
    - The parameter 'op' defines the binary calculation that you want to perform on the input vector. It is vital because it determines the mathematical function that will be applied to the vector and directly influences the result of the calculation.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter `a' represents the first four-dimensional vector in binary calculations (Vec4), which is a necessary input, as it constitutes an operational number that contributes to the final metric result.
    - Comfy dtype: Vec4
    - Python dtype: List[float]
- b
    - The parameter `b' indicates the second four-dimensional vector (Vec4) involved in binary calculations, which is a necessary input, since it supplements the first vector to complete the calculation and influences the value of the result.
    - Comfy dtype: Vec4
    - Python dtype: List[float]

# Output types
- result
    - The parameter'reult' is the standard output of binary calculations executed on the input vector. It represents the final result of the mathematical process, and the result of the calculation is enclosed in a single value.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class Vec4ToScalarBinaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_TO_SCALAR_BINARY_OPERATION.keys()),), 'a': DEFAULT_VEC4, 'b': DEFAULT_VEC4}}
    RETURN_TYPES = ('FLOAT',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec4'

    def op(self, op: str, a: Vec4, b: Vec4) -> tuple[float]:
        return (VEC_TO_SCALAR_BINARY_OPERATION[op](numpy.array(a), numpy.array(b)),)
```