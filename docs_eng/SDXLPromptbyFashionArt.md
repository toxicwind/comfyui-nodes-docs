# Documentation
- Class name: SDXLPromptbyFashionArt
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node is designed to enhance the creative process by generating fashion inspired tips based on positive and negative text input. It uses predefined style sets to produce tips that inspire designers and artists and aims to promote innovation and diversity in fashion creation.

# Input types
## Required
- text_positive
    - Positive text input, as a basis for creative tips, provides a constructive and exciting message that will be integrated into the ultimate style tips. It is essential for setting the tone and direction of fashion inspiration.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input is used to contrast positive information to add depth and complexity to the final hint. It helps to create a more detailed and attractive fashion concept by emphasizing areas that need to be avoided or overcome.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - A style parameter is essential to guide text input into a consistent and thematic fashion reminder. It influences the language, tone and structure of the output and ensures that the ultimate hint is consistent with the chosen fashion aesthetics.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - The log hint option allows optional recording of the alerts generated, which is very useful for review and improvement. It helps track the creation process and ensures that nodes function in accordance with user expectations.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output provides a positive hint that is refined and styled, combining user input and selected fashion styles. It is a key component in driving the creative direction and serving as a catalyst for further fashion design exploration.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The negative hint output complements the positive hint by providing comparative points and additional considerations. It presents a more comprehensive view of fashion concepts, enriches the overall creative output and encourages a balanced and informed approach to design.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptbyFashionArt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_fashion.json')
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