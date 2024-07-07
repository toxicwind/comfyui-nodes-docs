# Documentation
- Class name: CR_SetSwitchFromString
- Category: Comfyroll/Utils/Conditional
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SetSwitchFromString is designed to evaluate the given text input with a predefined string option and to determine an integer switch based on the matching item. It is a key decision-making component in the workflow that allows conditional branching or triggering specific actions based on input strings.

# Input types
## Required
- text
    - The 'text'parameter is the input text against which the node is compared. It is essential for providing the switch options. It plays a key role in determining the node output, as the matching process is at the core of the node function.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- switch_1
    - The `switch_1' parameter represents one of the switch options for which the node matches the input text. It is part of the decision-making process and affects the outcome on the basis of input.
    - Comfy dtype: STRING
    - Python dtype: str
- switch_2
    - The `switch_2' parameter is another potential switch option for node assessment. It is essential for expanding the range of conditions that node can respond to.
    - Comfy dtype: STRING
    - Python dtype: str
- switch_3
    - The `switch_3' parameter determines another additional switch option for its output as a node. It enhances the multifunctionality of nodes when processing input scenarios.
    - Comfy dtype: STRING
    - Python dtype: str
- switch_4
    - The `switch_4' parameter is the last switch option considered by the node. It completes the set of options for the node to perform its comparison and decision-making tasks.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- switch
    - The `switch' output represents the whole value determined by comparing the input text with the provided switch options. It represents the outcome of the node decision-making process.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - The `show_help' output provides URL links to node document pages and provides free guidance and information to users seeking to understand node functions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SetSwitchFromString:

    @classmethod
    def INPUT_TYPES(cls):
        methods = ['Fit', 'Crop']
        return {'required': {'text': ('STRING', {'multiline': False, 'default': '', 'forceInput': True})}, 'optional': {'switch_1': ('STRING', {'multiline': False, 'default': ''}), 'switch_2': ('STRING', {'multiline': False, 'default': ''}), 'switch_3': ('STRING', {'multiline': False, 'default': ''}), 'switch_4': ('STRING', {'multiline': False, 'default': ''})}}
    RETURN_TYPES = ('INT', 'STRING')
    RETURN_NAMES = ('switch', 'show_help')
    FUNCTION = 'set_switch'
    CATEGORY = icons.get('Comfyroll/Utils/Conditional')

    def set_switch(self, text, switch_1='', switch_2='', switch_3='', switch_4=''):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-set-switch-from-string'
        if text == switch_1:
            switch = 1
        elif text == switch_2:
            switch = 2
        elif text == switch_3:
            switch = 3
        elif text == switch_4:
            switch = 4
        else:
            pass
        return (switch, show_help)
```