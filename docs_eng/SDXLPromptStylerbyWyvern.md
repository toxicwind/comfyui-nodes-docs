# Documentation
- Class name: SDXLPromptStylerbyWyvern
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node is designed to style the hint based on a predefined template, enhancing the presentation and appeal of the content. It is designed to create a coherent and thematically consistent output by combining positive and negative text input with the selected style.

# Input types
## Required
- text_positive
    - Positive text input is essential to set the positive tone of the hint. It is the basis for the application of style elements from the selected template and significantly affects the validity of the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input complements the positive text by providing comparative content. Its integration with the style template is essential to create a balanced and nuanced reminder that addresses potential rebuttal points or limitations.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - Style parameters play a key role in determining the overall aesthetic and thematic orientation of the hint. They guide the selection of templates and determine the formatting and presentation of both positive and negative text.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - The log hint parameter allows an optional log recording of the process. When enabled, it provides transparency in node operations, helps to debug and ensures that the required styles are realized.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output is a styled text of a positive hint, which is formatted according to the selected style template and the positive text entered. This output is essential for node enhancement of the purpose of the content presentation.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output includes a styled text of a negative hint that complements the positive output by addressing potential rebuttals or limitations. It is a key component of the node function, ensuring a comprehensive and balanced presentation.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyWyvern:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_wyvern.json')
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