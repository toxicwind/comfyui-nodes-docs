# Documentation
- Class name: GlobalSeed
- Category: InspirePack/Prompt
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

GlobalSeed is designed to manage and control the generation process by using seed values. It allows users to determine randomity by using different modes, ensuring consistency or diversity of output.

# Input types
## Required
- value
    - The "value" parameter is essential for setting the seeds of the generation process. By changing the seed, you can control the variability of the output and produce reproducing or diversified results.
    - Comfy dtype: INT
    - Python dtype: int
- mode
    - The "mode" parameter determines how the seed value affects the generation process. It provides a variety of models, such as 'fixed', 'incorporated' and 'randomize', each of which has different effects on the output and provides flexibility for the generation process.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- action
    - The " action " parameter provides a set of options to further refine the effects of the seed on generation. It works with the " mode " parameter and allows for fine control over randomity and consistency of results.
    - Comfy dtype: COMBO
    - Python dtype: str
- last_seed
    - The “last_seed” parameter is used to inherit a seed from previous generation, allowing continuity between the operation of the different generation processes.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- output
    - The output of the GlobalSeed node provides the results of the generation process and contains randomity of input parameter control.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class GlobalSeed:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'value': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'mode': ('BOOLEAN', {'default': True, 'label_on': 'control_before_generate', 'label_off': 'control_after_generate'}), 'action': (['fixed', 'increment', 'decrement', 'randomize', 'increment for each node', 'decrement for each node', 'randomize for each node'],), 'last_seed': ('STRING', {'default': ''})}}
    RETURN_TYPES = ()
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Prompt'
    OUTPUT_NODE = True

    def doit(self, **kwargs):
        return {}
```