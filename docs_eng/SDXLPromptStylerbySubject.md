# Documentation
- Class name: SDXLPromptStylerbySubject
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The SDXLPromptStylerbySubject node is designed to style the tips according to the given theme. It accepts both positive and negative text input and uses the selected style to generate style tips. The node records the process for review and enhances the customization and individualization of the tips.

# Input types
## Required
- text_positive
    - The text_positive parameter is a string that represents the positive side of the hint. It is essential to define the optimistic tone of the styled output.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - The text_negative parameter is a string that represents the negative side of the hint. It plays a key role in shaping the pessimistic tone of the styled output.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - The style parameter determines the style approach applied to the hint. It is a key factor in the overall style and presentation of the style.
    - Comfy dtype: STRING
    - Python dtype: str
- log_prompt
    - The log_prompt parameter is an option that allows you to record a styled process. It can be set to 'Yes' so that you can review the conversion process in detail.
    - Comfy dtype: COMBO['No', 'Yes']
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The positionive_prompt_text_g output is a stylish, positive text of the reminder, reflecting the style of the application and the optimistic view of the input.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - Negative_prompt_text_g output is a stylish negative text of the reminder, reflecting the style of the application and the pessimistic view of the input.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbySubject:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_subject.json')
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