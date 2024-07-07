# Documentation
- Class name: TiledKSamplerProvider
- Category: ImpactPack/Sampler
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The TiledKSamplerProvider node is designed to facilitate the process of sampling image noise by using a lay-up strategy. It intelligently manages the division of images into plains, allowing for efficient and seamless noise removal. The node enhances the process by reducing the visibility of seams between sheets, thus contributing to more consistent and high-quality output images.

# Input types
## Required
- seed
    - Seed parameters are essential in the process of generating random numbers in the sampling algorithm, ensuring the replicability of the results. It affects the initial state of the random number generator and, in turn, the noise outcome.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - Steps parameters define the number of alternations that will occur during the denocture process. It is a key factor in determining the quality of the final denocture image, and more steps usually lead to better denocture outcomes.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter adjusts the configuration of the sampling process to allow fine-tuning of the performance of the de-noise algorithm. It plays an important role in balancing the speed and quality of the de-noise results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter specifies the type of sampler to be used in the noise removal process. It is essential to determine the sampling strategy and the effectiveness of the direct influence on noise removal.
    - Comfy dtype: STRING
    - Python dtype: str
- scheduler
    - Scheduler parameters determine the movement strategy for noise steps, which is important for controlling the pace of noise progress.
    - Comfy dtype: STRING
    - Python dtype: str
- denoise
    - Denoise parameter controls are applied to the noise intensity of each flat. It is a key factor in the final appearance of the denoise image, and higher values lead to more radical noise.
    - Comfy dtype: FLOAT
    - Python dtype: float
- tile_width
    - The tile_width parameter sets the width of each sheet in the flattening policy. It is important for determining the particle size of the denomination process and may affect the visibility of the seams in the final image.
    - Comfy dtype: INT
    - Python dtype: int
- tile_height
    - The tile_height parameter sets the height of each sheet in the flattening policy. It works with the tile_width, defines the flat overall structure and influences the noise result.
    - Comfy dtype: INT
    - Python dtype: int
- tiling_strategy
    - Tiling_strategy parameters determine how the image is divided into sheets. It is a key factor in reducing the suture effect and the overall quality of the decoupling image.
    - Comfy dtype: STRING
    - Python dtype: str
- basic_pipe
    - The basic_pipe parameter covers the basic components required for the noise removal process, including models and additional settings. It is essential for the application of the noise algorithm.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: comfy_extras.nodes_upscale_model.BasicPipe

# Output types
- KSAMPLER
    - The output of the TiledKSamplerProvider node is a KSampler object, which represents a configured noise sampler. It is important for following up on image processing tasks that require noise capabilities.
    - Comfy dtype: KSAMPLER
    - Python dtype: KSamplerWrapper

# Usage tips
- Infra type: GPU

# Source code
```
class TiledKSamplerProvider:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'tile_width': ('INT', {'default': 512, 'min': 320, 'max': MAX_RESOLUTION, 'step': 64}), 'tile_height': ('INT', {'default': 512, 'min': 320, 'max': MAX_RESOLUTION, 'step': 64}), 'tiling_strategy': (['random', 'padded', 'simple'],), 'basic_pipe': ('BASIC_PIPE',)}}
    RETURN_TYPES = ('KSAMPLER',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Sampler'

    def doit(self, seed, steps, cfg, sampler_name, scheduler, denoise, tile_width, tile_height, tiling_strategy, basic_pipe):
        (model, _, _, positive, negative) = basic_pipe
        sampler = core.TiledKSamplerWrapper(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, tile_width, tile_height, tiling_strategy)
        return (sampler,)
```