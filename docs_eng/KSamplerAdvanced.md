# Documentation
- Class name: KSamplerAdvanced
- Category: sampling
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The KSamplerAdvanced node is designed to provide advanced sampling from the model through various noise configuration and scheduling options. By controlling the addition of noise, it generates high-quality potential indications, which enhances the diversity and quality of output. The node is flexible in its ability to adapt to different sampling strategies, making it a multifunctional tool for exploring potential spaces for model creation.

# Input types
## Required
- model
    - Model parameters are essential because they define the production models from which nodes are to be sampled. They are the basis for all sampling operations and their properties directly affect the nature of the potential expression generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- add_noise
    - Add_noise parameters control whether to introduce additional noise in the sampling process. This is essential in the potential sample to achieve the required diversity and complexity.
    - Comfy dtype: COMBO[enable, disable]
    - Python dtype: str
- steps
    - The step parameters specify the number of turns that the sampling process will experience. It is a key factor in determining the condensability and quality of the final potential samples.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter adjusts the configuration of the sampling process to affect the balance of exploration and use in potential space. It is the key setup for achieving optimal sampling efficiency and sample quality.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter specifies the sampling method to be used, which is essential to the overall performance and effect of the node. Different samplers can significantly change the properties that produce the sample.
    - Comfy dtype: COMBO[comfy.samplers.KSampler.SAMPLERS]
    - Python dtype: str
- scheduler
    - The scheduler parameters define the dispatch strategy for noise applications, which is essential for managing the trade-off between sample quality and computational efficiency.
    - Comfy dtype: COMBO[comfy.samplers.KSampler.SCHEDULERS]
    - Python dtype: str
- positive
    - The positionive parameter provides conditional data to guide the sampling process to produce samples that meet specific desired characteristics.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - Negative parameters provide conditional data to help the sampling process avoid the generation of samples with adverse characteristics.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- latent_image
    - The latent_image parameter is the initial point of the sampling process. It sets the starting conditions that affect the trajectories and results of the sampling.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Any]
## Optional
- noise_seed
    - The noise_seed parameter is essential to control randomity during noise generation. It ensures that noise patterns are reproducing, which is important for consistent and reliable sampling results.
    - Comfy dtype: INT
    - Python dtype: int
- start_at_step
    - Start_at_step parameters determine the initial steps of the sampling process and allow the user to control from which point the sampling begins.
    - Comfy dtype: INT
    - Python dtype: int
- end_at_step
    - End_at_step parameters specify the final steps of the sampling process and define the end point of the sample generation.
    - Comfy dtype: INT
    - Python dtype: int
- return_with_leftover_noise
    - Return_with_leftover_noise parameters to determine whether to include residual noise in returned samples may be useful for further analysis or reprocessing.
    - Comfy dtype: COMBO[disable, enable]
    - Python dtype: str

# Output types
- latent
    - The potential output consists of the potential samples generated, which are the core results of the sampling process. These samples represent the characteristics learned and can be used for various downstream tasks.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: GPU

# Source code
```
class KSamplerAdvanced:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'add_noise': (['enable', 'disable'],), 'noise_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.1, 'round': 0.01}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'start_at_step': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'end_at_step': ('INT', {'default': 10000, 'min': 0, 'max': 10000}), 'return_with_leftover_noise': (['disable', 'enable'],)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'sample'
    CATEGORY = 'sampling'

    def sample(self, model, add_noise, noise_seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, start_at_step, end_at_step, return_with_leftover_noise, denoise=1.0):
        force_full_denoise = True
        if return_with_leftover_noise == 'enable':
            force_full_denoise = False
        disable_noise = False
        if add_noise == 'disable':
            disable_noise = True
        return common_ksampler(model, noise_seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise, disable_noise=disable_noise, start_step=start_at_step, last_step=end_at_step, force_full_denoise=force_full_denoise)
```