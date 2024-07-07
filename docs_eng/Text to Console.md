# Documentation
- Class name: WAS_Text_to_Console
- Category: WAS Suite/Debug
- Output node: True
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Text_to_Console node is designed to export text to the control table and can selectively format labels. It enhances the control table output by applying colours and styles to the text to increase visibility and differentiation.

# Input types
## Required
- text
    - The `text' parameter is essential for the operation of the node, as it defines what will be printed on the control table. It plays a key role in the implementation of the node and determines the information to be displayed.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- label
    - The 'label' parameter is used to add custom labels before text output. Although not necessary, it may be useful for classifying or highlighting the control table output in order to improve readability and organization.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- output
    - The 'output'parameter represents the text that has been formatted and printed to the control table. It marks the end result of the node operation and covers the styled text.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_to_Console:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False}), 'label': ('STRING', {'default': f'Text Output', 'multiline': False})}}
    RETURN_TYPES = (TEXT_TYPE,)
    OUTPUT_NODE = True
    FUNCTION = 'text_to_console'
    CATEGORY = 'WAS Suite/Debug'

    def text_to_console(self, text, label):
        if label.strip() != '':
            cstr(f'\x1b[33m{label}\x1b[0m:\n{text}\n').msg.print()
        else:
            cstr(f'\x1b[33mText to Console\x1b[0m:\n{text}\n').msg.print()
        return (text,)
```