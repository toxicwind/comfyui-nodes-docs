# Documentation
- Class name: CR_TextOperation
- Category: Comfyroll/Utils/Text
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_TextOperation node is designed to perform multiple text operations. It accepts a string input and applies specified operations, such as converting text into upper case, lower case or capital case. The node also handles more complex operations, such as invert case, invert text, cut blanks and completely delete spaces. It is a multifunctional tool for pre-processing and conversion of text data in workflows.

# Input types
## Required
- text
    - The 'text' parameter is the main input of the node and is essential for all text operations. It determines the data that will be operated according to the selected operation. The function of the node is directly linked to the content and format of the text provided.
    - Comfy dtype: STRING
    - Python dtype: str
- operation
    - The `option' parameter indicates that a specific text operation is to be performed. It is a key component because it defines the type of conversion that will be applied to the input text and affects the final output of the node.
    - Comfy dtype: COMBO['uppercase', 'lowercase', 'capitalize', 'invert_case', 'reverse', 'trim', 'remove_spaces']
    - Python dtype: str

# Output types
- STRING
    - The `STRING' output parameter represents the result of the text operation. It is the text converted after the specified operation has been applied and shows the ability of the node to operate.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The `show_help' output provides a URL link to the document for further help. It is particularly useful for users seeking more information about node operations or troubleshooting.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_TextOperation:

    @classmethod
    def INPUT_TYPES(cls):
        operations = ['uppercase', 'lowercase', 'capitalize', 'invert_case', 'reverse', 'trim', 'remove_spaces']
        return {'required': {'text': ('STRING', {'multiline': False, 'default': '', 'forceInput': True}), 'operation': (operations,)}}
    RETURN_TYPES = (any_type, 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    FUNCTION = 'text_operation'
    CATEGORY = icons.get('Comfyroll/Utils/Text')

    def text_operation(self, text, operation):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-text_operation'
        if operation == 'uppercase':
            text_out = text.upper()
        elif operation == 'lowercase':
            text_out = text.lower()
        elif operation == 'capitalize':
            text_out = text.capitalize()
        elif operation == 'invert_case':
            text_out = text.swapcase()
        elif operation == 'reverse':
            text_out = text[::-1]
        elif operation == 'trim':
            text_out = text.strip()
        elif operation == 'remove_spaces':
            text_out = text.replace(' ', '')
        else:
            return 'CR Text Operation: Invalid operation.'
        return (text_out, show_help)
```