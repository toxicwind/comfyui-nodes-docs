# Documentation
- Class name: SeargeStylePreprocessor
- Category: Searge/_deprecated_/UI
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

SeergeStylePreprocessor aims to process and operate style-related input in processing processes to ensure that style information is correctly interpreted and ready for subsequent phases.

# Input types
## Required
- inputs
    - This parameter is the main source of data for pre-processing operations. It contains a variety of inputs that are essential for the proper functioning of nodes and for producing meaningful results.
    - Comfy dtype: DICT[str, Any]
    - Python dtype: Dict[str, Any]
- active_style_name
    - This parameter is essential for entering the central recognition activity style. It guides pre-processing by specifying which style definitions should be applied.
    - Comfy dtype: STRING
    - Python dtype: str
- style_definitions
    - The parameter contains definitions of different styles that may be used in pre-processing. It is important because it determines how styles are interpreted and converted.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- inputs
    - The processed input returns with the correct preparation and structure of the style information, allowing seamless integration to the next phase of the treatment stream.
    - Comfy dtype: DICT[str, Any]
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeStylePreprocessor:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'inputs': ('PARAMETER_INPUTS',), 'active_style_name': ('STRING', {'multiline': False, 'default': ''}), 'style_definitions': ('STRING', {'multiline': True, 'default': '[unfinished work in progress]'})}}
    RETURN_TYPES = ('PARAMETER_INPUTS',)
    RETURN_NAMES = ('inputs',)
    FUNCTION = 'process'
    CATEGORY = 'Searge/_deprecated_/UI'

    def process(self, inputs, active_style_name, style_definitions):
        if inputs is None:
            inputs = {}
        style_template = inputs['style_template']
        if style_template is None or style_template != SeargeParameterProcessor.STYLE_TEMPLATE[1]:
            return (inputs,)
        return (inputs,)
```