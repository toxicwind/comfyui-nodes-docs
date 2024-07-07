# Documentation
- Class name: CharacterInText
- Category: ♾️Mixlab/GPT
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

This node facilitates the identification of the existence of a given character in the text and calculates the index of its occurrence. It processes text data to determine the frequency of given characters, starting with the specified index, and contributes to the text analysis task by providing simple and effective measurements of the frequency of the presence of characters.

# Input types
## Required
- text
    - Text parameters are essential because they are to verify the origin of the character. They are the main input for node processing and are used to achieve its purpose.
    - Comfy dtype: STRING
    - Python dtype: str
- character
    - Character parameters are essential for nodes, which determines which character the nodes look for in the text. It determines the focus of the search and affects the results of the node operation.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- start_index
    - The starting index parameter defines the starting point of the node that starts searching characters in the text. It affects the scope of the search and the result index values.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- result
    - The result output represents the index that the specified character appears in the text, starting with the given initial index. It is a direct output that reflects the main function of the node and provides a quantitative measure of the presence of the character.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class CharacterInText:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'character': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'start_index': ('INT', {'default': 1, 'min': 0, 'max': 1024, 'step': 1, 'display': 'number'})}}
    INPUT_IS_LIST = False
    RETURN_TYPES = ('INT',)
    FUNCTION = 'run'
    OUTPUT_IS_LIST = (False,)
    CATEGORY = '♾️Mixlab/GPT'

    def run(self, text, character, start_index):
        b = 1 if character.lower() in text.lower() else 0
        return (b + start_index,)
```