# Documentation
- Class name: SDXLPromptStylerbyFantasySetting
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The SDXLPromptStylerbyFantasySetting node is designed to style tips based on fantasy settings. It creatively combines positive and negative text input with the chosen style, generating style tips consistent with the chosen fantasy theme. The node plays a crucial role in enhancing thematic coherence and participation in the fantasy context.

# Input types
## Required
- text_positive
    - The text_positive parameter is a key element that provides a positive context or positive element of style. It is essential to set the tone of the final hint and significantly influences the thematic outcome.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Text_negative parameters are optional, allowing for negative contexts that can be compared with positive text creativity. This can add depth and complexity to styled tips.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - The style parameter determines the fantasy setting with which the hint will be styled. It is a key input that defines the thematic direction of the style process.
    - Comfy dtype: STRING
    - Python dtype: str
- log_prompt
    - Log_prompt parameters are an optional switch, and when set to 'Yes', records of style, text input, and style tips generated will be enabled. This is very useful for the debug or review of style processes.
    - Comfy dtype: COMBO['No', 'Yes']
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output represents a stylish, proactive text that has been creatively adapted to selected fantasy settings and has increased the attractiveness of the theme.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - Negative_prompt_text_g output provides a stylish negative hint text that complements the positive hint by providing comparative elements in fantasy settings.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyFantasySetting:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_fs.json')
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