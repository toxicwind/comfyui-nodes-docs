# Documentation
- Class name: SDXLPromptStylerbySteamPunkRealism
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node aims to strategize tips based on predefined steam punk realism styles and enhance the subject matter of the text by integrating style elements and narrative themes specific to steam punk streams.

# Input types
## Required
- text_positive
    - Positive text input is essential because it provides the basic content of the node application of steam punk realism style. This is a text that will be enhanced and converted to reflect the desired subject style.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input as a comparison of the positive text allows nodes to fine-tune style conversions by integrating elements that do not want to appear in the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - The style parameter is essential because it determines the node that will be applied to the subject orientation and aesthetic selection of the text. It is the guiding force behind the style conversion process.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - The log hint parameter is an optional setting that allows users to record the conversion process and provides insights on how the node can apply the steam punk realism style to input text.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output is a positive style text that has been transformed into a steam punk realism style prepared for various creative applications.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output is a negative styled text that helps to refine the subject matter and aesthetics of the final product by providing elements in contrast to the positive output.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbySteamPunkRealism:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_sr.json')
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