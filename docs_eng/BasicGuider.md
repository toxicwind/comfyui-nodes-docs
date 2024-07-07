# Documentation
- Class name: BasicGuider
- Category: sampling/custom_sampling/guiders
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The BasicGuider node is responsible for generating a guide object that supports the sampling process. It is designed to integrate with the model and apply the conditions to guide the sample towards the desired result.

# Input types
## Required
- model
    - Model parameters are essential for the BasicGuider node because they define the bottom model that the lead will operate. It is through this model that the lead influences the sampling process.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- conditioning
    - Conditional input is essential for the BasicGuider node because it provides the conditions that will be used to guide the sampling process. It determines the direction and focus of the sampling according to the conditions provided.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- guider
    - The output leader is a key component of the BasicGuider node function. It represents an object that is configured according to the models and conditions provided and will be used to guide the sampling process.
    - Comfy dtype: GUIDER
    - Python dtype: comfy.samplers.CFGGuider

# Usage tips
- Infra type: CPU

# Source code
```
class BasicGuider:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'conditioning': ('CONDITIONING',)}}
    RETURN_TYPES = ('GUIDER',)
    FUNCTION = 'get_guider'
    CATEGORY = 'sampling/custom_sampling/guiders'

    def get_guider(self, model, conditioning):
        guider = Guider_Basic(model)
        guider.set_conds(conditioning)
        return (guider,)
```