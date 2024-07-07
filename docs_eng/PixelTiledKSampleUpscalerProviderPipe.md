# Documentation
- Class name: PixelTiledKSampleUpscalerProviderPipe
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

PixelTiled KSampleUpscaler Provider Pipe is a node used to provide amplifiers based on smoothing sampling methods. Using the ComfyUI_TiledKSampler expansion, it noises images by dividing larger images into smaller flattens, improving image quality without introducing visible seams. This node is particularly suitable for tasks requiring the minimization of high-resolution image processing by artificial works.

# Input types
## Required
- scale_method
    - The scaling method determines how the image is magnified. This is a key parameter because it affects the quality and style of the magnifying image.
    - Comfy dtype: COMBO['nearest-exact', 'bilinear', 'lanczos', 'area']
    - Python dtype: str
- seed
    - Seeds are used in random number generation processes to ensure the replicability of the noise result.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The number of steps determines the thoroughness of the noise process, and usually more steps lead to better image quality.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The configuration value 'cfg' is the parameter that affects the noise removal process and balances the noise reduction with the preservation of details.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler name defines the sampling strategy used in the noise removal process, which can significantly affect the appearance of the final image.
    - Comfy dtype: comfy.samplers.KSampler.SAMPLERS
    - Python dtype: str
- scheduler
    - The scheduler determines the rate at which the parameters of the noise process are updated, affecting efficiency and results.
    - Comfy dtype: comfy.samplers.KSampler.SCHEDULERS
    - Python dtype: str
- denoise
    - Noise parameters control the intensity of the noise effect, and higher values lead to clearer images, but may lose details.
    - Comfy dtype: FLOAT
    - Python dtype: float
- tile_width
    - The level width specifies the width of each sheet during the levelling sampling process, which is important for managing memory usage and processing time.
    - Comfy dtype: INT
    - Python dtype: int
- tile_height
    - The flat height is specified for each flat height, working with the flat width to control the size of the flatbed grid.
    - Comfy dtype: INT
    - Python dtype: int
- tiling_strategy
    - Tiled-up strategies determine how images are divided into sheets, and different strategies optimize different outcomes, such as reduction of seams or compatibility with certain samplers.
    - Comfy dtype: COMBO['random', 'padded', 'simple']
    - Python dtype: str
- basic_pipe
    - Basic pipes provide the basic components needed for the operation of amplifiers, such as models and VAE.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Any
## Optional
- upscale_model_opt
    - An optional parameter allows the process to specify a custom magnification model.
    - Comfy dtype: UPSCALE_MODEL
    - Python dtype: Optional[Any]
- pk_hook_opt
    - An optional hook that can be used to modify the behaviour of the amplifier during the magnification process.
    - Comfy dtype: PK_HOOK
    - Python dtype: Optional[Any]

# Output types
- upscaler
    - The output of the node is an object of a magnifier capable of amplifying the image.
    - Comfy dtype: UPSCALER
    - Python dtype: core.PixelTiledKSampleUpscaler

# Usage tips
- Infra type: GPU

# Source code
```
class PixelTiledKSampleUpscalerProviderPipe:
    upscale_methods = ['nearest-exact', 'bilinear', 'lanczos', 'area']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'scale_method': (s.upscale_methods,), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'tile_width': ('INT', {'default': 512, 'min': 320, 'max': MAX_RESOLUTION, 'step': 64}), 'tile_height': ('INT', {'default': 512, 'min': 320, 'max': MAX_RESOLUTION, 'step': 64}), 'tiling_strategy': (['random', 'padded', 'simple'],), 'basic_pipe': ('BASIC_PIPE',)}, 'optional': {'upscale_model_opt': ('UPSCALE_MODEL',), 'pk_hook_opt': ('PK_HOOK',)}}
    RETURN_TYPES = ('UPSCALER',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Upscale'

    def doit(self, scale_method, seed, steps, cfg, sampler_name, scheduler, denoise, tile_width, tile_height, tiling_strategy, basic_pipe, upscale_model_opt=None, pk_hook_opt=None):
        if 'BNK_TiledKSampler' in nodes.NODE_CLASS_MAPPINGS:
            (model, _, vae, positive, negative) = basic_pipe
            upscaler = core.PixelTiledKSampleUpscaler(scale_method, model, vae, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, tile_width, tile_height, tiling_strategy, upscale_model_opt, pk_hook_opt, tile_size=max(tile_width, tile_height))
            return (upscaler,)
        else:
            print("[ERROR] PixelTiledKSampleUpscalerProviderPipe: ComfyUI_TiledKSampler custom node isn't installed. You must install BlenderNeko/ComfyUI_TiledKSampler extension to use this node.")
```