# Documentation
- Class name: CR_CombinePrompt
- Category: Essential
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_CombinePrompt node is used to bind multiple strings into a single output string. It is designed to simplify the creation of complex tips by using the specified separator to combine various text elements.

# Input types
## Optional
- part1
    - The first text segment that you want to combine in the final output. It is an essential part of the overall structure of the reminder.
    - Comfy dtype: STRING
    - Python dtype: str
- part2
    - Outputs the second text segment contained in the string. It plays a role in shaping the details of the hint.
    - Comfy dtype: STRING
    - Python dtype: str
- part3
    - . This is an optional element that can be included according to the user's needs.
    - Comfy dtype: STRING
    - Python dtype: str
- part4
    - Merges to the fourth and last text paragraph of the reminder. It completes the transmission of information and provides closure to the overall reminder structure.
    - Comfy dtype: STRING
    - Python dtype: str
- separator
    - Characters or strings that separate parts of the hint. It determines the structure and readability of the group output.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- prompt
    - By using the specified separator to combine the string formed from the input part. It represents the final output of the node and is ready for further processing or display.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - A URL link to the node using the help document page. It provides a reference resource for users to consult when needed.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_CombinePrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}, 'optional': {'part1': ('STRING', {'default': '', 'multiline': True}), 'part2': ('STRING', {'default': '', 'multiline': True}), 'part3': ('STRING', {'default': '', 'multiline': True}), 'part4': ('STRING', {'default': '', 'multiline': True}), 'separator': ('STRING', {'default': ',', 'multiline': False})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('prompt', 'show_help')
    FUNCTION = 'get_value'
    CATEGORY = icons.get('Comfyroll/Essential/Core')

    def get_value(self, part1='', part2='', part3='', part4='', separator=''):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Core-Nodes#cr-prompt-parts'
        prompt = part1 + separator + part2 + separator + part3 + separator + part4
        return (prompt, show_help)
```