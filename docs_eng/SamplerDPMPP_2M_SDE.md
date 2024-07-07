# Documentation
- Class name: SamplerDPMPP_2M_SDE
- Category: sampling/custom_sampling/samplers
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The SamplerDPMPP_2M_SDE class is designed to provide a sampling method for generating data points from the probability distribution. It uses the SDE method to create a Markov chain that captures the distribution required. This node is particularly suitable for applications that require high-quality samples and are critical for calculating efficiency.

# Input types
## Required
- solver_type
    - The solver_type parameter determines the numerical method used to solve the bottom SDE. It is essential for the accuracy and stability of the sampling process. The options available are'midpoint' and 'heun', each of which provides a different trade-off between speed and accuracy.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- eta
    - The eta parameter controls the learning rate during the SDE sampling process. It significantly affects the rate of collection and the quality of the samples generated. The eta value of a good choice to achieve a balance between exploration and utilization in the sampling space is essential.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s_noise
    - The s_noise parameter represents the level of noise during the sampling process. It is an important factor in determining the variability of the sample. The adjustment s_noise can help to achieve the required level of diversity in the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise_device
    - The noise_device parameter specifies the computing device used to generate noise during the sampling process. It can be set to 'gpu' or 'cpu', depending on the hardware available and the required performance properties.
    - Comfy dtype: COMBO[str]
    - Python dtype: str

# Output types
- sampler
    - The output of the SamplerDPMPP_2M_SDE node is a sampler object that covers a configured sampling method. This object can be used to generate a sample from a given distribution based on the parameters provided during the node configuration.
    - Comfy dtype: SAMPLER
    - Python dtype: KSAMPLER

# Usage tips
- Infra type: GPU

# Source code
```
class SamplerDPMPP_2M_SDE:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'solver_type': (['midpoint', 'heun'],), 'eta': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 's_noise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 'noise_device': (['gpu', 'cpu'],)}}
    RETURN_TYPES = ('SAMPLER',)
    CATEGORY = 'sampling/custom_sampling/samplers'
    FUNCTION = 'get_sampler'

    def get_sampler(self, solver_type, eta, s_noise, noise_device):
        if noise_device == 'cpu':
            sampler_name = 'dpmpp_2m_sde'
        else:
            sampler_name = 'dpmpp_2m_sde_gpu'
        sampler = comfy.samplers.ksampler(sampler_name, {'eta': eta, 's_noise': s_noise, 'solver_type': solver_type})
        return (sampler,)
```