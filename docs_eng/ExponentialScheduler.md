# Documentation
- Class name: ExponentialScheduler
- Category: sampling/custom_sampling/schedulers
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ExponentialScheduler node is designed to generate a plan for the level of noise that decreases exponentially with the number of steps specified. It is used in the context of the diffusion model to control the volume of noise added to or removed from the data during the sampling process, which is essential for generating high-quality output.

# Input types
## Required
- steps
    - The'steps' parameter defines the number of steps in the noise plan. It is very important because it determines the particle size of the noise reduction and affects the quality and condensation of the sampling process.
    - Comfy dtype: INT
    - Python dtype: int
- sigma_max
    - The'sigma_max' parameter sets the planned initial noise level. It's important because it determines the starting point of the loss of the noise index and affects the initial state of the diffusion process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sigma_min
    - The'sigma_min' parameter specifies the final noise level of the plan. It is important because it sets the target noise level that the sampling process aims to achieve, affecting the noise properties of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- SIGMAS
    - The `SIGMAS' output provides a calculated noise level plan that follows the index decay mode. It is important because it directly affects the next steps in the sampling process.
    - Comfy dtype: FLOAT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ExponentialScheduler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'sigma_max': ('FLOAT', {'default': 14.614642, 'min': 0.0, 'max': 1000.0, 'step': 0.01, 'round': False}), 'sigma_min': ('FLOAT', {'default': 0.0291675, 'min': 0.0, 'max': 1000.0, 'step': 0.01, 'round': False})}}
    RETURN_TYPES = ('SIGMAS',)
    CATEGORY = 'sampling/custom_sampling/schedulers'
    FUNCTION = 'get_sigmas'

    def get_sigmas(self, steps, sigma_max, sigma_min):
        sigmas = k_diffusion_sampling.get_sigmas_exponential(n=steps, sigma_min=sigma_min, sigma_max=sigma_max)
        return (sigmas,)
```