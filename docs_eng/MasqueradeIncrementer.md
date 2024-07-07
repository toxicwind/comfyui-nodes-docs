# Documentation
- Class name: MaqueradeIncrementerNode
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

A disguised incremental node is intended to perform a simple but critical operation in the data processing process. It accepts a seed value and a ceiling value to ensure that the output value remains within the specified range through the application of modelling. This node is essential in maintaining the integrity and sequencing of the data series, especially in a scenario where circulation patterns or boundary values are essential.

# Input types
## Required
- seed
    - The “seed” parameter is the starting point of the incremental operation. It is vital because it determines the initial value that nodes begin to calculate. Seeds are essential to ensure the replicability and consistency of the output, especially in iterative processes or simulations.
    - Comfy dtype: INT
    - Python dtype: int
- max_value
    - The " Max " parameter defines the upper limit of the incremental operation. It is important because it ensures that the output does not exceed a certain threshold, which is essential for maintaining the data'effectiveness within the expected range. This parameter plays a key role in controlling the range of node output.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- result
    - The " result" output is the result of the application of the modem to the input feed and the maximum value. It indicates a value that is limited to the specified range and applies to applications that require recycled or boundary numerical data.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class MaqueradeIncrementerNode:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'seed': ('INT', {'default': 0, 'min': -1, 'max': 18446744073709551615, 'step': 1}), 'max_value': ('INT', {'default': 1, 'min': 1, 'max': 18446744073709551615, 'step': 1})}}
    RETURN_TYPES = ('INT',)
    FUNCTION = 'increment'
    CATEGORY = 'Masquerade Nodes'

    def increment(self, seed, max_value):
        return (seed % max_value,)
```