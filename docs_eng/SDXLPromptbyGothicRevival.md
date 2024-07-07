# Documentation
- Class name: SDXLPromptbyGothicRevival
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node aims to stylish text tips based on a predefined Goth Renaissance style collection that enhances the subject matter of the text and the United States dollar review. It integrates style into the text, creating a unique and culturally resonant output that reflects the chosen historical beauty.

# Input types
## Required
- text_positive
    - Positive text entry is essential because it sets the basis for style conversion. It is a text that will be enhanced and shaped according to the chosen Goth renaissance style, ensuring that the final output is consistent with the desired thematic direction.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input as a positive text balance provides the contrast and depth of the style process. It ensures that the final output is not only beautiful, but also sound and multifaceted in subject matter.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - The style parameter is the core of the node function and determines the aesthetic and thematic orientation of the style. It is the reference point for converting input text into a work that reflects the nature of the chosen Goth revival style.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - The log hint parameter is essential for debugging and transparency in the style process. When enabled, it provides a detailed log of the conversion process, ensuring that each step is recorded and can be reviewed for quality and accuracy.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - Positive hint text, which has been stymied according to the chosen Goth Renaissance style, is the main output of the node. It is a direct reflection of the node that converts the input text to the new theoretical and style meaning level.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The same styled negative hint text complements the positive output by providing a comparative perspective. It is an essential part of node output, showing the depth and breadth of style conversion.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptbyGothicRevival:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_gothrev.json')
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