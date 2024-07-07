# Documentation
- Class name: DisableNoise
- Category: sampling/custom_sampling/noise
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

DisableNoise nodes are designed to contain noise during the sampling process and to ensure that there is no random element in the output. In a scenario that requires certainty, it provides a key component that provides a silent path to potential expression.

# Input types
## Optional
- seed
    - The Seed parameter is used in the initial noise generation process. Although it is not necessary, it plays a key role in ensuring the repeatability of results, allowing consistent results to be obtained in different operations.
    - Comfy dtype: int
    - Python dtype: int

# Output types
- NOISE
    - The output of DisableNoise is an example of the Noise_EmptyNoise class, which represents a noiseless state. It marks no noise in the potential image generated and is consistent with the purpose of the node to provide a definitive output.
    - Comfy dtype: Noise_EmptyNoise
    - Python dtype: comfy.k_diffusion.sampling.DisableNoise.Noise_EmptyNoise

# Usage tips
- Infra type: CPU

# Source code
```
class DisableNoise:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}}
    RETURN_TYPES = ('NOISE',)
    FUNCTION = 'get_noise'
    CATEGORY = 'sampling/custom_sampling/noise'

    def get_noise(self):
        return (Noise_EmptyNoise(),)
```