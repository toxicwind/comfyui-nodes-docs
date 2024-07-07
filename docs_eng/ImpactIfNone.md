# Documentation
- Class name: ImpactIfNone
- Category: ImpactPack/Logic
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImpactIfNone node is designed to assess the existence of the input. It returns the input itself and a boolean value, indicating whether the input is available. This node is used as a condition check in the workflow to ensure that it continues to operate only when the required data are available.

# Input types
## Optional
- signal
    - The `signal' parameter is an optional input, which can be of any type. It is used to indicate that nodes will assess the data they exist. The significance of this parameter lies in its role as the subject of node conditions logic.
    - Comfy dtype: any_typ
    - Python dtype: Any
- any_input
    - The `any_input' parameter is another optional input, any type. It is a generic input for nodes that can be used to trigger the operation of the node or to provide additional context for the `signal' parameter.
    - Comfy dtype: any_typ
    - Python dtype: Any

# Output types
- signal_opt
    - The `signal_opt' output is the original input evaluated by the node. It represents data determined by node logic as present or non-existent.
    - Comfy dtype: any_typ
    - Python dtype: Any
- bool
    - The `bool' output is a boolean value that indicates whether the `any_input' parameter is provided. It serves as a clear instruction for downstream operations to decide whether to operate according to the availability of the input data.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactIfNone:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}, 'optional': {'signal': (any_typ,), 'any_input': (any_typ,)}}
    RETURN_TYPES = (any_typ, 'BOOLEAN')
    RETURN_NAMES = ('signal_opt', 'bool')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic'

    def doit(self, signal=None, any_input=None):
        if any_input is None:
            return (signal, False)
        else:
            return (signal, True)
```