# Documentation
- Class name: IntBinaryCondition
- Category: math/int
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The IntBinaryCondition node is designed to assess the binary conditions between the two integer values. It works by applying the specified operation to the input and determining the true value of the result conditions. The decision-making process of the node in mathematical calculations is crucial, and the result is a relationship between the two integer numbers.

# Input types
## Required
- op
    - The parameter 'op' defines the binary operation that you want to perform on the integer input. It is vital because it determines the nature of the conditions being evaluated. The selection of the operation directly influences the decision-making power of the node in the mathematical context.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' represents the first integer in a binary condition. Its value is important because it helps the results of the condition assessment. The integer 'a' plays a key role in the decision-making process at the node.
    - Comfy dtype: int
    - Python dtype: int
- b
    - The parameter 'b' indicates the second integer involved in the binary condition. It is vital because it determines the final result of the condition together with 'a'. The integer'b' is a key element in the node assessment process.
    - Comfy dtype: int
    - Python dtype: int

# Output types
- result
    - The'reult' output represents the boolean result of the binary conditions assessed at the node. It is important because it represents the true value of the conditions and can be used for further processing or decision-making in mathematical or logical workflows.
    - Comfy dtype: bool
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class IntBinaryCondition:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(INT_BINARY_CONDITIONS.keys()),), 'a': DEFAULT_INT, 'b': DEFAULT_INT}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/int'

    def op(self, op: str, a: int, b: int) -> tuple[bool]:
        return (INT_BINARY_CONDITIONS[op](a, b),)
```