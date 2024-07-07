# Documentation
- Class name: SDXLPromptStylerbyCyberpunkSurrealism
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

By applying the template selected from the selection set, the node changes the input text creatively to a style-enhanced hint, generating an aestheticly consistent and thematically rich content.

# Input types
## Required
- text_positive
    - Positive text input, as a basis for style conversion, provides content that will be enhanced and shaped by the selected template.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input is used to supplement the positive text, providing the comparison and depth of the ultimate style tips.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - Style selection is essential because it determines the themes and aesthetic orientations of the suggested styles and guides the conversion process.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - The log-book preferences determine whether intermediate steps and results are to be exported and help understand the operation of nodes and the process of strategizing.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output shows a positive styled text, which is the result of applying the selected template to the original input and which now enhances the theme and style elements.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output includes negative styled text, which provides comparative elements for the positive text and enriches the overall styled output.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyCyberpunkSurrealism:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_cs.json')
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