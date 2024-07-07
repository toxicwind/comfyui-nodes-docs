# Documentation
- Class name: Vec4BinaryOperation
- Category: math/vec4
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec4BinaryOperation node is designed to perform binary calculations for two four-dimensional vectors (Vec4). It can handle the various calculations specified by the 'op' parameter, allowing for element-by-element calculations between vectors 'a' and 'b'. This node is essential in mathematics and calculation of vector algebra in context, enabling users to operate and analyse vector data effectively.

# Input types
## Required
- op
    - The parameter 'op' determines the type of binary operation that you want to perform on the input vector. It is vital because it determines the mathematical function applied to the vector, thus influencing the outcome of the node execution.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter'a' represents the first four-dimensional vector in binary calculations (Vec4), which plays an important role because it is an operational number in vector calculations that directly influences the final result.
    - Comfy dtype: Vec4
    - Python dtype: Tuple[float, float, float, float]
- b
    - The parameter `b' indicates the second four-dimensional vector (Vec4) involved in binary operations, which is important because it is the second operating number in vector calculations, affecting the output of nodes.
    - Comfy dtype: Vec4
    - Python dtype: Tuple[float, float, float, float]

# Output types
- result
    - The parameter'reult' saves the result of a binary calculation between the input vector 'a' and 'b'. It is important because it represents the final vector calculated after the application of the calculation.
    - Comfy dtype: Vec4
    - Python dtype: Tuple[float, float, float, float]

# Usage tips
- Infra type: CPU

# Source code
```
class Vec4BinaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_BINARY_OPERATIONS.keys()),), 'a': DEFAULT_VEC4, 'b': DEFAULT_VEC4}}
    RETURN_TYPES = ('VEC4',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec4'

    def op(self, op: str, a: Vec4, b: Vec4) -> tuple[Vec4]:
        return (_vec4_from_numpy(VEC_BINARY_OPERATIONS[op](numpy.array(a), numpy.array(b))),)
```