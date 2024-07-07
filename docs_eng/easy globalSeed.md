# Documentation
- Class name: globalSeed
- Category: EasyUse/Seed
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

Such envelopes capture the functions of generating and managing random seeds for various operations within the system, ensuring that the environments for experimental and model training are controlled and reproducing.

# Input types
## Required
- value
    - The “value” parameter is critical in assigning the initial seed value, which is important in ensuring the reposability of the random process of the system.
    - Comfy dtype: INT
    - Python dtype: int
- mode
    - The “mode” parameter determines the control mechanism for seed generation and determines whether the seed is set before or after the generation process, thus affecting the overall randomity of the system.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- action
    - The “action” parameter provides multiple seed operations strategies that allow for dynamic adjustments of seeds during the implementation of the system, which are essential for iterative or branch processes.
    - Comfy dtype: COMBO
    - Python dtype: str
- last_seed
    - The “last_seed” parameter serves as a reference for recently used seeds and facilitates the continuity and tracking of the system's randomization process.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- result
    - The “result” output provides a structured summary of seed management operations, encapsulating the results and application settings of the randomization process.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class globalSeed:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'value': ('INT', {'default': 0, 'min': 0, 'max': MAX_SEED_NUM}), 'mode': ('BOOLEAN', {'default': True, 'label_on': 'control_before_generate', 'label_off': 'control_after_generate'}), 'action': (['fixed', 'increment', 'decrement', 'randomize', 'increment for each node', 'decrement for each node', 'randomize for each node'],), 'last_seed': ('STRING', {'default': ''})}}
    RETURN_TYPES = ()
    FUNCTION = 'doit'
    CATEGORY = 'EasyUse/Seed'
    OUTPUT_NODE = True

    def doit(self, **kwargs):
        return {}
```