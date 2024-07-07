# Documentation
- Class name: WAS_Text_Add_Token_Input
- Category: WAS Suite/Text/Tokens
- Output node: True
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Text_Add_Token_Input is designed to manage and operate custom tags in text-processing workflows. It allows users to add or remove tags and provides the function to print the current tag list. This node plays a key role in customizing and personalizing text output according to predefined or user-provided tags.

# Input types
## Required
- token_name
    - The token_name parameter is essential for the sole name of the mark to be added or operated. It directly affects the ability of the node to correctly quote and modify the required mark in the text-processing system.
    - Comfy dtype: STRING
    - Python dtype: str
- token_value
    - The token_value parameter specifies the values to be associated with token_name. It is a key input because it determines the actual content of the label placeholder that will be replaced in the text during the processing period.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- print_current_tokens
    - When the print_current_tokens parameter is set to 'true', the current list of custom tags is triggered. This feature is very useful for debugging and validating the status of the modified list of tags.
    - Comfy dtype: COMBO['false', 'true']
    - Python dtype: Union[str, None]

# Output types
- token_name_output
    - Token_name_output provides the name of the mark added or operated by the node. It is important because it confirms the identity of the marks processed.
    - Comfy dtype: STRING
    - Python dtype: str
- token_value_output
    - Token_value_output returns the value associated with token_name. This output is important to verify the correct value set for tags in the text-processing system.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_Add_Token_Input:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'token_name': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False}), 'token_value': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False}), 'print_current_tokens': (['false', 'true'],)}}
    RETURN_TYPES = ()
    FUNCTION = 'text_add_token'
    OUTPUT_NODE = True
    CATEGORY = 'WAS Suite/Text/Tokens'

    def text_add_token(self, token_name, token_value, print_current_tokens='false'):
        if token_name.strip() == '':
            cstr(f'A `token_name` is required for a token; token name provided is empty.').error.print()
            pass
        tk = TextTokens()
        tk.addToken(token_name, token_value)
        if print_current_tokens == 'true':
            cstr(f'Current Custom Tokens:').msg.print()
            print(json.dumps(tk.custom_tokens, indent=4))
        return (token_name, token_value)

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
```