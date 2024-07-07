# Documentation
- Class name: dynamicCFGSettings
- Category: EasyUse/PreSampling
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The dynamicCFFGSettings node is designed to adjust the configuration settings for the given pipe dynamics to optimize the sampling process according to the specified parameters. It allows the use of fine-tuning sampling procedures such as Steps, cfg and Denoise, which jointly influence the generation of the output pipeline.

# Input types
## Required
- pipe
    - The pipe parameter represents the conduit to be configured and is essential for the operation of the node, as it determines the context in which the settings will be applied.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- steps
    - The Steps parameter defines the number of steps to be taken during the sampling process, which directly affects the particle size and duration of the sampling.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter is a floating point value used to adjust the configuration of the sampling process to affect the behaviour and output quality of the entire process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- cfg_mode
    - The cfg_mode parameter determines the configuration scaling pattern, which is essential for controlling the dynamic adjustment of sampling settings.
    - Comfy dtype: Enum
    - Python dtype: Enum
- cfg_scale_min
    - The cfg_scale_min parameter sets the minimum zoom value for the configuration to ensure that the dynamic adjustment does not fall below the specified threshold.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter selects the sampling method to be used, which is a key determinant in shaping the output of the sampling process.
    - Comfy dtype: Enum
    - Python dtype: Enum
- scheduler
    - Scheduler parameters determine the dispatch strategy of the sampling process and influence the way in which steps are managed over time.
    - Comfy dtype: Enum
    - Python dtype: Enum
- denoise
    - The denoise parameter controls the level of noise reduction applied during the sampling process, which improves the clarity and quality of the results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - Seed parameters are used to initialize the random number generator to ensure the repeatability of the sampling process.
    - Comfy dtype: INT
    - Python dtype: int
- image_to_latent
    - When providing the Image_to_latet parameter, it is used to convert the image to a potential expression for further processing in the sampling pipeline.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- latent
    - If a flatt parameter is specified, it means that potential spatial data will be used in the sampling process rather than derived from the image.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- prompt
    - Prompt parameters are optional text inputs that can be used to guide the sampling process to produce outputs that match certain text descriptions.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - If an extra_pnginfo parameter exists, it contains additional information relevant to the sampling process, which enhances understanding of the context of the input data.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: str
- my_unique_id
    - My_unique_id parameters are optional identifiers that can be used to track or mark specific examples of the sampling process.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- pipe
    - The output Pipe is a modified pipe that has been applied to the new settings and is prepared for subsequent sampling operations.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class dynamicCFGSettings:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'pipe': ('PIPE_LINE',), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'cfg_mode': (DynThresh.Modes,), 'cfg_scale_min': ('FLOAT', {'default': 3.5, 'min': 0.0, 'max': 100.0, 'step': 0.5}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': MAX_SEED_NUM})}, 'optional': {'image_to_latent': ('IMAGE',), 'latent': ('LATENT',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE',)
    RETURN_NAMES = ('pipe',)
    OUTPUT_NODE = True
    FUNCTION = 'settings'
    CATEGORY = 'EasyUse/PreSampling'

    def settings(self, pipe, steps, cfg, cfg_mode, cfg_scale_min, sampler_name, scheduler, denoise, seed, image_to_latent=None, latent=None, prompt=None, extra_pnginfo=None, my_unique_id=None):
        dynamic_thresh = DynThresh(7.0, 1.0, 'CONSTANT', 0, cfg_mode, cfg_scale_min, 0, 0, 999, False, 'MEAN', 'AD', 1)

        def sampler_dyn_thresh(args):
            input = args['input']
            cond = input - args['cond']
            uncond = input - args['uncond']
            cond_scale = args['cond_scale']
            time_step = args['timestep']
            dynamic_thresh.step = 999 - time_step[0]
            return input - dynamic_thresh.dynthresh(cond, uncond, cond_scale, None)
        model = pipe['model']
        m = model.clone()
        m.set_model_sampler_cfg_function(sampler_dyn_thresh)
        vae = pipe['vae']
        batch_size = pipe['loader_settings']['batch_size'] if 'batch_size' in pipe['loader_settings'] else 1
        if image_to_latent is not None:
            samples = {'samples': vae.encode(image_to_latent[:, :, :, :3])}
            samples = RepeatLatentBatch().repeat(samples, batch_size)[0]
            images = image_to_latent
        elif latent is not None:
            samples = RepeatLatentBatch().repeat(latent, batch_size)[0]
            images = pipe['images']
        else:
            samples = pipe['samples']
            images = pipe['images']
        new_pipe = {'model': m, 'positive': pipe['positive'], 'negative': pipe['negative'], 'vae': pipe['vae'], 'clip': pipe['clip'], 'samples': samples, 'images': images, 'seed': seed, 'loader_settings': {**pipe['loader_settings'], 'steps': steps, 'cfg': cfg, 'sampler_name': sampler_name, 'scheduler': scheduler, 'denoise': denoise}}
        del pipe
        return {'ui': {'value': [seed]}, 'result': (new_pipe,)}
```