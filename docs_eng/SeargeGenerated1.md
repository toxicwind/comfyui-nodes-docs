# Documentation
- Class name: SeargeGenerated1
- Category: Searge/_deprecated_/UI/Generated
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

This node is a multi-routine reuser that directs their paths to specific operations and styles specified by the input.

# Input types
## Required
- parameters
    - This parameter saves key values that play a key role in the operation and style selection of the indicator nodes and in determining the behaviour and output of the nodes.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Output types
- parameters
    - The output retains input parameters and provides a basis for follow-up operations.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]
- operation_selector
    - This output identifies the operation selected and guides the process of the node.
    - Comfy dtype: str
    - Python dtype: str
- prompt_style_selector
    - This output represents the selected hint style that affects the presentation and formatting of node results.
    - Comfy dtype: str
    - Python dtype: str
- prompt_style_group
    - This output represents a group of hint styles that influences the overall aesthetics and structure of the node output.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeGenerated1:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'parameters': ('PARAMETERS',)}}
    RETURN_TYPES = ('PARAMETERS', 'INT', 'INT', 'INT')
    RETURN_NAMES = ('parameters', 'operation_selector', 'prompt_style_selector', 'prompt_style_group')
    FUNCTION = 'demux'
    CATEGORY = 'Searge/_deprecated_/UI/Generated'

    def demux(self, parameters):
        operation_selector = parameters['operation_selector']
        prompt_style_selector = parameters['prompt_style_selector']
        prompt_style_group = parameters['prompt_style_group']
        return (parameters, operation_selector, prompt_style_selector, prompt_style_group)
```