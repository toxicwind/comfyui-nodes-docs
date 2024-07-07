# Documentation
- Class name: CR_ClipInputSwitch
- Category: Comfyroll/Utils/Logic
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ClipInputSwitch is a practical tool node designed to provide a conditional switch mechanism between two input clips. It operates on the basis of individual input parameters, allowing users to choose between the two provided clips depending on the value of the input. The function of the node is focused on its ability to simplify workflows through intelligent selection of the appropriate clips for further processing or presentation.

# Input types
## Required
- Input
    - The `Input' parameter is essential for the operation of the node because it determines which clips will be returned. When the `Input' value is 1, choose `clip1'; otherwise, `clip2'. The function of this parameter is essential when determining node output according to the user's particular needs.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- clip1
    - The `clip1' parameter is an optional input that represents the first clip that a node can choose. When the `Input' parameter is set to 1, it plays an important role in further processing, as it is the output selected.
    - Comfy dtype: CLIP
    - Python dtype: Clip
- clip2
    - The `clip2' parameter is another optional input, representing the second clip that the node can choose. When the `Input' parameter is not 1, its importance becomes apparent, making `clip2' an output for follow-up operations.
    - Comfy dtype: CLIP
    - Python dtype: Clip

# Output types
- CLIP
    - The 'CLIP'output is based on the value of the 'Input'parameter. It is the main output of the node and is used for further video processing or presentation.
    - Comfy dtype: CLIP
    - Python dtype: Clip
- show_help
    - The'show_help' output provides a URL link to the node document to provide additional guidance. It is a secondary output that provides users with easy access to more information about the use and functionality of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ClipInputSwitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': ('INT', {'default': 1, 'min': 1, 'max': 2})}, 'optional': {'clip1': ('CLIP',), 'clip2': ('CLIP',)}}
    RETURN_TYPES = ('CLIP', 'STRING')
    RETURN_NAMES = ('CLIP', 'show_help')
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Utils/Logic')

    def switch(self, Input, clip1=None, clip2=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Logic-Nodes#cr-clip-input-switch'
        if Input == 1:
            return (clip1, show_help)
        else:
            return (clip2, show_help)
```