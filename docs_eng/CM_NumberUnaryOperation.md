# Documentation
- Class name: NumberUnaryOperation
- Category: math/number
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The NumberUnaryOperation node is designed to perform various monogonal calculations for numerical input. It accepts a single operational identifier and a number, applying the corresponding mathematical function to the generation of results. This node plays a key role in simplifying mathematical calculations in the workflow and provides a simple and efficient way to process numerical data.

# Input types
## Required
- op
    - The parameter 'op' is a string that specifies the one-dimensional operation to be performed. It is essential to determine the mathematical function that will be applied to the input number. The selection of the operation directly affects the result of the node execution.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' represents the value that will be applied to a single-digit operation. It is an important part of the node function, because the result of the operation depends on the input value. The parameter ensures that the node can process a wide range of numerical data types.
    - Comfy dtype: number
    - Python dtype: Union[int, float]

# Output types
- result
    - The'reult' output parameter represents the result of the application of a single calculation to the input of a number. It contains the final values obtained after the operation and marks the contribution of the node to the data processing sequence.
    - Comfy dtype: float
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class NumberUnaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(FLOAT_UNARY_OPERATIONS.keys()),), 'a': DEFAULT_NUMBER}}
    RETURN_TYPES = ('NUMBER',)
    FUNCTION = 'op'
    CATEGORY = 'math/number'

    def op(self, op: str, a: number) -> tuple[float]:
        return (FLOAT_UNARY_OPERATIONS[op](float(a)),)
```