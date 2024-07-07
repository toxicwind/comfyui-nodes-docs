# Documentation
- Class name: SDXLPromptStyler
- Category: utils
- Output node: False
- Repo Ref: https://github.com/twri/sdxl_prompt_styler

The SDXLPromptStyler node is designed to glorify text input by applying predefined styles. It handles both positive and negative hints and allows customization through style selection and log-record options. The main objective of this node is to enhance the effect of the text while maintaining the original message intent.

# Input types
## Required
- text_positive
    - The text_positive parameter is essential to define the positive aspects of the text entered. It influences the implementation of nodes by deciding on text content that is stymied in a positive way.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - The text_negative parameter specifies the negative aspects of the input text. It is essential for the operation of the node, as it determines the text content that will be negatively stylized.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - The style parameter plays a key role in determining the style conversion that should be applied to input text. It indicates that nodes use a particular style in the available options.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- log_prompt
    - log_prompt parameters control whether node should be recorded. This is very useful for debugging or tracking node processing steps.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- style_positive
    - The style_positive parameter allows the user to enable or disable the positive style of the text. It plays an important role in the look of the final output.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- style_negative
    - The style_negative parameter is used to change the negative style of the text. This is an important aspect of the node in the text presentation function.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- text_positive
    - Text_positive output is the result of the application of the selected style to the text.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Text_negative output provides a negative text styled after node operations. It reflects the ability of node to style text with negative connotations.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStyler:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        (self.json_data, styles) = load_styles_from_directory(current_directory)
        return {'required': {'text_positive': ('STRING', {'default': '', 'multiline': True}), 'text_negative': ('STRING', {'default': '', 'multiline': True}), 'style': (styles,), 'log_prompt': ('BOOLEAN', {'default': True, 'label_on': 'yes', 'label_off': 'no'}), 'style_positive': ('BOOLEAN', {'default': True, 'label_on': 'yes', 'label_off': 'no'}), 'style_negative': ('BOOLEAN', {'default': True, 'label_on': 'yes', 'label_off': 'no'})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('text_positive', 'text_negative')
    FUNCTION = 'prompt_styler'
    CATEGORY = 'utils'

    def prompt_styler(self, text_positive, text_negative, style, log_prompt, style_positive, style_negative):
        (text_positive_styled, text_negative_styled) = read_sdxl_templates_replace_and_combine(self.json_data, style, text_positive, text_negative)
        if not style_positive:
            text_positive_styled = text_positive
            if log_prompt:
                print(f'style_positive: disabled')
        if not style_negative:
            text_negative_styled = text_negative
            if log_prompt:
                print(f'style_negative: disabled')
        if log_prompt:
            print(f'style: {style}')
            print(f'text_positive: {text_positive}')
            print(f'text_negative: {text_negative}')
            print(f'text_positive_styled: {text_positive_styled}')
            print(f'text_negative_styled: {text_negative_styled}')
        return (text_positive_styled, text_negative_styled)
```