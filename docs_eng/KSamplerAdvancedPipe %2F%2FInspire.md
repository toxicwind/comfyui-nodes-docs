# Documentation
- Class name: KSamplerAdvanced_inspire_pipe
- Category: InspirePack/a1111_compat
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node facilitates advanced sampling processes in the InspirePack stream and integrates noise management and scheduling mechanisms to improve the process of generating potential expressions.

# Input types
## Required
- basic_pipe
    - The basic_pipe parameter is necessary because it provides the basic components required for the sampling process, including models, clips and other necessary elements.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[torch.nn.Module, ...]
- add_noise
    - This parameter controls whether noise is introduced in the sampling process, affecting the diversity and quality of the potential images generated.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- noise_seed
    - Noise_seed parameters are essential for the replicability of noise patterns to ensure that the same noise can be regenerated for consistent results.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - Steps parameters define the progress of the sampling process, with higher values leading to more fine and detailed potential images.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - cfg parameters adjust the configuration of the sampler to affect the overall behaviour and output of the sampling process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter selects the specific sampling algorithm to be used, directly affecting the efficiency and effectiveness of the sampling process.
    - Comfy dtype: ENUM
    - Python dtype: str
- scheduler
    - The Scheduler parameter sets out the dispatch strategy for the sampling process and optimizes the trade-off between speed and quality.
    - Comfy dtype: ENUM
    - Python dtype: str
- latent_image
    - The latent_image parameter is the input of the sampling process as the basis for generating new potential indications.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- start_at_step
    - Start_at_step parameters indicate the initial steps of the sampling process and determine the starting point for potential image generation.
    - Comfy dtype: INT
    - Python dtype: int
- end_at_step
    - End_at_step parameters define the final steps of the sampling process and set boundaries for potential image generation.
    - Comfy dtype: INT
    - Python dtype: int
- noise_mode
    - The noise_mode parameter determines the computational resources used for noise generation, either using the parallel capabilities of the GPU or using the order of the CPU.
    - Comfy dtype: ENUM
    - Python dtype: str

# Output types
- latent
    - The latent parameter represents the output of the sampling process and provides a refined and detailed potential for further use in the flow line.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- vae
    - The vae parameter includes the output change from the encoder component, captures the distribution of the learning data and provides the basis for further analysis and generation.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class KSamplerAdvanced_inspire_pipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'basic_pipe': ('BASIC_PIPE',), 'add_noise': ('BOOLEAN', {'default': True, 'label_on': 'enable', 'label_off': 'disable'}), 'noise_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.5, 'round': 0.01}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'latent_image': ('LATENT',), 'start_at_step': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'end_at_step': ('INT', {'default': 10000, 'min': 0, 'max': 10000}), 'noise_mode': (['GPU(=A1111)', 'CPU'],), 'return_with_leftover_noise': ('BOOLEAN', {'default': False, 'label_on': 'enable', 'label_off': 'disable'}), 'batch_seed_mode': (['incremental', 'comfy', 'variation str inc:0.01', 'variation str inc:0.05'],), 'variation_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'variation_strength': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}, 'optional': {'noise_opt': ('NOISE',)}}
    RETURN_TYPES = ('LATENT', 'VAE')
    FUNCTION = 'sample'
    CATEGORY = 'InspirePack/a1111_compat'

    def sample(self, basic_pipe, add_noise, noise_seed, steps, cfg, sampler_name, scheduler, latent_image, start_at_step, end_at_step, noise_mode, return_with_leftover_noise, denoise=1.0, batch_seed_mode='comfy', variation_seed=None, variation_strength=None, noise_opt=None):
        (model, clip, vae, positive, negative) = basic_pipe
        latent = KSamplerAdvanced_inspire().sample(model=model, add_noise=add_noise, noise_seed=noise_seed, steps=steps, cfg=cfg, sampler_name=sampler_name, scheduler=scheduler, positive=positive, negative=negative, latent_image=latent_image, start_at_step=start_at_step, end_at_step=end_at_step, noise_mode=noise_mode, return_with_leftover_noise=return_with_leftover_noise, denoise=denoise, batch_seed_mode=batch_seed_mode, variation_seed=variation_seed, variation_strength=variation_strength, noise_opt=noise_opt)[0]
        return (latent, vae)
```