# Documentation
- Class name: SamplerLCMCycle
- Category: sampling/custom_sampling/samplers
- Output node: False
- Repo Ref: https://github.com/jojkaart/ComfyUI-sampler-lcm-alternative

The node is used to create a sampler dedicated to complex sampling tasks in the generation model. It abstractes the complexity of the sampling process and emphasizes the role of nodes in generating high-quality samples through the potential space of an effective navigation model. The main objective of the node is to provide users with a reliable and flexible model reasoning tool, without the need for in-depth knowledge of bottom algorithms.

# Input types
## Required
- euler_steps
    - This parameter determines the number of Eurosteps to be taken in the sampling process, directly affecting the quality and condensability of the samples generated. It is essential to balance the cost and the accuracy of the sampling.
    - Comfy dtype: INT
    - Python dtype: int
- lcm_steps
    - This parameter assigns a minimum common multiple (LCM) step, which is essential for synchronizing the sampling process at different dimensions and ensuring a consistent transition between steps.
    - Comfy dtype: INT
    - Python dtype: int
- tweak_sigmas
    - The boolean sign determines whether to adjust the sigma value, which allows the sampling process to be improved and leads to minor changes in the sample.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- ancestral
    - Ancestry parameters influence the direction of the sampling process to older potential states, which may affect the style or thematic characteristics of the samples generated.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- sampler
    - The output is a configured sampler that is customized according to input specifications and prepared for use in the generation model to produce a sample that meets the characteristics required.
    - Comfy dtype: SAMPLER
    - Python dtype: comfy.samplers.KSampler

# Usage tips
- Infra type: CPU

# Source code
```
class SamplerLCMCycle:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'euler_steps': ('INT', {'default': 1, 'min': 1, 'max': 50}), 'lcm_steps': ('INT', {'default': 2, 'min': 1, 'max': 50}), 'tweak_sigmas': ('BOOLEAN', {'default': False}), 'ancestral': ('FLOAT', {'default': 0, 'min': 0, 'max': 1.0, 'step': 0.01, 'round': False})}}
    RETURN_TYPES = ('SAMPLER',)
    CATEGORY = 'sampling/custom_sampling/samplers'
    FUNCTION = 'get_sampler'

    def get_sampler(self, euler_steps, lcm_steps, tweak_sigmas, ancestral):
        sampler = comfy.samplers.KSAMPLER(sample_lcm_cycle, extra_options={'euler_steps': euler_steps, 'lcm_steps': lcm_steps, 'tweak_sigmas': tweak_sigmas, 'ancestral': ancestral})
        return (sampler,)
```