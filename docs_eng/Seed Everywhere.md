# Documentation
- Class name: SeedEverywhere
- Category: Initialization
- Output node: True
- Repo Ref: https://github.com/chrisgoringe/cg-use-everywhere

SeedEverywhere node is designed to ensure the repeatability of random operations in different parts of the system. It is done by setting seeds for random number generators, which is essential for scientific experiments and simulations that require consistent results.

# Input types
## Required
- seed
    - The "seed" parameter is essential to initialize the random number generator to a known state. This ensures that, at each execution node, the subsequent random operation will produce the same result, which is essential for achieving consistent and comparable results in various applications.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- id
    - The “id” parameter, although not necessary, is an identifier of the message sent by the node. This may be particularly useful in systems that run multiple examples of the node at the same time, as it helps to track and manage messages from different examples.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- seed
    - The output “seed” corresponds to the input provided to the node, indicating the status of the random number generator after the node is executed. This can be used for further operations that require a consistent random state to ensure continuity of the random process.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SeedEverywhere(Base):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}, 'hidden': {'id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('INT',)

    def func(self, seed, id):
        message(id, seed)
        return (seed,)
```