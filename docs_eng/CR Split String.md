# Documentation
- Class name: CR_SplitString
- Category: Comfyroll/Utils/Text
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_SplitString node is designed to divide the given text string into multiple substrings based on the given separator. It is particularly suitable for processing and organizing text data separated by a consistent character or character series. The function of the node is that it can simplify the processing of complex text by decompositioning complex text structures into more manageable components.

# Input types
## Required
- text
    - The 'text' parameter is the main input of the node, which means the string that will be split. It is a core component, because all operations of the node revolve around dividing the text into substrings.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- delimiter
    - The 'delimiter 'parameter defines the character or character series used to divide the input text. Although it is optional, it plays a key role in determining how to divide the text into substrings, thus influencing the output of nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- string_1
    - The'string_1' output contains the first substring from the split operation. It represents part of the original text and is significant as one of the main outcomes of the node function.
    - Comfy dtype: STRING
    - Python dtype: str
- string_2
    - The'string_2' output saves a second substring from the split operation. It is another segment of the original text and is important to provide details of the input text.
    - Comfy dtype: STRING
    - Python dtype: str
- string_3
    - The'string_3' output provides a third substring after the text has been split. It continues the sequence of the part of the text that divides it and is part of the full text processing capability of the node.
    - Comfy dtype: STRING
    - Python dtype: str
- string_4
    - The'string_4' output includes the fourth substring from the split operation. It is another part of the text that helps the overall text operation function of the node.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The'show_help' output provides a URL link to the node document page, providing additional information and guidance to users on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SplitString:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': False, 'default': 'text'})}, 'optional': {'delimiter': ('STRING', {'multiline': False, 'default': ','})}}
    RETURN_TYPES = (any_type, any_type, any_type, any_type, 'STRING')
    RETURN_NAMES = ('string_1', 'string_2', 'string_3', 'string_4', 'show_help')
    FUNCTION = 'split'
    CATEGORY = icons.get('Comfyroll/Utils/Text')

    def split(self, text, delimiter=''):
        parts = text.split(delimiter)
        strings = [part.strip() for part in parts[:4]]
        (string_1, string_2, string_3, string_4) = strings + [''] * (4 - len(strings))
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-split-string'
        return (string_1, string_2, string_3, string_4, show_help)
```