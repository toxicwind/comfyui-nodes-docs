# Documentation
- Class name: CacheBackendData
- Category: InspirePack/Backend
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

Such nodes manage the storage and retrieval of data in the back end cache system to facilitate efficient data access and optimization of workflow processes.

# Input types
## Required
- key
    - The key parameter is essential for the unique identification data in the cache. It is used to index and retrieve relevant data to ensure access to and processing of the correct information.
    - Comfy dtype: STRING
    - Python dtype: str
- tag
    - Tag parameters, as descriptive labels of data, help to classify and quickly refer to data. It strengthens the organization in the cache and supports efficient data management.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- data
    - The data parameter represents the actual content of the cache. It is the basis for node operations, as it saves the values that will be stored and accessed later.
    - Comfy dtype: ANY
    - Python dtype: Any

# Output types
- data opt
    - The output provides the originally entered data to ensure that the flow of data is maintained throughout the process. It confirms that the data has been successfully stored for future use.
    - Comfy dtype: ANY
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class CacheBackendData:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'key': ('STRING', {'multiline': False, 'placeholder': "Input data key (e.g. 'model a', 'chunli lora', 'girl latent 3', ...)"}), 'tag': ('STRING', {'multiline': False, 'placeholder': 'Tag: short description'}), 'data': (any_typ,)}}
    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ('data opt',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Backend'
    OUTPUT_NODE = True

    def doit(self, key, tag, data):
        global cache
        if key == '*':
            print(f"[Inspire Pack] CacheBackendData: '*' is reserved key. Cannot use that key")
        cache[key] = (tag, (False, data))
        return (data,)
```