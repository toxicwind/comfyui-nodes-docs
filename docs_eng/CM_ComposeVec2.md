# Documentation
- Class name: ComposeVec2
- Category: math/conversion
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The ComposeVec2 node is designed to group the two metrics into a single two-dimensional vector. It plays a key role in vector mathematics by allowing the creation of Vec2 objects from separate fractions, which can then be used in further geometry or mathematical calculations.

# Input types
## Required
- x
    - The parameter 'x' represents the first fraction of a two-dimensional vector. It is essential for defining the horizontal position in the Cartesian coordinate system and makes an important contribution to the overall direction and size of the vector.
    - Comfy dtype: FLOAT
    - Python dtype: float
- y
    - The parameter 'y' represents the second fraction of a two-dimensional vector, indicating the vertical position in the coordinate system. It is essential to create the vertical direction of the vector and, together with 'x', determines the overall trajectory of the vector.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- Vec2
    - The output of the ComposeVec2 node is a Vec2 object that will encrypt the 'x' and 'y' fractions into a consistent two-dimensional vector. This vector can be used for a wide range of mathematical and geometric calculations.
    - Comfy dtype: VEC2
    - Python dtype: Vec2

# Usage tips
- Infra type: CPU

# Source code
```
class ComposeVec2:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'x': ('FLOAT', {'default': 0.0}), 'y': ('FLOAT', {'default': 0.0})}}
    RETURN_TYPES = ('VEC2',)
    FUNCTION = 'op'
    CATEGORY = 'math/conversion'

    def op(self, x: float, y: float) -> tuple[Vec2]:
        return ((x, y),)
```