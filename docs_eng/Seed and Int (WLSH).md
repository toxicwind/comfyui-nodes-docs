# Documentation
- Class name: WLSH_Seed_and_Int
- Category: WLSH Nodes/number
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

This node generates a pair of torrents and integer values based on the given seed and creates and manages the only identifier in the system.

# Input types
## Required
- seed
    - Seeds are the basic parameters for initiating the generation of the only integer process. They are essential to ensure consistency and repeatability of results.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- seed
    - The output torrent is the original input feed, marking its role as an identifier in the operation. Integer output is the transformation of the torrent, indicating its importance in the process.
    - Comfy dtype: INT
    - Python dtype: int
- int_representation
    - Integer expression is derived from the input feed as the only essential output of the node function.
    - Comfy dtype: SEED
    - Python dtype: Dict[str, int]

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Seed_and_Int:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('INT', 'SEED')
    FUNCTION = 'seed_and_int'
    CATEGORY = 'WLSH Nodes/number'

    def seed_and_int(self, seed):
        return (seed, {'seed': seed})
```