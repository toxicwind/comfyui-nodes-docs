# Documentation
- Class name: WAS_Logical_XOR
- Category: Logical Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Logical_XOR nodes are designed to perform logical differences or operations for two booleans. It is fundamental in the logical circuit and decision-making process and provides a simple and powerful mechanism for binary differences.

# Input types
## Required
- boolean_a
    - XOR operates the first boolean input. It plays a key role in determining the results of the logical comparison, as the function of the node depends on the assessment of the two inputs.
    - Comfy dtype: bool
    - Python dtype: bool
- boolean_b
    - The second boolean input for XOR operations. It is as important as the first input in the logical assessment and contributes to the final boolean results for node operations.
    - Comfy dtype: bool
    - Python dtype: bool

# Output types
- result
    - The output of a logical difference or operation is a single boolean value representing both input refractions or non-relationships.
    - Comfy dtype: bool
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Logical_XOR(WAS_Logical_Comparisons):

    def do(self, boolean_a, boolean_b):
        return (boolean_a != boolean_b,)
```