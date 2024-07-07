# Documentation
- Class name: SDXLPromptStylerbySurrealism
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

By applying a style template inspired by hyperrealism, the node creatively redesigns input text tips to enhance the expression and artistic quality of the content generated.

# Input types
## Required
- text_positive
    - Positive text input serves as the basis for a styled process, the content of which is converted to reflect the super-realistic style chosen.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input is used to compare and refine style to ensure that the final output is consistent and compatible with the desired aesthetic.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - The chosen style determines the ultra-realistic approach applied to the text, guides the transformation process and shapes the creative direction.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - This switch determines whether processes and results are recorded and provides insight into the styled process and the generation of tips.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output shows a positive style of text and now incorporates the selected hyperrealist elements for further use or demonstration.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output includes a negative styled text, which complements the positive output and contributes to the overall consistency and depth of the styled content.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbySurrealism:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_surrealism.json')
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