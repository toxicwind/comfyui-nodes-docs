# Documentation
- Class name: WAS_Logical_OR
- Category: Logical Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Logical_OR node is intended to perform logic or operation for two booleans. In the decision-making process, it is fundamental when either condition exists sufficient to trigger an action or result.

# Input types
## Required
- boolean_a
    - The first boolean input of the logic or operation. It plays a key role in determining the result of the function, because it is one of the conditions that will lead to the output as a whole when it is true.
    - Comfy dtype: bool
    - Python dtype: bool
- boolean_b
    - Logical or operational second boolean input. It is as important as the first input, because it represents another condition that can lead to a real output when the condition is met.
    - Comfy dtype: bool
    - Python dtype: bool

# Output types
- result
    - The result of the logic or operation between the two inputs. It indicates whether at least one condition has been met, summarized or the essence of the logic.
    - Comfy dtype: bool
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Logical_OR(WAS_Logical_Comparisons):

    def do(self, boolean_a, boolean_b):
        return (boolean_a or boolean_b,)
```