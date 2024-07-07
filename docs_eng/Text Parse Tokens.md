# Documentation
- Class name: WAS_Text_Parse_Tokens
- Category: WAS Suite/Text/Tokens
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Text_Parse_Tokens node is designed to process and replace the tokens in the given text string. It operates by identifying predefined and custom tokens and replacing them with corresponding values, thereby achieving dynamic text generation based on data in the context of current time, hostname and user information.

# Input types
## Required
- text
    - The `text' parameter is essential for the operation of the node, as it provides input text that will be scanned to replace the token. The function of the node relies heavily on this input to perform its replacement task, making it a key component of overall implementation.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- parsed_text
    - The `parsed_text' output contains the text after completion of the token replacement process. It marks the successful implementation of the node and the conversion of the input text on the basis of predefined and custom tokens.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_Parse_Tokens:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False})}}
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'text_parse_tokens'
    CATEGORY = 'WAS Suite/Text/Tokens'

    def text_parse_tokens(self, text):
        tokens = TextTokens()
        return (tokens.parseTokens(text),)

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
```