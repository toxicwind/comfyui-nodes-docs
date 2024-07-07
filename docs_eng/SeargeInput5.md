# Documentation
- Class name: SeargeInput5
- Category: Searge/_deprecated_/UI/Inputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

SeergeInput5 provides a consistent input set for further processing as a central hub for processing and integrating condition scales and style parameters. It is designed to handle the necessary and optional parameters to ensure flexibility in input configuration while maintaining a structured approach to data streams.

# Input types
## Required
- base_conditioning_scale
    - The base condition scale is a key parameter that affects the initial level of detail in the flow line. It sets the tone for the subsequent fine-tuning phase, affecting the overall quality and resolution of the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- refiner_conditioning_scale
    - The fine-tuning of the condition scale is essential to fine-tune the output after initial processing. It allows for adjustments in the details and clarity of the final result to ensure that the output is refined and refined.
    - Comfy dtype: FLOAT
    - Python dtype: float
- style_prompt_power
    - The style alert power determines the effect of the style template on the final output. It is a key factor in the artistic and aesthetic development of results, allowing for a balance between creativity and control.
    - Comfy dtype: FLOAT
    - Python dtype: float
- negative_style_power
    - Negative style power is used to offset or inhibit some of the style elements in the output. It provides a mechanism for fine control of the style direction of the result and achieves a subtle approach to style application.
    - Comfy dtype: FLOAT
    - Python dtype: float
- style_template
    - Style template parameters play a key role in defining the style frame of the output. They serve as blueprints for artistic expression and guide the overall look and feeling of the end product.
    - Comfy dtype: SeargeParameterProcessor.STYLE_TEMPLATE
    - Python dtype: str
## Optional
- inputs
    - The optional input parameter allows additional customization and flexibility in node operations. It allows the integration of external data sources or parameters and allows further refinement of the function of the node.
    - Comfy dtype: PARAMETER_INPUTS
    - Python dtype: Dict[str, Any]

# Output types
- parameters
    - The output parameter covers the post-processing input and provides a structured data set prepared for downstream processing. This output is important because it forms the basis for follow-up operations in the workflow.
    - Comfy dtype: PARAMETER_INPUTS
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeInput5:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'base_conditioning_scale': ('FLOAT', {'default': 2.0, 'min': 0.25, 'max': 4.0, 'step': 0.25}), 'refiner_conditioning_scale': ('FLOAT', {'default': 2.0, 'min': 0.25, 'max': 4.0, 'step': 0.25}), 'style_prompt_power': ('FLOAT', {'default': 0.33, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'negative_style_power': ('FLOAT', {'default': 0.67, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'style_template': (SeargeParameterProcessor.STYLE_TEMPLATE, {'default': SeargeParameterProcessor.STYLE_TEMPLATE[0]})}, 'optional': {'inputs': ('PARAMETER_INPUTS',)}}
    RETURN_TYPES = ('PARAMETER_INPUTS',)
    RETURN_NAMES = ('inputs',)
    FUNCTION = 'mux'
    CATEGORY = 'Searge/_deprecated_/UI/Inputs'

    def mux(self, base_conditioning_scale, refiner_conditioning_scale, style_prompt_power, negative_style_power, style_template, inputs=None):
        if inputs is None:
            parameters = {}
        else:
            parameters = inputs
        parameters['base_conditioning_scale'] = base_conditioning_scale
        parameters['refiner_conditioning_scale'] = refiner_conditioning_scale
        parameters['style_prompt_power'] = style_prompt_power
        parameters['negative_style_power'] = negative_style_power
        parameters['style_template'] = style_template
        return (parameters,)
```