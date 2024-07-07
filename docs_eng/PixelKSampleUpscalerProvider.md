# Documentation
- Class name: PixelKSampleUpscalerProvider
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

Pixel KSampleUpscalerProvider is a node for image magnification, which supports a variety of magnification methods. The node covers the logic needed to select magnification techniques and apply them to images, providing a seamless interface to enhance image quality.

# Input types
## Required
- scale_method
    - The scaling method determines the algorithm to be used for image magnification. This is a key parameter because it directly affects the quality and style of the magnification output.
    - Comfy dtype: str
    - Python dtype: str
- model
    - Model parameters are essential because it defines the machine learning model used to magnify the process. Model selection can significantly influence the end result.
    - Comfy dtype: MODEL
    - Python dtype: Any
- vae
    - The configuration enhances the detail and quality of the magnified image.
    - Comfy dtype: VAE
    - Python dtype: Any
- seed
    - Seeds ensure the replicability of the magnification process by providing known starting points for random number generation, which is essential for consistent results.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The number of steps determines the iterative process during the magnification period, which may affect the quality of the collection and final output.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The configuration value 'cfg'is a parameter that adjusts to magnify the detail and pseudo-mage balance in the image and plays an important role in the final appearance.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler name selects the sampling strategy used in the magnification process, which can significantly affect the efficiency and results of the operation.
    - Comfy dtype: str
    - Python dtype: str
- scheduler
    - The scheduler determines the rate at which parameters are updated during the magnification process and affects the stability and performance of the magnification output.
    - Comfy dtype: str
    - Python dtype: str
- positive
    - Guidance is being provided to the reconciliation during the magnification period for models, focusing on enhancing specific features or aspects of the image.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - Negative reconciliation helps to suppress certain hypotheses or features by guiding models and avoid undesirable effects during magnification.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- denoise
    - Noise control is used to magnify the image's noise reduction level, which increases the clarity and cleanness of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- use_tiled_vae
    - The use of flat-bed VAE allows for treatment by disaggregating larger images into smaller, easier-to-manage flats, which is beneficial for RAM.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- tile_size
    - When a flat-bed VAE is used, the flat size is assigned to the flat size used to level the image, affecting the particle size of the magnification process.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- upscaler
    - The amplifier is the main output of the node, which is an image of magnification or a model that can be used to magnify the image. It encapsulates the results of the magnification process.
    - Comfy dtype: UPSCALER
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class PixelKSampleUpscalerProvider:
    upscale_methods = ['nearest-exact', 'bilinear', 'lanczos', 'area']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'scale_method': (s.upscale_methods,), 'model': ('MODEL',), 'vae': ('VAE',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'use_tiled_vae': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'tile_size': ('INT', {'default': 512, 'min': 320, 'max': 4096, 'step': 64})}, 'optional': {'upscale_model_opt': ('UPSCALE_MODEL',), 'pk_hook_opt': ('PK_HOOK',)}}
    RETURN_TYPES = ('UPSCALER',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Upscale'

    def doit(self, scale_method, model, vae, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, use_tiled_vae, upscale_model_opt=None, pk_hook_opt=None, tile_size=512):
        upscaler = core.PixelKSampleUpscaler(scale_method, model, vae, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, use_tiled_vae, upscale_model_opt, pk_hook_opt, tile_size=tile_size)
        return (upscaler,)
```