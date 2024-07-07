# Documentation
- Class name: PixelKSampleUpscalerProviderPipe
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

Pixel KSampleUpscalerProviderPipe is a node used to improve the resolution of images, using a variety of sampling methods. It provides a powerful framework for selecting and applying different scaling techniques to ensure high-quality results. This node is essential for image sampling and provides seamless integration with other components of the system.

# Input types
## Required
- scale_method
    - The scaling method parameter is essential to determine the sampling technology to be used. It determines the algorithm for enhancing the resolution of images, which significantly affects the quality of the final output.
    - Comfy dtype: str
    - Python dtype: str
- seed
    - Seed parameters play an important role in the initialization of random number generators, ensuring repeatability of the sampling process. This is essential for consistency in the multiple run of nodes.
    - Comfy dtype: int
    - Python dtype: int
- steps
    - The step parameter defines the number of turns to be executed during the top-sampling process. It directly affects the level of detail and the complexity of the calculation.
    - Comfy dtype: int
    - Python dtype: int
- cfg
    - cfg parameters are used to control the configuration of sampling models and allow for fine-tuning of the scaling process to achieve the desired results.
    - Comfy dtype: float
    - Python dtype: float
- sampler_name
    - The sampler_name parameter specifies the sampling strategy to be used during the sampling. It is a key determinant of the efficiency and effectiveness of the sampling process.
    - Comfy dtype: str
    - Python dtype: str
- scheduler
    - The scheduler parameter is essential to manage the rhythm and sequence of sampling steps. It helps to optimize the sampling process to improve speed and quality.
    - Comfy dtype: str
    - Python dtype: str
- denoise
    - Noise parameters are used to control noise reduction during the sampling process. This is essential to achieve a cleaner and more refined image output.
    - Comfy dtype: float
    - Python dtype: float
- use_tiled_vae
    - This improves the efficiency of the sampling process, especially for larger images.
    - Comfy dtype: bool
    - Python dtype: bool
- basic_pipe
    - The basic_pipe parameter covers the basic components required for the sampling process. It is indispensable for the operation of nodes and provides the necessary infrastructure for image enhancement.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: BASIC_PIPE
## Optional
- tile_size
    - The tile_size parameter specifies the tile sizes to be used in the blocking process. It is particularly relevant when large images are processed to optimize memory use and processing time.
    - Comfy dtype: int
    - Python dtype: int

# Output types
- upscaler
    - Upscaler output provides the final upscaler model, which is the core result of node operations. It represents the top of the sampling process and provides a refined and enhanced image.
    - Comfy dtype: UPSCALER
    - Python dtype: PixelKSampleUpscaler

# Usage tips
- Infra type: GPU

# Source code
```
class PixelKSampleUpscalerProviderPipe(PixelKSampleUpscalerProvider):
    upscale_methods = ['nearest-exact', 'bilinear', 'lanczos', 'area']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'scale_method': (s.upscale_methods,), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'use_tiled_vae': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'basic_pipe': ('BASIC_PIPE',), 'tile_size': ('INT', {'default': 512, 'min': 320, 'max': 4096, 'step': 64})}, 'optional': {'upscale_model_opt': ('UPSCALE_MODEL',), 'pk_hook_opt': ('PK_HOOK',)}}
    RETURN_TYPES = ('UPSCALER',)
    FUNCTION = 'doit_pipe'
    CATEGORY = 'ImpactPack/Upscale'

    def doit_pipe(self, scale_method, seed, steps, cfg, sampler_name, scheduler, denoise, use_tiled_vae, basic_pipe, upscale_model_opt=None, pk_hook_opt=None, tile_size=512):
        (model, _, vae, positive, negative) = basic_pipe
        upscaler = core.PixelKSampleUpscaler(scale_method, model, vae, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, use_tiled_vae, upscale_model_opt, pk_hook_opt, tile_size=tile_size)
        return (upscaler,)
```