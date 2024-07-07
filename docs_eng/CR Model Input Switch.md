# Documentation
- Class name: CR_ModelInputSwitch
- Category: Comfyroll/Utils/Logic
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ModelInputSwitch is designed to select between the two models provided on the basis of input values. It plays a key role in simplifying the model selection process in the workflow, allowing conditions modelling programmes to be performed without complex branch logic.

# Input types
## Required
- Input
    - The 'Input'parameter is essential for determining which model to select. It guides the logic of the node to select'model1'or'model2'according to its value, thus influencing the output of the node.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- model1
    - The'model1 'parameter represents the first model you can select. When the 'Input 'parameter is set to 1, it is an optional input that becomes important.
    - Comfy dtype: MODEL
    - Python dtype: Any
- model2
    - The `model2'parameter represents the second model that node can choose. When the `Input'parameter is not equal to 1, it is taken into account, in which case the output is decided.
    - Comfy dtype: MODEL
    - Python dtype: Any

# Output types
- MODEL
    - The `MODEL'output is a model based on the 'Input'parameter selection. It represents the outcome of the decision-making process at the node on which model to provide.
    - Comfy dtype: MODEL
    - Python dtype: Any
- show_help
    - The'show_help'output provides URLs that point to node documents, providing additional information and guidance on how to use nodes effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ModelInputSwitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': ('INT', {'default': 1, 'min': 1, 'max': 2})}, 'optional': {'model1': ('MODEL',), 'model2': ('MODEL',)}}
    RETURN_TYPES = ('MODEL', 'STRING')
    RETURN_NAMES = ('MODEL', 'show_help')
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Utils/Logic')

    def switch(self, Input, model1=None, model2=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Logic-Nodes#cr-model-input-switch'
        if Input == 1:
            return (model1, show_help)
        else:
            return (model2, show_help)
```