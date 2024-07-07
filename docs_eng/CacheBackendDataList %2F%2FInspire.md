# Documentation
- Class name: CacheBackendDataList
- Category: InspirePack/Backend
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node manages the retrieval and storage of data in the backend system for efficient data access and organization.

# Input types
## Required
- key
    - The key parameter is essential for identifying specific data entries in the cache. As a unique identifier, it allows nodes to retrieve or store relevant data accurately.
    - Comfy dtype: STRING
    - Python dtype: str
- tag
    - The tag parameter provides a means of classifying and characterizing data in the cache. It helps to organize and filter the data and improves the overall efficiency of the system.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- data
    - Data parameters represent the content that you actually want to store or retrieve from the cache. This is a multifunctional field that can contain various types of information according to the example.
    - Comfy dtype: ANY
    - Python dtype: Any

# Output types
- data
    - Output data represents the information retrieved from the cache. It is the main result of node operations and demonstrates the effectiveness of nodes in managing and providing access to stored data.
    - Comfy dtype: ANY
    - Python dtype: Any
- opt
    - The opt parameter, as part of the output, may contain additional options or metadata associated with the retrieval of data. It complements the main data output and provides further context or practical tools.
    - Comfy dtype: ANY
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class CacheBackendDataList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'key': ('STRING', {'multiline': False, 'placeholder': "Input data key (e.g. 'model a', 'chunli lora', 'girl latent 3', ...)"}), 'tag': ('STRING', {'multiline': False, 'placeholder': 'Tag: short description'}), 'data': (any_typ,)}}
    INPUT_IS_LIST = True
    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ('data opt',)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Backend'
    OUTPUT_NODE = True

    def doit(self, key, tag, data):
        global cache
        if key == '*':
            print(f"[Inspire Pack] CacheBackendDataList: '*' is reserved key. Cannot use that key")
        cache[key[0]] = (tag[0], (True, data))
        return (data,)
```