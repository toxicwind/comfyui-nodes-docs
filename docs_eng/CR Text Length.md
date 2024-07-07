# Documentation
- Class name: CR_TextLength
- Category: Comfyroll/Utils/Text
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_TextLength node is designed to measure the length of the given text string. As a basic tool in the text-processing workflow, it provides a direct method for determining the number of characters in the input text. This node is essential for tasks that need to be considered for text length, such as data cleansing or formatting.

# Input types
## Required
- text
    - The 'text' parameter is the input text that will determine the length. This is a key element, because the operation of the node depends entirely on the content of the text. Node handles the input to provide the length of the text, which may be essential for various text analysis or processing tasks.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- INT
    - The 'INT' output represents the length of the text entered, i.e. the number of characters in the text string. This output is important because it directly reflects the result of the main function of the node and allows users to use this information for further processing or decision-making in their application.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - The'show_help' output provides a document page with a URL link to the node for further help. This output is useful for users who may need additional guidance or information about the node function and provides a reference for direct access to the node wiki page.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_TextLength:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': ('STRING', {'multiline': False, 'default': '', 'forceInput': True})}}
    RETURN_TYPES = ('INT', 'STRING')
    RETURN_NAMES = ('INT', 'show_help')
    FUNCTION = 'len_text'
    CATEGORY = icons.get('Comfyroll/Utils/Text')

    def len_text(self, text):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-text-length'
        int_out = len(text)
        return (int_out, show_help)
```