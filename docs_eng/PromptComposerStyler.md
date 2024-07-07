# Documentation
- Class name: PromptComposerStyler
- Category: AI WizArt/Prompt Composer Tools/Deprecated
- Output node: False
- Repo Ref: https://github.com/florestefano1975/comfyui-prompt-composer.git

PromptComposerStyler nodes are designed to enhance the creative process by applying style elements that allow the integration of style preferences and weights so that users can fine-tune the artistic direction of the text. The function of the node is focused on the concept of style applications, with the aim of enhancing the original text through specified aesthetics, thus contributing to the overall theme and sound quality of the work.

# Input types
## Required
- text_in_opt
    - The 'text_in_opt' parameter is an optional input that allows users to provide the basic text that will apply the style elements. It is important as the basis for node operations and determines what will be enhanced by art.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - The `style' parameter is essential to define the artistic style that will be integrated into the text. It is a necessary input that determines the node to be applied to the aesthetic features of the text, thus affecting the final creative output.
    - Comfy dtype: STRING
    - Python dtype: str
- style_weight
    - The `style_weight' parameter is essential for adjusting the strength of the application style. It allows fine control over the extent to which style is reflected in the text and ensures a balance between original content and style coverage.
    - Comfy dtype: FLOAT
    - Python dtype: float
- active
    - The 'active'parameter is a boolean symbol that determines whether to start the style application process. When set to True, it activates the function of the node and allows the style to be applied to the text.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- text_out
    - The 'text_out'output parameter represents the final text after the application of the style element. It contains the creative contributions of nodes and shows the results of the style application process.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class PromptComposerStyler:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'optional': {'text_in_opt': ('STRING', {'forceInput': True})}, 'required': {'style': (styles, {'default': styles[0]}), 'style_weight': ('FLOAT', {'default': 1, 'step': 0.05, 'min': 0, 'max': 1.95, 'display': 'slider'}), 'active': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('text_out',)
    FUNCTION = 'promptComposerStyler'
    CATEGORY = 'AI WizArt/Prompt Composer Tools/Deprecated'

    def promptComposerStyler(self, text_in_opt='', style='-', style_weight=0, active=True):
        prompt = []
        if text_in_opt != '':
            prompt.append(text_in_opt)
        if style != '-' and style_weight > 0 and active:
            prompt.append(f'({style} style:{round(style_weight, 2)})')
        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return (prompt,)
        else:
            return ('',)
```