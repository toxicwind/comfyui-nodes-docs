# Documentation
- Class name: PixelTiledKSampleUpscalerProvider
- Category: ImpactPack/Upscale
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

PixelTiledKSampleUpscalerProvider is a node that aims to improve image quality through a complex magnification process. It uses a variety of scaling methods and is integrated with advanced models to noise the image profile and optimizes the clarity and detail of the final output.

# Input types
## Required
- scale_method
    - The scaling method defines the algorithm used to magnify the image. It is essential to determine the quality and style of the magnification process, affecting the image's final appearance.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- model
    - Model parameters are essential because it assigns a machine learning model that will be used to magnify the task. The selection of models has a significant impact on the performance of nodes and the quality of the images generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- vae
    - VAE is a key component in the magnification process because it encodes and decodes image data. It plays a key role in the quality of noise output.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- seed
    - Seeds ensure the replicability of the magnification process by providing a consistent starting point for random number generation, which is essential for maintaining the integrity of results in different operations.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The number of steps determines the scope of the magnification process. More steps allow for more refined results, but also add to the complexity of calculations.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - Configure parameters, usually referred to as 'cfg', to control the balance between detail and noise during the magnification process and to influence the overall clarity of the magnification image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The name of the sampler determines the sampling strategy to be used in the noise process. It is a key factor in shaping the final image noise properties.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- scheduler
    - The scheduler defines the speed at which parameters are updated during the magnification process, which may affect the efficiency and ultimate quality of the magnifying image.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- positive
    - Guidance is being provided to the model on what features are enhanced or retained during the magnification period, which is essential to achieving the desired results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - Negative condition guidance models avoid certain features or prostheses during magnification and ensure that the final image meets the specified quality standards.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- denoise
    - Noise control applies to the noise intensity of each flat. It is a key factor in balancing image details with removing unwanted noise.
    - Comfy dtype: FLOAT
    - Python dtype: float
- tile_width
    - The tile width specifies the horizontal dimensions of each tile to be used in the magnification process. It affects the levelling strategy and may affect the resolution of the final image.
    - Comfy dtype: INT
    - Python dtype: int
- tile_height
    - The flat height specifies the vertical dimensions of each sheet used in the magnification process. It works with the flatten width to determine the flatten mode.
    - Comfy dtype: INT
    - Python dtype: int
- tiling_strategy
    - The flattened strategy determines how the image is divided into flattened and processed. It is essential to manage the seams and ensure a consistent magnification of the image as a whole.
    - Comfy dtype: COMBO[str]
    - Python dtype: str

# Output types
- upscaler
    - The amplifier output provides a treatment image after the magnification process. It represents the top of the node function and provides enhanced images with improved resolution and reduced noise.
    - Comfy dtype: UPSCALER
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class PixelTiledKSampleUpscalerProvider:
    upscale_methods = ['nearest-exact', 'bilinear', 'lanczos', 'area']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'scale_method': (s.upscale_methods,), 'model': ('MODEL',), 'vae': ('VAE',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'tile_width': ('INT', {'default': 512, 'min': 320, 'max': MAX_RESOLUTION, 'step': 64}), 'tile_height': ('INT', {'default': 512, 'min': 320, 'max': MAX_RESOLUTION, 'step': 64}), 'tiling_strategy': (['random', 'padded', 'simple'],)}, 'optional': {'upscale_model_opt': ('UPSCALE_MODEL',), 'pk_hook_opt': ('PK_HOOK',)}}
    RETURN_TYPES = ('UPSCALER',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Upscale'

    def doit(self, scale_method, model, vae, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, tile_width, tile_height, tiling_strategy, upscale_model_opt=None, pk_hook_opt=None):
        if 'BNK_TiledKSampler' in nodes.NODE_CLASS_MAPPINGS:
            upscaler = core.PixelTiledKSampleUpscaler(scale_method, model, vae, seed, steps, cfg, sampler_name, scheduler, positive, negative, denoise, tile_width, tile_height, tiling_strategy, upscale_model_opt, pk_hook_opt, tile_size=max(tile_width, tile_height))
            return (upscaler,)
        else:
            print("[ERROR] PixelTiledKSampleUpscalerProvider: ComfyUI_TiledKSampler custom node isn't installed. You must install BlenderNeko/ComfyUI_TiledKSampler extension to use this node.")
```