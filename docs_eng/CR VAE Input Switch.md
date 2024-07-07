# Documentation
- Class name: CR_VAEInputSwitch
- Category: Comfyroll/Utils/Logic
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_VAEInputSwitch is a node that is used to enter conditionally by route between two different VAE models according to a given choice. It operates by assessing 'Input' parameters and directing the process accordingly, thus achieving seamless integration and switching between two different VAE configurations.

# Input types
## Required
- Input
    - The `Input'parameter plays a key role in determining which VAE model will be used at which node. As a switch, it determines the flow of data between available options, of which `1' corresponds to VAE1, `2' corresponds to VAE2.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- VAE1
    - The 'VAE1'parameter indicates the first VAE model that node can choose. When the 'Input'parameter is set to '1'it is an optional input that allows the use of this particular model in the workflow.
    - Comfy dtype: VAE
    - Python dtype: VAE model object
- VAE2
    - The 'VAE2'parameter represents the second VAE model that node can choose. When the 'Input'parameter is set to '2'it is an optional input that allows the alternative model to be used in this process.
    - Comfy dtype: VAE
    - Python dtype: VAE model object

# Output types
- VAE
    - The `VAE'output provides the selected VAE model based on the `Input'parameter, allowing further processing or analysis in downstream nodes.
    - Comfy dtype: VAE
    - Python dtype: VAE model object
- show_help
    - The'show_help'output provides a URL link to the document page to obtain additional guidance or information about node functions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_VAEInputSwitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': ('INT', {'default': 1, 'min': 1, 'max': 2})}, 'optional': {'VAE1': ('VAE', {'forceInput': True}), 'VAE2': ('VAE', {'forceInput': True})}}
    RETURN_TYPES = ('VAE', 'STRING')
    RETURN_NAMES = ('VAE', 'show_help')
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Utils/Logic')

    def switch(self, Input, VAE1=None, VAE2=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Logic-Nodes#cr-vae-input-switch'
        if Input == 1:
            return (VAE1, show_help)
        else:
            return (VAE2, show_help)
```