# Documentation
- Class name: Vec4UnaryOperation
- Category: math/vec4
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec4UnaryOperation node is designed to perform a variety of monogonal operations for four-dimensional vectors. It can apply different mathematical variations to vectors, which may be critical in the computation of vectors in graphic, physical or other mathematical applications.

# Input types
## Required
- op
    - The parameter 'op' specifies a single-dimensional operation that you want to perform on the vector 'a'. It is a string that represents the operation itself and is essential for determining the changes to be applied to the vector.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' indicates that the four-dimensional vector of a single-dimensional operation will be applied. This is a basic input, because the effect of the operation is directly reflected in the change of the vector.
    - Comfy dtype: Vec4
    - Python dtype: Tuple[float, float, float, float]

# Output types
- result
    - The parameter'reult' is the result of a monolithic operation applied to the input vector 'a'. It is a variable changed to include the effects of the operation.
    - Comfy dtype: Vec4
    - Python dtype: Tuple[float, float, float, float]

# Usage tips
- Infra type: CPU

# Source code
```
class Vec4UnaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_UNARY_OPERATIONS.keys()),), 'a': DEFAULT_VEC4}}
    RETURN_TYPES = ('VEC4',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec4'

    def op(self, op: str, a: Vec4) -> tuple[Vec4]:
        return (_vec4_from_numpy(VEC_UNARY_OPERATIONS[op](numpy.array(a))),)
```