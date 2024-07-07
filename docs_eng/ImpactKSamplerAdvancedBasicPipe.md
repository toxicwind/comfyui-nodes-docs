# Documentation
- Class name: KSamplerAdvancedBasicPipe
- Category: sampling
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

KSamplerAdvancedBavicPipe node aims to promote advanced sampling techniques within the framework. It uses KSamplerAdvanced's ability to perform complex sampling operations to ensure a high degree of control and customization of the sampling process. The node is critical in generating potential expressions of diversity and quality that can be further refined or used for downstream tasks.

# Input types
## Required
- basic_pipe
    - The basic_pipe parameter is essential for the operation of the node because it contains the core components required for the sampling, including models, clips and VAE. It is the basis for the construction of the sampling process and is essential for the correct function of the node.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[torch.nn.Module, Any, torch.nn.Module, Any, Any]
- latent_image
    - The latent_image parameter is a key input that provides an initial potential state for the sampling process. It significantly influences the starting point and trajectories in which the samples are generated.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
## Optional
- add_noise
    - The add_noise parameter determines whether noise is introduced in the sampling process. This affects the diversity and quality of the samples generated and is a key factor in achieving the desired results.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- noise_seed
    - The noise_seed parameter is used for the initial noise addition of a random number generator to ensure the repeatability of the sampling process. It plays a vital role in controlling the random elements of the node operation.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The Steps parameter specifies the number of overlaps to be performed during the sampling process. It directly influences the collection and detail of the samples and is a key factor in node execution.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter adjusts the configuration of the sampling process to allow the behaviour of the micro-reconciliation point. It is essential to achieve optimal performance and results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter selects the specific sampling method to be used from the predefined sampler collection. It is the key determinant for shaping the characteristics of the sample.
    - Comfy dtype: KSampler.SAMPLERS
    - Python dtype: str
- scheduler
    - The Scheduler parameter defines the modem algorithm to be used in the sampling process. It is essential to manage the pace and rhythm of sampling.
    - Comfy dtype: KSampler.SCHEDULERS
    - Python dtype: str
- start_at_step
    - Start_at_step parameters set the initial steps to start the sampling process. It allows customization of the sampling tracks, which is important to achieve a given result.
    - Comfy dtype: INT
    - Python dtype: int
- end_at_step
    - End_at_step parameters determine the final steps at the end of the sampling process. It plays an important role in determining the scope and duration of the sampling continuum.
    - Comfy dtype: INT
    - Python dtype: int
- return_with_leftover_noise
    - Return_with_leftover_noise parameters determine whether nodes should return a sample with any remaining noise after the last step. This is an important consideration for reprocessing or further analysis.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- basic_pipe
    - Basic_pe output provides original components for sampling that can be used for further processing or analysis.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[torch.nn.Module, Any, torch.nn.Module, Any, Any]
- latent
    - The output represents the potential state of sampling of the model and is a key result of the sampling process and can be used as a follow-up task or input to the model.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- vae
    - The vae output, including the variable coders used in the sampling process, may be of interest for further study or application.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class KSamplerAdvancedBasicPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'basic_pipe': ('BASIC_PIPE',), 'add_noise': ('BOOLEAN', {'default': True, 'label_on': 'enable', 'label_off': 'disable'}), 'noise_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'latent_image': ('LATENT',), 'start_at_step': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'end_at_step': ('INT', {'default': 10000, 'min': 0, 'max': 10000}), 'return_with_leftover_noise': ('BOOLEAN', {'default': False, 'label_on': 'enable', 'label_off': 'disable'})}}
    RETURN_TYPES = ('BASIC_PIPE', 'LATENT', 'VAE')
    FUNCTION = 'sample'
    CATEGORY = 'sampling'

    def sample(self, basic_pipe, add_noise, noise_seed, steps, cfg, sampler_name, scheduler, latent_image, start_at_step, end_at_step, return_with_leftover_noise, denoise=1.0):
        (model, clip, vae, positive, negative) = basic_pipe
        if add_noise:
            add_noise = 'enable'
        else:
            add_noise = 'disable'
        if return_with_leftover_noise:
            return_with_leftover_noise = 'enable'
        else:
            return_with_leftover_noise = 'disable'
        latent = nodes.KSamplerAdvanced().sample(model, add_noise, noise_seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, start_at_step, end_at_step, return_with_leftover_noise, denoise)[0]
        return (basic_pipe, latent, vae)
```