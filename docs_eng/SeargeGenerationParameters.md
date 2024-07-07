# Documentation
- Class name: SeargeGenerationParameters
- Category: UI_INPUTS
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

Such nodes encapsulate the parameters needed to generate the image by searching methods. It simplifys the configuration process by allowing users to specify key attributes, such as seeds, image sizes and sampling presets, which together influence the quality and characteristics of the image.

# Input types
## Required
- seed
    - Seed parameters are essential for initializing the random number generator to ensure that the image generation process is recreated. It determines the starting point of the random element of the algorithm and thus plays a key role in determining the uniqueness and consistency of the image generated.
    - Comfy dtype: INT
    - Python dtype: int
- image_size_preset
    - The image size preset parameters allow the user to select a predefined resolution for the image generated. This selection directly affects the level of detail of the image and the computational resources required for image generation, and higher resolution requires more processing capacity.
    - Comfy dtype: COMBO
    - Python dtype: str
- image_width
    - The image width parameter specifies the horizontal dimensions that generate the image. It is a key factor in determining the width and overall appearance of the image, and it works with the image height parameters to determine the final dimensions.
    - Comfy dtype: INT
    - Python dtype: int
- image_height
    - The image height parameter defines the vertical dimensions in which the image is generated. Together with the width of the image, it sets the canvas size for the image generation process, affecting the size and layout of the content.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - Step parameters refer to the number of turns that the process will experience. More steps usually produce more sophisticated and detailed images, but also increase the computational costs and time required to generate them.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - Configure parameters, usually referred to as 'cfg', is a floating point value used to adjust the balance between image quality and generation speed. Lower values can produce images faster, but less detail, and higher values can enhance detail at the cost of processing time.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_preset
    - Sampler presets parameters that enable users to select from a predefined set of sampling strategies. Each preset is designed to optimize the generation process for specific types of content or intended outcomes, affecting the diversity and consistency of the images generated.
    - Comfy dtype: COMBO
    - Python dtype: str
- sampler_name
    - Sampler name parameters are essential for selecting a particular algorithm for image generation. Different samplers provide different image refining methods that affect the visual style and quality of the final output.
    - Comfy dtype: COMBO
    - Python dtype: str
- scheduler
    - The scheduler parameters determine the optimal strategy to be used in image generation. It regulates the balance between exploration and utilization, thus affecting the speed and quality of image generation.
    - Comfy dtype: COMBO
    - Python dtype: str
- base_vs_refiner_ratio
    - It affects the distribution of computing resources between the initial creation of the image and the subsequent enhancement of image details.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- data
    - The data output of this node represents a structured flow of information containing the generation parameters. It is a blueprint for the image generation process, encapsulating all user-defined settings and guiding algorithms to generate the required images.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: SRG_DATA_STREAM

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeGenerationParameters:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551600}), 'image_size_preset': (UI.RESOLUTION_PRESETS,), 'image_width': ('INT', {'default': 1024, 'min': 0, 'max': UI.MAX_RESOLUTION, 'step': 8}), 'image_height': ('INT', {'default': 1024, 'min': 0, 'max': UI.MAX_RESOLUTION, 'step': 8}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 200}), 'cfg': ('FLOAT', {'default': 7.0, 'min': 0.5, 'max': 30.0, 'step': 0.5}), 'sampler_preset': (UI.SAMPLER_PRESETS,), 'sampler_name': (UI.SAMPLERS, {'default': 'dpmpp_2m'}), 'scheduler': (UI.SCHEDULERS, {'default': 'karras'}), 'base_vs_refiner_ratio': ('FLOAT', {'default': 0.8, 'min': 0.0, 'max': 1.0, 'step': 0.05})}, 'optional': {'data': ('SRG_DATA_STREAM',)}}
    RETURN_TYPES = ('SRG_DATA_STREAM',)
    RETURN_NAMES = ('data',)
    FUNCTION = 'get'
    CATEGORY = UI.CATEGORY_UI_INPUTS

    @staticmethod
    def create_dict(seed, image_size_preset, image_width, image_height, steps, cfg, sampler_preset, sampler_name, scheduler, base_vs_refiner_ratio):
        if sampler_preset == UI.SAMPLER_PRESET_DPMPP_2M_KARRAS:
            (sampler_name, scheduler) = ('dpmpp_2m', 'karras')
        elif sampler_preset == UI.SAMPLER_PRESET_EULER_A:
            (sampler_name, scheduler) = ('euler_ancestral', 'normal')
        elif sampler_preset == UI.SAMPLER_PRESET_DPMPP_2M_SDE_KARRAS:
            (sampler_name, scheduler) = ('dpmpp_2m_sde', 'karras')
        elif sampler_preset == UI.SAMPLER_PRESET_DPMPP_3M_SDE_EXPONENTIAL:
            (sampler_name, scheduler) = ('dpmpp_3m_sde', 'exponential')
        elif sampler_preset == UI.SAMPLER_PRESET_DDIM_UNIFORM:
            (sampler_name, scheduler) = ('ddim', 'ddim_uniform')
        return {UI.F_SEED: seed, UI.F_IMAGE_SIZE_PRESET: image_size_preset, UI.F_IMAGE_WIDTH: image_width, UI.F_IMAGE_HEIGHT: image_height, UI.F_STEPS: steps, UI.F_CFG: round(cfg, 3), UI.F_SAMPLER_PRESET: sampler_preset, UI.F_SAMPLER_NAME: sampler_name, UI.F_SCHEDULER: scheduler, UI.F_BASE_VS_REFINER_RATIO: round(base_vs_refiner_ratio, 3)}

    def get(self, seed, image_size_preset, image_width, image_height, steps, cfg, sampler_preset, sampler_name, scheduler, base_vs_refiner_ratio, data=None):
        if data is None:
            data = {}
        data[UI.S_GENERATION_PARAMETERS] = self.create_dict(seed, image_size_preset, image_width, image_height, steps, cfg, sampler_preset, sampler_name, scheduler, base_vs_refiner_ratio)
        return (data,)
```