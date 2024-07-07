# Documentation
- Class name: ImpactNodeSetMuteState
- Category: ImpactPack/Logic/_for_test
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImpactNodeSetMuteState method is designed to control the silent state of signal processing nodes. It allows users to activate or silence nodes according to the'set_state' parameters provided, thus affecting the flow of signals in the system.

# Input types
## Required
- signal
    - The `signal' parameter represents the input signal that the node will process. It is an essential part of the node operation because it determines the data that will be affected by a change in the silent state.
    - Comfy dtype: ANY
    - Python dtype: Any
- node_id
    - The `node_id' parameter specifies the only identifier for the node to change the silent state. The precise location of the target node in the network of multiple nodes is essential.
    - Comfy dtype: INT
    - Python dtype: int
- set_state
    - The'set_state' parameter determines whether the node should be set as active or silent. It is a key input, as it directly controls the operational status of the node in the system.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- signal_opt
    - The `signal_opt' output represents the signal that can be modified after the silent state changes. It represents the result of the node operation and reflects whether the signal has been processed or silenced.
    - Comfy dtype: ANY
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactNodeSetMuteState:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'signal': (any_typ,), 'node_id': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'set_state': ('BOOLEAN', {'default': True, 'label_on': 'active', 'label_off': 'mute'})}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic/_for_test'
    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ('signal_opt',)
    OUTPUT_NODE = True

    def doit(self, signal, node_id, set_state):
        PromptServer.instance.send_sync('impact-node-mute-state', {'node_id': node_id, 'is_active': set_state})
        return (signal,)
```