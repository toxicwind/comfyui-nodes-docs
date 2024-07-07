# Documentation
- Class name: WAS_Text_Add_Tokens
- Category: WAS Suite/Text/Tokens
- Output node: True
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Text_Add_Tokens node is designed to process and operate text tags. It enhances input text by adding a custom mark that can be used for various purposes, such as time stamping, user recognition, or device information. The node's function is focused on injecting dynamic elements into static text, thus providing a multifunctional tool for text-processing tasks.

# Input types
## Required
- tokens
    - The `tokens' parameter is essential to the operation of the node because it defines the custom tags that you want to add to the text. These tags can indicate dynamic data such as current time, hostname, or other system-specific information. Including these tags allows for the creation of content-rich text that can be used in various applications.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- print_current_tokens
    - The `print_current_tokens' parameter is an optional switch, and when set to `true', the indicator node prints the current custom tag state. This feature is very useful for debugging and validating marks that are being applied to the text.
    - Comfy dtype: COMBO['false', 'true']
    - Python dtype: Union[str, None]

# Output types
- tokens
    - Output 'tokens' parameters represent a modified text with new or updated custom tags. This output can be used for further processing or analysis of downstream tasks and allows seamless integration of dynamic text elements into various workflows.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_Add_Tokens:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'tokens': ('STRING', {'default': '[hello]: world', 'multiline': True}), 'print_current_tokens': (['false', 'true'],)}}
    RETURN_TYPES = ()
    FUNCTION = 'text_add_tokens'
    OUTPUT_NODE = True
    CATEGORY = 'WAS Suite/Text/Tokens'

    def text_add_tokens(self, tokens, print_current_tokens='false'):
        import io
        tk = TextTokens()
        for line in io.StringIO(tokens):
            parts = line.split(':')
            token = parts[0].strip()
            token_value = parts[1].strip()
            tk.addToken(token, token_value)
        if print_current_tokens == 'true':
            cstr(f'Current Custom Tokens:').msg.print()
            print(json.dumps(tk.custom_tokens, indent=4))
        return tokens

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
```