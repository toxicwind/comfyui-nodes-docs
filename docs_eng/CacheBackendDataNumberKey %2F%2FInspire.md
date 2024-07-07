# Documentation
- Class name: CacheBackendDataNumberKey
- Category: InspirePack/Backend
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node is designed to manage and store data in the cache system, using the only numeric key for identification and retrieval. It plays a vital role in maintaining the efficiency and organization of data streams in back-end infrastructure.

# Input types
## Required
- key
    - The `key' parameter is essential for the operation of the node because it is the only identifying data in the cache. It is a key component that affects the ability of the node to store and retrieve information accurately.
    - Comfy dtype: INT
    - Python dtype: int
- data
    - The `data' parameter represents the actual content of the cache. It is the main input for node processing and storage, ensuring that the information is readily available.
    - Comfy dtype: ANY
    - Python dtype: Any
## Optional
- tag
    - The `tag' parameter, as a data descriptor, provides a short description that can be used to classify or filter cache information. It enhances the function of nodes by providing a more efficient way to organize and access data.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- data opt
    - Output 'data opt'means the raw data returned during the cache and any additional information or modifications that may occur. This ensures that the user receives the intended complete data set.
    - Comfy dtype: ANY
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class CacheBackendDataNumberKey:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'key': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'tag': ('STRING', {'multiline': False, 'placeholder': 'Tag: short description'}), 'data': (any_typ,)}}
    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ('data opt',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Backend'
    OUTPUT_NODE = True

    def doit(self, key, tag, data):
        global cache
        cache[key] = (tag, (False, data))
        return (data,)
```