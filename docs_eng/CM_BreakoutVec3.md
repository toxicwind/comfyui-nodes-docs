# Documentation
- Class name: BreakoutVec3
- Category: math/conversion
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

BreakoutVec 3 is designed to divide three-dimensional vectors into their individual fractions. It plays a fundamental role in mathematical calculations that need further processing or analysis, in which the separation of vector elements is necessary.

# Input types
## Required
- a
    - The 'a'parameter is a three-dimensional vector that is operated by a node. It is essential for the function of the node because it is an input vector that will be broken down into its components.
    - Comfy dtype: VEC3
    - Python dtype: Vec3

# Output types
- result
    - The output of BreakoutVec3 is a cluster of three separate fractions of the input vector. Each fraction is a floating point number, representing a dimension of the vector.
    - Comfy dtype: FLOAT
    - Python dtype: Tuple[float, float, float]

# Usage tips
- Infra type: CPU

# Source code
```
class BreakoutVec3:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'a': ('VEC3', {'default': VEC3_ZERO})}}
    RETURN_TYPES = ('FLOAT', 'FLOAT', 'FLOAT')
    FUNCTION = 'op'
    CATEGORY = 'math/conversion'

    def op(self, a: Vec3) -> tuple[float, float, float]:
        return (a[0], a[1], a[2])
```