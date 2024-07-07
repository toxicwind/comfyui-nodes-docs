# Documentation
- Class name: promptReplace
- Category: EasyUse/Prompt
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

This node facilitates the text conversion process by identifying and replacing the specified substrings in the given text. The main purpose is to simplify the editing process so that users can efficiently modify the target.

# Input types
## Required
- prompt
    - The `prompt' parameter is the basis for node operations, representing the text to be replaced. It is essential because it determines the content and context of the replacement.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- find1
    - The 'find1'parameter specifies the first substring in the text that you want to recognize and replace. Its significance is in terms of the purpose of the editing, which helps to make precise changes to the node.
    - Comfy dtype: STRING
    - Python dtype: str
- replace1
    - The `replace1' parameter defines the text that will replace the identified `find1' substring. It is an integral part of the conversion process because it determines the outcome of the replacement.
    - Comfy dtype: STRING
    - Python dtype: str
- find2
    - The `find2' parameter is used to identify and replace the second set of substrings in the text. The function is to extend the editorial power of the node to allow multiple target replacements.
    - Comfy dtype: STRING
    - Python dtype: str
- replace2
    - The `replace2' parameter corresponds to text that will replace the `find2' substring to further facilitate the overall text conversion process.
    - Comfy dtype: STRING
    - Python dtype: str
- find3
    - The `find3' parameter is used to identify and replace a third set of substrings, which enhances the multifunctionality and adaptability of nodes in text editing.
    - Comfy dtype: STRING
    - Python dtype: str
- replace3
    - The `replace3' parameter is used for final replacement to ensure that nodes address editorial needs in a single operation.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- prompt
    - Output 'prompt' is a modified text that applies all specified replacements. It represents the final result of the node function and provides the user with an updated version of the original text.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class promptReplace:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'prompt': ('STRING', {'multiline': True, 'default': '', 'forceInput': True})}, 'optional': {'find1': ('STRING', {'multiline': False, 'default': ''}), 'replace1': ('STRING', {'multiline': False, 'default': ''}), 'find2': ('STRING', {'multiline': False, 'default': ''}), 'replace2': ('STRING', {'multiline': False, 'default': ''}), 'find3': ('STRING', {'multiline': False, 'default': ''}), 'replace3': ('STRING', {'multiline': False, 'default': ''})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('prompt',)
    FUNCTION = 'replace_text'
    CATEGORY = 'EasyUse/Prompt'

    def replace_text(self, text, find1='', replace1='', find2='', replace2='', find3='', replace3=''):
        text = text.replace(find1, replace1)
        text = text.replace(find2, replace2)
        text = text.replace(find3, replace3)
        return (text,)
```