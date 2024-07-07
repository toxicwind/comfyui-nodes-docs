# Documentation
- Class name: KSamplerSelect
- Category: sampling/custom_sampling/samplers
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

KSamplerSelect is designed to provide a selection mechanism for different sampling methods in the diffusion process. It abstractes the complexity of selecting and initializing various samplers, allowing users to focus on advanced tasks of sampling without going into the details of the initialization process for each sampler.

# Input types
## Required
- sampler_name
    - The sampler_name parameter is essential for determining which sampling method will be used. It guides nodes to select the appropriate sampler according to the name provided, which is essential for the implementation and results of the sampling process.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- SAMPLER
    - SAMPLER output represents the sampling method chosen. It covers the function of the selected sampler, which is important for the sampling process and the results required.
    - Comfy dtype: sampler
    - Python dtype: comfy.samplers.KSampler

# Usage tips
- Infra type: CPU

# Source code
```
class KSamplerSelect:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'sampler_name': (comfy.samplers.SAMPLER_NAMES,)}}
    RETURN_TYPES = ('SAMPLER',)
    CATEGORY = 'sampling/custom_sampling/samplers'
    FUNCTION = 'get_sampler'

    def get_sampler(self, sampler_name):
        sampler = comfy.samplers.sampler_object(sampler_name)
        return (sampler,)
```