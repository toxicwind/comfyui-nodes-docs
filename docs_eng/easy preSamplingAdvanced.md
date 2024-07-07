# Documentation
- Class name: samplerSettingsAdvanced
- Category: EasyUse/PreSampling
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node is designed to provide a configuration process for sample parameters that generate models and provide a strong framework for fine-tuning the process according to specific needs. It emphasizes adaptive and user control over the sampling process, rather than exploring in depth the details of the bottom approach.

# Input types
## Required
- pipe
    - The `pipe' parameter is the primary source of information for nodes, containing all the context and data needed for the sampling process. It is essential because it determines the flow of data and the state of the model at each step.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict
- steps
    - The'steps' parameter defines the number of turns to be implemented during the sampling process. It is essential to determine the particle size of the sample and the extent to which model capacity is used.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The `cfg' parameter adjusts the configuration of the sampling process to allow fine-tuning of model behaviour. It plays an important role in shaping the output according to the required specifications.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The `sampler_name' parameter selects the specific sampling method to be used to influence the overall strategy and effectiveness of the sampling process.
    - Comfy dtype: COMBO
    - Python dtype: str
- scheduler
    - The `scheduler' parameter defines the dispatch strategy for the sampling process, which is essential for managing resources and ensuring efficient implementation.
    - Comfy dtype: COMBO
    - Python dtype: str
- start_at_step
    - The `start_at_step' parameter sets the starting point of the sampling process, which is important for controlling the timing and sequencing of the operation.
    - Comfy dtype: INT
    - Python dtype: int
- end_at_step
    - The `end_at_step' parameters define the end of the sampling process and ensure that implementation ends at the desired stage.
    - Comfy dtype: INT
    - Python dtype: int
- add_noise
    - The `add_noise' parameter controls the introduction of noise during the sampling process, affecting the diversity and quality of the output generated.
    - Comfy dtype: COMBO
    - Python dtype: str
- seed
    - The `seed' parameter ensures the replicability of the sampling process by providing a fixed point for random number generation.
    - Comfy dtype: INT
    - Python dtype: int
- return_with_leftover_noise
    - The `return_with_leftover_noise' parameter decides whether to include residual noise in the final output, which may affect the aesthetic and style aspects of the results.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- image_to_latent
    - The `image_to_latet' parameter allows the conversion of input images to potential space, which is essential for certain types of generation tasks.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- latent
    - The `latent' parameter, which directly provides input for potential variables, is critical to the tasks that need to be performed at the potential space level.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- prompt
    - The `prompt' parameter introduces text guidance for the generation of a model, leading the output to a particular theme or style.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - The `extra_pnginfo' parameter contains additional information related to PNG images that can be used for advanced image processing tasks.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: str
- my_unique_id
    - The `my_unique_id' parameter assigns the only identifier for the operation, which is essential for tracking and managing multiple simultaneous processes.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- pipe
    - The `pipe' output is an integrated structure that covers the updated state of the model generation and the results of the sampling process and provides the basis for follow-up operations.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict

# Usage tips
- Infra type: CPU

# Source code
```
class samplerSettingsAdvanced:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'pipe': ('PIPE_LINE',), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'start_at_step': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'end_at_step': ('INT', {'default': 10000, 'min': 0, 'max': 10000}), 'add_noise': (['enable', 'disable'],), 'seed': ('INT', {'default': 0, 'min': 0, 'max': MAX_SEED_NUM}), 'return_with_leftover_noise': (['disable', 'enable'],)}, 'optional': {'image_to_latent': ('IMAGE',), 'latent': ('LATENT',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE',)
    RETURN_NAMES = ('pipe',)
    OUTPUT_NODE = True
    FUNCTION = 'settings'
    CATEGORY = 'EasyUse/PreSampling'

    def settings(self, pipe, steps, cfg, sampler_name, scheduler, start_at_step, end_at_step, add_noise, seed, return_with_leftover_noise, image_to_latent=None, latent=None, prompt=None, extra_pnginfo=None, my_unique_id=None):
        vae = pipe['vae']
        batch_size = pipe['loader_settings']['batch_size'] if 'batch_size' in pipe['loader_settings'] else 1
        if image_to_latent is not None:
            samples = {'samples': vae.encode(image_to_latent[:, :, :, :3])}
            samples = RepeatLatentBatch().repeat(samples, batch_size)[0]
            images = image_to_latent
        elif latent is not None:
            samples = latent
            images = pipe['images']
        else:
            samples = pipe['samples']
            images = pipe['images']
        force_full_denoise = True
        if return_with_leftover_noise == 'enable':
            force_full_denoise = False
        new_pipe = {'model': pipe['model'], 'positive': pipe['positive'], 'negative': pipe['negative'], 'vae': pipe['vae'], 'clip': pipe['clip'], 'samples': samples, 'images': images, 'seed': seed, 'loader_settings': {**pipe['loader_settings'], 'steps': steps, 'cfg': cfg, 'sampler_name': sampler_name, 'scheduler': scheduler, 'start_step': start_at_step, 'last_step': end_at_step, 'denoise': 1.0, 'add_noise': add_noise, 'force_full_denoise': force_full_denoise}}
        del pipe
        return {'ui': {'value': [seed]}, 'result': (new_pipe,)}
```