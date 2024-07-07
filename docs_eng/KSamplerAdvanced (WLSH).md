# Documentation
- Class name: WLSH_KSamplerAdvanced
- Category: WLSH Nodes/sampling
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The WLSH_KSamplerAdvanced node is designed to perform advanced sampling using a specified model. It allows customizing the sampling process by parameters such as adding noise, random seeds and sampling steps. The node can produce high-quality samples by fine-tuning noise processes and using various sampling strategies and dispatchers.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes, as they define the production model used to produce the sample. The selection of the model significantly influences the quality and characteristics of the sample.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- sampler_name
    - The sampler_name parameter selects the specific sampling method to be used. Different sampling methods may lead to different sample quality and properties, making this parameter essential for achieving the desired result.
    - Comfy dtype: comfy.samplers.KSampler.SAMPLERS
    - Python dtype: str
- scheduler
    - The Scheduler parameter defines the dispatch strategy to be applied during the sampling process. It is important to control the speed of implementation of the sampling process.
    - Comfy dtype: comfy.samplers.KSampler.SCHEDULERS
    - Python dtype: str
- positive
    - The positionive parameters provide information on the conditions of the sampling process to generate samples with desired properties.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- negative
    - The nigative parameter provides additional conditional information and helps to avoid the generation of samples with undesirable properties.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- latent_image
    - The latent_image parameter is the key input to the sampling process and represents the initial potential state in which the sampling begins.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
## Optional
- add_noise
    - Add_noise parameters determine whether to add noise to the sampling process. This affects the diversity of the samples generated and is an important factor in controlling the balance between the quality of the samples and the noise.
    - Comfy dtype: COMBO['enable', 'disable']
    - Python dtype: str
- seed
    - The Seed parameter is used to introduce randomity in the sampling process. It ensures that the sampling results are recreated, which is essential for debugging and comparing different sampling configurations.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - Steps parameters specify the number of turns during the sampling process. The more steps you take, the higher the number of steps, usually leads to a higher quality sample, but increases the costing.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - cfg parameters, which represent the control factors of the sampling process, allow fine-tuning of the balance between exploration and utilization in sampling strategies.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_at_step
    - Start_at_step parameters determine the steps to begin the sampling process. It allows fine particle size control of the sampling process.
    - Comfy dtype: INT
    - Python dtype: int
- end_at_step
    - End_at_step parameters specify the final steps of the sampling process. It defines the range of steps to execute the sampling.
    - Comfy dtype: INT
    - Python dtype: int
- return_with_leftover_noise
    - Return_with_leftover_noise parameters control whether the sample image contains the remaining noise during the sampling process. This is useful for further processing or analysis.
    - Comfy dtype: COMBO['disable', 'enable']
    - Python dtype: str
- denoise
    - The denoise parameter adjusts the noise intensity applied during the sampling process. It is a key factor in determining the clarity and quality of the final sample.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- latent
    - The latent output represents the ultimate potential state of the sampling process and can be used for further analysis or as input for subsequent processing steps.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- info
    - The info output provides a summary of the sampling process, including details of the seeds used, the number of steps and the noise intensity of the application.
    - Comfy dtype: INFO
    - Python dtype: Dict[str, Union[int, float, str]]

# Usage tips
- Infra type: GPU

# Source code
```
class WLSH_KSamplerAdvanced:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'add_noise': (['enable', 'disable'],), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'start_at_step': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'end_at_step': ('INT', {'default': 10000, 'min': 0, 'max': 10000}), 'return_with_leftover_noise': (['disable', 'enable'],), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('LATENT', 'INFO')
    FUNCTION = 'sample'
    CATEGORY = 'WLSH Nodes/sampling'

    def sample(self, model, add_noise, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, start_at_step, end_at_step, return_with_leftover_noise, denoise):
        force_full_denoise = False
        if return_with_leftover_noise == 'enable':
            force_full_denoise = False
        disable_noise = False
        if add_noise == 'disable':
            disable_noise = True
        info = {'Seed: ': seed, 'Steps: ': steps, 'CFG scale: ': cfg, 'Sampler: ': sampler_name, 'Scheduler: ': scheduler, 'Start at step: ': start_at_step, 'End at step: ': end_at_step, 'Denoising strength: ': denoise}
        samples = common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise, disable_noise=disable_noise, start_step=start_at_step, last_step=end_at_step, force_full_denoise=force_full_denoise)
        return (samples[0], info)
```