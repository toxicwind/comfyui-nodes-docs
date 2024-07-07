# Documentation
- Class name: SamplerDPMPP_3M_SDE
- Category: sampling/custom_sampling/samplers
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

SamplerDPMPP_3M_SDE nodes are designed to produce high-quality samples from trained models using specific sampling methods (known as DPM++, equipped with 3-Mixture SDE controllers). They apply to scenarios that require efficient and high-realistic sampling, providing a balance between speed and quality of samples.

# Input types
## Required
- eta
    - The parameter 'eta' controls the search rate during the sampling process. It is the key factor that determines the diversity of the sample. Adjusting 'eta' can lead to more or less changes in the output, thus affecting the overall creativity and uniqueness of the result.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s_noise
    - The parameter's_noise' defines the initial noise level applied during the sampling process. It plays an important role in the initial state of the sampling algorithm and influences the starting point for generating the sample. This parameter is essential for setting the right noise conditions to achieve the required quality of the sample.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- noise_device
    - The parameter'noise_device' is specified as a computing device for generating noise, which may be GPS or CPU. This option affects the performance and efficiency of the sampling process, especially in scenarios where high computing capacity is required to achieve faster processing.
    - Comfy dtype: COMBO['gpu', 'cpu']
    - Python dtype: str

# Output types
- sampler
    - The output'sampler' is an example of a sampling method tailored to the specific requirements of the DPM++3-Mixture SDE. It covers the functions required to perform the sampling process and provides a structured approach to generating high-quality samples from the model.
    - Comfy dtype: SAMPLER
    - Python dtype: KSAMPLER

# Usage tips
- Infra type: GPU

# Source code
```
class SamplerDPMPP_3M_SDE:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'eta': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 's_noise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 'noise_device': (['gpu', 'cpu'],)}}
    RETURN_TYPES = ('SAMPLER',)
    CATEGORY = 'sampling/custom_sampling/samplers'
    FUNCTION = 'get_sampler'

    def get_sampler(self, eta, s_noise, noise_device):
        if noise_device == 'cpu':
            sampler_name = 'dpmpp_3m_sde'
        else:
            sampler_name = 'dpmpp_3m_sde_gpu'
        sampler = comfy.samplers.ksampler(sampler_name, {'eta': eta, 's_noise': s_noise})
        return (sampler,)
```