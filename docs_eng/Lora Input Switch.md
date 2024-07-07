# Documentation
- Class name: WAS_Lora_Input_Switch
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

This node serves as a conditional switch in the WAS Suite, selecting and forwarding a group of two sets of inputs according to the state of the Boolean parameters.

# Input types
## Required
- model_a
    - The first model input is essential to the operation of the node, representing one of the two possible data streams that Boolean switches can select.
    - Comfy dtype: MODEL
    - Python dtype: Any
- clip_a
    - The first clip input is part of the first data stream, and if the boolean parameter is true, it is selected to influence the output of the node.
    - Comfy dtype: CLIP
    - Python dtype: Any
- model_b
    - The second model input represents an alternative data stream that is selected if the boolean parameter is false.
    - Comfy dtype: MODEL
    - Python dtype: Any
- clip_b
    - The second clip input is part of an alternative data stream whose selection is determined by the state of the Boolean parameter.
    - Comfy dtype: CLIP
    - Python dtype: Any
- boolean
    - The Boolean parameter is the control signal for the switch and determines which group of inputs will be forwarded to the node.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- output
    - The output of the node is determined by the Boolean parameter, either by forwarding the first group input or by forwarding the alternative group input.
    - Comfy dtype: MODEL,CLIP
    - Python dtype: Tuple[Any, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Lora_Input_Switch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model_a': ('MODEL',), 'clip_a': ('CLIP',), 'model_b': ('MODEL',), 'clip_b': ('CLIP',), 'boolean': ('BOOLEAN', {'forceInput': True})}}
    RETURN_TYPES = ('MODEL', 'CLIP')
    FUNCTION = 'lora_input_switch'
    CATEGORY = 'WAS Suite/Logic'

    def lora_input_switch(self, model_a, clip_a, model_b, clip_b, boolean=True):
        if boolean:
            return (model_a, clip_a)
        else:
            return (model_b, clip_b)
```