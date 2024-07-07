# Documentation
- Class name: CR_TextInputSwitch4way
- Category: Logic
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_TextInputSwitch4way is a practical tool node designed to manage conditional text output based on input selection. It allows the selection of one of the four text strings provided, thereby promoting text-based streams of information in the workflow. Node determines the text string to be exported by assessing the 'Input'parameter, thus enabling a dynamic content presentation.

# Input types
## Required
- Input
    - The 'Input'parameter is essential because it determines which of the four text string will be selected for output. As a decision-making factor within a node, it guides the flow of text information according to its overall value.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- text1
    - The 'text1 'parameter is one of the optional text inputes that nodes can use. It represents a text string that is exported when 'Input' is set to 1, allowing custom content to be provided according to user-defined criteria.
    - Comfy dtype: STRING
    - Python dtype: str
- text2
    - The 'text2 'parameter is another optional text input for the node. Use 'Input'when set to 2 to ensure that node can provide a different text string as part of the output of the condition.
    - Comfy dtype: STRING
    - Python dtype: str
- text3
    - The 'text3' parameter is entered as another optional text for the node. When 'Input' is set to 3 it becomes relevant so that the node can display a different text segment in the workflow.
    - Comfy dtype: STRING
    - Python dtype: str
- text4
    - The 'text4' parameter is the last optional text input for the node. When the 'Input'set to 4 is selected for output, completes the set of conditional text options available in the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- STRING
    - The main output of the node is a text string determined by the 'Input'parameter. It represents the selected text based on user selection and provides a clear and direct result of the node operation.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - Secondary output'show_help' provides URL links to node document pages. This is useful for users seeking additional information or guidance on how to use nodes effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_TextInputSwitch4way:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': ('INT', {'default': 1, 'min': 1, 'max': 4})}, 'optional': {'text1': ('STRING', {'forceInput': True}), 'text2': ('STRING', {'forceInput': True}), 'text3': ('STRING', {'forceInput': True}), 'text4': ('STRING', {'forceInput': True})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Utils/Logic')

    def switch(self, Input, text1=None, text2=None, text3=None, text4=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Logic-Nodes#cr-text-input-switch-4-way'
        if Input == 1:
            return (text1, show_help)
        elif Input == 2:
            return (text2, show_help)
        elif Input == 3:
            return (text3, show_help)
        else:
            return (text4, show_help)
```