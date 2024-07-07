# Documentation
- Class name: SeargeInput3
- Category: Searge/_deprecated_/UI/Inputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node, as a multi-routine reuser for various input parameters, streamlines the process of integrating the diversity configuration into the system. It is designed to process the necessary and optional input to ensure that the necessary data are transmitted efficiently and that there is no loss of information.

# Input types
## Required
- base_ratio
    - The base scale parameter is essential for establishing the basic scale of input data. It significantly affects the initial size of the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- refiner_strength
    - The intensity of the fine-tuning determines the intensity of the reprocessing steps to be applied to scalable data. It affects the final quality and detail of the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- refiner_intensity
    - The fine-tuning strength setting adjusts the level of detail retained during the magnification process. It is essential to strike a balance between performance and output clarity.
    - Comfy dtype: ENUM
    - Python dtype: Enum
- precondition_steps
    - The number of pre-treatment steps determines the complexity of the initial processing. It is a key factor in optimizing the efficiency and effectiveness of the magnification process.
    - Comfy dtype: INT
    - Python dtype: int
- batch_size
    - It is a key parameter for managing the computational resources and accelerating the pace of implementation.
    - Comfy dtype: INT
    - Python dtype: int
- upscale_resolution_factor
    - This factor has a direct effect on magnifying the final resolution of the image. It is critical in determining the visual authenticity of the output and in calculating the needs.
    - Comfy dtype: FLOAT
    - Python dtype: float
- save_upscaled_image
    - The decision to save the magnified image affects the results of the workflow. It ensures that the results are saved for further analysis or use.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- inputs
    - This parameter allows for the inclusion of additional input parameters, which enhances the multifunctionality of nodes and their ability to adapt to different scenarios.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]
- denoise
    - Noise parameters are essential for the noise reduction process to control the noise level filtered from the magnified image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- inputs
    - The output is a comprehensive set of parameters containing all inputs and provides a structured and orderly expression for further processing of the data.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeInput3:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'base_ratio': ('FLOAT', {'default': 0.8, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'refiner_strength': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 1.0, 'step': 0.05}), 'refiner_intensity': (SeargeParameterProcessor.REFINER_INTENSITY, {'default': SeargeParameterProcessor.REFINER_INTENSITY[1]}), 'precondition_steps': ('INT', {'default': 0, 'min': 0, 'max': 10}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 4}), 'upscale_resolution_factor': ('FLOAT', {'default': 2.0, 'min': 0.25, 'max': 4.0, 'step': 0.25}), 'save_upscaled_image': (SeargeParameterProcessor.STATES, {'default': SeargeParameterProcessor.STATES[1]})}, 'optional': {'inputs': ('PARAMETER_INPUTS',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('PARAMETER_INPUTS',)
    RETURN_NAMES = ('inputs',)
    FUNCTION = 'mux'
    CATEGORY = 'Searge/_deprecated_/UI/Inputs'

    def mux(self, base_ratio, refiner_strength, refiner_intensity, precondition_steps, batch_size, upscale_resolution_factor, save_upscaled_image, inputs=None, denoise=None):
        if inputs is None:
            parameters = {}
        else:
            parameters = inputs
        parameters['denoise'] = denoise
        parameters['base_ratio'] = base_ratio
        parameters['refiner_strength'] = refiner_strength
        parameters['refiner_intensity'] = refiner_intensity
        parameters['precondition_steps'] = precondition_steps
        parameters['batch_size'] = batch_size
        parameters['upscale_resolution_factor'] = upscale_resolution_factor
        parameters['save_upscaled_image'] = save_upscaled_image
        return (parameters,)
```