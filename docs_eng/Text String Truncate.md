# Documentation
- Class name: WAS_Text_String_Truncate
- Category: WAS Suite/Text/Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Text_String_Truncate' method is designed to reduce the input string to a specified length, either by character or word, from the beginning or at the end of the string. This method is used to manage the text length in a way that preserves the integrity of the information and ensures that the cut-off text adapts to the required limitations without losing important content.

# Input types
## Required
- text
    - The parameter'text' is the main input of the node, which means the string that is to be cut off. This is a key element, because the node's operational focus is to reduce the length of the text while retaining its core information.
    - Comfy dtype: STRING
    - Python dtype: str
- truncate_by
    - The parameter 'truncate_by' determines the unit to be cut off, which may be a character or a word. This option significantly affects the way the text is reduced and which part of the text is retained.
    - Comfy dtype: COMBO['characters', 'words']
    - Python dtype: str
- truncate_from
    - The parameter 'truncate_from' decides whether the cut should start at the end or at the beginning of the text. This decision directly affects the visibility and context of the remaining text after the cut.
    - Comfy dtype: COMBO['end', 'beginning']
    - Python dtype: str
- truncate_to
    - The parameter 'truncate_to' specifies the maximum length of text that should be cut off. This is a key setting because it defines the ultimate length of a string after a cutoff process.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- text_b
    - The parameter 'text_b' is an optional additional string that can be used to cut off. It provides flexibility to process multiple strings simultaneously, increasing the usefulness of nodes in the text management landscape.
    - Comfy dtype: STRING
    - Python dtype: str
- text_c
    - The parameter 'text_c' is another optional string used to cut off, similar to the function 'text_b'. It expands the ability of nodes to process more text data in a single operation.
    - Comfy dtype: STRING
    - Python dtype: str
- text_d
    - The parameter'text_d' is the last optional string in the node cutoff process. It further expands the node's ability to manage more text at the same time.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- truncated_text
    - The output parameter 'Trust_text' represents the result of the cut-off process. It is a shortened version of the input text that meets the specified limit, ensuring that the output text is simple and relevant.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str
- truncated_text_b
    - Output parameter 'Trusted_text_b' corresponds to a cutout version that you can choose to enter 'text_b'. It provides the same function as 'Trusted_text', but applies to the second optional string.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str
- truncated_text_c
    - The output parameter'Trust_text_c'like'Trust_text_b', provides the result of the third optional string'text_c'. It ensures that nodes can process multiple strings in a single call.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str
- truncated_text_d
    - The output parameter 'Trusted_text_d' is the final output of the optional string 'text_d'. It completes the ability of the node to cut multiple strings once and for all and provides a comprehensive text management solution.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_String_Truncate:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': ('STRING', {'forceInput': True}), 'truncate_by': (['characters', 'words'],), 'truncate_from': (['end', 'beginning'],), 'truncate_to': ('INT', {'default': 10, 'min': -99999999, 'max': 99999999, 'step': 1})}, 'optional': {'text_b': ('STRING', {'forceInput': True}), 'text_c': ('STRING', {'forceInput': True}), 'text_d': ('STRING', {'forceInput': True})}}
    RETURN_TYPES = (TEXT_TYPE, TEXT_TYPE, TEXT_TYPE, TEXT_TYPE)
    FUNCTION = 'truncate_string'
    CATEGORY = 'WAS Suite/Text/Operations'

    def truncate_string(self, text, truncate_by, truncate_from, truncate_to, text_b='', text_c='', text_d=''):
        return (self.truncate(text, truncate_to, truncate_from, truncate_by), self.truncate(text_b, truncate_to, truncate_from, truncate_by), self.truncate(text_c, truncate_to, truncate_from, truncate_by), self.truncate(text_d, truncate_to, truncate_from, truncate_by))

    def truncate(self, string, max_length, mode='end', truncate_by='characters'):
        if mode not in ['beginning', 'end']:
            cstr("Invalid mode. 'mode' must be either 'beginning' or 'end'.").error.print()
            mode = 'end'
        if truncate_by not in ['characters', 'words']:
            cstr("Invalid truncate_by. 'truncate_by' must be either 'characters' or 'words'.").error.print()
        if truncate_by == 'characters':
            if mode == 'beginning':
                return string[:max_length] if max_length >= 0 else string[max_length:]
            else:
                return string[-max_length:] if max_length >= 0 else string[:max_length]
        words = string.split()
        if mode == 'beginning':
            return ' '.join(words[:max_length]) if max_length >= 0 else ' '.join(words[max_length:])
        else:
            return ' '.join(words[-max_length:]) if max_length >= 0 else ' '.join(words[:max_length])
```