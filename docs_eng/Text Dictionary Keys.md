# Documentation
- Class name: WAS_Dictionary_Keys
- Category: WAS Suite/Text
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The SAS_Dictionary_Keys node is designed to extract keys from a given dictionary. It is used as a basic component in the data processing workflow to identify the dictionaries before further analysis or operation of the data structure.

# Input types
## Required
- dictionary
    - The parameter 'dictionary' is essential for the running of the node because it is the source from which the key will be extracted. This is a key input that directly influences the output of the node by identifying the identified key set.
    - Comfy dtype: DICT
    - Python dtype: Dict[Any, Any]

# Output types
- keys
    - The output parameter'keys' represents the set of keys extracted from the input dictionary. It is important because it provides the basis for any subsequent operation that requires knowledge of the dictionary structure and does not involve the relevant values.
    - Comfy dtype: LIST
    - Python dtype: List[Any]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Dictionary_Keys:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'dictionary': ('DICT',)}, 'optional': {}}
    RETURN_TYPES = ('LIST',)
    FUNCTION = 'dictionary_keys'
    CATEGORY = 'WAS Suite/Text'

    def dictionary_keys(self, dictionary):
        return (dictionary.keys(),)
```