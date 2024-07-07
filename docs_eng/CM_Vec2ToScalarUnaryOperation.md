# Documentation
- Class name: Vec2ToScalarUnaryOperation
- Category: math/vec2
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec2ToScalUnaryOperation node is designed to perform multiple one-dimensional calculations of two-dimensional vectors and convert them to metric values. It encapsifies mathematical calculations that can be applied to vectors, emphasizing the role of the node in mathematical computation of vector-mark conversion.

# Input types
## Required
- op
    - The parameter 'op' defines the single-digit calculation to be performed on the vector 'a'. It is vital because it determines the specific mathematical function to be applied, thus influencing the outcome of the node execution.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' indicates the two-dimensional vector on which a single-dimensional operation is to be carried out. It is important because it is the main input for node operations to produce a nominal result.
    - Comfy dtype: Vec2
    - Python dtype: numpy.ndarray

# Output types
- result
    - Output 'Result' is the value of the mark obtained after using the specified one-dimensional calculation to enter the vector 'a'. It marks the result of the node mathematical processing.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class Vec2ToScalarUnaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_TO_SCALAR_UNARY_OPERATION.keys()),), 'a': DEFAULT_VEC2}}
    RETURN_TYPES = ('FLOAT',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec2'

    def op(self, op: str, a: Vec2) -> tuple[float]:
        return (VEC_TO_SCALAR_UNARY_OPERATION[op](numpy.array(a)),)
```