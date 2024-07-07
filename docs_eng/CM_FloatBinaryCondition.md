# Documentation
- Class name: FloatBinaryCondition
- Category: math/float
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

This node provides a mechanism for the binary calculation of floating points. It is designed to determine a boolean output based on a comparison of two floating points. The function of the node is focused on assessing mathematical conditions, thus supporting the decision-making process that relies on numerical thresholds.

# Input types
## Required
- op
    - The operating parameter defines the type of binary condition to be evaluated. It is a key element because it determines the specific comparison or operation to be performed on the input float number. The choice of the operation directly affects the decision-making power of the node.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a'indicates the first number of operations in the binary condition. It is essential for the operation of the node, as it is one of the two values to be compared or operated. The value 'a'plays an important role in determining the results of the condition check.
    - Comfy dtype: float
    - Python dtype: float
- b
    - The parameter 'b' is the second number of operations in a binary condition. It is as important as 'a', because it is the second value for the comparison or operation. The function of the node depends on 'a' and 'b' to produce the right boolean result.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- result
    - The output of the node is a boolean value that represents the result of a binary condition. It indicates whether the conditions specified by the 'op'parameter are valid for the given input float numbers 'a 'and 'b'.
    - Comfy dtype: bool
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class FloatBinaryCondition:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(FLOAT_BINARY_CONDITIONS.keys()),), 'a': DEFAULT_FLOAT, 'b': DEFAULT_FLOAT}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/float'

    def op(self, op: str, a: float, b: float) -> tuple[bool]:
        return (FLOAT_BINARY_CONDITIONS[op](a, b),)
```