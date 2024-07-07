# Documentation
- Class name: WLSH_Seed_to_Number
- Category: WLSH Nodes/number
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The node is intended to convert input data into numerical expressions that facilitate the processing and analysis of data within the system.

# Input types
## Required
- seed
    - Seed parameters are essential as they provide raw data necessary for node implementation of conversion functions.
    - Comfy dtype: SEED
    - Python dtype: Dict[str, Any]

# Output types
- number
    - The output is expressed from the input of derived figures, which is essential for the further calculation process within the system.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Seed_to_Number:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'seed': ('SEED',)}}
    RETURN_TYPES = ('INT',)
    FUNCTION = 'number_to_seed'
    CATEGORY = 'WLSH Nodes/number'

    def number_to_seed(self, seed):
        return (int(seed['seed']),)
```