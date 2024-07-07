# Documentation
- Class name: TiledKSamplerAdvanced
- Category: sampling
- Output node: False
- Repo Ref: https://github.com/BlenderNeko/ComfyUI_TiledKSampler.git

The TiledKSamplerAdvanced group achieves advanced sampling procedures by dividing sampling spaces into stand-alone tiles and treating them separately. This approach increases the efficiency and control of the sampling process and allows for fine handling of the samples produced. It integrates noise management, tiles strategy and condition input to achieve high-quality and detailed output.

# Input types
## Required
- model
    - Model parameters are essential for the sampling process, which defines the basic structure and parameters of the sampling process. It determines the type of data that can be processed and the quality of the output.
    - Comfy dtype: MODEL
    - Python dtype: comfy.sd.Model
- add_noise
    - This parameter controls whether noise is introduced in the sampling process, thus affecting the diversity and randomity of the samples generated. This is essential for achieving the results of diversification.
    - Comfy dtype: COMBO
    - Python dtype: str
- noise_seed
    - Noise seed parameters play an important role in ensuring the repeatability of noise generation processes. When using the same seeds, they allow for consistent results.
    - Comfy dtype: INT
    - Python dtype: int
- tile_width
    - The tile width parameters determine the horizontal dimensions of each tile and affect the particle size of the sampling process. It is critical in achieving detailed control over the spatial distribution of the samples generated.
    - Comfy dtype: INT
    - Python dtype: int
- tile_height
    - The tile height parameter sets the vertical dimension of each tile, affecting the particle size and width ratio of the sampling process. It is important for fine-tuning the spatial order of output.
    - Comfy dtype: INT
    - Python dtype: int
- tiling_strategy
    - The debris strategy parameters determine the methodology used to divide sampling spaces, which can significantly affect the efficiency and consistency of the sampling process.
    - Comfy dtype: COMBO
    - Python dtype: str
- steps
    - The step parameter defines the number of turns that the sampling process will experience. It directly affects the complexity and precision of the final output.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - cfg parameters adjust the configuration of the sampler to affect the behaviour and performance of the sampling process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - Sampler name parameters specify the type of sampler to be used, which determines the basic method of sample generation and influences the overall result.
    - Comfy dtype: COMBO
    - Python dtype: str
- scheduler
    - The scheduler parameters determine the sampler's schedule strategy and affect the progress and rhythm of the sampling process.
    - Comfy dtype: COMBO
    - Python dtype: str
- positive
    - Positive parameters provide a positive input of conditions, guide the sampling process towards the desired result and shape the characteristics that produce the sample.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Dict[str, Any]]
- negative
    - Negative parameters provide negative conditionalities that help improve the sampling process by avoiding undesirable outcomes.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Dict[str, Any]]
- latent_image
    - Potential image parameters include the potential expression of the image, which is the core input into the sampling process. It directly affects the quality and properties of the samples generated.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Any]
- start_at_step
    - The starting-step parameters specify the initial steps of the sampling process and set the starting point for sample generation.
    - Comfy dtype: INT
    - Python dtype: int
- end_at_step
    - End-step parameters define the final steps of the sampling process and determine the end point of the sample generation.
    - Comfy dtype: INT
    - Python dtype: int
- return_with_leftover_noise
    - Returns the remaining noise parameters to control whether residual noise is contained in the final output, which can influence the texture and appearance of the sample.
    - Comfy dtype: COMBO
    - Python dtype: str
- preview
    - Preview parameters enable or disable preview image generation during sampling to provide visual feedback on progress.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- preview
    - Preview parameters enable or disable preview image generation during sampling to provide visual feedback on progress.
    - Comfy dtype: COMBO
    - Python dtype: str

# Usage tips
- Infra type: GPU

# Source code
```
class TiledKSamplerAdvanced:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'add_noise': (['enable', 'disable'],), 'noise_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'tile_width': ('INT', {'default': 512, 'min': 256, 'max': MAX_RESOLUTION, 'step': 64}), 'tile_height': ('INT', {'default': 512, 'min': 256, 'max': MAX_RESOLUTION, 'step': 64}), 'tiling_strategy': (['random', 'random strict', 'padded', 'simple'],), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'start_at_step': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'end_at_step': ('INT', {'default': 10000, 'min': 0, 'max': 10000}), 'return_with_leftover_noise': (['disable', 'enable'],), 'preview': (['disable', 'enable'],)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'sample'
    CATEGORY = 'sampling'

    def sample(self, model, add_noise, noise_seed, tile_width, tile_height, tiling_strategy, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, start_at_step, end_at_step, return_with_leftover_noise, preview, denoise=1.0):
        return sample_common(model, add_noise, noise_seed, tile_width, tile_height, tiling_strategy, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, start_at_step, end_at_step, return_with_leftover_noise, denoise=1.0, preview=preview == 'enable')
```