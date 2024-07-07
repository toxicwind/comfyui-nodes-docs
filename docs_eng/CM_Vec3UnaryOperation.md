# Documentation
- Class name: Vec3UnaryOperation
- Category: math/vec3
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec3UnaryOrganization class is designed to perform a single-dimensional calculation of three-dimensional vectors. It covers the logic of various vector operations and provides a flexible interface for mathematical operations in three-dimensional spaces.

# Input types
## Required
- op
    - The parameter 'op'specifies the one-dimensional calculation that you want to perform on the vector. It is vital because it determines the type of mathematical function that will be applied to each fraction of the vector.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a'indicates that a three-dimensional vector of a single-dimensional operation will be performed. It is a necessary input because it is the object of a mathematical operation.
    - Comfy dtype: Vec3
    - Python dtype: Tuple[float, float, float]

# Output types
- result
    - The output'reult' is a three-dimensional change after applying the specified one-dimensional operation. It's important because it represents the result of the mathematical process.
    - Comfy dtype: VEC3
    - Python dtype: Tuple[float, float, float]

# Usage tips
- Infra type: CPU

# Source code
```
class Vec3UnaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_UNARY_OPERATIONS.keys()),), 'a': DEFAULT_VEC3}}
    RETURN_TYPES = ('VEC3',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec3'

    def op(self, op: str, a: Vec3) -> tuple[Vec3]:
        return (_vec3_from_numpy(VEC_UNARY_OPERATIONS[op](numpy.array(a))),)
```