# Documentation
- Class name: CR_LatentInputSwitch
- Category: Comfyroll/Utils/Logic
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_LatentInputSwitch node is designed to manage the choice between the two potential states according to input values. It is a decision-making component in the workflow that allows data to be conditioned through the system. The function of the node is essential in a scenario that requires dynamic selection of different potential expressions.

# Input types
## Required
- Input
    - The `Input' parameter is essential because it determines which potential state the node will choose. It is an integer number, which should be between one and two, with one corresponding to the first potential state and two corresponding to the second. This decision variable is essential for the operation of the node because it directly affects the output selection.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- latent1
    - The `latet1' parameter represents the first potential state that a node can choose. It is optional and becomes important when the `Input' parameter is set to 1. In this case, `latet1' is the output that the node returns.
    - Comfy dtype: LATENT
    - Python dtype: Union[torch.Tensor, None]
- latent2
    - The `latent2' parameter represents the second potential state of choice. It is also optional and is considered when the `Input' parameter is set to 2, resulting in `latent2' being an output returned by node.
    - Comfy dtype: LATENT
    - Python dtype: Union[torch.Tensor, None]

# Output types
- LATENT
    - The `LATENT' output represents the potential state selected on the basis of the `Input' parameter. It is the main output of the node and carries the potential data selected from the `latent1' or `latent2' conditions.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- show_help
    - The'show_help' output provides a document page with a URL link to the node for more help. It is included as a secondary output to guide users in seeking more information about the use and function of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_LatentInputSwitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': ('INT', {'default': 1, 'min': 1, 'max': 2})}, 'optional': {'latent1': ('LATENT',), 'latent2': ('LATENT',)}}
    RETURN_TYPES = ('LATENT', 'STRING')
    RETURN_NAMES = ('LATENT', 'show_help')
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Utils/Logic')

    def switch(self, Input, latent1=None, latent2=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Logic-Nodes#cr-latent-input-switch'
        if Input == 1:
            return (latent1, show_help)
        else:
            return (latent2, show_help)
```