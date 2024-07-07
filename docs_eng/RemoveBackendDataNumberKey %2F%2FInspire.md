# Documentation
- Class name: RemoveBackendDataNumberKey
- Category: DataProcessing
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node is intended to remove data entries associated with specific numerical keys from the back end cache, ensure data integrity and optimize storage space.

# Input types
## Required
- key
    - The `key' parameter is essential to identify the exact data entry that you want to remove from the cache. It is the only identifier for the target data.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- signal_opt
    - The `signal_opt' parameter provides flexibility during the deletion process to specify additional options for operations.
    - Comfy dtype: ANY
    - Python dtype: Any

# Output types
- signal_opt
    - The `signal_opt' output reflects any additional options or signals provided as input, maintaining the integrity of the operational context.
    - Comfy dtype: ANY
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class RemoveBackendDataNumberKey(RemoveBackendData):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'key': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}, 'optional': {'signal_opt': (any_typ,)}}

    def doit(self, key, signal_opt=None):
        global cache
        if key in cache:
            del cache[key]
        else:
            print(f'[Inspire Pack] RemoveBackendDataNumberKey: invalid data key {key}')
        return (signal_opt,)
```