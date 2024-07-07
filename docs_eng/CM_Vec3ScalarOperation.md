# Documentation
- Class name: Vec3ScalarOperation
- Category: math/vec3
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec3ScallarOperation node is designed to perform a variety of metric calculations for three-dimensional vectors. It does this by applying the specified operation to each element of the vector to the given mark. This node is essential for mathematical calculations involving vectors in three-dimensional spaces and provides a simple and direct way to operate vectors.

# Input types
## Required
- op
    - The parameter 'op' defines the specific metric operation to be performed on the vector. It is vital because it determines the type of mathematical operation that will be executed on the vector. The selection of the operation directly affects the outcome of the node execution.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' indicates that the three-dimensional vector of the operation will be applied. As a core input, it is essential for the function of the node, and the output of the node depends on the value within the vector.
    - Comfy dtype: Vec3
    - Python dtype: Tuple[float, float, float]
- b
    - The parameter 'b' is the metric value that interacts with the vector 'a' during the operation. Its role is vital because it is the value that will be used with each element of the vector to specify the operation.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- result
    - The output'reult' is a three-dimensional vector that has been assigned to the target. It contains node calculations and reflects the changes made by operation to the original vector 'a'.
    - Comfy dtype: VEC3
    - Python dtype: Tuple[float, float, float]

# Usage tips
- Infra type: CPU

# Source code
```
class Vec3ScalarOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_SCALAR_OPERATION.keys()),), 'a': DEFAULT_VEC3, 'b': ('FLOAT',)}}
    RETURN_TYPES = ('VEC3',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec3'

    def op(self, op: str, a: Vec3, b: float) -> tuple[Vec3]:
        return (_vec3_from_numpy(VEC_SCALAR_OPERATION[op](numpy.array(a), b)),)
```