# Documentation
- Class name: SamplerDPMPP_SDE
- Category: sampling/custom_sampling/samplers
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

SamplerDPMPP_SDE is designed to provide a self-defined sampling method for generating samples from proliferation models. It enhances the sampling process using the DPM-PP framework (pre-predictation of diffusion probabilities models) with random differential equations (SDE) methods. This node is essential for users who need detailed control of sampling parameters to achieve specific characteristics in the samples produced.

# Input types
## Required
- eta
    - The `eta' parameter is essential for controlling the level of noise during the sampling process. It directly affects the quality and condensability of the samples generated. Properly adjusted `eta' can lead to a more stable and efficient sampling process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s_noise
    - The `s_noise' parameter defines the initial noise scale that should be applied to the data during the sampling process. It plays an important role in determining the starting point of the diffusion process and the overall behaviour that affects the sampling method.
    - Comfy dtype: FLOAT
    - Python dtype: float
- r
    - The 'r' parameter is essential for adjusting the rate of absorption in the sampling algorithm. It affects the speed at which the sampling process approaches the target distribution, thus affecting the certainty of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise_device
    - The `noise_device' parameter determines the computing device used to generate noise, which may be GPS or CPU. The selection of the device can significantly affect the performance and velocity of the sampling process.
    - Comfy dtype: COMBO['gpu','cpu']
    - Python dtype: str

# Output types
- sampler
    - The output'sampler' is an example of a sampling algorithm tailored to the specific requirements set by the input parameters. It is important because it enables the sample to be produced in accordance with the required noise properties and collection criteria.
    - Comfy dtype: SAMPLER
    - Python dtype: KSAMPLER

# Usage tips
- Infra type: GPU

# Source code
```
class SamplerDPMPP_SDE:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'eta': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 's_noise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 'r': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 'noise_device': (['gpu', 'cpu'],)}}
    RETURN_TYPES = ('SAMPLER',)
    CATEGORY = 'sampling/custom_sampling/samplers'
    FUNCTION = 'get_sampler'

    def get_sampler(self, eta, s_noise, r, noise_device):
        if noise_device == 'cpu':
            sampler_name = 'dpmpp_sde'
        else:
            sampler_name = 'dpmpp_sde_gpu'
        sampler = comfy.samplers.ksampler(sampler_name, {'eta': eta, 's_noise': s_noise, 'r': r})
        return (sampler,)
```