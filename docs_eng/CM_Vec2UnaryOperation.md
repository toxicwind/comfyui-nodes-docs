# Documentation
- Class name: Vec2UnaryOperation
- Category: math/vec2
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec2UnaryOperation node is designed to perform multiple one-dimensional calculations of two-dimensional vectors. It accepts an operation as an input, which is a string, means a mathematical function, and applies it to a vector'a', thereby obtaining a variable with a change. This node is essential in mathematics and in calculating vector algebras in the context, which may require a negative, inverted or absolute value equivalent calculation.

# Input types
## Required
- op
    - The parameter 'op' specifies the one-dimensional calculation that you want to apply to the vector 'a'. It is a string that corresponds to a predefined mathematical function. This parameter is essential because it determines the nature of the change that the input vector will experience.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' is a two-dimensional vector that will be applied to a single-dimensional calculation. This is a key input, because the whole calculation is built around a variable that changes according to the specified mathematical function.
    - Comfy dtype: VEC2
    - Python dtype: Tuple[float, float]

# Output types
- result
    - Output'redult' is the conversion of a single-dimensional vector specified by 'op' on the input vector 'a'. It represents the result of a mathematical change and is the main output of the Vec2UnaryOperation node.
    - Comfy dtype: VEC2
    - Python dtype: Tuple[float, float]

# Usage tips
- Infra type: CPU

# Source code
```
class Vec2UnaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_UNARY_OPERATIONS.keys()),), 'a': DEFAULT_VEC2}}
    RETURN_TYPES = ('VEC2',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec2'

    def op(self, op: str, a: Vec2) -> tuple[Vec2]:
        return (_vec2_from_numpy(VEC_UNARY_OPERATIONS[op](numpy.array(a))),)
```