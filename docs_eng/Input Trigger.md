# Documentation
- Class name: Trigger
- Category: 😺dzNodes
- Output node: True
- Repo Ref: https://github.com/chflame163/ComfyUI_MSSpeech_TTS

The node serves as a conditionality door, assessing inputs to determine whether they meet the specified conditions and thus controlling the data flow system.

# Input types
## Required
- always_true
    - A boolean sign, when true, directly triggers the action of the node. It is a key parameter, because it represents the main condition for node activation.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- anything
    - An optional input, if available, can help to trigger nodes, adding flexibility to the conditions required to activate them.
    - Comfy dtype: ANY
    - Python dtype: Any

# Output types
- ret
    - The results of the nodal assessment indicate whether the conditions for activation have been met.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class Trigger:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'always_true': ('BOOLEAN', {'default': False})}, 'optional': {'anything': (any, {})}}
    RETURN_TYPES = ('BOOLEAN',)
    FUNCTION = 'check_input'
    OUTPUT_NODE = True
    CATEGORY = '😺dzNodes'

    def check_input(self, always_true, anything=None):
        ret = False
        if always_true or anything is not None:
            ret = True
        print(f'# 😺dzNodes: Input Trigger: {ret}')
        return (ret,)
```