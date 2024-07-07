# Documentation
- Class name: ImpactRemoteInt
- Category: ImpactPack/Logic/_for_test
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

This node is used as a test tool in the ImpactPack logical package to assess and demonstrate the functions of remote interaction through defined interfaces.

# Input types
## Required
- node_id
    - The node_id parameter is essential for the sole identification node in the system, which makes it possible to communicate and process the target.
    - Comfy dtype: INT
    - Python dtype: int
- widget_name
    - The widget_name parameter specifies the name of the little widget to interact with and points the operation of the node to the right interface.
    - Comfy dtype: STRING
    - Python dtype: str
- value
    - The value parameter is kept at the core of the node function for the data to be processed or transmitted during the remote interaction.
    - Comfy dtype: INT
    - Python dtype: int

# Output types

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactRemoteInt:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'node_id': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'widget_name': ('STRING', {'multiline': False}), 'value': ('INT', {'default': 0, 'min': -18446744073709551615, 'max': 18446744073709551615})}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic/_for_test'
    RETURN_TYPES = ()
    OUTPUT_NODE = True

    def doit(self, **kwargs):
        return {}
```