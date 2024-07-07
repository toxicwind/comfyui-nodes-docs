# Documentation
- Class name: SeargeInput6
- Category: Searge/_deprecated_/UI/Inputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node serves as an interface for the configuration and combination of parameters associated with high-resolution image processing. It is designed to simplify the process of setting up high-resolution restoration tasks by allowing users to enter and adjust multiple parameters at once. The main function of the node is to facilitate the preparation and management of image processing tasks and to ensure the correct application and organization of the necessary settings.

# Input types
## Required
- hires_fix
    - This parameter is essential for defining the state of the high-resolution restoration process. It sets the initial conditions for the start of image processing and significantly affects the outcome of the mission.
    - Comfy dtype: SeargeParameterProcessor.STATES
    - Python dtype: SeargeParameterProcessor.STATES
- hrf_steps
    - The number of high-resolution repair steps is essential to control the iterative process of image fine-tuning. It affects the level of detail and overall quality of the final output.
    - Comfy dtype: INT
    - Python dtype: int
- hrf_denoise
    - Noise parameters play a key role in reducing image noise and prostheses, thus increasing the clarity and visual attractiveness of processing images.
    - Comfy dtype: FLOAT
    - Python dtype: float
- hrf_upscale_factor
    - The magnification factor determines the extent to which the image will be magnified, directly affecting the resolution and detail of the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- hrf_intensity
    - Strength parameters affect the intensity of image-processing effects, such as sharpness and increased contrasts, which are essential for achieving the desired visual results.
    - Comfy dtype: SeargeParameterProcessor.REFINER_INTENSITY
    - Python dtype: SeargeParameterProcessor.REFINER_INTENSITY
- hrf_seed_offset
    - Seed deviations are important to ensure the randomity and diversity of image-processing results, especially when processing multiple images or batches.
    - Comfy dtype: SeargeParameterProcessor.HRF_SEED_OFFSET
    - Python dtype: SeargeParameterProcessor.HRF_SEED_OFFSET
- hrf_smoothness
    - Smoothness parameters help to control the sharpness and texture of the processing of images and contribute to the overall beauty and quality of the final product.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- inputs
    - This parameter allows for additional input that can be used to further customize high-resolution image processing workflows.
    - Comfy dtype: PARAMETER_INPUTS
    - Python dtype: dict

# Output types
- inputs
    - Output is an orderly set of parameters that are configured through nodes. These parameters are essential for the next steps in the high-resolution image processing stream.
    - Comfy dtype: PARAMETER_INPUTS
    - Python dtype: dict

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeInput6:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'hires_fix': (SeargeParameterProcessor.STATES, {'default': SeargeParameterProcessor.STATES[1]}), 'hrf_steps': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'hrf_denoise': ('FLOAT', {'default': 0.1, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'hrf_upscale_factor': ('FLOAT', {'default': 1.5, 'min': 0.25, 'max': 4.0, 'step': 0.25}), 'hrf_intensity': (SeargeParameterProcessor.REFINER_INTENSITY, {'default': SeargeParameterProcessor.REFINER_INTENSITY[1]}), 'hrf_seed_offset': (SeargeParameterProcessor.HRF_SEED_OFFSET, {'default': SeargeParameterProcessor.HRF_SEED_OFFSET[1]}), 'hrf_smoothness': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.05})}, 'optional': {'inputs': ('PARAMETER_INPUTS',)}}
    RETURN_TYPES = ('PARAMETER_INPUTS',)
    RETURN_NAMES = ('inputs',)
    FUNCTION = 'mux'
    CATEGORY = 'Searge/_deprecated_/UI/Inputs'

    def mux(self, hires_fix, hrf_steps, hrf_denoise, hrf_upscale_factor, hrf_intensity, hrf_seed_offset, hrf_smoothness, inputs=None):
        if inputs is None:
            parameters = {}
        else:
            parameters = inputs
        parameters['hires_fix'] = hires_fix
        parameters['hrf_steps'] = hrf_steps
        parameters['hrf_denoise'] = hrf_denoise
        parameters['hrf_upscale_factor'] = hrf_upscale_factor
        parameters['hrf_intensity'] = hrf_intensity
        parameters['hrf_seed_offset'] = hrf_seed_offset
        parameters['hrf_smoothness'] = hrf_smoothness
        return (parameters,)
```