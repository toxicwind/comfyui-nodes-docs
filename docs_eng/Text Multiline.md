# Documentation
- Class name: WAS_Text_Multiline
- Category: WAS Suite/Text
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Text_Multiline node is designed to process and format multi-line text input. It filters out comments and empty lines and then replaces predefined and custom tags with corresponding values, providing a multifunctional way to inject dynamic data into the text template.

# Input types
## Required
- text
    - The `text' parameter is the main input of the node, accepting a multi-line string that may contain notes and tags. It is essential for the operation of the node, as it defines the underlying text that will be processed and formatted.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- new_text
    - The `new_text' output parameter represents the text processed after filtering and tagging. It is important because it is the final output of the node and provides the user with a formatted text ready for use.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_Multiline:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': ('STRING', {'default': '', 'multiline': True})}}
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'text_multiline'
    CATEGORY = 'WAS Suite/Text'

    def text_multiline(self, text):
        import io
        new_text = []
        for line in io.StringIO(text):
            if not line.strip().startswith('#'):
                if not line.strip().startswith('\n'):
                    line = line.replace('\n', '')
                new_text.append(line)
        new_text = '\n'.join(new_text)
        tokens = TextTokens()
        new_text = tokens.parseTokens(new_text)
        return (new_text,)
```