# Documentation
- Class name: SamplerEulerAncestral
- Category: sampling/custom_sampling/samplers
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

SampolerEuler Ancestral is designed to produce an ancestry sampler using the Euler method. It contributes to the sampling process by providing a customised method, using the properties of the Euler method to produce samples that match the specific noise plan.

# Input types
## Required
- eta
    - The eta parameter is essential to control the noise level during the sampling process. It directly affects the quality and condensation of the samples generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s_noise
    - The s_noise parameter is very important in defining the initial noise level during the sampling process. It sets the starting point for noise reduction and affects overall sample generation.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- sampler
    - The output sampler is the key component in the sampling process, and it covers the logic of generating samples based on the noise plan and parameters provided.
    - Comfy dtype: SAMPLER
    - Python dtype: comfy.samplers.KSampler

# Usage tips
- Infra type: CPU

# Source code
```
class SamplerEulerAncestral:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'eta': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 's_noise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False})}}
    RETURN_TYPES = ('SAMPLER',)
    CATEGORY = 'sampling/custom_sampling/samplers'
    FUNCTION = 'get_sampler'

    def get_sampler(self, eta, s_noise):
        sampler = comfy.samplers.ksampler('euler_ancestral', {'eta': eta, 's_noise': s_noise})
        return (sampler,)
```