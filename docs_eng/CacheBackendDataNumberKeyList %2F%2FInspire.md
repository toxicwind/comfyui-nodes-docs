# Documentation
- Class name: CacheBackendDataNumberKeyList
- Category: InspirePack/Backend
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The CacheBackendDataNumberKeyList node is designed to efficiently manage and store data associated with numeric keys in backend systems. As a key component of the cache mechanism, it ensures quick access to frequently used data without the need for redundant retrieval processes.

# Input types
## Required
- key
    - The "key" parameter is the numeric identifier used to quote and access the data stored in the cache. It plays a key role in the operation of the node, as it directly affects the efficiency and accuracy of data retrieval.
    - Comfy dtype: INT
    - Python dtype: int
- tag
    - The Tag parameter is a string that provides a short description or label of the data associated with the key. It helps to organize and identify the cached data and enhances the overall function of the node.
    - Comfy dtype: STRING
    - Python dtype: str
- data
    - The 'data'parameter indicates the actual data to be cached. It is essential for the operation of the node, as it is the main element that will be stored and retrieved upon request.
    - Comfy dtype: any_typ
    - Python dtype: Any

# Output types
- data opt
    - The "data opt" output provides the requested data in the cache to ensure that nodes achieve their purpose of efficient data retrieval and storage.
    - Comfy dtype: any_typ
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class CacheBackendDataNumberKeyList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'key': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'tag': ('STRING', {'multiline': False, 'placeholder': 'Tag: short description'}), 'data': (any_typ,)}}
    INPUT_IS_LIST = True
    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ('data opt',)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Backend'
    OUTPUT_NODE = True

    def doit(self, key, tag, data):
        global cache
        cache[key[0]] = (tag[0], (True, data))
        return (data,)
```