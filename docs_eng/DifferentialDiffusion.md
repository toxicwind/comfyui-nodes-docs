# Documentation
- Class name: DifferentialDiffusion
- Category: _for_testing
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The DifferentialDiffusion node is designed to enhance the function of the given model by integrating self-defined noise processes. It operates on the basis of differential diffusion principles, allowing for the application of a decoupling code adjusted to the dynamics of the internal parameters of the model. The node is critical in refining model output by reducing the level of noise applied at each step of the diffusion process.

# Input types
## Required
- model
    - The'model' parameter is essential because it represents the core model that the DifferentialDiffusion node will operate. It is through this model that the node applies its noise function to make it an essential part of the node execution and the quality of the results produced.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- sigma
    - The'sigma' parameter is essential for determining the level of noise in the diffusion process. It directly influences how noise masks are applied, thus affecting the ultimate output of models. The'sigma' value is used to calculate the threshold for noise masks, and thus to form a proliferation step.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- denoise_mask
    - The 'denoise_mask'parameter plays an important role in node operations because it determines the areas in model output that will experience a reduction in noise. It is a key component of achieving the required level of noise control, ensuring that the diffusion process leads to refining and improving model output.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- extra_options
    - The 'extra_options' parameter is a dictionary that provides additional settings and information for node operations. It includes'model' and'sigmas' used to define the scope and parameters of the diffusion process. This parameter is essential for customization and flexibility of node functions.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Output types
- model
    - The output'model' is an enhanced version of the input model, now equipped with differential diffusion noise. It marks a successful application of the node function and provides a model that is better suited to produce high-quality output.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class DifferentialDiffusion:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',)}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'apply'
    CATEGORY = '_for_testing'
    INIT = False

    def apply(self, model):
        model = model.clone()
        model.set_model_denoise_mask_function(self.forward)
        return (model,)

    def forward(self, sigma: torch.Tensor, denoise_mask: torch.Tensor, extra_options: dict):
        model = extra_options['model']
        step_sigmas = extra_options['sigmas']
        sigma_to = model.inner_model.model_sampling.sigma_min
        if step_sigmas[-1] > sigma_to:
            sigma_to = step_sigmas[-1]
        sigma_from = step_sigmas[0]
        ts_from = model.inner_model.model_sampling.timestep(sigma_from)
        ts_to = model.inner_model.model_sampling.timestep(sigma_to)
        current_ts = model.inner_model.model_sampling.timestep(sigma[0])
        threshold = (current_ts - ts_to) / (ts_from - ts_to)
        return (denoise_mask >= threshold).to(denoise_mask.dtype)
```