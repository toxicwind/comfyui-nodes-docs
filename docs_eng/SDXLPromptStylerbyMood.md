# Documentation
- Class name: SDXLPromptStylerbyMood
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node is designed to enhance the thematic expression of text input based on emotional style. It uses predefined styles to creatively modify the emotions of the text provided, and aims to enrich the overall narrative and emotional depth of the content.

# Input types
## Required
- text_positive
    - Positive text input is essential for setting the underlying emotions of the hint. It is the basis for an enhanced emotional style that significantly influences the tone and emotional resonance of the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input is essential to provide an emotional comparison with the positive text. It allows nodes to create more subtle and balanced emotional expressions that help to strategize the complexity and depth of the hint.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - Style parameters play a key role in determining the aesthetic and emotional direction of styled tips. They guide nodes in selecting appropriate emotional-based templates that are critical to achieving the desired themes and style results.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - Log hint parameters facilitate debugging and monitoring by selectively enabling the records of the reminder generation process. This function helps to understand the operation of nodes and ensures transparency in style conversions.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output provides a positive styled version of the text entered, reflecting the increased mood and style chosen. This result is very important in conveying emotional resonance and consistent narratives.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output provides a negative styled version of the input text, providing a comparative view of the positive hint. It plays a crucial role in building a comprehensive emotional scope and depth of the styled content.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyMood:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_mood.json')
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