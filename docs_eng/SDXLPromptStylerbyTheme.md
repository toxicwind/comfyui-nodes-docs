# Documentation
- Class name: SDXLPromptStylerbyTheme
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The SDXLPromptStylerby Theme class is designed to style tips according to predefined themes. It uses the JSON file, which contains styles and templates, to generate styled positive and negative hints and enhances the thematic consistency of text input.

# Input types
## Required
- text_positive
    - The text_positive parameter is a string that represents the positive content of the hint. It is essential because it forms the basis for a stylish positive hint output.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - The text_negative parameter is a string that represents the negative content of the hint. It plays a key role in shaping a styled negative hint output.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - The style parameter determines the theme style that should be applied to the hint. It is a key factor in the appearance and tone custom.
    - Comfy dtype: STRING
    - Python dtype: str
- log_prompt
    - Log_prompt parameters are optional settings that, when set to 'Yes', enable log records of the stylishing process to be used for debug or review purposes.
    - Comfy dtype: COMBO['No', 'Yes']
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The positionive_prompt_text_g output is a stylish, positive hint text designed to be consistent with the specified theme and to enhance the overall appeal of the information.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - Negative_prompt_text_g output is a styled negative hint text designed to reflect a given theme and maintain the thematic integrity of the message.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyTheme:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_themes.json')
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