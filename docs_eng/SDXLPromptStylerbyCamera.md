# Documentation
- Class name: SDXLPromptStylerbyCamera
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The node is designed to enhance the creative process by dynamically generating styled tips based on a given text input, both positive and negative, using a predefined set of styles. It is designed to inspire and guide users to create more attractive and targeted content.

# Input types
## Required
- text_positive
    - Positive text input is essential to set the desired tone and direction for generating the hint. It is the basis for applying the style elements to ensure that the output is consistent with the expected information and emotion.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative text input is essential to define the aspects that should be avoided in creating the hint. It helps to refine the output by removing elements that may weaken the desired information or tone.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - A style parameter is essential to select the appropriate style template from the available options. It affects the overall aesthetic and thematic direction of the hint and ensures that the content generated is consistent with the chosen style.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- log_prompt
    - The log hint parameter allows the user to selectively activate the log log record of the hint generation process. This function is useful for debugging and understanding the internal working mechanisms of the nodes and provides insight into how the final output is formed.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - The output provides a refined text of a positive hint that combines selected styles and excludes negative text input to specified unwanted elements. This result is intended to serve as a guide to creating content that is consistent with the desired tone and information.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - The output provides a modified negative hint text that has been adapted to the chosen style to ensure that the final content is not influenced by elements that weaken the expected information or tone.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyCamera:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_camera.json')
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