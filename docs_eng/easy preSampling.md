# Documentation
- Class name: samplerSettings
- Category: EasyUse/PreSampling
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The samplerSettings class covers the configuration of the sampling flow line, providing a structured way to define the parameters that affect the sampling process. It is designed to simplify the configuration of complex sampling tasks and ensure that the necessary settings are correctly applied to achieve the desired results.

# Input types
## Required
- pipe
    - The pipe parameter is necessary because it contains the core data and settings required during the sampling process. It includes models, images, and other relevant information used by the samplerSettings to configure the sampling environment.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- steps
    - The Steps parameter specifies the number of turns to be implemented during the sampling process. It is essential to control the duration and particle size of the sampling, directly affecting the quality and diversity of the results.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter is a floating point value used to adjust the configuration of the sampling process. It plays an important role in fine-tuning the behaviour of the sampler to obtain the best results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter specifies the type of sampler to be used in the sampling process. It is critical in determining the method and strategy of the samplerSettings class for the generation of samples.
    - Comfy dtype: COMBO
    - Python dtype: str
- scheduler
    - The Scheduler parameter defines the dispatch strategy for the sampling process. It is important for managing the dynamics of the sampling to ensure that the process adapts and evolves over time to produce the best possible results.
    - Comfy dtype: COMBO
    - Python dtype: str
- denoise
    - The denoise parameter is used to control the level of noise reduction applied during the sampling process. It significantly affects the clarity and quality of the samples generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - Seed parameters are essential to ensure the repeatability of the sampling process. It initializes the random number generator and allows consistent results to be obtained in different operations.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- image_to_latent
    - The image_to_latet parameter provides a way to convert the image to a potential expression. It is an optional input that, when used, changes the focus of the sampling process in order to generate a sample based on image data.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- latent
    - The latent parameter allows direct operation of the potential space during the sampling process. It is an optional input which, when provided, can generate a sample from a particular potential state.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- prompt
    - The prompt parameter introduces text guidance into the sampling process, influencing the direction and style in which the sample is generated. It is an optional input that adds an additional layer of control to the output.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - The extra_pnginfo parameter contains additional information relevant to the PNG image that can be used to refine the sampling process. It is an optional input that provides more context for the generation of the sample.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: str
- my_unique_id
    - My_unique_id parameter is used to track and identify unique sampling sessions. It is an optional input that helps to maintain the integrity and traceability of the sampling process.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- pipe
    - Output Pipe is an integrated structure that contains up-to-date settings and data that are needed for the subsequent stages of the sampling process. It is a critical output because it paves the way for the generation of high-quality samples.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class samplerSettings:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'pipe': ('PIPE_LINE',), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': MAX_SEED_NUM})}, 'optional': {'image_to_latent': ('IMAGE',), 'latent': ('LATENT',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE',)
    RETURN_NAMES = ('pipe',)
    OUTPUT_NODE = True
    FUNCTION = 'settings'
    CATEGORY = 'EasyUse/PreSampling'

    def settings(self, pipe, steps, cfg, sampler_name, scheduler, denoise, seed, image_to_latent=None, latent=None, prompt=None, extra_pnginfo=None, my_unique_id=None):
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
        new_pipe = {'model': pipe['model'], 'positive': pipe['positive'], 'negative': pipe['negative'], 'vae': pipe['vae'], 'clip': pipe['clip'], 'samples': samples, 'images': images, 'seed': seed, 'loader_settings': {**pipe['loader_settings'], 'steps': steps, 'cfg': cfg, 'sampler_name': sampler_name, 'scheduler': scheduler, 'denoise': denoise, 'add_noise': 'enabled'}}
        del pipe
        return {'ui': {'value': [seed]}, 'result': (new_pipe,)}
```