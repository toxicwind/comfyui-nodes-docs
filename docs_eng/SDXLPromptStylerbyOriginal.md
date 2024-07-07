# Documentation
- Class name: SDXLPromptStylerbyOriginal
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node is intended to be a glorified reminder based on a predefined template that enhances the performance and attractiveness of the content.

# Input types
## Required
- text_positive
    - Positive text input is essential because it forms the basis for a glorification tip. This is the text that will be formatted according to the selected style.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input is essential to provide elements comparable to the positive text, allowing for more detailed and comprehensive tips.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - Style parameters are essential in determining the aesthetic and structural elements to be applied to the reminder and guide the overall look and feeling.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - The log-record option allows for a selective process of recording alert generation, which is very useful for debugging and review purposes.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output provides a positive hint after beautification, which is a formatted and enhanced version of the original input text.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output provides a glorified negative hint, provides a complementary perspective to the positive tip, and enriches the overall information.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyOriginal:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_original.json')
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