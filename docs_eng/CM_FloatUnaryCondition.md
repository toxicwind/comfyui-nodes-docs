# Documentation
- Class name: FloatUnaryCondition
- Category: math/float
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The node is designed to assess the mathematical condition of a single operating number of floating points. It provides a method for carrying out a condition check, such as checking whether a number is positive, negative or zero, without the need for direct logic in the code.

# Input types
## Required
- op
    - The operational parameter defines the single-operational number conditions to be applied to input floating points. It is essential because it determines the type of check that will be performed on the input value.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The 'a'parameter represents the number of floating points that will be assessed for a single operating number. It is essential because the entire operation is organized around this value.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- result
    - The result of the operation is a boolean value, which indicates whether the condition of the single operation applied to the input of the floating point is true or false.
    - Comfy dtype: bool
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class FloatUnaryCondition:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(FLOAT_UNARY_CONDITIONS.keys()),), 'a': DEFAULT_FLOAT}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/float'

    def op(self, op: str, a: float) -> tuple[bool]:
        return (FLOAT_UNARY_CONDITIONS[op](a),)
```