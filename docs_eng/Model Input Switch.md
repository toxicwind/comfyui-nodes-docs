# Documentation
- Class name: WAS_Model_Input_Switch
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The model switching method is designed to select one of the two models according to the boolean conditions. It serves as a decision node in the workflow, or a flow of data to the model _a or model _b based on the boolean input. This node plays a key role in the logic of conditions in the model processing sequence.

# Input types
## Required
- model_a
    - The parameter `model_a'represents the first model that can be chosen for the node. It is essential for the decision-making process at the node, as it determines one of the possible outcomes when the boolean conditions are met.
    - Comfy dtype: MODEL
    - Python dtype: Union[torch.nn.Module, Any]
- model_b
    - The parameter `model_b'represents the second model that can be selected for the node. It plays an important role in the decision-making process, as it determines the alternative outcome when the conditions in the Boolean are not met.
    - Comfy dtype: MODEL
    - Python dtype: Union[torch.nn.Module, Any]
## Optional
- boolean
    - The parameter `boolean' acts as a switch to determine which model the node returns. It is important because it directly influences the output of the node and thus the next steps in the workflow.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- selected_model
    - Output `seleted_model' means a model selected according to a Boolean condition. It is a key output because it determines the next steps in the workflow.
    - Comfy dtype: MODEL
    - Python dtype: Union[torch.nn.Module, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Model_Input_Switch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model_a': ('MODEL',), 'model_b': ('MODEL',), 'boolean': ('BOOLEAN', {'forceInput': True})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'model_switch'
    CATEGORY = 'WAS Suite/Logic'

    def model_switch(self, model_a, model_b, boolean=True):
        if boolean:
            return (model_a,)
        else:
            return (model_b,)
```