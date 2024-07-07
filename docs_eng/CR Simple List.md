# Documentation
- Class name: CR_SimpleList
- Category: Comfyroll/List
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_SimpleList node is designed to process and operate the string list. The main function is to perform cross-linking operations for the list values provided, effectively combining the elements in a variety of ways. The node is designed to simplify the list operation and provide a direct interface for users to interact with the list data.

# Input types
## Required
- list_values
    - List_values parameters are essential because they are input lists processed by nodes. It should be a string with multiple lines, each of which represents a separate element in the list. Node uses this parameter to perform its cross-link function.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- LIST
    - The LIST output parameter represents the list processed by the node's cross_join function. It is a list of processed strings that has been removed from the top-end blank character and filters out any empty lines.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- show_help
    - Show_help output provides a document URL link for further help. It is a string with a web site where users can find more information about how to use CR_SimpleList nodes and their properties.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SimpleList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'list_values': ('STRING', {'multiline': True, 'default': 'text'})}}
    RETURN_TYPES = (any_type, 'STRING')
    RETURN_NAMES = ('LIST', 'show_help')
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = 'cross_join'
    CATEGORY = icons.get('Comfyroll/List')

    def cross_join(self, list_values):
        lines = list_values.split('\n')
        list_out = [i.strip() for i in lines if i.strip()]
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-simple-list'
        return (list_out, show_help)
```