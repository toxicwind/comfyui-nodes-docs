# Documentation
- Class name: BreakoutVec2
- Category: math/conversion
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

BreakoutVec node 2 is designed to divide two-dimensional vectors into their components. It plays a fundamental role in vector operations by providing access to individual elements of Vec2 objects that can then be used independently for further calculations or operations.

# Input types
## Required
- a
    - The parameter 'a' is a two-dimensional vector that is the object of a node operation. It is essential because it is the main input that determines the node output. The node divides the vector into its components, and then these parts can be used by other processes.
    - Comfy dtype: VEC2
    - Python dtype: Vec2

# Output types
- x
    - Output 'x' represents the first fraction of the input vector that is processed by a node. It is important because it allows for the separation and separate processing of vector elements, which may be critical in various mathematical and geometric calculations.
    - Comfy dtype: FLOAT
    - Python dtype: float
- y
    - The output 'y' corresponds to the second fraction of the input vector. It is as important as the 'x' output and applies to applications that require separate operations or analysis of vectors, for example in graphic renderings or physical simulations.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class BreakoutVec2:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'a': ('VEC2', {'default': VEC2_ZERO})}}
    RETURN_TYPES = ('FLOAT', 'FLOAT')
    FUNCTION = 'op'
    CATEGORY = 'math/conversion'

    def op(self, a: Vec2) -> tuple[float, float]:
        return (a[0], a[1])
```