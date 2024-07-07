# Documentation
- Class name: Vec3ToScalarBinaryOperation
- Category: math/vec3
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec3ScalBinaryOperation node is designed to perform binary calculations of two three-dimensional vectors, resulting in a metric value. It encapsifies the mathematical logic of vector operations and optimizes the computational efficiency to ensure that the node contributes to the system by providing accurate and reliable vector calculations.

# Input types
## Required
- op
    - The parameter 'op' defines the binary calculation that you want to perform on the input vector. It is vital because it determines the mathematical function applied to the vector and affects the result of the node calculation.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' represents the first vector in the binary calculation. It is essential to provide the number of operations required to calculate the vector, affecting the final metric result.
    - Comfy dtype: Vec3
    - Python dtype: numpy.ndarray
- b
    - The parameter 'b' represents the second vector involved in binary calculations. It is essential to provide another number of operations required for vector calculations, directly affecting the output of nodes.
    - Comfy dtype: Vec3
    - Python dtype: numpy.ndarray

# Output types
- result
    - The'reult' output provides the metrics obtained for the binary operation of the input vector. It is important because it contains node mathematical processing results.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class Vec3ToScalarBinaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_TO_SCALAR_BINARY_OPERATION.keys()),), 'a': DEFAULT_VEC3, 'b': DEFAULT_VEC3}}
    RETURN_TYPES = ('FLOAT',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec3'

    def op(self, op: str, a: Vec3, b: Vec3) -> tuple[float]:
        return (VEC_TO_SCALAR_BINARY_OPERATION[op](numpy.array(a), numpy.array(b)),)
```