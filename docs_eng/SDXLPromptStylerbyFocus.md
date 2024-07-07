# Documentation
- Class name: SDXLPromptStylerbyFocus
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node is designed to enhance the presentation of tips by applying specific style templates, thereby enhancing user experience and participation through customized and visually attractive text formats.

# Input types
## Required
- text_positive
    - Positive text input is essential because it sets the basis for the positive aspects of the hint. This is what will be styled and presented to the user, with a view to generating a positive response.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input is essential for providing the comparative elements of the hint, allowing for a more detailed and balanced presentation. It complements the positive text by providing different perspectives.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- style
    - Style input is a key component of the aesthetic and structural format that determines the tips. It guides the text to visualally attractive and consistent information.
    - Comfy dtype: COMBO
    - Python dtype: str
- log_prompt
    - Logtip input is used as a debugging tool to record the details of the hint for analysis and review. It helps refine the function of the node and ensures the best output.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output provides a stylish text of a positive hint, which is formatted according to the selected style template and enhances the readability and attractiveness of the information.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output contributes to comprehensive and balanced communication by providing a stylish text of negative indications, complementing the positive ones by providing a comparative perspective.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyFocus:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_focus.json')
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