# Documentation
- Class name: CR_SetValueOnString
- Category: Comfyroll/Utils/Conditional
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SetValueOn String is a node to replace the parts of the string according to the existence of a specific substring. It evaluates the given test string in the input text and replaces the text with a value or another value depending on whether a test string is found. This node applies to creating dynamic text when certain conditions are met.

# Input types
## Required
- text
    - The 'text' parameter is the main element to be assessed by the node. It is essential because it is the basis for determining whether there is 'test_string' and which replacement values will be used.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- test_string
    - The 'test_string' parameter is the substring that the node searches in 'text'. If found, use 'value_if_true' as a replacement; otherwise, use 'value_if_false'.
    - Comfy dtype: STRING
    - Python dtype: str
- value_if_true
    - The 'value_if_true' parameter specifies that if a 'test_string' is found in 'text', the string 'text' will be replaced.
    - Comfy dtype: STRING
    - Python dtype: str
- value_if_false
    - The 'value_if_false' parameter defines the string that will replace 'text' if the 'test_string' is not found in 'text'.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- STRING
    - Output 'STRING' is the result of a conditional replacement process. If the input text contains 'test_string', it is 'value_if_true'; if it does not exist, it is 'value_if_false'.
    - Comfy dtype: STRING
    - Python dtype: str
- BOOLEAN
    - Did the 'BOOLEAN'output instruction find 'test_string' in the input text?
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- show_help
    - The'show_help' output provides a URL link to the node document for further help.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SetValueOnString:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': ('STRING', {'multiline': False, 'default': '', 'forceInput': True})}, 'optional': {'test_string': ('STRING', {'multiline': False, 'default': ''}), 'value_if_true': ('STRING', {'multiline': False, 'default': ''}), 'value_if_false': ('STRING', {'multiline': False, 'default': ''})}}
    RETURN_TYPES = (any_type, 'BOOLEAN', 'STRING')
    RETURN_NAMES = ('STRING', 'BOOLEAN', 'show_help')
    FUNCTION = 'replace_text'
    CATEGORY = icons.get('Comfyroll/Utils/Conditional')

    def replace_text(self, text, test_string, value_if_true, value_if_false):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-set-value-on-string'
        if test_string in text:
            text_out = value_if_true
            bool_out = True
        else:
            text_out = value_if_false
            bool_out = False
        return (text_out, bool_out, show_help)
```