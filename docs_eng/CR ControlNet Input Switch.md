# Documentation
- Class name: CR_ControlNetInputSwitch
- Category: Comfyroll/Utils/Logic
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ControlNetInputSwitch is designed to provide a condition switch mechanism for controlling the network. It allows users to choose between the two control networks based on input values, thus facilitating the route of data to the required network path.

# Input types
## Required
- Input
    - The `Input' parameter is essential for determining which control network to use. It determines the implementation process within the node by specifying the index of the control network to be selected.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- control_net1
    - The 'control_net1' parameter represents the first control network that can be selected. When the 'Input' parameter is set to 1, it plays an important role in decision-making at the node.
    - Comfy dtype: CONTROL_NET
    - Python dtype: str
- control_net2
    - The 'control_net2' parameter represents the second control network that you can select. When the 'Input' parameter is set to 2, it becomes relevant and guides the choice of the node.
    - Comfy dtype: CONTROL_NET
    - Python dtype: str

# Output types
- CONTROL_NET
    - The `CONTROL_NET' output provides a control network selected on the basis of input values. It is the main output, moving node decisions forward into the workflow.
    - Comfy dtype: CONTROL_NET
    - Python dtype: str
- show_help
    - The'show_help' output is a URL that provides additional information and guidance on how to use nodes effectively. It is a secondary output that provides users with access to node documents.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ControlNetInputSwitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': ('INT', {'default': 1, 'min': 1, 'max': 2}), 'control_net1': ('CONTROL_NET',), 'control_net2': ('CONTROL_NET',)}, 'optional': {'control_net1': ('CONTROL_NET',), 'control_net2': ('CONTROL_NET',)}}
    RETURN_TYPES = ('CONTROL_NET', 'STRING')
    RETURN_NAMES = ('CONTROL_NET', 'show_help')
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Utils/Logic')

    def switch(self, Input, control_net1=None, control_net2=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Logic-Nodes#cr-controlnet-input-switch'
        if Input == 1:
            return (control_net1, show_help)
        else:
            return (control_net2, show_help)
```