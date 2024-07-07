# Documentation
- Class name: IntUnaryCondition
- Category: math/int
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The IntUnaryCondition node is designed to assess a single integer based on a set of one-dimensional conditions. It is a basic building block for more complex mathematical operations, allowing for the determination of whether an integer meets a specific condition without changing its value.

# Input types
## Required
- op
    - The parameter 'op' is a string that defines a single condition for checking the integer 'a'. It is essential for the operation of the node, because it determines the specific conditions to be assessed.
    - Comfy dtype: STRING
    - Python dtype: str
- a
    - The parameter 'a' indicates the integer number to be assessed according to the one-dimensional condition specified in the parameter 'op'. It is a basic input to the node because it is the object of the condition check.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- BOOL
    - The output of the IntUnaryCondition node is a boolean value that indicates whether the integer 'a' meets the one-size-fits-all conditions specified by 'op'. This result is important for the decision-making process in subsequent operations.
    - Comfy dtype: BOOL
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class IntUnaryCondition:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(INT_UNARY_CONDITIONS.keys()),), 'a': DEFAULT_INT}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/int'

    def op(self, op: str, a: int) -> tuple[bool]:
        return (INT_UNARY_CONDITIONS[op](a),)
```