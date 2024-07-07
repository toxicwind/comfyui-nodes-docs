# Documentation
- Class name: Vec4BinaryCondition
- Category: math/vec4
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec4BinaryCondition node is designed to perform binary calculations of four vectors. It applies two input vectors to specified operations, produces a boolean result that indicates the validity of the conditions. This node plays a key role in vector analysis and comparison in the mathematics field.

# Input types
## Required
- op
    - The parameter 'op' defines the binary conditions to be applied to input vectors. It is essential to determine the nature of the comparison or operation performed by the node and directly influences the outcome of the process.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' represents the first vector in a binary operation. As a basic input, it plays an important role in the execution of the node, influencing the final boolean result according to the terms specified by 'op'.
    - Comfy dtype: Vec4
    - Python dtype: Vec4
- b
    - The parameter 'b' indicates the second vector involved in binary operations. It is essential for calculating the comparison or operation of the node with 'a', and its value is essential for the output of the node.
    - Comfy dtype: Vec4
    - Python dtype: Vec4

# Output types
- result
    - The'redult' output is a boolean value that represents the result of the binary conditions applied to the input vector. It indicates whether the conditions specified by the 'op' parameter are valid for the given amount.
    - Comfy dtype: BOOL
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class Vec4BinaryCondition:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_BINARY_CONDITIONS.keys()),), 'a': DEFAULT_VEC4, 'b': DEFAULT_VEC4}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec4'

    def op(self, op: str, a: Vec4, b: Vec4) -> tuple[bool]:
        return (VEC_BINARY_CONDITIONS[op](numpy.array(a), numpy.array(b)),)
```