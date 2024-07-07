# Documentation
- Class name: If
- Category: EasyUse/Logic/Math
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The If node, as a condition execution unit, assesses the conditions entered and decides which of the two branches it provides, thus constructing the control stream in the calculation chart.

# Input types
## Required
- any
    - The 'any'input is a conditional expression that determines the flow of the If node. It is essential to determine which output branch will be executed.
    - Comfy dtype: *
    - Python dtype: Any
- if
    - `if' represents the action to be performed when `any' conditions are met. It is an important part of the node function, as it defines the positive result.
    - Comfy dtype: *
    - Python dtype: Any
- else
    - `else' defines the alternative action to be performed when `any' conditions are not met. It is essential to provide a complete conditionality logic within the node.
    - Comfy dtype: *
    - Python dtype: Any

# Output types
- ?
    - The output of the If node is a result of one of the `if' or `else' inputs, based on an assessment of the `any' condition. It represents the final result of the condition implementation.
    - Comfy dtype: *
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class If:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'any': (AlwaysEqualProxy('*'),), 'if': (AlwaysEqualProxy('*'),), 'else': (AlwaysEqualProxy('*'),)}}
    RETURN_TYPES = (AlwaysEqualProxy('*'),)
    RETURN_NAMES = ('?',)
    FUNCTION = 'execute'
    CATEGORY = 'EasyUse/Logic/Math'

    def execute(self, *args, **kwargs):
        return (kwargs['if'] if kwargs['any'] else kwargs['else'],)
```