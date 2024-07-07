# Documentation
- Class name: PolyexponentialScheduler
- Category: sampling/custom_sampling/schedulers
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

PollyexponentialScheduler nodes are designed to generate custom timetables for sigma values in diffusion models. It uses the polyexponential function to smooth changes in noise levels within the given number of steps. The scheduler is essential for controlling learning dynamics and ensuring stable sampling results.

# Input types
## Required
- steps
    - The Steps parameter defines the number of intervals that will set the sigma value. It is essential because it directly affects the particle size and duration of the noise schedule and the overall sampling process.
    - Comfy dtype: INT
    - Python dtype: int
- sigma_max
    - The sigma_max parameter represents the maximum sigma value, i.e. the initial noise level during the diffusion. It is important because it sets a ceiling on the noise level, which affects the condensation and quality of the final sample.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sigma_min
    - The sigma_min parameter represents the minimum value of the sigma, corresponding to the target noise level at the end of the diffusion process. It is essential because it determines the final noise level and affects the clarity and accuracy of the samples generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- rho
    - The " rho " parameter adjusts the curvature of the polyexponential schedule. It affects the speed of reduction of the sigma value from "sigma_max" to "sigma_min", thus affecting the overall shape and sampling dynamics of the noise schedule.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- SIGMAS
    - The output 'SIGMAS' is a sigma sequence generated by PolyexponentialScheduler. These values are essential for the sampling process because they specify the noise level of each step and directly affect the quality and stability of the samples obtained.
    - Comfy dtype: FLOAT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class PolyexponentialScheduler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'sigma_max': ('FLOAT', {'default': 14.614642, 'min': 0.0, 'max': 1000.0, 'step': 0.01, 'round': False}), 'sigma_min': ('FLOAT', {'default': 0.0291675, 'min': 0.0, 'max': 1000.0, 'step': 0.01, 'round': False}), 'rho': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False})}}
    RETURN_TYPES = ('SIGMAS',)
    CATEGORY = 'sampling/custom_sampling/schedulers'
    FUNCTION = 'get_sigmas'

    def get_sigmas(self, steps, sigma_max, sigma_min, rho):
        sigmas = k_diffusion_sampling.get_sigmas_polyexponential(n=steps, sigma_min=sigma_min, sigma_max=sigma_max, rho=rho)
        return (sigmas,)
```