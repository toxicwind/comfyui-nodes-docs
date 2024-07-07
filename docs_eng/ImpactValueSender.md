# Documentation
- Class name: ImpactValueSender
- Category: ImpactPack/Logic
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImpactValueSender node is intended to transmit the impact values to the specified server. It is a key component of the data stream, ensuring that the impact values are effectively communicated for further processing or analysis.

# Input types
## Required
- value
    - The "value" parameter is essential for the operation of the node because it represents the impact value to be sent. It plays a central role in the function of the node and determines the data to be transmitted.
    - Comfy dtype: any_typ
    - Python dtype: Any
## Optional
- link_id
    - The " link_id " parameter is an optional identifier for connection. It helps to distinguish between different data streams or connections and enhances the ability of nodes to manage and organize the transmission process.
    - Comfy dtype: INT
    - Python dtype: int
- signal_opt
    - The'signal_opt' parameter is an optional input that can be used to modify the behaviour of the nodes. It provides additional control over the transmission process and allows customization according to specific needs.
    - Comfy dtype: any_typ
    - Python dtype: Any

# Output types
- signal
    - The " signal" output represents the result of the transmission process. It is a key indicator of the successful operation of the node that can be used for further processing or as feedback in the system.
    - Comfy dtype: any_typ
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactValueSender:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'value': (any_typ,), 'link_id': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1})}, 'optional': {'signal_opt': (any_typ,)}}
    OUTPUT_NODE = True
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic'
    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ('signal',)

    def doit(self, value, link_id=0, signal_opt=None):
        PromptServer.instance.send_sync('value-send', {'link_id': link_id, 'value': value})
        return (signal_opt,)
```