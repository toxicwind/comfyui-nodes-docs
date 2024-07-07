# Documentation
- Class name: promptConcat
- Category: EasyUse/Prompt
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

This node, which facilitates the integration of text input, provides a simple way to combine strings into a single output. It emphasizes simplicity and ease of use and is well suited to the context in which the text is operated without the need for complex processing.

# Input types
## Required
- prompt1
    - The first text input is used as an initial segment during the consolidation process. It is essential because it sets a starting point for the output of the combined text.
    - Comfy dtype: STRING
    - Python dtype: str
- prompt2
    - The second text input, which is combined with the first input. It is essential to complete the text sequence and form the final output.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- separator
    - A string that is inserted between two text inputes is used to separate them in the final output. It plays a role in building the puzzle text and improving readability.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- prompt
    - The output of the text after two input spells may contain separator. It represents the consolidated and structured information in the input.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class promptConcat:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}, 'optional': {'prompt1': ('STRING', {'multiline': False, 'default': '', 'forceInput': True}), 'prompt2': ('STRING', {'multiline': False, 'default': '', 'forceInput': True}), 'separator': ('STRING', {'multiline': False, 'default': ''})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('prompt',)
    FUNCTION = 'concat_text'
    CATEGORY = 'EasyUse/Prompt'

    def concat_text(self, prompt1='', prompt2='', separator=''):
        return (prompt1 + separator + prompt2,)
```