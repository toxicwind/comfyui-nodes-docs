# Documentation
- Class name: KSamplerAdvanced_inspire
- Category: InspirePack/a1111_compat
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The KSamplerAdvanced_inspire class is designed to promote advanced sampling operations within the model and to integrate noise and scheduling mechanisms to enhance the generation process. It is designed to provide users with a flexible and efficient tool to explore the potential space of the model, thereby creating diversified and high-quality outputs.

# Input types
## Required
- model
    - Model parameters are essential because they define the underlying production models that the nodes will operate. They are the basis for all sampling activities and directly affect the quality and type of output generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- add_noise
    - The add_noise parameter controls whether random elements are included in the sampling process, which can lead to a more diverse and creative outcome. It is an important aspect of exploring modelling capabilities and diversifying outputs.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- noise_seed
    - Noise_seed parameters play an important role in determining the randomity and diversity of noise patterns applied in the sampling process. It ensures that noise is recognizable and consistent, which is essential for experimental control and comparison.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The Steps parameter determines the progress of the sampling process, affecting the particle size and depth of the exploration in the potential space of the model. It is a key factor in achieving a comprehensive and detailed set of results.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter is a configuration value that adjusts the behaviour of the sampling process and allows fine-tuning of the output characteristics. It is an important tool for adjusting node functions to specific requirements and expectations.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter specifies the sampling strategy to be used, which is essential to the ability of the node to effectively navigate the potential space. It shapes the overall approach and direction of the sampling process.
    - Comfy dtype: ENUM
    - Python dtype: str
- scheduler
    - Scheduler parameters define the method of dispatching the sampling process, which is essential to manage the dynamic aspects of node operations. It ensures that nodes are able to adapt to and respond to changing conditions within the potential space of the model.
    - Comfy dtype: ENUM
    - Python dtype: str
- positive
    - The positionive parameter, as a guide to the sampling process, provides a positive example or condition to be followed at the node. It is essential to guide the output towards the desired characteristics and to ensure that the results are consistent with the desired direction.
    - Comfy dtype: CONDITIONING
    - Python dtype: dict
- negative
    - The negative parameter establishes binding or undesired conditions for the sampling process, which are essential to steer nodes away from undesirable outcomes. It plays an important role in shaping the end result and maintaining the quality of the output.
    - Comfy dtype: CONDITIONING
    - Python dtype: dict
- latent_image
    - The lower_image parameter is the main input for node sampling operations, representing the initial state or condition in the potential space of the model. It is the basis for node output and directly affects the nature of the result.
    - Comfy dtype: LATENT
    - Python dtype: dict
- start_at_step
    - The start_at_step parameter defines the starting point of the sampling process and indicates the stage from which the node should start its operation. It is an important factor in controlling the timing and sequencing of the sampling activity.
    - Comfy dtype: INT
    - Python dtype: int
- end_at_step
    - End_at_step parameters set the end of the sampling process and determine the maximum number of steps that nodes should continue to operate. It is essential to define the scope and duration of the sampling activity.
    - Comfy dtype: INT
    - Python dtype: int
- noise_mode
    - The noise_mode parameter determines the computational resources used to generate noise, including options for GPU and CPU. This is a key decision that affects the performance and efficiency of the sampling process.
    - Comfy dtype: ENUM
    - Python dtype: str
- return_with_leftover_noise
    - Return_with_leftover_noise parameters determine whether nodes should return additional noise information outside the main output. This may be useful for further analysis or subsequent processing steps.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- batch_seed_mode
    - Match_seed_mode parameters manage seed distribution in batch processing, which is important for consistency and control noise generation in parallel processing scenarios. It ensures that each batch has the only noise seed, promotes diversity and prevents duplication in output.
    - Comfy dtype: ENUM
    - Python dtype: str
- variation_seed
    - Variation_seed parameters introduce variability in noise generation and allow for the exploration of a wider range of outcomes. It is essential to create unique and diverse outcomes in the sampling process.
    - Comfy dtype: INT
    - Python dtype: int
- variation_strength
    - The variation_strength parameter adjusts the intensity of changes introduced by noise, which can influence the extent of changes in the final output. It is a key factor in controlling the diversity of outcomes and creativity.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- noise_opt
    - Noise_opt parameters provide an option for customizing noises applied during sampling and provide users with the ability to try different noise configurations and their impact on output.
    - Comfy dtype: NOISE
    - Python dtype: torch.Tensor

# Output types
- latent
    - The latent parameter contains a sample of the results of the sampling process and represents the end result of the node operation. It is important because it contains important information for further analysis or generation of the final image.
    - Comfy dtype: LATENT
    - Python dtype: dict

# Usage tips
- Infra type: GPU

# Source code
```
class KSamplerAdvanced_inspire:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'add_noise': ('BOOLEAN', {'default': True, 'label_on': 'enable', 'label_off': 'disable'}), 'noise_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.5, 'round': 0.01}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'start_at_step': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'end_at_step': ('INT', {'default': 10000, 'min': 0, 'max': 10000}), 'noise_mode': (['GPU(=A1111)', 'CPU'],), 'return_with_leftover_noise': ('BOOLEAN', {'default': False, 'label_on': 'enable', 'label_off': 'disable'}), 'batch_seed_mode': (['incremental', 'comfy', 'variation str inc:0.01', 'variation str inc:0.05'],), 'variation_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'variation_strength': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}, 'optional': {'noise_opt': ('NOISE',)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'sample'
    CATEGORY = 'InspirePack/a1111_compat'

    def sample(self, model, add_noise, noise_seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, start_at_step, end_at_step, noise_mode, return_with_leftover_noise, denoise=1.0, batch_seed_mode='comfy', variation_seed=None, variation_strength=None, noise_opt=None):
        force_full_denoise = True
        if return_with_leftover_noise:
            force_full_denoise = False
        disable_noise = False
        if not add_noise:
            disable_noise = True
        return common_ksampler(model, noise_seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise, disable_noise=disable_noise, start_step=start_at_step, last_step=end_at_step, force_full_denoise=force_full_denoise, noise_mode=noise_mode, incremental_seed_mode=batch_seed_mode, variation_seed=variation_seed, variation_strength=variation_strength, noise=noise_opt)
```