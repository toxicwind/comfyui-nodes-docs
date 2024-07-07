# Documentation
- Class name: RemoveBackendData
- Category: InspirePack/Backend
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node is intended to manage and remove data stored in back-end caches and to ensure efficient memory use and data organization within the system.

# Input types
## Required
- key
    - The 'key' parameter is essential for identifying specific data in the backside cache. It determines which data are specified for deletion and the wildcard '*' is used to remove the entire cache.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- signal_opt
    - The `signal_opt' parameter is an optional input that can be used to provide additional commands or signals to nodes to enhance their adaptability and flexibility in various scenarios.
    - Comfy dtype: ANY
    - Python dtype: Any

# Output types
- signal
    - The `signal' output represents the result of a data deletion operation, which may be a status indicator or a response to an `signal_opt' input, ensuring effective communication between nodes and the system.
    - Comfy dtype: ANY
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class RemoveBackendData:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'key': ('STRING', {'multiline': False, 'placeholder': "Input data key ('*' = clear all)"})}, 'optional': {'signal_opt': (any_typ,)}}
    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ('signal',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Backend'
    OUTPUT_NODE = True

    def doit(self, key, signal_opt=None):
        global cache
        if key == '*':
            cache = {}
        elif key in cache:
            del cache[key]
        else:
            print(f'[Inspire Pack] RemoveBackendData: invalid data key {key}')
        return (signal_opt,)
```