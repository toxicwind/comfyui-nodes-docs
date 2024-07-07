# Documentation
- Class name: Vec4UnaryCondition
- Category: math/vec4
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec4UnaryCondition node is designed to perform a one-dimensional calculation of a four-dimensional vector. It evaluates the conditions on each vector, returns a single boolean result, and indicates whether all fractions meet the conditions. This node is essential in the mathematical calculation of the vector based on the logic of the condition.

# Input types
## Required
- op
    - The parameter 'op' defines the one-dimensional conditions to be applied to each fraction of the vector. It is very important because it determines the nature of the condition checks performed by the node.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' indicates that the four-dimensional vector of a one-dimensional condition will be evaluated. It is a key input, because the operation of the node depends entirely on the value within that vector.
    - Comfy dtype: Vec4
    - Python dtype: Vec4

# Output types
- result
    - Output'reult' is a boolean value that indicates whether a single condition applied to all fractions of the input vector is calculated as true.
    - Comfy dtype: BOOL
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class Vec4UnaryCondition:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_UNARY_CONDITIONS.keys()),), 'a': DEFAULT_VEC4}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec4'

    def op(self, op: str, a: Vec4) -> tuple[bool]:
        return (VEC_UNARY_CONDITIONS[op](numpy.array(a)),)
```