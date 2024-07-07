# Documentation
- Class name: SDXLPromptStylerbyLighting
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node is intended to enhance the presentation of tips by applying style templates, with the aim of improving the readability and attractiveness of the text.

# Input types
## Required
- text_positive
    - This parameter is a positive text that requires node stylement and is the basis for enhanced presentation.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - This parameter is a negative text that needs to be combined with the positive text to increase the ratio and depth of the final style output.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - This parameter determines the style template that you want to apply and significantly affects the overall aesthetic and tone of the style tips.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - This parameter controls whether intermediate steps and results are recorded and helps debug and understand the operation of nodes.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output is a styled positive text that enhances its visual appeal and effectiveness through the selected template.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - Output is a negative text that is styled, adds a positive text, and contributes to the comprehensiveness of the information that is styled.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyLighting:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_lighting.json')
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