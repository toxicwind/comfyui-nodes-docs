# Documentation
- Class name: TonemapNoiseWithRescaleCFG
- Category: custom_node_experiments
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI_experiments

TonemapnoiseWithcaleCFG is designed to enhance the visual quality of generating images by applying a combination of noise mitigation strategies using colour-mapping techniques. It adjusts the contrast and brightness of the images through complex resizing operations in order to optimize their appearance and reduce noise.

# Input types
## Required
- model
    - Model parameters are essential because they represent the generation models that the nodes will operate. They are the basis for applying colour-typographical mapping and repainting operations to produce high-quality images.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
## Optional
- tonemap_multiplier
    - The tonemap_multiplier parameter controls the strength of the colour map effect applied to the image. It is essential to fine-tune the visual results to achieve the required contrast and brightness levels.
    - Comfy dtype: FLOAT
    - Python dtype: float
- rescale_multiplier
    - Rescale_multiplier parameters determine the balance between resize and original image values during noise reduction. It plays an important role in keeping image details while reducing noise.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- model
    - The output model is a modified generation model with an enhanced sampler configuration function, which combines colored mapping and noise abatement techniques to produce images that are more visually attractive.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class TonemapNoiseWithRescaleCFG:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'tonemap_multiplier': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01}), 'rescale_multiplier': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = 'custom_node_experiments'

    def patch(self, model, tonemap_multiplier, rescale_multiplier):

        def tonemap_noise_rescale_cfg(args):
            cond = args['cond']
            uncond = args['uncond']
            cond_scale = args['cond_scale']
            noise_pred = cond - uncond
            noise_pred_vector_magnitude = (torch.linalg.vector_norm(noise_pred, dim=1) + 1e-10)[:, None]
            noise_pred /= noise_pred_vector_magnitude
            mean = torch.mean(noise_pred_vector_magnitude, dim=(1, 2, 3), keepdim=True)
            std = torch.std(noise_pred_vector_magnitude, dim=(1, 2, 3), keepdim=True)
            top = (std * 3 + mean) * tonemap_multiplier
            noise_pred_vector_magnitude *= 1.0 / top
            new_magnitude = noise_pred_vector_magnitude / (noise_pred_vector_magnitude + 1.0)
            new_magnitude *= top
            x_cfg = uncond + noise_pred * new_magnitude * cond_scale
            ro_pos = torch.std(cond, dim=(1, 2, 3), keepdim=True)
            ro_cfg = torch.std(x_cfg, dim=(1, 2, 3), keepdim=True)
            x_rescaled = x_cfg * (ro_pos / ro_cfg)
            x_final = rescale_multiplier * x_rescaled + (1.0 - rescale_multiplier) * x_cfg
            return x_final
        m = model.clone()
        m.set_model_sampler_cfg_function(tonemap_noise_rescale_cfg)
        return (m,)
```