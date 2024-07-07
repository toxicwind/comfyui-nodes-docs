# Documentation
- Class name: RandomGeneratorForList
- Category: InspirePack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node is intended to generate a series of random numbers based on given seeds and to ensure that the same seeds will produce the same random list, which is essential for repeatability in various applications.

# Input types
## Required
- signal
    - Signal parameters represent input data that triggers random numbers. It is important because it may affect the initialization of the random number generator.
    - Comfy dtype: ANY
    - Python dtype: Any
## Optional
- seed
    - Seed parameters are essential for determining the starting point of a random sequence. It ensures that the same seeds will produce the same random list, which is essential for repeatability.
    - Comfy dtype: INT
    - Python dtype: int
- unique_id
    - The unique_id parameter is used to track and manage the number of random numbers generated for each of the only examples, ensuring that each case has a different set of random numbers.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- signal
    - The output signal retains the original input signal, indicating that the random number generation process has been completed.
    - Comfy dtype: ANY
    - Python dtype: Any
- random_value
    - The Random_value output represents the newly generated seed, which is a random integer that can be used for further random number generation or other purposes.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class RandomGeneratorForList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'signal': (utils.any_typ,), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = (utils.any_typ, 'INT')
    RETURN_NAMES = ('signal', 'random_value')
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Util'

    def doit(self, signal, seed, unique_id):
        if unique_id not in list_counter_map:
            count = 0
        else:
            count = list_counter_map[unique_id]
        list_counter_map[unique_id] = count + 1
        rn = random.Random()
        rn.seed(seed + count)
        new_seed = random.randint(0, 1125899906842624)
        return (signal, new_seed)
```