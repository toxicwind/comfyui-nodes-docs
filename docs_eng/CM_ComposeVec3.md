# Documentation
- Class name: ComposeVec3
- Category: math/conversion
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

This node synthesizes a Vec3 object from three separate floating point values to create and operate three-dimensional vectors in mathematical or geometric context.

# Input types
## Required
- x
    - The x-coordinate of the vector is a basic parameter that defines the position of the horizontal axis in a three-dimensional space and influences the direction and size of the vector.
    - Comfy dtype: FLOAT
    - Python dtype: float
- y
    - The y coordinates of the vector determine its position on the vertical axis in the three-dimensional space, which is essential for establishing the direction and impact of the vector in the coordinate system.
    - Comfy dtype: FLOAT
    - Python dtype: float
- z
    - The z-coordinate of the vector determines its position on the deep axis of the three-dimensional space, which plays a vital role in the overall spatial expression of the vector.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- Vec3
    - The output is a Vec3 object that contains three input values representing a vector in a three-dimensional space that can be used for various mathematical and geometric operations.
    - Comfy dtype: VEC3
    - Python dtype: Vec3

# Usage tips
- Infra type: CPU

# Source code
```
class ComposeVec3:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'x': ('FLOAT', {'default': 0.0}), 'y': ('FLOAT', {'default': 0.0}), 'z': ('FLOAT', {'default': 0.0})}}
    RETURN_TYPES = ('VEC3',)
    FUNCTION = 'op'
    CATEGORY = 'math/conversion'

    def op(self, x: float, y: float, z: float) -> tuple[Vec3]:
        return ((x, y, z),)
```