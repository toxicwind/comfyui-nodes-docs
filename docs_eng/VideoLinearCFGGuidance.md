# Documentation
- Class name: VideoLinearCFGGuidance
- Category: sampling/video_models
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

VideoLinearCfGuidance node is designed to provide a way to modify the guidance of the sampling process for video models. It does this by using linear configuration function patches, which mixes the unconditional and conditional sampling in a smooth manner according to the minimum configuration scale. This node enhances the ability of models to generate videos with different details and levels of control.

# Input types
## Required
- model
    - Model parameters are essential for VideoLinearCfGuidance nodes, as they represent the video model that will be repaired. It is through this model that nodes perform their functions and allow custom sampling processes.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- min_cfg
    - Min_cfg parameters determine the minimum configuration ratio of the linear guidance function within the VideoLinearCfGuidance node. It is a key factor in controlling the mixing between unconditional and conditional sampling, thus influencing the properties of the output video.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- modified_model
    - The output of the VideoLinearCfGuidance node is a modified video model that integrates linear configuration functions. This allows for a more detailed approach to video generation and provides greater flexibility and control over the final output.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class VideoLinearCFGGuidance:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'min_cfg': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.5, 'round': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = 'sampling/video_models'

    def patch(self, model, min_cfg):

        def linear_cfg(args):
            cond = args['cond']
            uncond = args['uncond']
            cond_scale = args['cond_scale']
            scale = torch.linspace(min_cfg, cond_scale, cond.shape[0], device=cond.device).reshape((cond.shape[0], 1, 1, 1))
            return uncond + scale * (cond - uncond)
        m = model.clone()
        m.set_model_sampler_cfg_function(linear_cfg)
        return (m,)
```