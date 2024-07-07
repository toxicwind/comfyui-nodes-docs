# Documentation
- Class name: SDXLPromptStylerHorror
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The purpose of the node is to refine texttips based on a given terrorist theme and to enhance the particular mood and atmosphere in which they are presented.

# Input types
## Required
- text_positive
    - Positive text input is essential for setting the basic mood for a terrorist theme. It provides the starting point for a style shift.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text entry is essential to contrast positive text, providing depth to the subject of terror by increasing tension and conflict.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - Style parameters are essential in determining the specific terrorist themes to be applied to the text and guide the overall aesthetics of the output.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - The log hint option allows for a selective recording of the conversion process, which is useful for debugging and understanding the operation of nodes.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output provides a positive version of the terrorist theme, which has been enhanced through the chosen theme to create a immersion experience.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output provides a negative-style text on the subject of terror, which complements the positive text and deepens the overall culture of terror.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerHorror:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_horror.json')
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