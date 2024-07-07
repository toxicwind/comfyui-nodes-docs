# Documentation
- Class name: Text2InputOr3rdOption
- Category: Mikey/Text
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The `output' function for the Text2InputOr3rdOption node is designed to process and return text input according to the logic of the condition. It uses the values in the hint provided to replace the placeholder in the input text and can return two separate text or a pair of text depending on a boolean sign.

# Input types
## Required
- text_a
    - The parameter 'text_a' is a string input that is expected to contain text. It is essential because it is one of the main inputs that will be processed and may be replaced with the value in the hint.
    - Comfy dtype: STRING
    - Python dtype: str
- text_b
    - The parameter 'text_b' is another string input that will be treated in the same way as 'text_a'. It is important because when 'use_text_c_for_both' is set to 'false', it determines secondary text output.
    - Comfy dtype: STRING
    - Python dtype: str
- text_c
    - The parameter 'text_c' is a string input that, if 'use_text_c_for_both' sign is set as 'true', it may be used as an alternative to 'text_a' and 'text_b'. It plays a key role in determining the final output of the node.
    - Comfy dtype: STRING
    - Python dtype: str
- use_text_c_for_both
    - The parameter 'use_text_c_for_both' is a boolean symbol that determines whether or not to use 'text_c' as an output of 'text_a' and'text_b'. It is essential to control the output behavior of nodes.
    - Comfy dtype: COMBO['true', 'false']
    - Python dtype: str
## Optional
- extra_pnginfo
    - The parameter 'extra_pnginfo' is an optional input that, when provided, contains additional information to search for and replace placeholders in text input.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Union[Dict, str]
- prompt
    - The parameter 'prompt' is an optional input that provides a structured set of values to replace placeholders in text input. It is essential for the text replacement process.
    - Comfy dtype: PROMPT
    - Python dtype: Union[Dict, str]

# Output types
- text_a
    - Output 'text_a' is the original 'text_a' input of the processing version in which placeholders have been replaced by the corresponding values in the reminder.
    - Comfy dtype: STRING
    - Python dtype: str
- text_b
    - Output'text_b' corresponds structurally to 'text_a' output, but comes from 'text_b' input. It is a text that is processed and replaced by placeholders.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class Text2InputOr3rdOption:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text_a': ('STRING', {'multiline': True, 'default': 'Text A'}), 'text_b': ('STRING', {'multiline': True, 'default': 'Text B'}), 'text_c': ('STRING', {'multiline': True, 'default': 'Text C'}), 'use_text_c_for_both': (['true', 'false'], {'default': 'false'})}, 'hidden': {'extra_pnginfo': 'EXTRA_PNGINFO', 'prompt': 'PROMPT'}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('text_a', 'text_b')
    FUNCTION = 'output'
    CATEGORY = 'Mikey/Text'

    def output(self, text_a, text_b, text_c, use_text_c_for_both, extra_pnginfo, prompt):
        text_a = search_and_replace(text_a, extra_pnginfo, prompt)
        text_b = search_and_replace(text_b, extra_pnginfo, prompt)
        text_c = search_and_replace(text_c, extra_pnginfo, prompt)
        if use_text_c_for_both == 'true':
            return (text_c, text_c)
        else:
            return (text_a, text_b)
```