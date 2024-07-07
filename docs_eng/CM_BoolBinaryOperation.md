# Documentation
- Class name: BoolBinaryOperation
- Category: math/bool
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The BoolBinaryOperation node is designed to perform binary calculations of the boolean value. It accepts two booleans and a string indicating that it is to perform the operation, and returns the result of the operation. This node is essential for the logical calculation and decision-making process in the system.

# Input types
## Required
- op
    - The `op' parameter is a string that specifies the binary calculation that you want to perform on the Boolean input. It is essential to determine the logic and final result of the operation.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The `a' parameter is the first operation in a binary operation. It is a boolean value that plays an important role in the calculation process.
    - Comfy dtype: bool
    - Python dtype: bool
- b
    - The 'b' parameter is the second operation in binary calculations. It is also a boolean value that contributes to the calculation.
    - Comfy dtype: bool
    - Python dtype: bool

# Output types
- result
    - The result of the Boolean binary calculation is a single boolean value representing the result of the operation.
    - Comfy dtype: bool
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class BoolBinaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(BOOL_BINARY_OPERATIONS.keys()),), 'a': DEFAULT_BOOL, 'b': DEFAULT_BOOL}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/bool'

    def op(self, op: str, a: bool, b: bool) -> tuple[bool]:
        return (BOOL_BINARY_OPERATIONS[op](a, b),)
```