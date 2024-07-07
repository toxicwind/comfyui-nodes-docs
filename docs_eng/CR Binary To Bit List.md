# Documentation
- Class name: CR_BinaryToBitList
- Category: Comfyroll/List
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_BinaryToBitList node is designed to convert binary strings into a single-bit list. It accepts a binary string as an input, produces a list in which each element corresponds to one bit of the string. This node is particularly suitable for processing binary data in a more detailed and accessible manner.

# Input types
## Required
- bit_string
    - The " bit_string " parameter is a mandatory input that expects a string that contains binary data. This string is the main data source for node operations and converts it to a bytes list is the core function of the node. The correct formatting of binary strings is essential for the node to work as expected.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- list_out
    - The 'list_out'output is a list of strings in which each string represents one from the entered binary string. This output allows users to operate and analyse binary data at bit levels and facilitates operations such as data coding, decoding or conversion.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- show_help
    - The Show_help output provides a URL link for more help information documents. It guides users to the GitHub wiki page, where they can find more information about how to use the node and its associated properties.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_BinaryToBitList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'bit_string': ('STRING', {'multiline': True, 'default': ''})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = 'make_list'
    CATEGORY = icons.get('Comfyroll/List')

    def make_list(self, bit_string):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-binary-to-list'
        list_out = [str(bit) for bit in bit_string]
        return (list_out, show_help)
```