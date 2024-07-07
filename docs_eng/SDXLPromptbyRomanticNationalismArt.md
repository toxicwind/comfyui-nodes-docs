# Documentation
- Class name: SDXLPromptbyRomanticNationalismArt
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node, based on the principles of romantic nationalistic art, creatively adapts the text to the specified style and enhances the subject content and emotional expression of the original text.

# Input types
## Required
- text_positive
    - Positive text input is essential because it sets the basis for style conversion. This is a text that will be enhanced and adapted to the chosen style.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input as a comparison of the positive text provides a point of comparison that can be integrated into the final style tips.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - Style parameters are essential in determining the subject and emotional direction of text conversion and in guiding nodes to produce a coherent output.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - The log option allows for selective visualization of the conversion process and provides insights on how nodes can adapt to their style.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output shows enhanced positive text and is now integrated into the chosen style for further use or analysis.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The negative post-adaptation text complements the positive output and provides a comparative perspective that enriches the overall thematic depth.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptbyRomanticNationalismArt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_romanticnat.json')
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