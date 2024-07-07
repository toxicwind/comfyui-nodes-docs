# Documentation
- Class name: CR_ConditioningInputSwitch
- Category: Comfyroll/Utils/Logic
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ConditioningInputSwitch is designed to enter a data stream according to conditions. It allows one of the two conditions to be selected according to the value of the 'Input'parameter. This node plays a key role in a complex workflow that guides the flow of data and achieves the logic of conditions without using an embedded structure.

# Input types
## Required
- Input
    - The 'Input'parameter is essential for determining which condition data is to be selected. It is a switch, with a value of 1 choosing 'conventioning 1', and any other value choosing 'conventioning 2'. This parameter directly influences the output of nodes and promotes the decision-making process in the workflow.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- conditioning1
    - The 'convention1 'parameter is one of the optional inputes that will be used when the 'Input 'parameter equals 1. It represents a set of conditional data that can be used when specified conditions are met, allowing seamless integration of information specific to the context into the workflow.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- conditioning2
    - The 'convention2 'parameter is an alternative input to 'convention1 ', which is called when the 'Input 'parameter is not equal to 1. It allows different conditions to be provided and ensures the flexibility and adaptability of nodes in different scenarios.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any

# Output types
- CONDITIONING
    - The output 'conditioning 'is conditional data based on the 'Input'parameter value selection. It represents the result of node condition logic and provides the necessary information for the next steps in the workflow.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- show_help
    - The'show_help' output provides a URL link to the node document, allowing users to quickly access additional information and guidance on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ConditioningInputSwitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': ('INT', {'default': 1, 'min': 1, 'max': 2})}, 'optional': {'conditioning1': ('CONDITIONING',), 'conditioning2': ('CONDITIONING',)}}
    RETURN_TYPES = ('CONDITIONING', 'STRING')
    RETURN_NAMES = ('CONDITIONING', 'show_help')
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Utils/Logic')

    def switch(self, Input, conditioning1=None, conditioning2=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Logic-Nodes#cr-conditioning-input-switch'
        if Input == 1:
            return (conditioning1, show_help)
        else:
            return (conditioning2, show_help)
```