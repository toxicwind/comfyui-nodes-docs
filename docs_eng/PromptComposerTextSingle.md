# Documentation
- Class name: PromptComposerTextSingle
- Category: AI WizArt/Prompt Composer Tools
- Output node: False
- Repo Ref: https://github.com/florestefano1975/comfyui-prompt-composer.git

The node creatively combines text input, adjusted to the given weights and conditions to produce refined output. It is a tool for customizing text content, emphasizing the importance of each input in shaping the final work.

# Input types
## Required
- text
    - The main text input is essential to the operation of the node. It forms the core of the group and is essential for generating the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- weight
    - This parameter affects the way the text is adjusted in the group. Higher weight means a greater emphasis on the corresponding text segments.
    - Comfy dtype: FLOAT
    - Python dtype: float
- active
    - This symbol determines whether to apply weight parameters to the text. It has control to re-modify the activation of the function.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- text_in_opt
    - This optional input can be included as an initial element in a combination. Its existence enriches the text base and may add depth to the output.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- text_out
    - Output represents the final package text, reflecting the integration of all inputs and their corresponding adjustments.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class PromptComposerTextSingle:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'optional': {'text_in_opt': ('STRING', {'forceInput': True})}, 'required': {'text': ('STRING', {'multiline': True}), 'weight': ('FLOAT', {'default': 1, 'min': 0, 'max': 1.95, 'step': 0.05, 'display': 'slider'}), 'active': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('text_out',)
    FUNCTION = 'promptComposerTextSingle'
    CATEGORY = 'AI WizArt/Prompt Composer Tools'

    def promptComposerTextSingle(self, text_in_opt='', text='', weight=0, active=True):
        prompt = []
        if text_in_opt != '':
            prompt.append(text_in_opt)
        if text != '' and weight > 0 and active:
            prompt.append(applyWeight(text, weight))
        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return (prompt,)
        else:
            return ('',)
```