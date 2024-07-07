# Documentation
- Class name: Vec3BinaryOperation
- Category: math/vec3
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec3BinaryOperation node is designed to perform binary calculations for two three-dimensional vectors. It is the basic building block for vector mathematics, allowing for additions, subtractions and quantum multipliers. In geometric calculations, this node is essential for modelling and analysis, and vector counting is essential.

# Input types
## Required
- op
    - Parameter 'op' specifies the binary calculation to be performed on the input vector. It is a key in a predefined vector operation and is essential for determining the type of calculation that the node will perform.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' represents the first three-dimensional vector in the operation. It is a basic input that directly affects the result of the binary calculations performed by the node.
    - Comfy dtype: tuple[float, float, float]
    - Python dtype: Tuple[float, float, float]
- b
    - The parameter 'b' represents the second three-dimensional vector involved in binary calculations. It is a key input that determines the final result of the calculations with 'a'.
    - Comfy dtype: tuple[float, float, float]
    - Python dtype: Tuple[float, float, float]

# Output types
- result
    - The output'reult' is a three-dimensional variable from a binary calculation performed on the input vector 'a' and 'b'. It contains the result of a vector calculation and is a direct reflection of the specified operation 'op'.
    - Comfy dtype: tuple[float, float, float]
    - Python dtype: Tuple[float, float, float]

# Usage tips
- Infra type: CPU

# Source code
```
class Vec3BinaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_BINARY_OPERATIONS.keys()),), 'a': DEFAULT_VEC3, 'b': DEFAULT_VEC3}}
    RETURN_TYPES = ('VEC3',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec3'

    def op(self, op: str, a: Vec3, b: Vec3) -> tuple[Vec3]:
        return (_vec3_from_numpy(VEC_BINARY_OPERATIONS[op](numpy.array(a), numpy.array(b))),)
```