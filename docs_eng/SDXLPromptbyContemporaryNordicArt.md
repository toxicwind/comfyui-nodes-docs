# Documentation
- Class name: SDXLPromptbyContemporaryNordicArt
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

SDXLPromptbyContemporaryNodicArt is designed to generate and stylish tips based on contemporary Nordic styles of art. It creatively combines positive and negative text input with selected artistic styles to produce aesthetic inspirational tips that can be used for various creative or descriptive purposes.

# Input types
## Required
- text_positive
    - The text_positive parameter is the key input for the node, providing a positive background or confirmation that the art is integrated into the reminder. It significantly influences the tone and content of the reminder, ensuring that it is consistent with the positive information required.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - The text_negative parameter allows for the inclusion of a negative background, which allows for artistic comparisons or conversions in the reminder. Although not necessary, it can add depth to the final output by providing a view relative to the positive text.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - The style parameter is necessary because it determines the particular contemporary Nordic style of art that will be applied to the hint. Style selection directly affects the aesthetic and subject matter elements that generate the hint and guides its overall artistic direction.
    - Comfy dtype: STRING
    - Python dtype: str
- log_prompt
    - log_prompt parameters are an optional switch, and when set to 'Yes', enable the record of the reminder generation process. This is very useful for debuging or viewing the intermediate steps taken to create the final tip.
    - Comfy dtype: COMBO['No', 'Yes']
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - A positive_prompt_text_g output contains a positive node-generated styled text. It represents a combination of input text and the selected Nordic style of art that can be used for a variety of applications.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - Negative_prompt_text_g output provides a stylish text of the negative hint, which complements the positive hint by providing a point of view for comparison or conversion. It is an integral part of the node output and helps to generate the comprehensiveness of the hint.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptbyContemporaryNordicArt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_contempnordic.json')
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