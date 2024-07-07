# Documentation
- Class name: ImpactRemoteBoolean
- Category: ImpactPack/Logic/_for_test
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

This node, as a logical component for remote execution, can transmit and evaluate boolean values in distributed systems. It is designed to assess the authenticity of input conditions and disseminate the results to other nodes, playing a key role in controlling data flows and executing paths.

# Input types
## Required
- node_id
    - The node_id parameter is essential for the sole identification node in the system. It ensures that the correct node receives input and that the result is accurately associated with the correct example.
    - Comfy dtype: INT
    - Python dtype: int
- widget_name
    - The widget_name parameter is essential for the user interface because it marks the input field for the boolean value. This parameter affects the user's interaction with the system and the clarity of the interface.
    - Comfy dtype: STRING
    - Python dtype: str
- value
    - The value parameter is the core element of this node, representing the boolean conditions to be assessed. It is the main input that drives node functions and subsequent actions.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactRemoteBoolean:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'node_id': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'widget_name': ('STRING', {'multiline': False}), 'value': ('BOOLEAN', {'default': True, 'label_on': 'True', 'label_off': 'False'})}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic/_for_test'
    RETURN_TYPES = ()
    OUTPUT_NODE = True

    def doit(self, **kwargs):
        return {}
```