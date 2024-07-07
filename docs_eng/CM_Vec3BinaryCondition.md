# Documentation
- Class name: Vec3BinaryCondition
- Category: math/vec3
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The Vec3BinaryCondition node is designed to perform binary calculations for two three-dimensional vectors. It evaluates the conditions specified by the 'op' parameter and returns a Boolean result indicating whether the conditions for the targeted quantities 'a' and 'b' are valid.

# Input types
## Required
- op
    - The parameter 'op' defines the type of binary condition to be evaluated. It is vital because it determines the specific operation to be performed on the input vector.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' represents the first three-dimensional vector involved in binary calculations. Its values have a significant impact on the results of the condition assessment.
    - Comfy dtype: Vec3
    - Python dtype: numpy.ndarray
- b
    - The parameter 'b' represents the second three-dimensional vector in binary calculations. It works with 'a' to determine the results of the condition check.
    - Comfy dtype: Vec3
    - Python dtype: numpy.ndarray

# Output types
- result
    - The'reult' output is a boolean value indicating whether the binary conditions specified by the 'op' parameter are satisfied by the input vector 'a' and 'b'.
    - Comfy dtype: BOOL
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class Vec3BinaryCondition:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(VEC_BINARY_CONDITIONS.keys()),), 'a': DEFAULT_VEC3, 'b': DEFAULT_VEC3}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/vec3'

    def op(self, op: str, a: Vec3, b: Vec3) -> tuple[bool]:
        return (VEC_BINARY_CONDITIONS[op](numpy.array(a), numpy.array(b)),)
```