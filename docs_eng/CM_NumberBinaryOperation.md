# Documentation
- Class name: NumberBinaryOperation
- Category: math/number
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The NumerbinaryOperation node is designed to perform binary calculations for value input. It covers arithmetic calculations that can be applied between two numbers, promoting complex mathematical calculations in a simplified interface.

# Input types
## Required
- op
    - The parameter 'op' determines the specific binary operation to be performed. It is vital because it determines the mathematical function that the node will execute, thereby influencing the result of the calculation.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a'represents the first number of operations in binary calculations. It is essential because it constitutes half of the input required for arithmetic calculations.
    - Comfy dtype: number
    - Python dtype: Union[int, float]
- b
    - The parameter 'b'represents the second number of operations in binary calculations. It is vital because it completes the input set required for the arithmetic process.
    - Comfy dtype: number
    - Python dtype: Union[int, float]

# Output types
- result
    - Output 'Result' provides the results of binary calculations performed on input 'a' and 'b'. It is important because it represents the final calculations derived from the specified operation.
    - Comfy dtype: float
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class NumberBinaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(FLOAT_BINARY_OPERATIONS.keys()),), 'a': DEFAULT_NUMBER, 'b': DEFAULT_NUMBER}}
    RETURN_TYPES = ('NUMBER',)
    FUNCTION = 'op'
    CATEGORY = 'math/number'

    def op(self, op: str, a: number, b: number) -> tuple[float]:
        return (FLOAT_BINARY_OPERATIONS[op](float(a), float(b)),)
```