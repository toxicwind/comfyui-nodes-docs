# Documentation
- Class name: Vec3UnaryCondition
- Category: math/vec3
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec3UnaryCondition node is intended to perform a single-dimensional calculation of the three-dimensional vector. It applies the specified condition for each element of the vector and returns a Boolean result indicating the result of the condition. This node is essential for the mathematical calculation of the conditional logic of the vector element, such as filtering or threshold processing.

# Input types
## Required
- op
    - The parameter 'op' defines the one-dimensional conditions to be applied to each element of the vector. It is a key to the predefined one-dimensional set of conditions. This parameter is essential because it determines the particular conditions that the node will assess.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' indicates that a three-dimensional vector of a one-dimensional condition will be applied. This is a key input, because the operation of the node depends directly on the value within that vector. The node processes each element in accordance with the specified conditions to produce a boolean result.
    - Comfy dtype: Vec3
    - Python dtype: Vec3

# Output types
- result
    - The output'reult' is a boolean value that indicates that a one-dimensional condition is applied to the result of the input vector. It indicates whether each element of the vector is established and provides a clear and concise assessment of the vector state in accordance with the specified conditions.
    - Comfy dtype: BOOL
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class Vec3UnaryCondition:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_UNARY_CONDITIONS.keys()),), 'a': DEFAULT_VEC3}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec3'

    def op(self, op: str, a: Vec3) -> tuple[bool]:
        return (VEC_UNARY_CONDITIONS[op](numpy.array(a)),)
```