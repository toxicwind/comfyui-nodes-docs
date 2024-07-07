# Documentation
- Class name: CR_TextInputSwitch
- Category: Comfyroll/Utils/Logic
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_TextInputSwitch node is designed to select conditions that facilitate text input according to the given integer. It provides a simple mechanism for switching between two text inputes, which is particularly useful in scenarios where different text output is selected according to input values.

# Input types
## Required
- Input
    - The 'Input' parameter is essential because it determines which text to choose. It works within the integer range, and the input of one corresponds to 'text1' and 2 corresponds to 'text2', thereby controlling the output of the node.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- text1
    - The 'text1'parameter is an optional string input that indicates the text to be returned when the 'Input'parameter is set to 1. It plays an important role in defining the output of one of the possible input conditions.
    - Comfy dtype: STRING
    - Python dtype: str
- text2
    - The 'text2'parameter is another optional string input, which indicates the text to be returned when the 'Input'parameter is set to 2. It supplements the 'text1' parameter by providing alternative text output for different input conditions.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- STRING
    - The main output of the node is a string, which, according to the value of the 'Input' parameter, should be 'text1' or 'text2'. This output is important because it represents the text selected after the condition is changed.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The'show_help' output provides a URL link to the node document page, allowing users easy access to more information and guidance on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_TextInputSwitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': ('INT', {'default': 1, 'min': 1, 'max': 2})}, 'optional': {'text1': ('STRING', {'forceInput': True}), 'text2': ('STRING', {'forceInput': True})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Utils/Logic')

    def switch(self, Input, text1=None, text2=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Logic-Nodes#cr-text-input-switch'
        if Input == 1:
            return (text1, show_help)
        else:
            return (text2, show_help)
```