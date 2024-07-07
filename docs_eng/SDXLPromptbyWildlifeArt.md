# Documentation
- Class name: SDXLPromptbyWildlifeArt
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node is designed to modify texttips according to selected wildlife art styles to enhance the creative process by generating thematically based positive and negative tips.

# Input types
## Required
- text_positive
    - Positive text input is essential to generate a positive indication of thematicization, which is the basis of the stylistic process.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input is essential to create contrasting negative hints, which complement positive hints and enrich overall subject expression.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - Style selection parameters are essential because they determine the art theme to be applied to both positive and negative indications, and guide the aesthetics of the output as a whole.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - Log parameters facilitate debugging and monitoring by providing, on an optional basis, a printout of detailed styleing processes and results.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output positive hint is a creatively enhanced text that reflects the chosen wildlife art style as the basis for further content development of the otatic.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The negative hint of output provides a contrasting thematic element, provides a face-to-face for the positive hint and enriches the narrative.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptbyWildlifeArt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_wildlife.json')
        self.json_data = read_json_file(file_path)
        styles = read_sdxl_styles(self.json_data)
        return {'required': {'text_positive': ('STRING', {'default': '', 'multiline': True}), 'text_negative': ('STRING', {'default': '', 'multiline': True}), 'style': (styles,), 'log_prompt': (['No', 'Yes'], {'default': 'No'})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('positive_prompt_text_g', 'negative_prompt_text_g')
    FUNCTION = 'prompt_styler'
    CATEGORY = 'Style Prompts'

    def prompt_styler(self, text_positive, text_negative, style, log_prompt):
        (positive_prompt, negative_prompt) = read_sdxl_templates_replace_and_combine(self.json_data, style, text_positive, text_negative)
        if log_prompt == 'Yes':
            print(f'style: {style}')
            print(f'text_positive: {text_positive}')
            print(f'text_negative: {text_negative}')
            print(f'positive_prompt: {positive_prompt}')
            print(f'negative_prompt: {negative_prompt}')
        return (positive_prompt, negative_prompt)
```