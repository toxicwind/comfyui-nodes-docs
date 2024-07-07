# Documentation
- Class name: BoolUnaryOperation
- Category: math/bool
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The BoolUnaryOperation node is designed to perform a single-dollar operation on the boolean value. It accepts a boolean input, applies a given monogram operation, and produces a boolean output. This node is essential to manipulate the boolean logic in a flow-lined and efficient manner.

# Input types
## Required
- op
    - The parameter 'op' specifies that will be applied to a single-digit operation entered in Boolean. It is essential to determine the logic that the node will process.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a' indicates that the boolean value of the one-dollar operation will be applied. It plays a central role in the execution of the node because it is the object of the operation.
    - Comfy dtype: bool
    - Python dtype: bool

# Output types
- result
    - The parameter'reult' is the output of a single-dimensional operation performed by entering a boolean value. It marks the result of a logical operation within a node.
    - Comfy dtype: bool
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class BoolUnaryOperation:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(BOOL_UNARY_OPERATIONS.keys()),), 'a': DEFAULT_BOOL}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/bool'

    def op(self, op: str, a: bool) -> tuple[bool]:
        return (BOOL_UNARY_OPERATIONS[op](a),)
```