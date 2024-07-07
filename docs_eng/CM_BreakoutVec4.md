# Documentation
- Class name: BreakoutVec4
- Category: math/conversion
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

BreakoutVec 4 is designed to divide the four-dimensional vectors into its components. Its function is to facilitate the operation of each element of the Vec4 object that needs to be operated separately. The node plays a key role in mathematical conversions, especially when the context requires that vectors be treated separately.

# Input types
## Required
- a
    - The parameter 'a' is the input four-dimensional vector that the node will decompose. It is essential for the operation of the node, as it is the main data structure that is being processed. The function of the node concentrates on decomposition of the vector into its components for further use.
    - Comfy dtype: VEC4
    - Python dtype: Vec4

# Output types
- a components
    - BreakoutVec4 output consists of four separate floating points, each representing a fraction of the original Vec4. This output allows for separate analysis and operation of vectors, which are important for a variety of mathematical and computational applications.
    - Comfy dtype: FLOAT
    - Python dtype: Tuple[float, float, float, float]

# Usage tips
- Infra type: CPU

# Source code
```
class BreakoutVec4:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'a': ('VEC4', {'default': VEC4_ZERO})}}
    RETURN_TYPES = ('FLOAT', 'FLOAT', 'FLOAT', 'FLOAT')
    FUNCTION = 'op'
    CATEGORY = 'math/conversion'

    def op(self, a: Vec4) -> tuple[float, float, float, float]:
        return (a[0], a[1], a[2], a[3])
```