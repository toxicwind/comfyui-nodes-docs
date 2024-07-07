# Documentation
- Class name: Vec2BinaryOperation
- Category: math/vec2
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec2BinaryOperation node is designed to perform binary calculations for two-dimensional vectors. It can handle a variety of vector calculations, such as additions, subtractions, multiplications and division, providing multifunctional tools for vector mathematics within applications. This node plays a key role in operational vector data, enabling users to perform complex calculations with ease and precision.

# Input types
## Required
- op
    - The parameter 'op' defines the type of binary operation that you want to perform on the input vector. It is essential to determine the mathematical operation that the node will execute, thus directly affecting the calculation results. The choice of the calculation can significantly influence the outcome and the subsequent analysis or processing steps.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' represents the first vector in binary calculations. It is a necessary input, because it constitutes half the number of operations required for vector calculations. The value and characteristics of the vector 'a' will greatly influence the final result of the calculations, making it a key element of the node function.
    - Comfy dtype: Vec2
    - Python dtype: Tuple[float, float]
- b
    - The parameter 'b' indicates the second vector involved in binary operations. Like 'a', it is a necessary input that completes the number of operations required for vector operations. The properties and values in the vector'b' are essential to the computation process and the ability of nodes to produce accurate and meaningful results.
    - Comfy dtype: Vec2
    - Python dtype: Tuple[float, float]

# Output types
- result
    - The output parameter 'Result' contains the results of a binary calculation performed for input vectors. It is a key output because it conveys the final calculated value, representing the main function and purpose of the node in the calculation workflow.
    - Comfy dtype: Vec2
    - Python dtype: Tuple[float, float]

# Usage tips
- Infra type: CPU

# Source code
```
class Vec2BinaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_BINARY_OPERATIONS.keys()),), 'a': DEFAULT_VEC2, 'b': DEFAULT_VEC2}}
    RETURN_TYPES = ('VEC2',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec2'

    def op(self, op: str, a: Vec2, b: Vec2) -> tuple[Vec2]:
        return (_vec2_from_numpy(VEC_BINARY_OPERATIONS[op](numpy.array(a), numpy.array(b))),)
```