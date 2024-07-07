# Documentation
- Class name: SamplerLMS
- Category: sampling/custom_sampling/samplers
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

SamplerLMS node is designed to generate a specific sampler for a specific sampling strategy. It encapsifies the function of creating and configures the sampler using the 'ksampler' function, which optimizes different sampling methods such as 'dpm_fast' or 'dpm_adaptive'. This node is essential during the sampling process to ensure that the appropriate sampler is used for the task at hand.

# Input types
## Required
- order
    - The `order' parameter is essential for determining the sequence of sampling methods to be used at SamplerLMS nodes. It directly affects the configuration of the sampler and, in turn, the quality and characteristics of the sampling process.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- sampler
    - The output of the SamplerLMS node's's'sampler' for a configured sampler object. It's important because it is used as a follow-up to the sampling process and directly affects the results of the sampling task.
    - Comfy dtype: SAMPLER
    - Python dtype: KSAMPLER

# Usage tips
- Infra type: CPU

# Source code
```
class SamplerLMS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'order': ('INT', {'default': 4, 'min': 1, 'max': 100})}}
    RETURN_TYPES = ('SAMPLER',)
    CATEGORY = 'sampling/custom_sampling/samplers'
    FUNCTION = 'get_sampler'

    def get_sampler(self, order):
        sampler = comfy.samplers.ksampler('lms', {'order': order})
        return (sampler,)
```