# Documentation
- Class name: DualCFGGuider
- Category: sampling/custom_sampling/guiders
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The DualCFGGuider node is designed to guide the sampling process for the generation of models by using two sets of conditions. It focuses on adjusting the effects of positive, negative and intermediate conditions through the configuration of parameters, thereby enhancing control over the generation of results and allowing fine-tuning of outputs.

# Input types
## Required
- model
    - Model parameters are essential because they represent the node that will be used to produce the model for the sampling process. It defines the application conditions and the basis for the configuration to produce the output required.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- cond1
    - The first condition input is essential to provide the initial context or direction of the sampling process. It helps to shape the direction in which the content is generated according to the specific requirements of the task at hand.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- cond2
    - The second condition input further refines the sampling process by providing additional contextual layers. It works in tandem with the first condition input to achieve more subtle and detailed results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - Negative condition input plays a key role in guiding the sampling process away from desired outcomes. It helps to define what should be avoided in generating content, ensuring that the results are more targeted and focused.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
## Optional
- cfg_conds
    - The cfg_conds parameter allows the configuration to be adjusted to affect the balance of both positive and negative effects during the sampling process. This is an important adjustment parameter for achieving the level required for generating control.
    - Comfy dtype: FLOAT
    - Python dtype: float
- cfg_cond2_negative
    - cfg_cond2_negative parameters are used to fine-tune the impact of the second conditionalities, especially in their role as negative conditionalities. It provides a mechanism to adjust the intensity of the negative guidance applied during sampling.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- guider
    - The output guider is an example of the configuration of the DualCFGGuider class, which is intended to be used during the sampling process. It encapsifies the conditions and configurations set by the user to ensure that the sampling meets the required specifications.
    - Comfy dtype: GUIDER
    - Python dtype: comfy.samplers.CFGGuider

# Usage tips
- Infra type: CPU

# Source code
```
class DualCFGGuider:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'cond1': ('CONDITIONING',), 'cond2': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'cfg_conds': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.1, 'round': 0.01}), 'cfg_cond2_negative': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.1, 'round': 0.01})}}
    RETURN_TYPES = ('GUIDER',)
    FUNCTION = 'get_guider'
    CATEGORY = 'sampling/custom_sampling/guiders'

    def get_guider(self, model, cond1, cond2, negative, cfg_conds, cfg_cond2_negative):
        guider = Guider_DualCFG(model)
        guider.set_conds(cond1, cond2, negative)
        guider.set_cfg(cfg_conds, cfg_cond2_negative)
        return (guider,)
```