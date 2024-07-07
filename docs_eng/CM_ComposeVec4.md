# Documentation
- Class name: ComposeVec4
- Category: math/conversion
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

ComposeVec 4 is designed to group four separate float-point values into a Vec4 object. It plays a key role in mathematical calculations to convert and aggregate space or colour data. The node streamlines the process of creating four-dimensional vectors from a marker component, which is essential for calculating geometry and graphic applications.

# Input types
## Required
- x
    - The parameter 'x' represents the first fraction of a four-dimensional vector. It is essential to define the spatial direction or colour intensity of the Vec4 object generated. This parameter directly affects the result of the vector mix and is an integral part of the node function.
    - Comfy dtype: FLOAT
    - Python dtype: float
- y
    - The parameter 'y' represents the second fraction of Vec4, which contributes to the overall structure of the vector. It is essential for a comprehensive representation of the application of spatial or colour data, ensuring the role of nodes in generating a well-defined vector.
    - Comfy dtype: FLOAT
    - Python dtype: float
- z
    - The parameter 'z' represents the third fraction of a four-dimensional vector. It is the key element in a vector construction, especially when a three-dimensional space indicates or involves a colour channel. The 'z' value is essential to the ability of the node to generate a meaningful vector from each fraction.
    - Comfy dtype: FLOAT
    - Python dtype: float
- w
    - The parameter 'w' is the fourth and last fraction of the Vec4 object. It usually represents additional information, such as the alpha channel in the view or colour data in the hyphenation system. It contains 'w' that completes the vector and allows full representation in various mathematical and graphic contexts.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- Vec4
    - The output of ComposeVec4 is a Vec4 object that wraps four input parameters into a coherent structure. This output is important because it provides a uniform indication of further processing or analysis in downstream operations and facilitates seamless integration of vector data in computational workflows.
    - Comfy dtype: VEC4
    - Python dtype: Vec4

# Usage tips
- Infra type: CPU

# Source code
```
class ComposeVec4:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'x': ('FLOAT', {'default': 0.0}), 'y': ('FLOAT', {'default': 0.0}), 'z': ('FLOAT', {'default': 0.0}), 'w': ('FLOAT', {'default': 0.0})}}
    RETURN_TYPES = ('VEC4',)
    FUNCTION = 'op'
    CATEGORY = 'math/conversion'

    def op(self, x: float, y: float, z: float, w: float) -> tuple[Vec4]:
        return ((x, y, z, w),)
```