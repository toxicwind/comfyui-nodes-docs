# Documentation
- Class name: VPScheduler
- Category: sampling/custom_sampling/schedulers
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

VPSscheduler nodes are designed to maintain a continuous VP noise schedule for proliferation models. It plays a vital role in the sampling process, which is essential for achieving high-quality results in the resulting samples by determining the level of noise at each step.

# Input types
## Required
- steps
    - The parameter'steps' defines the number of steps in the noise schedule. It is a fundamental aspect of the sampling process, as it determines the particle size of the noise level applied at each step and directly affects the quality of the final output.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- beta_d
    - The parameter 'beta_d' controls the rate of noise increase in the schedule. It's important because it affects the distribution of noise in the process and, in turn, the collection and detail of the samples generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- beta_min
    - The parameter 'beta_min' sets the minimum level of noise in the schedule. It is important because it ensures that the initial steps of the sampling process have sufficient noise levels to facilitate the generation of diverse and detailed outputs.
    - Comfy dtype: FLOAT
    - Python dtype: float
- eps_s
    - Parameter 'eps_s' specifies the end value for the noise schedule. It is a key factor in determining the final noise level to be applied during the sampling process, which is essential for the fine detail and overall quality of the sample to be generated.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- sigmas
    - The output'sigmas' provides the level of noise calculated at each step of the VP noise schedule. It is important because it forms the basis for the sampling process and guides the generation of the final output.
    - Comfy dtype: SIGMAS
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class VPScheduler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'beta_d': ('FLOAT', {'default': 19.9, 'min': 0.0, 'max': 1000.0, 'step': 0.01, 'round': False}), 'beta_min': ('FLOAT', {'default': 0.1, 'min': 0.0, 'max': 1000.0, 'step': 0.01, 'round': False}), 'eps_s': ('FLOAT', {'default': 0.001, 'min': 0.0, 'max': 1.0, 'step': 0.0001, 'round': False})}}
    RETURN_TYPES = ('SIGMAS',)
    CATEGORY = 'sampling/custom_sampling/schedulers'
    FUNCTION = 'get_sigmas'

    def get_sigmas(self, steps, beta_d, beta_min, eps_s):
        sigmas = k_diffusion_sampling.get_sigmas_vp(n=steps, beta_d=beta_d, beta_min=beta_min, eps_s=eps_s)
        return (sigmas,)
```