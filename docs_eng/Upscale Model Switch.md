# Documentation
- Class name: WAS_Upscale_Model_Input_Switch
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The method 'upscale_model_switch'is designed to provide a condition selection mechanism to select one of two magnification models based on the Boolean sign. As a logical switch, it determines the model to be used for image magnification operations, thereby increasing the flexibility of the system.

# Input types
## Required
- upscale_model_a
    - The parameter 'upscale_model_a'is the first magnification model used for selection. It is essential in the decision-making process because it is one of two models that can be selected on the basis of Boolean marker values.
    - Comfy dtype: UPSCALE_MODEL
    - Python dtype: Union[torch.nn.Module, Any]
- upscale_model_b
    - The parameter 'upscale_model_b' represents the second magnification model, which is an alternative option for nodes. When the Boolean flag is set to False, it plays a key role because it is selected as image magnification.
    - Comfy dtype: UPSCALE_MODEL
    - Python dtype: Union[torch.nn.Module, Any]
## Optional
- boolean
    - The parameter 'boolean', as the control sign, affects the node to determine which magnification model to return. When set to True, select 'upscale_model_a'; when it is False, select 'upscale_model_b'.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- selected_upscale_model
    - Output'selected_upscale_model' means a zoom model selected according to the Boolean logo. It is important because it determines the subsequent image magnification process.
    - Comfy dtype: UPSCALE_MODEL
    - Python dtype: Union[torch.nn.Module, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Upscale_Model_Input_Switch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'upscale_model_a': ('UPSCALE_MODEL',), 'upscale_model_b': ('UPSCALE_MODEL',), 'boolean': ('BOOLEAN', {'forceInput': True})}}
    RETURN_TYPES = ('UPSCALE_MODEL',)
    FUNCTION = 'upscale_model_switch'
    CATEGORY = 'WAS Suite/Logic'

    def upscale_model_switch(self, upscale_model_a, upscale_model_b, boolean=True):
        if boolean:
            return (upscale_model_a,)
        else:
            return (upscale_model_b,)
```