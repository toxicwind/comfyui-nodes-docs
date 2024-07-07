# Documentation
- Class name: SeargeInput2
- Category: Searge/_deprecated_/UI/Inputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergeInput2 node is designed to process the initial input of image-processing tasks. It configures and activates the parameters that define image features, such as their size, the number of processing steps and the configuration settings that will guide the processing algorithms. The node abstractes the complexity of setting these parameters and provides a simplified interface for users to enter the data needed for image generation or operation.

# Input types
## Required
- seed
    - The `seed' parameter is essential to the image generation process, as it ensures the replicability of results. It serves as a starting point for random numbers to be generated, affecting the final output image. The significance of this parameter lies in its ability to control randomity and achieve consistent results in different operations.
    - Comfy dtype: INT
    - Python dtype: int
- image_width
    - The `image_width' parameter specifies the width needed to generate the image. It plays an important role in determining the overall size of the image, which affects the level of detail and the computational resources needed to process it. This parameter is essential for setting the size of visual output.
    - Comfy dtype: INT
    - Python dtype: int
- image_height
    - The `image_height' parameter defines the vertical dimensions of the image. Similar to `image_width', it is a key determinant of the resolution of the image and contains negative effects on details and calculations. Adjusting this parameter controls the vertical ratio and overall size of the image.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The'steps' parameter refers to the number of turns or steps the image processing algorithm will perform. It directly affects the quality and detail of the final image, and more steps usually lead to more refined results. This parameter is essential for balancing processing time with output quality.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - `cfg' parameter, which represents configuration settings for fine-tuning image processing algorithms. It affects all aspects of image generation, such as clarity and the existence of certain features. This parameter is important for achieving the required visual effects and ensuring that the output meets specific requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The'sampler_name' parameter selects the sampling method used for random processes in image generation. It is important for determining the randomity and diversity of images generated. The selection of the sampler can significantly influence the style and characteristics of the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- scheduler
    - The'scheduler' parameter determines the dispatch strategy for the image generation process. It determines how the algorithm works through step-by-step progress, which can affect efficiency and the end result. This parameter is essential to optimize the generation process and achieve the best results within the given time frame.
    - Comfy dtype: STRING
    - Python dtype: str
- save_image
    - The `save_image' parameter indicates whether the image generated should be saved in the file. It controls the action after the image is processed. It is important for users who want to keep the output for further use or analysis.
    - Comfy dtype: STRING
    - Python dtype: str
- save_directory
    - The'save_directory' parameter specifies the location where the image will be saved. It is essential to organize output and ensure that users can easily access and manage their files.
    - Comfy dtype: STRING
    - Python dtype: str
- inputs
    - The 'inputs'parameter is an optional dictionary that allows users to provide additional settings or parameters for image-processing tasks. It provides flexibility and customization to enable users to adjust node behaviour to specific requirements.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Output types
- parameters
    - The 'parameters'output contains configurations and input sets that are processed by the SeergeInput2 node. It encapsifies all necessary information for the follow-up phase of image processing to ensure a smooth transition from input to execution.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeInput2:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'image_width': ('INT', {'default': 1024, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'image_height': ('INT', {'default': 1024, 'min': 0, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'steps': ('INT', {'default': 20, 'min': 0, 'max': 200}), 'cfg': ('FLOAT', {'default': 7.0, 'min': 0.0, 'max': 30.0, 'step': 0.5}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS, {'default': 'ddim'}), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS, {'default': 'ddim_uniform'}), 'save_image': (SeargeParameterProcessor.STATES, {'default': SeargeParameterProcessor.STATES[1]}), 'save_directory': (SeargeParameterProcessor.SAVE_TO, {'default': SeargeParameterProcessor.SAVE_TO[0]})}, 'optional': {'inputs': ('PARAMETER_INPUTS',)}}
    RETURN_TYPES = ('PARAMETER_INPUTS',)
    RETURN_NAMES = ('inputs',)
    FUNCTION = 'mux'
    CATEGORY = 'Searge/_deprecated_/UI/Inputs'

    def mux(self, seed, image_width, image_height, steps, cfg, sampler_name, scheduler, save_image, save_directory, inputs=None):
        if inputs is None:
            parameters = {}
        else:
            parameters = inputs
        parameters['seed'] = seed
        parameters['image_width'] = image_width
        parameters['image_height'] = image_height
        parameters['steps'] = steps
        parameters['cfg'] = cfg
        parameters['sampler_name'] = sampler_name
        parameters['scheduler'] = scheduler
        parameters['save_image'] = save_image
        parameters['save_directory'] = save_directory
        return (parameters,)
```