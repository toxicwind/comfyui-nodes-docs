# Documentation
- Class name: WAS_Logical_AND
- Category: Logical Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Logical_AND node is designed to perform logic and operations. It evaluates two boolean inputes to determine whether both conditions are true, returns a boolean result, indicating the logic and logic of the input.

# Input types
## Required
- boolean_a
    - The first Boolean input is used for logic and operation. It is essential because it represents one of the conditions that must be true, so that the final result is true.
    - Comfy dtype: bool
    - Python dtype: bool
- boolean_b
    - The second boolean input is also used for logic and operation. Its value is equally important because node returns the true result only if it is true at the same time as the first input.
    - Comfy dtype: bool
    - Python dtype: bool

# Output types
- result
    - The result of the logic and operation between the two input values. It is important because it provides the final result of the logic and operation.
    - Comfy dtype: bool
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Logical_AND(WAS_Logical_Comparisons):

    def do(self, boolean_a, boolean_b):
        return (boolean_a and boolean_b,)
```