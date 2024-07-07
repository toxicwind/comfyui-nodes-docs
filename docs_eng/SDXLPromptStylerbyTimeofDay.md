# Documentation
- Class name: SDXLPromptStylerbyTimeofDay
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node is designed in a styled fashion according to the current dynamics of time and enhances the interactive experience of users by customizing the presentation of information according to the context of the current time.

# Input types
## Required
- text_positive
    - Positive text input is very important because it sets a baseline of positive emotions that are customised and displayed at the chosen time.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input is essential to provide a sense of comparison with the positive text, allowing nodes to balance the overall tone of style tips.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - Style parameters play a key role in determining the style to customise tips according to time, affecting the overall aesthetics and emotions of the output.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - Recording reminder parameters are practical tools for developers and testers that enable them to export detailed information on the process for debugging and validation.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output contains text in a positive style that has been formatted to match the selected time and enhances the user's experience through customized messages.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output, which includes negative-style text, complements the positive text by providing contrasting emotions, and helps to provide a nuanced display of tips.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyTimeofDay:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_tod.json')
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