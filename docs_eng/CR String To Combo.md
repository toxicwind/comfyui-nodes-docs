# Documentation
- Class name: CR_StringToCombo
- Category: Comfyroll/Utils/Conversion
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_StringToCombo node, which aims to convert text string to value, provides a way to process and operate text data more efficiently. It plays a key role in data conversion, especially when processing comma separator values.

# Input types
## Required
- text
    - The `text' parameter is essential for the operation of the node, as it is the input text to be converted. It is important to determine the content and structure of the output list and make it an essential part of the conversion process.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- any
    - The 'any'output represents a list of converted values derived from the input text. It is important because it is the main result of the node conversion function and contains the converted data for further use.
    - Comfy dtype: STRING
    - Python dtype: List[str]
- show_help
    - The `show_help' output provides a URL link to the node document page and direct references to users for further information and guidance for the effective use of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_StringToCombo:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': ('STRING', {'multiline': False, 'default': '', 'forceInput': True})}}
    RETURN_TYPES = (any, 'STRING')
    RETURN_NAMES = ('any', 'show_help')
    FUNCTION = 'convert'
    CATEGORY = icons.get('Comfyroll/Utils/Conversion')

    def convert(self, text):
        text_list = list()
        if text != '':
            values = text.split(',')
            text_list = values[0]
            print(text_list)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Conversion-Nodes#cr-string-to-combo'
        return (text_list, show_help)
```