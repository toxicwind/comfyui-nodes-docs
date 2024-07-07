# Documentation
- Class name: SampleSettingsNode
- Category: Animate Diff 🎭🅐🅓
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The `create_settings'method of the SampleSettings Node class is designed to configure and generate sampling settings for animating processes. It covers parameters that define noise generation behaviour, iterative options and other customable aspects of the sampling process. This method plays a key role in preparing the basis for the next steps in the animation workflow, ensuring that the settings are properly set up to achieve the desired results.

# Input types
## Required
- batch_offset
    - The parameter `batch_offset'is essential to manage the batch processing of noise generation. It allows the system to deflect batch indexes, which may be essential to ensure a unique noise pattern between batches. This parameter significantly influences the execution and results of the sampling process.
    - Comfy dtype: INT
    - Python dtype: int
- noise_type
    - Parameter `noise_type'determines the type of noise layer to be used in the sampling process. It is a key factor in creating noise characteristics, which in turn affects the overall quality and style of the animation. This parameter is indispensable for achieving the required noise contour in the final output.
    - Comfy dtype: NoiseLayerType.LIST
    - Python dtype: str
- seed_gen
    - The parameter `seed_gen'determines the method of seed generation of the noise layer. It is important to ensure consistency and repeatability of the noise patterns generated. This parameter is essential to maintain the integrity of the noise generation process in different operations.
    - Comfy dtype: SeedNoiseGeneration.LIST
    - Python dtype: str
- seed_offset
    - The parameter `seed_offset'is used to adjust the seed value of noise generation, which changes the mode of noise production. It plays an important role in customizing noise properties and is essential for achieving specific visual effects in animations.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- noise_layers
    - The parameter `noise_layers'allows the custom noise layers to be specified during the sampling process. It provides a high degree of flexibility to customise noise properties according to specific creative requirements. This parameter is particularly useful for users wishing to try different noise configurations.
    - Comfy dtype: NOISE_LAYERS
    - Python dtype: NoiseLayerGroup
- iteration_opts
    - The parameter `iteration_opts'provides the option to control the iterative process during the sampling process. It can be used to fine-tune the sampling process to optimize factors such as speed, accuracy or resource use. It is essential to achieve a balance between performance and quality in the animation.
    - Comfy dtype: ITERATION_OPTS
    - Python dtype: IterationOptions
- seed_override
    - Parameter `seed_override' allows manual overlaying of default seed values for noise generation. This may be particularly useful in scenarios that require a specific noise mode or replication of previously run results. This parameter adds additional layers of control to the noise generation process.
    - Comfy dtype: INT
    - Python dtype: Union[int, None]
- adapt_denoise_steps
    - The parameter `adapt_denoise_steps'is a boolean symbol that allows the system to adapt to the noise step during the sampling process. This can lead to more efficient and efficient noise reduction and improve the overall quality of animations.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- custom_cfg
    - Parameter `custom_cfg'allows the use of custom-defined configuration frames that can be applied to the sampling process. This provides a way to introduce specific creative adjustments and micromobilization drawings to meet unique project requirements. This parameter is particularly useful for advanced users seeking greater control over animation.
    - Comfy dtype: CUSTOM_CFG
    - Python dtype: CustomCFGKeyframeGroup
- sigma_schedule
    - The parameter `sigma_schedule'defines the timetable for the sigma values used in noise generation. It is essential to control the differences in noise and can significantly influence the visual results of animation. This parameter provides a method for applying different levels of noise reduction at different stages of the sampling process.
    - Comfy dtype: SIGMA_SCHEDULE
    - Python dtype: SigmaSchedule

# Output types
- settings
    - The output `settings' provides sampling settings custom-made by `create_settings '. These settings encapsulate all parameters and options specified during the method call and are used to guide the next steps in the animation process.
    - Comfy dtype: SAMPLE_SETTINGS
    - Python dtype: SampleSettings

# Usage tips
- Infra type: CPU

# Source code
```
class SampleSettingsNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'batch_offset': ('INT', {'default': 0, 'min': 0, 'max': BIGMAX}), 'noise_type': (NoiseLayerType.LIST,), 'seed_gen': (SeedNoiseGeneration.LIST,), 'seed_offset': ('INT', {'default': 0, 'min': BIGMIN, 'max': BIGMAX})}, 'optional': {'noise_layers': ('NOISE_LAYERS',), 'iteration_opts': ('ITERATION_OPTS',), 'seed_override': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615, 'forceInput': True}), 'adapt_denoise_steps': ('BOOLEAN', {'default': False}), 'custom_cfg': ('CUSTOM_CFG',), 'sigma_schedule': ('SIGMA_SCHEDULE',)}}
    RETURN_TYPES = ('SAMPLE_SETTINGS',)
    RETURN_NAMES = ('settings',)
    CATEGORY = 'Animate Diff 🎭🅐🅓'
    FUNCTION = 'create_settings'

    def create_settings(self, batch_offset: int, noise_type: str, seed_gen: str, seed_offset: int, noise_layers: NoiseLayerGroup=None, iteration_opts: IterationOptions=None, seed_override: int=None, adapt_denoise_steps=False, custom_cfg: CustomCFGKeyframeGroup=None, sigma_schedule: SigmaSchedule=None):
        sampling_settings = SampleSettings(batch_offset=batch_offset, noise_type=noise_type, seed_gen=seed_gen, seed_offset=seed_offset, noise_layers=noise_layers, iteration_opts=iteration_opts, seed_override=seed_override, adapt_denoise_steps=adapt_denoise_steps, custom_cfg=custom_cfg, sigma_schedule=sigma_schedule)
        return (sampling_settings,)
```