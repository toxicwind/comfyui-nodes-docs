# Documentation
- Class name: StableCascade_StageB_Conditioning
- Category: conditioning/stable_cascade
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The method `set_prior'is designed to integrate a priori information into the conditionality process and to enhance the stability and predictability of the cascade phase. This method plays a key role in shaping the output by setting up a priori information based on the conditions and context provided.

# Input types
## Required
- conditioning
    - The parameter 'conventioning' is essential to the operation of the node, as it provides the context information necessary to set the a priori. It directly influences the execution of the node by identifying the characteristics of the a priori.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
- stage_c
    - The parameter'stage_c' is critical to the function of the node, which represents the potential context of the stage to be used to reconcile the a priori. Its value influences how to set the a priori in the node operation.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Any]

# Output types
- conditioning
    - Output 'conventioning' is the modified version entered, reflecting the updated a priori information. It is important because it transmits the context of the node processed to the subsequent stage.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]

# Usage tips
- Infra type: CPU

# Source code
```
class StableCascade_StageB_Conditioning:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING',), 'stage_c': ('LATENT',)}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'set_prior'
    CATEGORY = 'conditioning/stable_cascade'

    def set_prior(self, conditioning, stage_c):
        c = []
        for t in conditioning:
            d = t[1].copy()
            d['stable_cascade_prior'] = stage_c['samples']
            n = [t[0], d]
            c.append(n)
        return (c,)
```