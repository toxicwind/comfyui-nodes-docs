# Documentation
- Class name: easySeed
- Category: EasyUse/Seed
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node is intended to generate random seeds for various processes and to ensure that the system has some recoverability and control over random elements.

# Input types
## Required
- seed
    - Seed parameters are essential for the operation of nodes, as they determine the starting point for random numbers generation, thus influencing the outcome of the random process.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- prompt
    - While reminders are not necessary, they can provide additional context or guidance for the operation of nodes and may make randomness more sophisticated to meet specific objectives.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - This parameter, while optional, can provide additional information that may be used to enhance functionality or adjust the behaviour of nodes in image-processing tasks.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: str
- my_unique_id
    - The provision of only ID parameters helps track and manage the implementation of multiple examples of nodes and helps the organization of the entire workflow.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- seed
    - The exported torrent represents the random number generated as a reference for subsequent operations that rely on this initial random point.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class easySeed:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'seed': ('INT', {'default': 0, 'min': 0, 'max': MAX_SEED_NUM})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('seed',)
    FUNCTION = 'doit'
    CATEGORY = 'EasyUse/Seed'
    OUTPUT_NODE = True

    def doit(self, seed=0, prompt=None, extra_pnginfo=None, my_unique_id=None):
        return (seed,)
```