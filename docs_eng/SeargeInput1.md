# Documentation
- Class name: SeargeInput1
- Category: Searge/_deprecated_/UI/Inputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergeInput1 node serves as an input interface for the Seage system, which collects and organizes various tips and optional inputs. It aims to simplify the input process by allowing users to specify primary, secondary, style and negative hints, as well as optional images, masks and additional parameters, and wrap them in a structured format for downstream tasks.

# Input types
## Required
- main_prompt
    - The main_prompt parameter is essential to define the main context or theme of the input. It is a string that can cross multiple lines and allows a detailed description, which is essential for the operation of the node and the generation of the output required.
    - Comfy dtype: STRING
    - Python dtype: str
- secondary_prompt
    - Second_prompt provides additional context or details for main_prompt. It enhances the ability of nodes to understand and process inputs and helps produce more detailed outputs.
    - Comfy dtype: STRING
    - Python dtype: str
- style_prompt
    - The style_prompt parameter is used to specify the style elements or tone that the output should embody. It is a key component in shaping the aesthetic or thematic quality of the end result.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt
    - It plays an important role in guiding nodes to remove unwanted elements from the end product.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_style
    - The negative_prompt parameter is an important tool for fine-tuning output to meet specific requirements by further specifying the style or quality to be omitted.
    - Comfy dtype: STRING
    - Python dtype: str
- inputs
    - The inputs parameter is an optional dictionary that contains other parameters used by nodes. It provides flexibility for nodes to operate and allows customization according to specific cases.
    - Comfy dtype: PARAMETER_INPUTS
    - Python dtype: Dict[str, Any]
- image
    - The Image parameter is an optional input that allows the processing of visual data. When you process an image-related task, it can significantly influence the nature of the execution and output of the node.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- mask
    - The mask parameter is an optional input that defines the image range that should be treated differently or ignored during processing. It is essential for a task that requires selective handling of visual data.
    - Comfy dtype: MASK
    - Python dtype: np.ndarray

# Output types
- inputs
    - The 'inputs' output is a set of structured parameters for which nodes are sealed. It is the basis for the next steps in the Sarge system.
    - Comfy dtype: PARAMETER_INPUTS
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeInput1:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'main_prompt': ('STRING', {'multiline': True, 'default': ''}), 'secondary_prompt': ('STRING', {'multiline': True, 'default': ''}), 'style_prompt': ('STRING', {'multiline': True, 'default': ''}), 'negative_prompt': ('STRING', {'multiline': True, 'default': ''}), 'negative_style': ('STRING', {'multiline': True, 'default': ''})}, 'optional': {'inputs': ('PARAMETER_INPUTS',), 'image': ('IMAGE',), 'mask': ('MASK',)}}
    RETURN_TYPES = ('PARAMETER_INPUTS',)
    RETURN_NAMES = ('inputs',)
    FUNCTION = 'mux'
    CATEGORY = 'Searge/_deprecated_/UI/Inputs'

    def mux(self, main_prompt, secondary_prompt, style_prompt, negative_prompt, negative_style, inputs=None, image=None, mask=None):
        if inputs is None:
            parameters = {}
        else:
            parameters = inputs
        parameters['main_prompt'] = main_prompt
        parameters['secondary_prompt'] = secondary_prompt
        parameters['style_prompt'] = style_prompt
        parameters['negative_prompt'] = negative_prompt
        parameters['negative_style'] = negative_style
        parameters['image'] = image
        parameters['mask'] = mask
        return (parameters,)
```