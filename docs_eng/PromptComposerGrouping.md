# Documentation
- Class name: PromptComposerGrouping
- Category: AI WizArt/Prompt Composer Tools
- Output node: False
- Repo Ref: https://github.com/florestefano1975/comfyui-prompt-composer.git

This node creatively processes the text by adjusting the weight and structure of the input text to generate modified tips for various AI applications.

# Input types
## Required
- text_in
    - The input text is the basis for node operations, and its content and structure directly influence the output results.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- weight
    - The weight parameters are fine-tuned to apply to the conversion of the input text, affecting the emphasis and presentation of the creation tips.
    - Comfy dtype: FLOAT
    - Python dtype: float
- active
    - The activation sign determines whether the processing of nodes should be used for inputting the text, thereby controlling the execution of the nodes.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- text_out
    - The output text is the result of node processing and contains a modified hint to be used for AI applications.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class PromptComposerGrouping:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text_in': ('STRING', {'forceInput': True}), 'weight': ('FLOAT', {'default': 1, 'step': 0.05, 'min': 0, 'max': 1.95, 'display': 'slider'}), 'active': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('text_out',)
    FUNCTION = 'promptComposerGrouping'
    CATEGORY = 'AI WizArt/Prompt Composer Tools'

    def promptComposerGrouping(self, text_in='', weight=0, active=True):
        prompt = text_in
        if text_in != '' and weight > 0 and active:
            prompt = applyWeight(text_in, weight)
        return (prompt,)
```