# Documentation
- Class name: WAS_Dictionary_Get
- Category: WAS Suite/Text
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Dictionary_Get node is designed to retrieve a particular entry from a dictionary based on the given key. It plays a vital role in data extraction and operation, providing a flow-lined way to access and use the dictionary values in the workflow.

# Input types
## Required
- dictionary
    - Dictionary parameters are essential for the operation of nodes because they are the source of the keys that will be retrieved. This is a key component that directly influences the output of the nodes.
    - Comfy dtype: DICT
    - Python dtype: Dict[Any, Any]
- key
    - key parameter is used to specify a specific entry in the dictionary that the node will visit. Its existence is essential for the proper running of the node, and the exact data that you want can be determined.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- default_value
    - The default_value parameter is provided as an option if the specified key does not exist in the dictionary. It ensures that nodes can deal with the situation in an elegant manner and continue the workflow without interruption.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- value
    - Value output parameter means the data retrieved from the dictionary using the specified key. It is important because it is a direct result of node operations and can be used for further processing in the workflow.
    - Comfy dtype: TEXT
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Dictionary_Get:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'dictionary': ('DICT',), 'key': ('STRING', {'default': '', 'multiline': False})}, 'optional': {'default_value': ('STRING', {'default': '', 'multiline': False})}}
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'dictionary_get'
    CATEGORY = 'WAS Suite/Text'

    def dictionary_get(self, dictionary, key, default_value=''):
        return (str(dictionary.get(key, default_value)),)
```