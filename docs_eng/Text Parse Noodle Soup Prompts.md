# Documentation
- Class name: WAS_Text_Parse_NSP
- Category: WAS Suite/Text/Parse
- Output node: True
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Text_Parse_NSP node is designed to process and convert text according to the specified mode. It uses the function of 'Noodle Soup Products' for creative text operations, or for more structured processing using wildcard replacements. This node is essential for tasks that require text resolution or enhancement, providing a multifunctional solution for various text-based applications.

# Input types
## Required
- text
    - The text parameter is the core input of the node. It determines the content that will be parsed and converted. The operation of the node relies heavily on this input, making it essential to achieve the desired output.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- mode
    - Model parameters determine the solution strategy to be used for nodes. They can be set to be creative for 'Noodle Soup Projects', or to be set for 'Wildcards' for more structured text operations. This parameter is essential for guiding node handling behaviour.
    - Comfy dtype: STRING
    - Python dtype: str
- noodle_key
    - The noodle_key parameter is used as a separator in the text under the 'Noodle Soup Projects' mode. It marks the beginning and end of a term that can be replaced or operated, and thus plays an important role in the process.
    - Comfy dtype: STRING
    - Python dtype: str
- seed
    - Seed parameter is an optional integer that can be used to introduce randomity in the analysis process. It ensures the recurrence of results by providing a consistent starting point for random operations.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- new_text
    - The new_text output represents the text processed after the node application of the specified resolution method. It is the final result of the node function and is valuable for follow-up operations or analysis.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_Parse_NSP:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mode': (['Noodle Soup Prompts', 'Wildcards'],), 'noodle_key': ('STRING', {'default': '__', 'multiline': False}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'text': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False})}}
    OUTPUT_NODE = True
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'text_parse_nsp'
    CATEGORY = 'WAS Suite/Text/Parse'

    def text_parse_nsp(self, text, mode='Noodle Soup Prompts', noodle_key='__', seed=0):
        if mode == 'Noodle Soup Prompts':
            new_text = nsp_parse(text, seed, noodle_key)
            cstr(f'Text Parse NSP:\n{new_text}').msg.print()
        else:
            new_text = replace_wildcards(text, None if seed == 0 else seed, noodle_key)
            cstr(f'CLIPTextEncode Wildcards:\n{new_text}').msg.print()
        return (new_text,)
```