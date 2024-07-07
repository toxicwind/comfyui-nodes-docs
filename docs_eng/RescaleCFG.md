# Documentation
- Class name: RescaleCFG
- Category: advanced/model
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

RescaleCFG nodes are designed to modify the configuration of the model by applying a zoom factor to its parameters. This adjustment is intended to enhance the performance of the model or adapt it to different operating conditions, without changing its basic architecture.

# Input types
## Required
- model
    - Model parameters are essential because they define the basic model that will be scaled back. They are the main input for node operations to achieve the scaling effect required.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- multiplier
    - Multiplier parameters are essential because they determine the extent of scaling to be applied to model configurations. They directly affect the final outcome of the re-scaling process.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- rescaled_model
    - Resizeed model output represents the model following the application scaling process. It is the result of node operations and marks a new configuration of the model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class RescaleCFG:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'multiplier': ('FLOAT', {'default': 0.7, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = 'advanced/model'

    def patch(self, model, multiplier):

        def rescale_cfg(args):
            cond = args['cond']
            uncond = args['uncond']
            cond_scale = args['cond_scale']
            sigma = args['sigma']
            sigma = sigma.view(sigma.shape[:1] + (1,) * (cond.ndim - 1))
            x_orig = args['input']
            x = x_orig / (sigma * sigma + 1.0)
            cond = (x - (x_orig - cond)) * (sigma ** 2 + 1.0) ** 0.5 / sigma
            uncond = (x - (x_orig - uncond)) * (sigma ** 2 + 1.0) ** 0.5 / sigma
            x_cfg = uncond + cond_scale * (cond - uncond)
            ro_pos = torch.std(cond, dim=(1, 2, 3), keepdim=True)
            ro_cfg = torch.std(x_cfg, dim=(1, 2, 3), keepdim=True)
            x_rescaled = x_cfg * (ro_pos / ro_cfg)
            x_final = multiplier * x_rescaled + (1.0 - multiplier) * x_cfg
            return x_orig - (x - x_final * sigma / (sigma * sigma + 1.0) ** 0.5)
        m = model.clone()
        m.set_model_sampler_cfg_function(rescale_cfg)
        return (m,)
```