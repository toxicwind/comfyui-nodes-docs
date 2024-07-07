# Documentation
- Class name: SeargeOutput6
- Category: Searge/_deprecated_/UI/Outputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

It plays a key role in simplifying data processing, ensuring that parameters are effectively separated and facilitating the follow-up processing phase.

# Input types
## Required
- parameters
    - The “parameters” input is at the core of the SeergeOutput6 node and contains the basic data needed to deactivate the operation. It is essential for the implementation of the node, as it determines the next steps and results.
    - Comfy dtype: Dict[str, Union[str, int, float, bool]]
    - Python dtype: Dict[str, Union[str, int, float, bool]]

# Output types
- parameters
    - The “parameters” output retains structured data formats and provides a clear and organized presentation of data for further use.
    - Comfy dtype: Dict[str, Union[str, int, float, bool]]
    - Python dtype: Dict[str, Union[str, int, float, bool]]
- hrf_steps
    - The “hrf_steps” output indicates the number of steps involved in the high-resolution repair process, which is important for controlling the level of detail of the output.
    - Comfy dtype: int
    - Python dtype: int
- hrf_denoise
    - The output of “hrf_denoise” indicates the level of noise that should be used for high-resolution restoration, affecting the clarity and quality of the final result.
    - Comfy dtype: float
    - Python dtype: float
- hrf_upscale_factor
    - “hrf_upscale_factor” output represents the scaling factors used in the sampling process, which are essential for determining the resolution of the image being sampled.
    - Comfy dtype: float
    - Python dtype: float
- hrf_noise_offset
    - The output of “hrf_noise_offset” represents the level of noise offset, which is the key parameter for fine-tuning noise properties in image processing.
    - Comfy dtype: int
    - Python dtype: int
- hrf_seed
    - The "hrf_seed" output is the seed value used to generate random numbers to ensure repeatability and consistency in the processing process.
    - Comfy dtype: int
    - Python dtype: int
- hires_fix
    - The “hires_fix” output is a boolean sign indicating whether a high-resolution restoration process has been applied to improve image quality.
    - Comfy dtype: bool
    - Python dtype: bool
- hrf_smoothness
    - The “hrf_smoothness” output controls the smoothness of high-resolution restoration and plays a key role in the final appearance of the sample image.
    - Comfy dtype: float
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeOutput6:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'parameters': ('PARAMETERS',)}}
    RETURN_TYPES = ('PARAMETERS', 'INT', 'FLOAT', 'FLOAT', 'INT', 'INT', 'ENABLE_STATE', 'FLOAT')
    RETURN_NAMES = ('parameters', 'hrf_steps', 'hrf_denoise', 'hrf_upscale_factor', 'hrf_noise_offset', 'hrf_seed', 'hires_fix', 'hrf_smoothness')
    FUNCTION = 'demux'
    CATEGORY = 'Searge/_deprecated_/UI/Outputs'

    def demux(self, parameters):
        hrf_steps = parameters['hrf_steps']
        hrf_denoise = parameters['hrf_denoise']
        hrf_upscale_factor = parameters['hrf_upscale_factor']
        hrf_noise_offset = parameters['hrf_noise_offset']
        hrf_seed = parameters['hrf_seed']
        hires_fix = parameters['hires_fix']
        hrf_smoothness = parameters['hrf_smoothness']
        return (parameters, hrf_steps, hrf_denoise, hrf_upscale_factor, hrf_noise_offset, hrf_seed, hires_fix, hrf_smoothness)
```