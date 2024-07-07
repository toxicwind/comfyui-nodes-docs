# Documentation
- Class name: KSamplerProvider
- Category: ImpactPack/Sampler
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

KSamplerProvider is designed to facilitate the creation and configuration of KSampler, a sampling method used in the generation model. It covers the process of initializing samplers using a variety of parameters (e.g. seeds, steps and configurations), thus allowing high-quality samples to be generated from the model.

# Input types
## Required
- seed
    - Seed parameters are essential for the repeatability of the sampling process. It ensures that the same seeds always produce the same samples and is a key element in controlling the randomity of the sampling.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - Step parameters define the number of turns that the sampling process will experience. More steps can produce more high-quality samples, but they may also increase the calculation time.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter, which represents the configuration, is used to adjust the configuration of the sampling process. It influences the quality and properties of the samples generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter specifies the type of sampler to be used in the sampling process. Different samplers can produce different results, so this parameter is essential for achieving the desired result.
    - Comfy dtype: STRING
    - Python dtype: str
- scheduler
    - The scheduler parameters determine the modem algorithm to be applied during the sampling process. It plays an important role in the efficiency and effectiveness of the sampling.
    - Comfy dtype: STRING
    - Python dtype: str
- denoise
    - The denoise parameter controls the level of noise reduction applied during the sampling process. It is an important factor in achieving a balance between the quality of the sample and the noise.
    - Comfy dtype: FLOAT
    - Python dtype: float
- basic_pipe
    - The basic_pipe parameter is a complex structure that contains the additional data required for the model and sampling process. It is essential for the function of KSamplerProvider node.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[torch.nn.Module, Any, Any, Any, Any]

# Output types
- KSAMPLER
    - The output of KSamplerProvider is a KSampler object used to model samples. It represents a configured sampler prepared for the sampling process.
    - Comfy dtype: KSAMPLER
    - Python dtype: KSamplerWrapper

# Usage tips
- Infra type: GPU

# Source code
```
class KSamplerProvider:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'basic_pipe': ('BASIC_PIPE',)}}
    RETURN_TYPES = ('KSAMPLER',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Sampler'

    def doit(self, seed, steps, cfg, sampler_name, scheduler, denoise, basic_pipe):
        (model, _, _, positive, negative) = basic_pipe
        sampler = KSamplerWrapper(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise)
        return (sampler,)
```