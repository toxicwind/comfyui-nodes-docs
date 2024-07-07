# Documentation
- Class name: SDXLPromptbyStreetArt
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node matches the input text to the specified style and enhances the subject content by extracting style elements from street art.

# Input types
## Required
- text_positive
    - The parameter provides a positive text that will be styled according to the chosen street art theme as a basis for the creative adaptation process.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - This parameter contains negative text in contrast to the positive text, allowing nodes to focus on the required style elements without interference.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - This parameter defines the street art style to be applied and directs nodes to select appropriate templates and artistic elements for text conversion.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - This parameter enables or disables log records of the styled process and provides a method for tracking any problems that may arise from conversion and debugging.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output consists of a text with a positive style, which is converted to reflect the selected street art style and enhances the expression of the theme and the attractiveness of the art.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - Output provides negative styled text as a cross-reference to the positive text, ensuring clarity and focus at the end.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptbyStreetArt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_street.json')
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