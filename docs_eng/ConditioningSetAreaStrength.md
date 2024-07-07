# Documentation
- Class name: ConditioningSetAreaStrength
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

ConditionSetAreaStrength is designed to modify and enhance these sets of conditions by adding specified strength values to the set of conditions. It plays a key role in adjusting the effects of the set of conditions in the model, allowing fine-tuning the sensitivity of the model to different inputs.

# Input types
## Required
- conditioning
    - A condition set parameter is essential to define the basic set of conditions that the model will consider. It is the starting point for node operations and determines the initial state of the condition set.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]
- strength
    - The strength parameter is essential to determine the size of the influence of the set of conditions on model output. It allows the strength of the conditions to be adjusted to influence the end result.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- conditioning
    - The output condition set is modified according to the input parameters, with strength values attached to enhance its impact on the model. It represents an updated set of conditions ready for further processing or analysis.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]]]

# Usage tips
- Infra type: CPU

# Source code
```
class ConditioningSetAreaStrength:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'append'
    CATEGORY = 'conditioning'

    def append(self, conditioning, strength):
        c = node_helpers.conditioning_set_values(conditioning, {'strength': strength})
        return (c,)
```