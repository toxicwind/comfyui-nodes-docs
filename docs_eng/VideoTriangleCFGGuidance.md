# Documentation
- Class name: VideoTriangleCFGGuidance
- Category: sampling/video_models
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The VideoTriangleCfGGuidance node is designed to enhance the controlability of the video model by applying patches that can be configured to guide functions. It changes the sampling process to allow fine-tuning of the resulting video content, based on linear configuration proportionally mixed conditions and non-conditional output.

# Input types
## Required
- model
    - Model parameters are essential for the Video TriangleCfGguidance node, as it represents a video model that will be guided and modified. Node relies on this input to apply patches and adjust sampling behaviour accordingly.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- min_cfg
    - Min_cfg parameters determine the minimum proportion of configurations that are used for mixed video models and for non-conditional output. It plays a key role in controlling the level of guidance applied during sampling.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- modified_model
    - The modified_model output represents an updated video model that has been updated using a new sampling guide. It is important because it is a direct result of the application of patches through the VideoTriangleCfGguidance node, enabling the creation of video features with adjusted content.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class VideoTriangleCFGGuidance:

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
            period = 1.0
            values = torch.linspace(0, 1, cond.shape[0], device=cond.device)
            values = 2 * (values / period - torch.floor(values / period + 0.5)).abs()
            scale = (values * (cond_scale - min_cfg) + min_cfg).reshape((cond.shape[0], 1, 1, 1))
            return uncond + scale * (cond - uncond)
        m = model.clone()
        m.set_model_sampler_cfg_function(linear_cfg)
        return (m,)
```