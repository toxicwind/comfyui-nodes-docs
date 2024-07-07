# Documentation
- Class name: SamplerDPMAdaptative
- Category: sampling/custom_sampling/samplers
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The SamplerDPMadaptive node is designed to produce high-quality samples from the adaptation sampling process. Using the capacity of the k-diffusion library, it provides a flexible and efficient sampling mechanism that can fine-tune different cases.

# Input types
## Required
- order
    - The " order" parameter is essential for determining the order of the numerical method used in the sampling. It directly affects the accuracy and stability of the sampling process.
    - Comfy dtype: INT
    - Python dtype: int
- rtol
    - The “rtol” parameter sets the relative tolerance of the sampling algorithm, which is essential for controlling the accuracy of the sampling process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- atol
    - The “atol” parameter defines the absolute tolerance level of the sampling process and ensures that the samples produced meet certain quality standards.
    - Comfy dtype: FLOAT
    - Python dtype: float
- h_init
    - The length of the initial sampling algorithm for the “h_init” parameter plays a key role in the efficiency and performance of sampling operations.
    - Comfy dtype: FLOAT
    - Python dtype: float
- pcoeff
    - The “pcoeff” parameter affects the projected component of the adaptation to the sampling process, as well as the overall quality and condensability of the samples generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- icoeff
    - The “coeff” parameter controls the integral parts of the sample from which it is adapted, which is essential for maintaining the integrity of the sampling results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- dcoeff
    - The “dcoeff” parameter adjusts to the resistance factors during the sampling process to ensure stability and smoothness in the generation of the sample.
    - Comfy dtype: FLOAT
    - Python dtype: float
- accept_safety
    - The “accept_safety” parameter defines the safety threshold for the acceptance of new samples during the self-adaptation sampling process, which is important for the reliability of the sampling results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- eta
    - The “eta” parameter is a key factor in the process of adaptation to the sampling process and influences decision-making on the acceptance of new samples.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s_noise
    - The "s_noise" parameter sets the level of noise introduced during the sampling process, which can influence the diversity and randomity of the samples generated.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- SAMPLER
    - The output SAMPLER is an example of a configured sampling algorithm to be used to generate a sample based on the parameters provided.
    - Comfy dtype: SAMPLER
    - Python dtype: KSAMPLER

# Usage tips
- Infra type: GPU

# Source code
```
class SamplerDPMAdaptative:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'order': ('INT', {'default': 3, 'min': 2, 'max': 3}), 'rtol': ('FLOAT', {'default': 0.05, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 'atol': ('FLOAT', {'default': 0.0078, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 'h_init': ('FLOAT', {'default': 0.05, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 'pcoeff': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 'icoeff': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 'dcoeff': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 'accept_safety': ('FLOAT', {'default': 0.81, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 'eta': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False}), 's_noise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01, 'round': False})}}
    RETURN_TYPES = ('SAMPLER',)
    CATEGORY = 'sampling/custom_sampling/samplers'
    FUNCTION = 'get_sampler'

    def get_sampler(self, order, rtol, atol, h_init, pcoeff, icoeff, dcoeff, accept_safety, eta, s_noise):
        sampler = comfy.samplers.ksampler('dpm_adaptive', {'order': order, 'rtol': rtol, 'atol': atol, 'h_init': h_init, 'pcoeff': pcoeff, 'icoeff': icoeff, 'dcoeff': dcoeff, 'accept_safety': accept_safety, 'eta': eta, 's_noise': s_noise})
        return (sampler,)
```