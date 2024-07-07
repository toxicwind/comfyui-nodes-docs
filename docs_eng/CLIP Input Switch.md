# Documentation
- Class name: WAS_CLIP_Input_Switch
- Category: WAS Suite/Logic
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

Method `clip_switch'is designed to select conditionally one of the two CLIP objects provided on the basis of a boolean sign. It acts as a logical switch in the workflow and guides the direction of the data stream according to the authenticity of the boolean value.

# Input types
## Required
- clip_a
    - The first CLIP object selected by the condition when the boolean parameter is true. It plays a key role in the decision-making process at node, determining the output according to the state of the Boolean flag.
    - Comfy dtype: CLIP
    - Python dtype: Union[torch.Tensor, comfy.sd.CLIP]
- clip_b
    - The second CLIP object that is selected by conditions when the boolean parameter is false. It is essential in the operation of the node to provide an alternative output when the boolean condition is not fulfilled.
    - Comfy dtype: CLIP
    - Python dtype: Union[torch.Tensor, comfy.sd.CLIP]
## Optional
- boolean
    - Determines the boolean mark of which CLIP object to return. It is a key parameter because it directly affects the output selection logic of the node.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- selected_clip
    - The output of the node is a single CLIP object, which can be `clip_a'or `clip_b'according to the value of the boolean parameter. This output is important because it represents the result of the node condition logic.
    - Comfy dtype: CLIP
    - Python dtype: Union[torch.Tensor, comfy.sd.CLIP]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_CLIP_Input_Switch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'clip_a': ('CLIP',), 'clip_b': ('CLIP',), 'boolean': ('BOOLEAN', {'forceInput': True})}}
    RETURN_TYPES = ('CLIP',)
    FUNCTION = 'clip_switch'
    CATEGORY = 'WAS Suite/Logic'

    def clip_switch(self, clip_a, clip_b, boolean=True):
        if boolean:
            return (clip_a,)
        else:
            return (clip_b,)
```