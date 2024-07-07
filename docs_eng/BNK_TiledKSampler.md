# Documentation
- Class name: TiledKSampler
- Category: sampling
- Output node: False
- Repo Ref: https://github.com/BlenderNeko/ComfyUI_TiledKSampler.git

The TiledKSampler node is designed to facilitate the generation of high-resolution images by dividing tasks into smaller, easier-to-manage components (known as tiles). It allows complex control of the sampling process and enables the integration of conditions input to guide the generation process by applying user-defined tiles strategies and refining images over multiple steps.

# Input types
## Required
- model
    - Model parameters are essential because it defines the basic production model used to generate an image sample. It is the core component that determines the type and quality of output.
    - Comfy dtype: MODEL
    - Python dtype: comfy.sd.Model
- seed
    - Seeds are used to initialize random number generators to ensure that the image sampling process is replicable and consistent between different operations.
    - Comfy dtype: INT
    - Python dtype: int
- tile_width
    - The width of the tiles determines the horizontal dimensions of each tile, influencing the particle size of the sampling process and the level of detail of the final image.
    - Comfy dtype: INT
    - Python dtype: int
- tile_height
    - The height of tiles determines the vertical dimension of each tile, directly affecting the overall structure and structure of the images generated.
    - Comfy dtype: INT
    - Python dtype: int
- tiling_strategy
    - The tiles strategy parameters define how images are divided into tiles, which can significantly change the efficiency and quality of the sampling process.
    - Comfy dtype: COMBO
    - Python dtype: str
- steps
    - The number parameters of the steps determine the process of refinement over time, with higher values leading to more detailed and nuanced image generation.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - Configuration parameters are usually associated with model-specific settings and play a key role in the overall performance and output quality of image sampling.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - Sampler name parameters specify the type of sampler to be used, which can significantly influence the style and characteristics of the images generated.
    - Comfy dtype: COMBO
    - Python dtype: str
- scheduler
    - The scheduler parameters define the strategy to adjust the sampling process over time, affecting the condensation and stability of image generation.
    - Comfy dtype: COMBO
    - Python dtype: str
- positive
    - Positive condition input is essential for shaping the final output by leading the image to produce desired features or characteristics.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Dict[str, Any]]
- negative
    - Negative conditions are entered to exclude certain features or characteristics in image generation, allowing for more controlled and specific results.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Dict[str, Any]]
- latent_image
    - Potential image parameters include the initial potential expression of the image, which is detailed over the sampling process to generate the final image.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Any]
- denoise
    - Noise parameters control the level of noise reduction applied during the sampling process, affecting the clarity and quality of the image generated.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- latent_image
    - The output of a potential image contains a potential indication of fine-tuning after the sampling process, and the resulting image and its associated metadata are sealed.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: GPU

# Source code
```
class TiledKSampler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'tile_width': ('INT', {'default': 512, 'min': 256, 'max': MAX_RESOLUTION, 'step': 64}), 'tile_height': ('INT', {'default': 512, 'min': 256, 'max': MAX_RESOLUTION, 'step': 64}), 'tiling_strategy': (['random', 'random strict', 'padded', 'simple'],), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'sample'
    CATEGORY = 'sampling'

    def sample(self, model, seed, tile_width, tile_height, tiling_strategy, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise):
        steps_total = int(steps / denoise)
        return sample_common(model, 'enable', seed, tile_width, tile_height, tiling_strategy, steps_total, cfg, sampler_name, scheduler, positive, negative, latent_image, steps_total - steps, steps_total, 'disable', denoise=1.0, preview=True)
```