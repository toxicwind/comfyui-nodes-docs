# Documentation
- Class name: CreateSeedNode
- Category: ♾️Mixlab/Utils
- Output node: True
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node is used to generate seed values for various randomization processes to ensure that randomity can be controlled and replicated when needed.

# Input types
## Required
- seed
    - Seed parameters are essential for the initialization of random number generators and can produce repeatable and predictable results in a random process.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- seed
    - The value of the exported torrent is used as a reference for the initial randomization process, indicating the specific state from which the randomity is derived.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class CreateSeedNode:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('seed',)
    OUTPUT_NODE = True
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Utils'

    def run(self, seed):
        return (seed,)
```