# Documentation
- Class name: CR_TextReplace
- Category: Comfyroll/Utils/Text
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_TextReplace is a node to perform text replacement operations. It can efficiently replace a given string in the given text. This node is particularly suitable for pre-processing text data, where certain patterns or strings need to be changed consistently in the data pool.

# Input types
## Required
- text
    - The `text' parameter is the main input for the node. It is the text data that will go through the replacement operation. This parameter is essential because it is the content that will be modified by the node.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- find1
    - The 'find1' parameter is an optional string that specifies the first substring that you want to replace in the text. It is used with'replace1' to define the first replacement operation.
    - Comfy dtype: STRING
    - Python dtype: str
- replace1
    - The'replace1' parameter is the string that will replace the 'find1' substring in the text. It is an optional parameter, working with 'find1'.
    - Comfy dtype: STRING
    - Python dtype: str
- find2
    - The 'find2'parameter specifies the second substring that needs to be replaced. It is part of the second search and replacement operation in the node.
    - Comfy dtype: STRING
    - Python dtype: str
- replace2
    - The'replace2' parameter defines the string that will replace the 'find2' substring in the text. It is an optional component for the second pair of replacements.
    - Comfy dtype: STRING
    - Python dtype: str
- find3
    - The 'find3'parameter specifies the third substring that you intend to replace. It completes the third set of search and replacement actions in the node.
    - Comfy dtype: STRING
    - Python dtype: str
- replace3
    - The'replace3' parameter is the string that will replace the 'find3' substring in the text. It is the last part of the optional replacement parameter.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- STRING
    - The `STRING' output parameter represents the text after all replacement operations have been completed. It is the main result of node execution.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The `show_help' output parameter provides a URL linked to the node document page and provides further help if required.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_TextReplace:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': ('STRING', {'multiline': True, 'default': '', 'forceInput': True})}, 'optional': {'find1': ('STRING', {'multiline': False, 'default': ''}), 'replace1': ('STRING', {'multiline': False, 'default': ''}), 'find2': ('STRING', {'multiline': False, 'default': ''}), 'replace2': ('STRING', {'multiline': False, 'default': ''}), 'find3': ('STRING', {'multiline': False, 'default': ''}), 'replace3': ('STRING', {'multiline': False, 'default': ''})}}
    RETURN_TYPES = (any_type, 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    FUNCTION = 'replace_text'
    CATEGORY = icons.get('Comfyroll/Utils/Text')

    def replace_text(self, text, find1='', replace1='', find2='', replace2='', find3='', replace3=''):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-text-replace'
        text = text.replace(find1, replace1)
        text = text.replace(find2, replace2)
        text = text.replace(find3, replace3)
        return (text, show_help)
```