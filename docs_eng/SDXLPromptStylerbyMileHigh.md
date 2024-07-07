# Documentation
- Class name: SDXLPromptStylerbyMileHigh
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The SDXLPromptStylerbyMireHigh node is designed to style texttips according to predefined styles. It accepts both positive and negative text input and selected style identifiers, which generate styled tips. The node can also record input and output for review, which is very useful for debugging or transparency purposes.

# Input types
## Required
- text_positive
    - Positive text input is essential for the optimism aspect of definitional hints. It significantly influences the tone and direction of styled output.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input contrasts with the positive text and provides an opposing side that can be used to refine the style of the reminder.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - Style parameters determine the style template that should be applied to the text. It is essential to achieve the desired style of reminder according to the user's needs.
    - Comfy dtype: STRING
    - Python dtype: str
- log_prompt
    - When the log_prompt parameter is set to 'Yes', the record of the reminder process is enabled. This may be useful for monitoring and reviewing the operation of the nodes.
    - Comfy dtype: COMBO['No', 'Yes']
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The positionive_prompt_text_g output represents a styled positive texttip, which is a key result of node implementation.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - Negative_prompt_text_g output provides a styled negative texttip, which is complemented by a positive tip to give the full style output.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyMileHigh:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_mh.json')
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