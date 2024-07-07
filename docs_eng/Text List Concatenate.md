# Documentation
- Class name: WAS_Text_List_Concatenate
- Category: WAS Suite/Text
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Text_List_Concatenate node is designed to efficiently merge multiple string lists into a single uniform list. It plays a key role in simplifying data pre-processing workflows, especially when processing text data from different sources that require aggregation for further processing or analysis.

# Input types
## Required
- list_a
    - The 'list_a'parameter is a string list that will be merged with other lists. It is the basic input of the node, as it directly contributes to the formation of the final consolidated list.
    - Comfy dtype: LIST
    - Python dtype: List[str]
## Optional
- list_b
    - The 'list_b' parameter is an optional list of strings that can be linked to the main list. It enhances the flexibility of nodes by allowing additional data to be included in the final list.
    - Comfy dtype: LIST
    - Python dtype: Optional[List[str]]
- list_c
    - The 'list_c' parameter is another optional string list for connection. It provides further custom options for nodes to enable users to control more precisely the composition of the output list.
    - Comfy dtype: LIST
    - Python dtype: Optional[List[str]]
- list_d
    - The 'list_d' parameter is another optional list that can be connected to the merged list. It provides users with the ability to include more strings and customizes the final output further to specific requirements.
    - Comfy dtype: LIST
    - Python dtype: Optional[List[str]]

# Output types
- merged_list
    - The'merged_list' output is the result of connecting all input lists. It represents a combination of text data that can be used for follow-up or analysis.
    - Comfy dtype: LIST
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_List_Concatenate:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}, 'optional': {'list_a': ('LIST', {'forceInput': True}), 'list_b': ('LIST', {'forceInput': True}), 'list_c': ('LIST', {'forceInput': True}), 'list_d': ('LIST', {'forceInput': True})}}
    RETURN_TYPES = ('LIST',)
    FUNCTION = 'text_concatenate_list'
    CATEGORY = 'WAS Suite/Text'

    def text_concatenate_list(self, **kwargs):
        merged_list: list[str] = []
        for k in sorted(kwargs.keys()):
            v = kwargs[k]
            if isinstance(v, list):
                merged_list += v
        return (merged_list,)
```