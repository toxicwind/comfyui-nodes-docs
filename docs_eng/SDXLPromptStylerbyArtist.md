# Documentation
- Class name: SDXLPromptStylerbyArtist
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node is designed to modify text tips according to the style of the selected artist to enhance the creative process by integrating artistic nuances into the production of content.

# Input types
## Required
- text_positive
    - Positive text input is essential because it sets the basis for nodes and ensures that the tips generated are consistent with the desired theme.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input as a comparison of the positive text allows nodes to fine-tune style by excluding unwanted elements.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - Style parameters are essential because they determine the artistic influence to be applied to the text and shape the overall aesthetics of the output.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - The log options allow internal processes to be monitored for nodes and provide insights on how to apply styles to tips.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output provides a positive style texttip that reflects the style of the chosen artist and enhances creative messages.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output provides a negative style texttip that complements the positive output by providing a comparative perspective.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyArtist:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_artists.json')
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