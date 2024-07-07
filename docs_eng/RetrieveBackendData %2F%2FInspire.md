# Documentation
- Class name: RetrieveBackendData
- Category: InspirePack/Backend
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node is designed to extract data from the backend cache system and provides a flow-lined method based on the specified key access to stored information. As a key component of the data retrieval workflow, it ensures efficient and accurate access to backend data without the need to repeat the data.

# Input types
## Required
- key
    - The `key' parameter is essential for identifying a particular data set to be retrieved from the back-end cache. It is the only identifier that allows nodes to locate and return the correct information.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- data
    - The `data' output represents the information retrieved from the back-end cache. It is a key component of the node function because it transmits the requested data to the subsequent phase of the workflow.
    - Comfy dtype: COMBO[any_typ]
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class RetrieveBackendData:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'key': ('STRING', {'multiline': False, 'placeholder': "Input data key (e.g. 'model a', 'chunli lora', 'girl latent 3', ...)"})}}
    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ('data',)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Backend'

    def doit(self, key):
        global cache
        (is_list, data) = cache[key][1]
        if is_list:
            return (data,)
        else:
            return ([data],)
```