# Documentation
- Class name: Vec2UnaryCondition
- Category: math/vec2
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

Vec2UnaryCondition is designed to perform various monogonal operations on two-dimensional vectors. It applies the specified conditions to each element of the vector and returns a boolean result, indicating the results of each element's operation.

# Input types
## Required
- op
    - The parameter 'op' defines the one-dimensional conditions that will be applied to vector elements. It is essential to determine the nature of the operation and the expected results.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' represents the two-dimensional vector of a one-dimensional condition that will be evaluated on it. It is the key to node implementation because it provides input data for operations.
    - Comfy dtype: Vec2
    - Python dtype: Vec2

# Output types
- result
    - The output'reult' is a group of boolean values corresponding to an assessment of the one-dimensional conditions for each element of the input vector.
    - Comfy dtype: tuple[bool]
    - Python dtype: Tuple[bool]

# Usage tips
- Infra type: CPU

# Source code
```
class Vec2UnaryCondition:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_UNARY_CONDITIONS.keys()),), 'a': DEFAULT_VEC2}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec2'

    def op(self, op: str, a: Vec2) -> tuple[bool]:
        return (VEC_UNARY_CONDITIONS[op](numpy.array(a)),)
```