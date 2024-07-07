# Documentation
- Class name: NumberBinaryCondition
- Category: math/float
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The `NumberBinaryCondition'node is designed to assess the binary conditions between the two digital inputes. It performs the comparison operation specified by the user and returns a boolean result, indicating the result of the condition.

# Input types
## Required
- op
    - The parameter 'op'defines the binary conditions to be assessed. It is vital because it determines the type of comparison to be performed between the two figures.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a'means the first number in a binary condition. It plays an important role because it is an operation in a comparison operation.
    - Comfy dtype: number
    - Python dtype: Union[int, float]
- b
    - The parameter 'b' represents the second number in the binary condition. It is vital because it is another number of operations that compare operations.
    - Comfy dtype: number
    - Python dtype: Union[int, float]

# Output types
- result
    - The output'reult'provided the results of the Boolean evaluation of the binary condition, with instructions as to whether it was valid or not.
    - Comfy dtype: bool
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class NumberBinaryCondition:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(FLOAT_BINARY_CONDITIONS.keys()),), 'a': DEFAULT_NUMBER, 'b': DEFAULT_NUMBER}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/float'

    def op(self, op: str, a: number, b: number) -> tuple[bool]:
        return (FLOAT_BINARY_CONDITIONS[op](float(a), float(b)),)
```