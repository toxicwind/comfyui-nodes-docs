# Documentation
- Class name: SeargeSDXLSampler
- Category: Searge/_deprecated_/Sampling
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergeSDXLSampler node is designed to facilitate the sampling process within the framework of in-depth learning, particularly for style migration tasks. It combines basic models and fine-tuning models to gradually improve the quality of output generation, starting with potential images, and applying noise mitigation techniques.

# Input types
## Required
- base_model
    - The base model is essential for the sampling process, and it forms the basis for the output. This is the initial neural network used to generate the output base.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- base_positive
    - The underlying reconciliation is essential to guide the style and content of the image generation towards the desired results, ensuring that the image is consistent with the target area.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- base_negative
    - The underlying negative regulation helps to avoid creating features or styles that are not required in the image and to make the output more in line with the expected results.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- refiner_model
    - The fine-tuning model plays a key role in improving the quality of basic output by applying additional layers and fine-tuning the final results.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- refiner_positive
    - The refinement is further fine-tuning the image towards the reconciliation to emphasize particular features or styles to ensure that the final output has greater detail and certainty.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- refiner_negative
    - The fine-tuning of negative adjustments is used to inhibit certain features or styles that may not meet the expected results and to ensure that the final image meets quality standards.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- latent_image
    - Potential images are the starting point of the sampling process and represent the initial state in which the final images are generated and developed.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- noise_seed
    - Noise seeds play an important role in introducing variability and randomity in the sampling process, ensuring diversity in the generation of outputs.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The steps define the number of turns to be experienced in the sampling process, directly affecting the details and level of detail of the final image.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The configuration parameters are essential for adjusting the balance of style and content in the generation of images to ensure a harmonious integration between the two.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler name determines the specific sampling strategy to be used, which significantly affects the efficiency and quality of the sampling process.
    - Comfy dtype: COMBO[comfy.samplers.KSampler.SAMPLERS]
    - Python dtype: str
- scheduler
    - The scheduler determines the rhythm and progress of the sampling process to ensure a smooth transition from the initial to the final state.
    - Comfy dtype: COMBO[comfy.samplers.KSampler.SCHEDULERS]
    - Python dtype: str
- base_ratio
    - The base scale parameters adjust the proportion of the total step devoted to the basic sampling phase, affecting the initial quality of the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- denoise
    - Noise parameters control the level of noise reduction applied during the sampling process, directly affecting the clarity and sharpness of the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- 
    - The output is a potential expression of the image, which contains the final state after the sampling process has been completed and represents a combination of inputs and parameters.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class SeargeSDXLSampler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'base_model': ('MODEL',), 'base_positive': ('CONDITIONING',), 'base_negative': ('CONDITIONING',), 'refiner_model': ('MODEL',), 'refiner_positive': ('CONDITIONING',), 'refiner_negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'noise_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 30, 'min': 1, 'max': 1000}), 'cfg': ('FLOAT', {'default': 7.0, 'min': 0.0, 'max': 100.0, 'step': 0.5}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS, {'default': 'dpmpp_2m'}), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS, {'default': 'karras'}), 'base_ratio': ('FLOAT', {'default': 0.8, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('LATENT',)
    RETURN_NAMES = ('',)
    FUNCTION = 'sample'
    CATEGORY = 'Searge/_deprecated_/Sampling'

    def sample(self, base_model, base_positive, base_negative, refiner_model, refiner_positive, refiner_negative, latent_image, noise_seed, steps, cfg, sampler_name, scheduler, base_ratio, denoise):
        base_steps = int(steps * base_ratio)
        if denoise < 0.01:
            return (latent_image,)
        if base_steps >= steps:
            return nodes.common_ksampler(base_model, noise_seed, steps, cfg, sampler_name, scheduler, base_positive, base_negative, latent_image, denoise=denoise, disable_noise=False, start_step=0, last_step=steps, force_full_denoise=True)
        base_result = nodes.common_ksampler(base_model, noise_seed, steps, cfg, sampler_name, scheduler, base_positive, base_negative, latent_image, denoise=denoise, disable_noise=False, start_step=0, last_step=base_steps, force_full_denoise=False)
        return nodes.common_ksampler(refiner_model, noise_seed, steps, cfg, sampler_name, scheduler, refiner_positive, refiner_negative, base_result[0], denoise=1.0, disable_noise=True, start_step=base_steps, last_step=steps, force_full_denoise=True)
```