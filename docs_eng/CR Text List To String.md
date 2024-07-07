# Documentation
- Class name: CR_TextListToString
- Category: Comfyroll/List/Utils
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_TextListToString is designed to connect a string list to a single string, separated by line breaks between each string. It is used to simplify the process of converting multiple text entries to a consistent uniform format that can be easily managed and displayed.

# Input types
## Required
- text_list
    - The parameter 'text_list' is a list of strings that are linked by nodes into a single string. It plays a key role in determining the final output, as it directly affects the content and structure of the result string.
    - Comfy dtype: STRING
    - Python dtype: List[str]

# Output types
- STRING
    - The 'STRING' output is a string string that links all elements of the input text list through line breaks. It represents the main result of the node operation.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The'show_help' output provides a URL link to a document with node functions for further help or information. It is a useful resource for users seeking additional guidance.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_TextListToString:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text_list': ('STRING', {'forceInput': True})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    INPUT_IS_LIST = True
    FUNCTION = 'joinlist'
    CATEGORY = icons.get('Comfyroll/List/Utils')

    def joinlist(self, text_list):
        string_out = '\n'.join(text_list)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-text-list-to-string'
        return (string_out, show_help)
```