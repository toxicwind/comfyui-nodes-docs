# Documentation
- Class name: SamplerLCMAlternative
- Category: sampling/custom_sampling/samplers
- Output node: False
- Repo Ref: https://github.com/jojkaart/ComfyUI-sampler-lcm-alternative

The SamplerLCMAlternative node is designed to provide a self-defined sampling method for the generation of models. It uses advanced technology to enhance sampling processes to ensure that outputs are more nuanced and likely of higher quality. When traditional sampling methods may not be sufficient, this node is particularly useful and provides users with a customized sampling method.

# Input types
## Required
- euler_steps
    - The euler_steps parameter is essential for determining the steps of the Euratom method used in the numeric score, which can significantly affect the accuracy and stability of the sampling process. It allows users to fine-tune sampling methods to achieve the desired balance between performance and accuracy.
    - Comfy dtype: INT
    - Python dtype: int
- ancestral
    - The accelerator parameter controls the level of ancestral sampling, which affects the diversity of samples generated. It allows for a trade-off between exploration and use in the sampling process, allowing users to control the extent to which models explore new possibilities and adhere to known solutions.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise_mult
    - The noise_mult parameter adjusts the volume of noise added to the sampling process, which affects the variability and randomity of the samples. This parameter is essential for users who want to introduce controlled noise levels into the sample, which may enhance the creativity or diversity of the output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- sampler
    - The output sampler is a custom sample object, which encapsifies the specified parameters and sampling logic. As a tool for the user to generate a new sample from the model, it provides a custom-made method that is consistent with its particular needs and preferences.
    - Comfy dtype: SAMPLER
    - Python dtype: comfy.samplers.KSAMPLER

# Usage tips
- Infra type: CPU

# Source code
```
class SamplerLCMAlternative:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'euler_steps': ('INT', {'default': 0, 'min': -10000, 'max': 10000}), 'ancestral': ('FLOAT', {'default': 0, 'min': 0, 'max': 1.0, 'step': 0.01, 'round': False}), 'noise_mult': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 2.0, 'step': 0.001, 'round': False})}}
    RETURN_TYPES = ('SAMPLER',)
    CATEGORY = 'sampling/custom_sampling/samplers'
    FUNCTION = 'get_sampler'

    def get_sampler(self, euler_steps, ancestral, noise_mult):
        sampler = comfy.samplers.KSAMPLER(sample_lcm_alt, extra_options={'euler_steps': euler_steps, 'noise_mult': noise_mult, 'ancestral': ancestral})
        return (sampler,)
```