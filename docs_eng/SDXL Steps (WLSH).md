# Documentation
- Class name: WLSH_SDXL_Steps
- Category: WLSH Nodes/number
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The `set_steps' method of the WLSH_SDXL_Steps node is designed to configure step-long parameters for a weighted minimum two-fold problem. It plays a key role in determining the sequence and spacing of steps, which can significantly influence the outcome of the numerical process.

# Input types
## Required
- precondition
    - The " preconvention " parameter is essential for setting the initial conditions before the step sequence. It affects the starting point of the numerical process and is essential for the overall implementation of the node.
    - Comfy dtype: INT
    - Python dtype: int
- base
    - The “base” parameter defines the basic step length values of the derivative sequence. It is the key determinant in the calculation and directly affects the structure of the step length pattern.
    - Comfy dtype: INT
    - Python dtype: int
- total
    - The 'total' parameter specifies the total number of steps to take in the sequence. It is a key factor in controlling the range of numerical operations and their calculation of loads.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- pre
    - The "pre" output reflects the initial conditions set by the "preconvention" parameter and marks the starting point of the step sequence.
    - Comfy dtype: INT
    - Python dtype: int
- base
    - The "base" output corresponds to the basic step length value of the input, representing the basis on which the step sequence is calculated.
    - Comfy dtype: INT
    - Python dtype: int
- total
    - The total number of steps to be performed by the "total " output instruction program is determined by the "total " parameter.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_SDXL_Steps:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'precondition': ('INT', {'default': 3, 'min': 1, 'max': 10000}), 'base': ('INT', {'default': 12, 'min': 1, 'max': 10000}), 'total': ('INT', {'default': 20, 'min': 1, 'max': 10000})}}
    RETURN_TYPES = ('INT', 'INT', 'INT')
    RETURN_NAMES = ('pre', 'base', 'total')
    FUNCTION = 'set_steps'
    CATEGORY = 'WLSH Nodes/number'

    def set_steps(self, precondition, base, total):
        return (precondition, base, total)
```