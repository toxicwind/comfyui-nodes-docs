# Documentation
- Class name: SDXLPromptStylerbyFilter
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node is based on the provision of text input, both positive and negative, dynamically designs the tips and uses the specified style template to generate refined and targeted messages.

# Input types
## Required
- text_positive
    - Positive text input is very important because it sets the tone of expected messages. It is used to create a refined and targeted positive hint.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input is essential to define the comparative elements that should be avoided in the message. It helps to create a careful hint of balance, both positive and negative.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - Style parameters are essential in determining the overall aesthetic and conveyance manner in which a hint is generated. They guide the conversion of input text into a coherent and consistent output.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - The log hint option allows an optional log record of the reminder generation process, providing transparency and insight into the reminder style and how it is constructed.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output positive hint text is the result of the style design process, which encapsifies the desired message in a refined and attractive manner.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output negative hint text provides a balance for the positive tip, ensuring that the message is comprehensive and addresses potential concerns or objections.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyFilter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_filter.json')
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