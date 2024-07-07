# Documentation
- Class name: SeargeOutput1
- Category: Searge/_deprecated_/UI/Outputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node class serves as an interface for the purpose of disassembly input parameters into different outputs to facilitate the organization and flow of data within the system.

# Input types
## Required
- parameters
    - Parameter input is essential for the operation of the node, which contains all the tips and images required for the node operation. It is the main source of information for the recovery process.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Output types
- parameters
    - The output 'parameters' is an input reflection that marks the integrity of the data through nodes.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]
- main_prompt
    - Output'main_prompt' represents the main text input for follow-up or content generation within the guidance system.
    - Comfy dtype: String
    - Python dtype: str
- secondary_prompt
    - This output provides additional text content to enrich data for further operation of the system.
    - Comfy dtype: String
    - Python dtype: str
- style_prompt
    - Output'style_prompt' is used to define style elements or themes that should be included in system processing or generation.
    - Comfy dtype: String
    - Python dtype: str
- negative_prompt
    - This output contains information that the system should avoid or exclude during processing or content generation.
    - Comfy dtype: String
    - Python dtype: str
- negative_style
    - Output 'negative_style' specified elements of style or themes that should be consciously avoided when generating content.
    - Comfy dtype: String
    - Python dtype: str
- image
    - Output 'image' is a visual element that can be provided as input or generated within the system to influence subsequent visual processing or creation of content.
    - Comfy dtype: Image
    - Python dtype: PIL.Image
- mask
    - Output'mask' is a binary or multi-category array that indicates which parts of the image or content should be operated or protected during the process.
    - Comfy dtype: Mask
    - Python dtype: numpy.ndarray

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeOutput1:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'parameters': ('PARAMETERS',)}}
    RETURN_TYPES = ('PARAMETERS', 'STRING', 'STRING', 'STRING', 'STRING', 'STRING', 'IMAGE', 'MASK')
    RETURN_NAMES = ('parameters', 'main_prompt', 'secondary_prompt', 'style_prompt', 'negative_prompt', 'negative_style', 'image', 'mask')
    FUNCTION = 'demux'
    CATEGORY = 'Searge/_deprecated_/UI/Outputs'

    def demux(self, parameters):
        main_prompt = parameters['main_prompt']
        secondary_prompt = parameters['secondary_prompt']
        style_prompt = parameters['style_prompt']
        negative_prompt = parameters['negative_prompt']
        negative_style = parameters['negative_style']
        image = parameters['image']
        mask = parameters['mask']
        return (parameters, main_prompt, secondary_prompt, style_prompt, negative_prompt, negative_style, image, mask)
```