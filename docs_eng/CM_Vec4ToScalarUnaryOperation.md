# Documentation
- Class name: Vec4ToScalarUnaryOperation
- Category: math/vec4
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The node performs mathematical calculations for four-dimensional vectors and converts them to marker values. It is designed to encapsulate a series of single-dimensional calculations that can be applied to each element of the vector, thus achieving complex mathematical conversions in a simplified and efficient manner.

# Input types
## Required
- op
    - The parameter 'op'specifies the one-dimensional calculation to be applied to each element of the input vector. It is essential because it determines the type of mathematical conversion to be performed.
    - Comfy dtype: str
    - Python dtype: str
- a
    - Parameter 'a'means the four-dimensional vector that the node will process. This is a basic input, because the function of the node revolves around the calculation of the vector.
    - Comfy dtype: Vec4
    - Python dtype: numpy.ndarray

# Output types
- result
    - The parameter'reult' is the output of the node, which is the nominal value obtained by applying a single-digit calculation specified for the input vector. It marks the completion of the node mathematical processing.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class Vec4ToScalarUnaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_TO_SCALAR_UNARY_OPERATION.keys()),), 'a': DEFAULT_VEC4}}
    RETURN_TYPES = ('FLOAT',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec4'

    def op(self, op: str, a: Vec4) -> tuple[float]:
        return (VEC_TO_SCALAR_UNARY_OPERATION[op](numpy.array(a)),)
```