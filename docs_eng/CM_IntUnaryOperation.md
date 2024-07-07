# Documentation
- Class name: IntUnaryOperation
- Category: math/int
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The IntUnaryOperation node is designed to perform multiple monolithic calculations for integer input, providing a flexible and efficient way to operate numerical data. It emphasizes the ability of the node to convert the whole value through a predefined set of mathematical calculations, without changing the basic nature of the input.

# Input types
## Required
- op
    - The parameter 'op' is essential because it determines the specific one-dimensional operation to be applied to the integer input. It influences the execution of the node by specifying the mathematical function to be used, thereby influencing the result of the operation.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' represents an integer input for a single-digit operation. Its value directly influences the result of the operation, as it is the number of operations that all mathematical functions will apply.
    - Comfy dtype: int
    - Python dtype: int

# Output types
- result
    - The output parameter'reult' indicates that a single-digit calculation is applied to the result of the integer input. It encapsulates the value converted after the operation and reflects the main function of the node - the number operation.
    - Comfy dtype: int
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class IntUnaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(INT_UNARY_OPERATIONS.keys()),), 'a': DEFAULT_INT}}
    RETURN_TYPES = ('INT',)
    FUNCTION = 'op'
    CATEGORY = 'math/int'

    def op(self, op: str, a: int) -> tuple[int]:
        return (INT_UNARY_OPERATIONS[op](a),)
```