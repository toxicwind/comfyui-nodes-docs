# Documentation
- Class name: NumberUnaryCondition
- Category: math/number
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The `NumberUnaryCondition'node is designed to assess the relationship between the number of individual operations and a set of one-dimensional conditions and to determine the validity of the conditions in the mathematical context. It serves as a basic building block for more complex numerical operations, ensuring that the numerical conditions are met before further calculations are made.

# Input types
## Required
- op
    - The parameter 'op'defines the one-size-fits-all conditions to be applied to the number of operations 'a '. It is vital because it determines the type of mathematical conditions to be performed and directly influences the output of nodes.
    - Comfy dtype: str
    - Python dtype: str
- a
    - The parameter 'a'indicates the number of operations that will apply a one-size-fits-all condition. Its value is important because it is the subject of a condition check and determines the outcome of the node evaluation.
    - Comfy dtype: number
    - Python dtype: Union[int, float]

# Output types
- result
    - Output'redult' means the result of a single condition check. It is a boolean value, and the number 'a' indicates whether the condition defined by 'op' is met.
    - Comfy dtype: bool
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class NumberUnaryCondition:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'op': (list(FLOAT_UNARY_CONDITIONS.keys()),), 'a': DEFAULT_NUMBER}}
    RETURN_TYPES = ('BOOL',)
    FUNCTION = 'op'
    CATEGORY = 'math/number'

    def op(self, op: str, a: number) -> tuple[bool]:
        return (FLOAT_UNARY_CONDITIONS[op](float(a)),)
```