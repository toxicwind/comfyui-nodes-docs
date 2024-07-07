# Documentation
- Class name: IntBinaryOperation
- Category: math/int
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The IntBinaryOperation node is designed to perform all kinds of integer binary calculations. It receives two integer numbers and a string indicating the operation to be performed, and returns the result of the operation. This node is essential for mathematical calculations involving integer numbers and provides a direct method for implementing basic arithmetic calculations in a programmed manner.

# Input types
## Required
- op
    - The parameter 'op' is a string that specifies the binary operation to be performed on two integer numbers. It is very important because it determines the arithmetic operation type to be performed. The selection of the operation directly influences the outcome of the execution of the node.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' represents the first number of operations in binary calculations. As an integral part of the calculation, it plays an important role in mathematical calculations. The value of 'a' directly influences the final result of the operation.
    - Comfy dtype: int
    - Python dtype: int
- b
    - The parameter 'b' represents the second number of operations in binary calculations. It is essential to complete the calculations and get the correct results. The value of 'b', like 'a', is equally important in influencing the calculation results.
    - Comfy dtype: int
    - Python dtype: int

# Output types
- result
    - The parameter'reult' is the result of a binary calculation performed by the node. It contains the final values calculated on the basis of the number of input operations and the specified operations and is the main output of the node.
    - Comfy dtype: int
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class IntBinaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(INT_BINARY_OPERATIONS.keys()),), 'a': DEFAULT_INT, 'b': DEFAULT_INT}}
    RETURN_TYPES = ('INT',)
    FUNCTION = 'op'
    CATEGORY = 'math/int'

    def op(self, op: str, a: int, b: int) -> tuple[int]:
        return (INT_BINARY_OPERATIONS[op](a, b),)
```