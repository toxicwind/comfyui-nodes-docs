# Documentation
- Class name: SDXLPromptStylerbyQuantumRealism
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node is intended to fine-tune tips according to predefined styles, enhancing the theme and aesthetic presentation of the text without changing its core messages.

# Input types
## Required
- text_positive
    - Positive text input is essential to generate a hint of a positive frame. It is the basis for applying the style elements.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input is essential to provide elements that are comparable to the positive text, enabling nodes to create more detailed and balanced hints.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - Style parameters play a key role in determining the overall aesthetic and thematic orientation of styled tips and guide the transition process.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - The log hint option allows optional recording of the reminder generation process, which is very useful for debugging and understanding the operation of nodes.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output provides a positive hint of enhanced style, reflecting the integration of input text with the selected style.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output provides a more stylish negative hint, provides a point of comparison for the positive hint and helps in its full presentation.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyQuantumRealism:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_qr.json')
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