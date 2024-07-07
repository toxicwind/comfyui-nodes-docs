# Documentation
- Class name: RescaleClassifierFreeGuidance
- Category: custom_node_experiments
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI_experiments

The `patch' method of the RescaleClassifier FreeGuidance node is designed to modify the given model by introducing a repainting operation. It adjusts the internal configuration of the model to apply a dynamic zoom factor to the lead signal of the separator, thus allowing for more sophisticated control of model behaviour. This method is particularly suitable for fine-tuning model output to meet specific requirements or constraints.

# Input types
## Required
- model
    - The `model' parameter is essential for the node because it represents the machine learning model that will be modified by the `patch' method. It is the main input and determines the operation of the node and the subsequent behaviour of the post-repair model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- multiplier
    - The `multiplier' parameter plays a key role in controlling the extent to which it should be applied to model-guided signals. It is a floating number that determines the balance between the original configuration and the resizing configuration and directly affects the output of the repaired model.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- modified_model
    - The `modified_model' output is the result of the application of the `patch' method to the input model. It is a modified version of the original model, and the scaling factor for the guiding signal has been adjusted, which may result in different results based on the specified multipliers.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class RescaleClassifierFreeGuidance:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'multiplier': ('FLOAT', {'default': 0.7, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = 'custom_node_experiments'

    def patch(self, model, multiplier):

        def rescale_cfg(args):
            cond = args['cond']
            uncond = args['uncond']
            cond_scale = args['cond_scale']
            x_cfg = uncond + cond_scale * (cond - uncond)
            ro_pos = torch.std(cond, dim=(1, 2, 3), keepdim=True)
            ro_cfg = torch.std(x_cfg, dim=(1, 2, 3), keepdim=True)
            x_rescaled = x_cfg * (ro_pos / ro_cfg)
            x_final = multiplier * x_rescaled + (1.0 - multiplier) * x_cfg
            return x_final
        m = model.clone()
        m.set_model_sampler_cfg_function(rescale_cfg)
        return (m,)
```