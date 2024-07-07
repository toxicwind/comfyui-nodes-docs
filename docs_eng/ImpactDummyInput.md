# Documentation
- Class name: ImpactDummyInput
- Category: ImpactPack/Debug
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImpactDummyInput node 'doit' method acts as a placeholder function in the ImpactPack/Debug category. It is designed to perform a simple operation that is usually used for testing or debugging purposes without affecting the main workflow.

# Input types
## Required
- required
    - The'required' parameter is a dictionary that specifies the necessary input for the ImpactDummy Input node. This is essential for the operation of the node, because it determines the data that must be provided so that the 'doit' method can be correctly implemented.
    - Comfy dtype: Dict[str, any_typ]
    - Python dtype: Dict[str, any_typ]

# Output types
- output
    - The 'output' parameter represents the result of the 'doit' method, in which case it is a simple string indicating the result of the virtual operation. It is important because it provides direct feedback on node execution during the debugging process.
    - Comfy dtype: str
    - Python dtype: Tuple[str, ...]

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactDummyInput:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}}
    CATEGORY = 'ImpactPack/Debug'
    RETURN_TYPES = (any_typ,)
    FUNCTION = 'doit'

    def doit(self):
        return ('DUMMY',)
```