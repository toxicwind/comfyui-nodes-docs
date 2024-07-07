# Documentation
- Class name: SDXLPromptbyVikingArt
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node is based on a given text input, both positive and negative, using a specified style dynamic from the Viking art theme to generate style tips. It is designed to enhance the creative process by integrating the theme elements into the content generated.

# Input types
## Required
- text_positive
    - Positive text input is essential to set the positive tone for generating the hint. It provides the basic elements that will be enhanced in style to match the chosen Viking art theme.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input is essential to the aspects that should be avoided in the definition creation hint. It helps to optimize output and ensures that it follows the desired thematic direction, rather than containing unwanted elements.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - Style parameters play a key role in determining the thematic direction of the hint. They guide nodes in choosing the appropriate template and language elements to match the chosen Viking style of art.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - The log hint parameter allows optional recording of the reminder generation process. When enabled, it provides valuable insights about how the nodes function and the conversion that should be applied to the input text.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output, which contains a positive styled reminder text, has been enhanced through the thematic elements of the Viking style of art, providing a creative and attractive outcome.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output of the hint text, which is negatively styled, has been adjusted to remove the elements that are not required and to ensure that the final output meets the specified subject requirements.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptbyVikingArt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_viking.json')
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