# Documentation
- Class name: CR_TextConcatenate
- Category: Comfyroll/Utils/Text
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_TextConcatenate node is designed to combine two separate text strings into a single string. It achieves this by inserting a given separator between two input text, effectively combining them into a coherent sequence. This node is particularly useful when creating a single text block from multiple sources, which can play a key role in various text-processing tasks.

# Input types
## Required
- text1
    - The parameter'text1' indicates the first text string to be connected. It plays a key role in determining the initial content of the final output. The execution of the node is directly influenced by the content and length of the parameter.
    - Comfy dtype: STRING
    - Python dtype: str
- text2
    - The parameter'text2' is the second text string that will connect with 'text1'. It is essential when forming the final output, as it provides the subsequent part of the text sequence.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- separator
    - The parameter'separator' defines the string that will be inserted between 'text1' and 'text2'. It is important in controlling the formatting of the connecting text, allowing users to customise spaces and separators as required.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- STRING
    - The output 'STRING' is the result of providing'separator' connections to 'text1' and 'text2'. It represents a grouped text that is the main output of the node function.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_TextConcatenate:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}, 'optional': {'text1': ('STRING', {'multiline': False, 'default': '', 'forceInput': True}), 'text2': ('STRING', {'multiline': False, 'default': '', 'forceInput': True}), 'separator': ('STRING', {'multiline': False, 'default': ''})}}
    RETURN_TYPES = (any_type, 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    FUNCTION = 'concat_text'
    CATEGORY = icons.get('Comfyroll/Utils/Text')

    def concat_text(self, text1='', text2='', separator=''):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-save-text-to-file'
        return (text1 + separator + text2,)
```