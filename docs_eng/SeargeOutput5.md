# Documentation
- Class name: SeargeOutput5
- Category: Searge/_deprecated_/UI/Outputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node classifies the input parameters and separates them into different outputs to facilitate the organization and flow of data within the system.

# Input types
## Required
- parameters
    - This parameter, as a set of integrated settings, guides the operation of nodes. It is essential for the nodes to function properly and to produce meaningful results.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Output types
- parameters
    - The original set of parameters provided remains unchanged. This output maintains the integrity of the input data for further use.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]
- base_conditioning_scale
    - This output represents the scaling factor for base conditions and is essential for adjusting the impact of base input throughout the process.
    - Comfy dtype: float
    - Python dtype: float
- refiner_conditioning_scale
    - The output is a scaling factor for refining conditions and plays a key role in fine-tuning output according to input parameters.
    - Comfy dtype: float
    - Python dtype: float
- style_prompt_power
    - The output represents the power level of style tips, which is very important in determining the style impact of the final result.
    - Comfy dtype: float
    - Python dtype: float
- negative_style_power
    - The output represents the negative power level of the style hint, which is important in controlling the style elements that do not want to appear in the output.
    - Comfy dtype: float
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeOutput5:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'parameters': ('PARAMETERS',)}}
    RETURN_TYPES = ('PARAMETERS', 'FLOAT', 'FLOAT', 'FLOAT', 'FLOAT')
    RETURN_NAMES = ('parameters', 'base_conditioning_scale', 'refiner_conditioning_scale', 'style_prompt_power', 'negative_style_power')
    FUNCTION = 'demux'
    CATEGORY = 'Searge/_deprecated_/UI/Outputs'

    def demux(self, parameters):
        base_conditioning_scale = parameters['base_conditioning_scale']
        refiner_conditioning_scale = parameters['refiner_conditioning_scale']
        style_prompt_power = parameters['style_prompt_power']
        negative_style_power = parameters['negative_style_power']
        return (parameters, base_conditioning_scale, refiner_conditioning_scale, style_prompt_power, negative_style_power)
```