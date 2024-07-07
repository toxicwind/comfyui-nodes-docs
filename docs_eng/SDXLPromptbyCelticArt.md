# Documentation
- Class name: SDXLPromptbyCelticArt
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The SDXLPromptbyCelticArt node is designed to generate styled text tips based on Celtic art themes. It creatively combines both positive and negative text input and selected styles to generate thematic tips. The node plays a key role in enhancing the thematic richness of text output for various applications, such as art generation or theme text styles.

# Input types
## Required
- text_positive
    - The text_positive parameter is essential to define the positive aspects of the hint. It significantly influences the tone and content of the eventual styled hint and ensures that the output is consistent with the required positive subject element.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Text_negative parameters allow negative aspects to be included in the hint. This is essential for providing contrasts and depths to styled text and enriches the overall subject expression.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - The style parameter determines the style of the subject matter of the Celtic art to be applied to the hint. It is a key factor in shaping the aesthetic and thematic outcomes of the text, ensuring that it resonates with the chosen theme of the art.
    - Comfy dtype: STRING
    - Python dtype: str
- log_prompt
    - Log_prompt parameters are optional, controlling whether to record the intermediate steps of the hint styler process. This may be useful for users who debug or want to see the conversion process.
    - Comfy dtype: COMBO['No', 'Yes']
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The postive_prompt_text_g output represents the final stylish text of the positive tip, which is the key element of the node function. It contains the creative integration of the input text with the selected style, resulting in a subject-rich text output.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - Negative_prompt_text_g output provides the final styled negative hint text, which complements the positive hint. It plays an important role in adding complexity and nuances to the overall reminder, contributing to more comprehensive thematic performance.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptbyCelticArt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_celticart.json')
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