# Documentation
- Class name: Vec2BinaryCondition
- Category: math/vec2
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec2BinaryCondition node is designed to perform binary calculations for two-dimensional vectors, providing a method for comparing and assessing vector pairs based on specified conditions. It is very important in mathematical calculations, the result of which is a boolean value, representing the result of applied binary conditions.

# Input types
## Required
- op
    - The parameter 'op' defines the binary conditions to be applied to vector input. It is essential because it determines the nature of the comparison or operation to be performed and directly affects the output of the node.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' represents the first vector in a binary operation. It is vital because it makes up half of the comparison or operation, and the function of the node depends on the value in the vector.
    - Comfy dtype: Vec2
    - Python dtype: Vec2
- b
    - The parameter 'b' means the second vector involved in binary operations. It's important because it completes the matching required for the operation, and the validity of the node depends on the interaction between 'a' and 'b'.
    - Comfy dtype: Vec2
    - Python dtype: Vec2

# Output types
- result
    - Output 'Result' means the result of a binary condition applied to the input vector. It is a boolean value that contains the success or failure of a condition check.
    - Comfy dtype: BOOL
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class Vec2BinaryCondition:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_BINARY_CONDITIONS.keys()),), 'a': DEFAULT_VEC2, 'b': DEFAULT_VEC2}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec2'

    def op(self, op: str, a: Vec2, b: Vec2) -> tuple[bool]:
        return (VEC_BINARY_CONDITIONS[op](numpy.array(a), numpy.array(b)),)
```