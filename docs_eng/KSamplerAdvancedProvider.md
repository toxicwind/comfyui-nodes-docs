# Documentation
- Class name: KSamplerAdvancedProvider
- Category: ImpactPack/Sampler
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

KSamplerAdvancedProvider is designed to generate advanced sampling techniques for the generation of models. It provides a complex sampling process using KSamplerAdvancedWrapper, which can be fine-tuned by various parameters, such as configuration settings, sampler names and schedulers. This node is essential for achieving high-quality results in image synthesis missions, as it allows fine control of sampling processes.

# Input types
## Required
- cfg
    - The `cfg' parameter is essential to configure the sampling process. It influences the overall behaviour of the sampler by determining key aspects such as the size of the sampling step. It is essential to achieve the desired results in image synthesis.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The `sampler_name' parameter specifies the type of sampler to be used in the sampling process. It is the key determinant for creating the characteristics of the sample and therefore plays an important role in the implementation of the node.
    - Comfy dtype: SAMPLER
    - Python dtype: str
- scheduler
    - The'scheduler' parameter defines the dispatch strategy for sampling steps. It is essential for controlling the progress of sampling, thus affecting the final output of the sampling process.
    - Comfy dtype: SCHEDULER
    - Python dtype: str
- basic_pipe
    - The `basic_pipe' parameter covers the basic components of the sampling process, including models, configurations and conditions. It is essential for the operation of nodes, as it provides the necessary context for advanced sampling techniques.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: tuple
## Optional
- sigma_factor
    - The `sigma_factor' parameter adjusts the level of noise during the sampling process to allow control of noise introduced at each step. This fine-tuning capability is important to achieve a balance between detail and noise in the image generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_opt
    - The optional `sampler_opt' parameter provides additional options to further define the sampling process. It allows for advanced control and can significantly influence the results of the sampling and provide users with a greater degree of flexibility.
    - Comfy dtype: SAMPLER
    - Python dtype: dict

# Output types
- KSAMPLER_ADVANCED
    - The output of KSamplerAdvancedProvider is an advanced sampler object that covers complex sampling processes. It is important because it represents the top of the node function and provides a powerful tool for users to generate high-quality images through fine sampling techniques.
    - Comfy dtype: KSAMPLER_ADVANCED
    - Python dtype: KSamplerAdvancedWrapper

# Usage tips
- Infra type: GPU

# Source code
```
class KSamplerAdvancedProvider:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'sigma_factor': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'basic_pipe': ('BASIC_PIPE',)}, 'optional': {'sampler_opt': ('SAMPLER',)}}
    RETURN_TYPES = ('KSAMPLER_ADVANCED',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Sampler'

    def doit(self, cfg, sampler_name, scheduler, basic_pipe, sigma_factor=1.0, sampler_opt=None):
        (model, _, _, positive, negative) = basic_pipe
        sampler = KSamplerAdvancedWrapper(model, cfg, sampler_name, scheduler, positive, negative, sampler_opt=sampler_opt, sigma_factor=sigma_factor)
        return (sampler,)
```