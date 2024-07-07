# Documentation
- Class name: ModelSamplerTonemapNoiseTest
- Category: custom_node_experiments
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI_experiments

Node `patch'of `ModelSamplerTonemap NoiseTest'aims to enhance the sampling process of the given model by applying colour mapping and noise reduction techniques. It works by adjusting noise predictions in the context of the Reinhard colour mapping operation, with the aim of improving the visual quality and consistency of sample output.

# Input types
## Required
- model
    - The parameter `model'is essential because it represents the machine learning model to be sampled. This is the main input, which will be used to reduce colour mapping and noise.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
## Optional
- multiplier
    - The parameter `multiplier'is used to scal the noise reduction effect. It allows the intensity of the noise filtering process to be fine-tuned to the specific needs of the task at hand.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- model
    - The output `model'is a modified version of the input model, which is now equipped with an enhanced sampling function that combines colored mapping and noise reduction techniques to improve the quality of the output.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class ModelSamplerTonemapNoiseTest:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'multiplier': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = 'custom_node_experiments'

    def patch(self, model, multiplier):

        def sampler_tonemap_reinhard(args):
            cond = args['cond']
            uncond = args['uncond']
            cond_scale = args['cond_scale']
            noise_pred = cond - uncond
            noise_pred_vector_magnitude = (torch.linalg.vector_norm(noise_pred, dim=1) + 1e-10)[:, None]
            noise_pred /= noise_pred_vector_magnitude
            mean = torch.mean(noise_pred_vector_magnitude, dim=(1, 2, 3), keepdim=True)
            std = torch.std(noise_pred_vector_magnitude, dim=(1, 2, 3), keepdim=True)
            top = (std * 3 + mean) * multiplier
            noise_pred_vector_magnitude *= 1.0 / top
            new_magnitude = noise_pred_vector_magnitude / (noise_pred_vector_magnitude + 1.0)
            new_magnitude *= top
            return uncond + noise_pred * new_magnitude * cond_scale
        m = model.clone()
        m.set_model_sampler_cfg_function(sampler_tonemap_reinhard)
        return (m,)
```