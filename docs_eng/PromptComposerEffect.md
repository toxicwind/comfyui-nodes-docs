# Documentation
- Class name: PromptComposerEffect
- Category: AI WizArt/Prompt Composer Tools/Deprecated
- Output node: False
- Repo Ref: https://github.com/florestefano1975/comfyui-prompt-composer.git

The node is designed to enhance text input by applying a styled effect, allowing for more attractive and diverse content. It emphasizes the role of node in text conversion without going into details of implementation.

# Input types
## Required
- effect
    - This parameter determines the type of effect to be applied to the text and fundamentally changes the style and tone of the output.
    - Comfy dtype: COMBO[effects]
    - Python dtype: str
- effect_weight
    - This parameter adjusts the intensity of application effects, affects the extent of conversion and the characteristics of the end result.
    - Comfy dtype: FLOAT
    - Python dtype: float
- active
    - This parameter controls whether the effects are applied and determines whether the function of the node is active in text processing.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- text_in_opt
    - This parameter serves as the basic text for the application of styled effects. It is important to provide the content that nodes are to be converted.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- text_out
    - The output represents the application of the conversion text with effect, showing the contribution of nodes to content enhancement.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class PromptComposerEffect:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'optional': {'text_in_opt': ('STRING', {'forceInput': True})}, 'required': {'effect': (effects, {'default': effects[0]}), 'effect_weight': ('FLOAT', {'default': 1, 'step': 0.05, 'min': 0, 'max': 1.95, 'display': 'slider'}), 'active': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('text_out',)
    FUNCTION = 'promptComposerEffect'
    CATEGORY = 'AI WizArt/Prompt Composer Tools/Deprecated'

    def promptComposerEffect(self, text_in_opt='', effect='-', effect_weight=0, active=True):
        prompt = []
        if text_in_opt != '':
            prompt.append(text_in_opt)
        if effect != '-' and effect_weight > 0 and active:
            prompt.append(f'({effect} effect:{round(effect_weight, 2)})')
        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return (prompt,)
        else:
            return ('',)
```