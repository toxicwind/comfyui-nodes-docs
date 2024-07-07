# Documentation
- Class name: SDXLPromptStylerAdvanced
- Category: utils
- Output node: False
- Repo Ref: https://github.com/twri/sdxl_prompt_styler

The node is intended to enhance the presentation of the text by using advanced style techniques based on a predefined set of templates. It integrates both positive and negative hints into a coherent format that allows custom text to be tailored to a particular style.

# Input types
## Required
- text_positive_g
    - The main positive hint is the core message that needs to be emphasized. It is essential for setting the tone and direction of a styled text.
    - Comfy dtype: STRING
    - Python dtype: str
- text_positive_l
    - A positive indication of subsidiarity provides additional context or detail to supplement key information and enrich the overall content.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - Negative hints are used to introduce comparative elements or opposing views, which can increase the depth and attractiveness of styled texts.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - Style parameters determine the aesthetic and structural format to be applied to the text and guide the overall look and feeling of the output.
    - Comfy dtype: STYLE
    - Python dtype: dict
- negative_prompt_to
    - This parameter determines the application objectives of negative hints, whether applied to primary and secondary hints or selectively applied.
    - Comfy dtype: COMBO
    - Python dtype: str
- copy_to_l
    - When enabled, this sign ensures that the main positive hint is copied to the helper, provides consistency and enhances the key information.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- log_prompt
    - This switch to records that enable or disable tips and styled text is very useful for debugging and review purposes.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- text_positive_g
    - The main styled text reflects the main positive messages after applying the selected style.
    - Comfy dtype: STRING
    - Python dtype: str
- text_positive_l
    - Ancillary styled text, which provides additional context for the main message, is reflected in the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- text_positive
    - The combination of primary and auxiliary positive hints is integrated into a coherent and consistent output.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative_g
    - A comparison of the elements is presented as a whole, based on the main negative hint of styled template selected.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative_l
    - Adverse indications of subsidiarity are styled to supplement the main negative text and enhance the depth of the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- text_negative
    - The combination's negative hints are stymied as a whole, contributing to the comprehensive and attractive presentation of the content.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLPromptStylerAdvanced:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        (self.json_data, styles) = load_styles_from_directory(current_directory)
        return {'required': {'text_positive_g': ('STRING', {'default': '', 'multiline': True}), 'text_positive_l': ('STRING', {'default': '', 'multiline': True}), 'text_negative': ('STRING', {'default': '', 'multiline': True}), 'style': (styles,), 'negative_prompt_to': (['Both', 'G only', 'L only'], {'default': 'Both'}), 'copy_to_l': ('BOOLEAN', {'default': False, 'label_on': 'yes', 'label_off': 'no'}), 'log_prompt': ('BOOLEAN', {'default': False, 'label_on': 'yes', 'label_off': 'no'})}}
    RETURN_TYPES = ('STRING', 'STRING', 'STRING', 'STRING', 'STRING', 'STRING')
    RETURN_NAMES = ('text_positive_g', 'text_positive_l', 'text_positive', 'text_negative_g', 'text_negative_l', 'text_negative')
    FUNCTION = 'prompt_styler_advanced'
    CATEGORY = 'utils'

    def prompt_styler_advanced(self, text_positive_g, text_positive_l, text_negative, style, negative_prompt_to, copy_to_l, log_prompt):
        (text_positive_g_styled, text_positive_l_styled, text_positive_styled, text_negative_g_styled, text_negative_l_styled, text_negative_styled) = read_sdxl_templates_replace_and_combine_advanced(self.json_data, style, text_positive_g, text_positive_l, text_negative, negative_prompt_to, copy_to_l)
        if log_prompt:
            print(f'style: {style}')
            print(f'text_positive_g: {text_positive_g}')
            print(f'text_positive_l: {text_positive_l}')
            print(f'text_negative: {text_negative}')
            print(f'text_positive_g_styled: {text_positive_g_styled}')
            print(f'text_positive_l_styled: {text_positive_l_styled}')
            print(f'text_positive_styled: {text_positive_styled}')
            print(f'text_negative_g_styled: {text_negative_g_styled}')
            print(f'text_negative_l_styled: {text_negative_l_styled}')
            print(f'text_negative_styled: {text_negative_styled}')
        return (text_positive_g_styled, text_positive_l_styled, text_positive_styled, text_negative_g_styled, text_negative_l_styled, text_negative_styled)
```