# Documentation
- Class name: SDXLPromptStylerbyImpressionism
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node enhances the aesthetic and thematic depth of the text by creatively converting input through the application of animated style template.

# Input types
## Required
- text_positive
    - Positive text input, as a basis for style conversion, provides content that will be given impressions.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input is used in contrast to the positive text and may add depth and complexity to the final style output.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - The style selected from the predefined Impression style template determines the overall tone and direction of text conversion.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - This parameter controls whether to record the intermediate steps and results of the styled process and helps to understand the operation and output of the nodes.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output displays a positive style of text and is now integrated into the selected impressionist style for further use or presentation.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output includes a negative styled text, which complements the positive output and may provide a comparative perspective or additional context.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyImpressionism:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_impressionism.json')
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