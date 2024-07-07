# Documentation
- Class name: Vec3ToScalarUnaryOperation
- Category: math/vec3
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec3ToScalUnaryOperation node is designed to perform multiple monolithic calculations of three-dimensional vectors and convert them to metric values. This node is essential for applications that need to be simplified to indicate the size or directional properties of the volume as a single value for further analysis or decision-making.

# Input types
## Required
- op
    - The 'op' parameter is a string that specifies the one-dimensional calculation that you want to perform on the input vector. It is essential to determine the nature of the mark output and the mathematical changes applied to the vector.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The 'a'parameter indicates that a single-dimensional three-dimensional vector will be performed on it. This is a necessary input, as the whole operation revolves around converting this vector to a nominal value.
    - Comfy dtype: Vec3
    - Python dtype: numpy.ndarray

# Output types
- result
    - The `redult' output is derived from a monolithic operation performed on the input vector. It summarizes the nature of the vector in a single numeric form for subsequent calculation tasks.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class Vec3ToScalarUnaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_TO_SCALAR_UNARY_OPERATION.keys()),), 'a': DEFAULT_VEC3}}
    RETURN_TYPES = ('FLOAT',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec3'

    def op(self, op: str, a: Vec3) -> tuple[float]:
        return (VEC_TO_SCALAR_UNARY_OPERATION[op](numpy.array(a)),)
```