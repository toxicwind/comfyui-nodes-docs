# Documentation
- Class name: KarrasScheduler
- Category: sampling/custom_sampling/schedulers
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

KarrasScheduler nodes are designed to generate noise schedules based on the Karras et al. (2022) method. It plays a key role in the self-defined sampling process, providing a range of considerations that determine the level of noise added to the data during the sampling overlap. The node plays a key role in controlling proliferation, ensuring a smooth transition from noise to clear data.

# Input types
## Required
- steps
    - The'steps' parameter defines the number of overlaps in the sampling process. It is essential because it directly affects the particle size of the noise schedule and, in turn, the quality of the sampling results.
    - Comfy dtype: INT
    - Python dtype: int
- sigma_max
    - The `sigma_max' parameter specifies the maximum standard deviation of noise during the sampling process. It is a key determinant of the initial noise level and is essential for the overall authenticity of the sampling.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sigma_min
    - The `sigma_min' parameter sets the minimum standard deviation for noise, affecting the ultimate clarity of the sampling data. It plays an important role in fine-tuning the noise schedule at the end of the sampling process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- rho
    - The `rho' parameter controls the rate at which noise standard deviations during sampling overlaps decrease. It is a key factor in the planning for noise reduction and affects the consolidation of sampling algorithms.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- SIGMAS
    - The output 'SIGMAS' is a series of values that represent the noise schedule of the sampling process. This schedule is essential for algorithms to gradually reduce noise and generate clear data expressions.
    - Comfy dtype: SIGMAS
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class KarrasScheduler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'sigma_max': ('FLOAT', {'default': 14.614642, 'min': 0.0, 'max': 1000.0, 'step': 0.01, 'round': False}), 'sigma_min': ('FLOAT', {'default': 0.0291675, 'min': 0.0, 'max': 1000.0, 'step': 0.01, 'round': False}), 'rho': ('FLOAT', {'default': 7.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False})}}
    RETURN_TYPES = ('SIGMAS',)
    CATEGORY = 'sampling/custom_sampling/schedulers'
    FUNCTION = 'get_sigmas'

    def get_sigmas(self, steps, sigma_max, sigma_min, rho):
        sigmas = k_diffusion_sampling.get_sigmas_karras(n=steps, sigma_min=sigma_min, sigma_max=sigma_max, rho=rho)
        return (sigmas,)
```