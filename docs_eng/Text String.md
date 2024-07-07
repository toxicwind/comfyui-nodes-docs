# Documentation
- Class name: WAS_Text_String
- Category: WAS Suite/Text
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `text_string'method is designed to process and mark the input string and replace predefined and custom tags with their corresponding values. It plays a key role in dynamic text generation, allowing the inclusion of contextual elements such as time stampes and system information.

# Input types
## Required
- text
    - The 'text' parameter is essential to the operation of the node, as it is the main input that will be marked and processed. It influences implementation by determining that the underlying text of the mark will be replaced with actual values.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- text_b
    - The 'text_b' parameter is optional as an additional text input to the node. It allows more complex tag replacements and text operations and increases the flexibility of the node function.
    - Comfy dtype: STRING
    - Python dtype: str
- text_c
    - The 'text_c' parameter is similar to 'text_b' and is another optional text input that can be processed by nodes. It expands the ability of nodes to process multiple text inputes for more complex tagging tasks.
    - Comfy dtype: STRING
    - Python dtype: str
- text_d
    - The 'text_d' parameter is also optional, providing further text input for processing. It helps nodes manage more text input to meet more complex labelling needs.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- text_output
    - The 'text_output' parameter represents the processed text replaced by the tag. It is important because it reflects the results of node text operations and tagging processes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_String:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': ('STRING', {'default': '', 'multiline': False})}, 'optional': {'text_b': ('STRING', {'default': '', 'multiline': False}), 'text_c': ('STRING', {'default': '', 'multiline': False}), 'text_d': ('STRING', {'default': '', 'multiline': False})}}
    RETURN_TYPES = (TEXT_TYPE, TEXT_TYPE, TEXT_TYPE, TEXT_TYPE)
    FUNCTION = 'text_string'
    CATEGORY = 'WAS Suite/Text'

    def text_string(self, text='', text_b='', text_c='', text_d=''):
        tokens = TextTokens()
        text = tokens.parseTokens(text)
        text_b = tokens.parseTokens(text_b)
        text_c = tokens.parseTokens(text_c)
        text_d = tokens.parseTokens(text_d)
        return (text, text_b, text_c, text_d)
```