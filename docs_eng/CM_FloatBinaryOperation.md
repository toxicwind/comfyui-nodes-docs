# Documentation
- Class name: FloatBinaryOperation
- Category: math/float
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The floatbinaryOperation node is designed to perform binary calculations of floating points. It receives two inputs, 'a' and 'b', and applies the specified operation, 'op', to produce a single floating point result. This node is essential for mathematical calculations that require binary calculations that combine the two numbers.

# Input types
## Required
- op
    - The parameter 'op' specifies the binary calculations that you want to perform on 'a' and 'b'. It is vital because it determines the mathematical function that will be applied to the input and directly influences the output of the node.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' is the first number of operations in binary calculations. It is an important part of the input, as it contributes to the final result of the calculation when it is combined with the second number 'b'.
    - Comfy dtype: float
    - Python dtype: float
- b
    - The parameter 'b' is the second operating number in binary calculations. It plays an important role in the calculation because it is combined with the first operating number 'a' to produce the final result.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- result
    - The parameter'reult' represents the result of the binary operation 'op' applied to the input 'a' and 'b'. It is a single float number, containing the combined effects of two operations.
    - Comfy dtype: float
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class FloatBinaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(FLOAT_BINARY_OPERATIONS.keys()),), 'a': DEFAULT_FLOAT, 'b': DEFAULT_FLOAT}}
    RETURN_TYPES = ('FLOAT',)
    FUNCTION = 'op'
    CATEGORY = 'math/float'

    def op(self, op: str, a: float, b: float) -> tuple[float]:
        return (FLOAT_BINARY_OPERATIONS[op](a, b),)
```