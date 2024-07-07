# Documentation
- Class name: SDXLPromptStylerbyDepth
- Category: Style Prompts
- Output node: False
- Repo Ref: https://github.com/wolfden/ComfyUi_PromptStylers

The SDXLPromptStylerbyDepth node is designed to enhance user experience through in-depth styled tips. It is intelligently combined with positive and negative text input and selected styles to generate more attractive and targeted tips. The node plays a crucial role in creating alerts that echo the target audience, thereby enhancing the effectiveness of communication.

# Input types
## Required
- text_positive
    - The text_positive parameter is essential because it provides positive text content that will be styled in nodes. It directly influences the tone and information of the final hint and is a key component of node operations.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - The text_negative parameter is important for providing negative text content in contrast to the positive text. It helps shape the overall feeling of the hint and is an important element of node implementation.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - The style parameter is essential because it determines the style approach applied to the text. It determines the selection of the template and the overall beauty of generating the hint, which is a key element of the node function.
    - Comfy dtype: STRING
    - Python dtype: str
- log_prompt
    - Log_prompt parameters are optional to control whether nodes should record tip messages during execution. This is useful for debugging and monitoring node behaviour and does not affect primary functions.
    - Comfy dtype: COMBO['No', 'Yes']
    - Python dtype: str

# Output types
- positive_prompt_text_g
    - This is the key result of node operations and is important for subsequent applications.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_g
    - Negative_prompt_text_g output represents a node-generated negative styled text. It supplements the positive text and is an important aspect of creating balanced and delicate node output.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerbyDepth:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        p = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(p, 'sdxl_styles_depth.json')
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