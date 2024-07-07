# Documentation
- Class name: CR_ModelAndCLIPInputSwitch
- Category: Comfyroll/Utils/Logic
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ModelAndCLIPInputSwitch is a node used to select two sets of models and CLIP input based on binary input. As a decision node, it allows users to choose between two different models and their corresponding CLIP expression. The function of the node is essential in the context of the condition logic needed to determine which model and CLIP are to be used in subsequent processing steps.

# Input types
## Required
- Input
    - The 'Input'parameter is a key binary selection that determines which models and CLIPs are to be used in the node. It directly influences the node's decision-making process and activates the condition-based input route according to its value.
    - Comfy dtype: INT
    - Python dtype: int
- model1
    - The'model1 'parameter represents the first model input used when the 'Input 'parameter is set to 1. It plays an important role in the operation of the node, as it defines the model to be processed when the first condition is met.
    - Comfy dtype: MODEL
    - Python dtype: Any
- clip1
    - The 'clip1'parameter corresponds to the CLIP input associated with the first model. It is the key to node implementation, as it provides the CLIP expression that is needed when selecting the first model.
    - Comfy dtype: CLIP
    - Python dtype: Any
- model2
    - The'model2 'parameter means using the second model input when the 'Input'parameter is set to 2. It is essential for the function of the node, as it determines the model to be processed when the second condition is met.
    - Comfy dtype: MODEL
    - Python dtype: Any
- clip2
    - The 'clip2' parameter is a CLIP input that matches the second model. It is an integral part of the node function because it provides the CLIP that is needed when selecting the second model.
    - Comfy dtype: CLIP
    - Python dtype: Any

# Output types
- MODEL
    - The " MODEL " output provides the selected model based on the 'Input'parameter. It is a key component of the node output and ensures that the appropriate model is forwarded for further processing.
    - Comfy dtype: MODEL
    - Python dtype: Any
- CLIP
    - The 'CLIP'output provides the CLIP that corresponds to the selected model. It plays an important role in ensuring that node output is comprehensive, including the model and its associated CLIP.
    - Comfy dtype: CLIP
    - Python dtype: Any
- show_help
    - The'show_help'output provides a URL link to the node document page, allowing users easy access to additional information and guidance on how to use node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ModelAndCLIPInputSwitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': ('INT', {'default': 1, 'min': 1, 'max': 2}), 'model1': ('MODEL',), 'clip1': ('CLIP',), 'model2': ('MODEL',), 'clip2': ('CLIP',)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'STRING')
    RETURN_NAMES = ('MODEL', 'CLIP', 'show_help')
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Utils/Logic')

    def switch(self, Input, clip1, clip2, model1, model2):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Logic-Nodes#cr-switch-model-and-clip'
        if Input == 1:
            return (model1, clip1, show_help)
        else:
            return (model2, clip2, show_help)
```