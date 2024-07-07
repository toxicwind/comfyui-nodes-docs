# Documentation
- Class name: SeargeOutput3
- Category: Searge/_deprecated_/UI/Outputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node class covers the logic of decomposition of a set of parameters into stand-alone components for further processing and analysis within the system.

# Input types
## Required
- parameters
    - This parameter, as a key input, contains a dictionary containing various settings that determine the behaviour and output of nodes.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Output types
- parameters
    - The original set of parameters is passed on, maintaining the integrity of the input data.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]
- denoise
    - The output represents a noise setting, which is essential to the image quality enhancement process.
    - Comfy dtype: Float
    - Python dtype: float
- base_ratio
    - The base-scale output is used to control the basic aspects of image scaling and to ensure proportionality and consistency.
    - Comfy dtype: Float
    - Python dtype: float
- refiner_strength
    - The fine-tuning intensity is an output that influences the fine-tuning process of image details and is designed to optimize clarity and sharpness.
    - Comfy dtype: Float
    - Python dtype: float
- noise_offset
    - Noise offset output is essential to adjust the level of noise in the image and helps to improve overall visual quality.
    - Comfy dtype: Float
    - Python dtype: float
- precondition_steps
    - This output defines the number of pre-treatment steps to be implemented, which is an important part of the preparation phase of the image treatment stream.
    - Comfy dtype: Int
    - Python dtype: int
- batch_size
    - Batch-processing output determines the number of images to be processed simultaneously, affecting the efficiency of the system and the volume of throughput.
    - Comfy dtype: Int
    - Python dtype: int
- upscale_resolution_factor
    - The output is responsible for defining the scaling factors to be applied to image resolution, which is a key factor in achieving the desired output dimensions.
    - Comfy dtype: Float
    - Python dtype: float
- save_upscaled_image
    - The preservation of magnified image output is a sign used to determine whether a processed image should be saved to influence the persistence of the data.
    - Comfy dtype: Bool
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeOutput3:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'parameters': ('PARAMETERS',)}}
    RETURN_TYPES = ('PARAMETERS', 'FLOAT', 'FLOAT', 'FLOAT', 'INT', 'INT', 'INT', 'FLOAT', 'ENABLE_STATE')
    RETURN_NAMES = ('parameters', 'denoise', 'base_ratio', 'refiner_strength', 'noise_offset', 'precondition_steps', 'batch_size', 'upscale_resolution_factor', 'save_upscaled_image')
    FUNCTION = 'demux'
    CATEGORY = 'Searge/_deprecated_/UI/Outputs'

    def demux(self, parameters):
        denoise = parameters['denoise']
        base_ratio = parameters['base_ratio']
        refiner_strength = parameters['refiner_strength']
        noise_offset = parameters['noise_offset']
        precondition_steps = parameters['precondition_steps']
        batch_size = parameters['batch_size']
        upscale_resolution_factor = parameters['upscale_resolution_factor']
        save_upscaled_image = parameters['save_upscaled_image']
        return (parameters, denoise, base_ratio, refiner_strength, noise_offset, precondition_steps, batch_size, upscale_resolution_factor, save_upscaled_image)
```