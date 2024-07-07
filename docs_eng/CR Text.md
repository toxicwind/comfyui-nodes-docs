# Documentation
- Class name: CR_Text
- Category: Comfyroll/Utils/Text
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_Text node is designed to process and process text data and to provide a function for the efficient management of multi-line text input. It applies in particular to applications that require text operation and ability to interact with external documents.

# Input types
## Required
- text
    - The `text' parameter is essential for the operation of the node, as it is the main input for text processing. It allows multiple lines of input and enhances the multifunctionality of node processing various text formats.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- text
    - The 'text'output parameter represents the processed text data, which may include modifications or enhancements to the internal function of the node. It is a key element of a downstream application that relies on the text update state.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The'show_help' output provides a URL link to an external document, providing users with additional resources to understand the function and use of nodes. It is a valuable tool for users seeking more information or help.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_Text:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': ('STRING', {'default': '', 'multiline': True})}}
    RETURN_TYPES = (any_type, 'STRING')
    RETURN_NAMES = ('text', 'show_help')
    FUNCTION = 'text_multiline'
    CATEGORY = icons.get('Comfyroll/Utils/Text')

    def text_multiline(self, text):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-text'
        return (text, show_help)
```