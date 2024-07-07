# Documentation
- Class name: CR_SDXLStyleText
- Category: Comfyroll/SDXL
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_SDXLStyleText node is designed to process and manage style-related text input, especially for style conversion operations in image processing workflows. It is smart to process both positive and negative style descriptions, enabling users to define style properties that they want to enhance or inhibit in their output. The node plays a key role in guiding the style direction of image conversion and ensuring that the required aesthetic results are achieved.

# Input types
## Required
- positive_style
    - The positionive_style parameter is essential to define the style features that users want to highlight in the final image. It allows detailed descriptions, which can significantly influence the creative direction of the style conversion process.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_style
    - Negative_style parameters are used to specify the style elements that the user wishes to avoid or minimize in image output. This input is essential to fine-tune style to meet user expectations and to omit features that are not required.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- positive_prompt_text_l
    - The positionive_prompt_text_l output contains processed text in a positive style that will guide image processing towards desired style enhancements.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt_text_l
    - Negative_prompt_text_l output saves processed negative style text, which is essential to guide image processing away from unwanted style features.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - Show_help output provides a document URL link for further help and guidance when using nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SDXLStyleText:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'positive_style': ('STRING', {'default': 'POS_STYLE', 'multiline': True}), 'negative_style': ('STRING', {'default': 'NEG_STYLE', 'multiline': True})}}
    RETURN_TYPES = ('STRING', 'STRING', 'STRING')
    RETURN_NAMES = ('positive_prompt_text_l', 'negative_prompt_text_l', 'show_help')
    FUNCTION = 'get_value'
    CATEGORY = icons.get('Comfyroll/SDXL')

    def get_value(self, positive_style, negative_style):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/SDXL-Nodes#cr-sdxl-style-text'
        return (positive_style, negative_style, show_help)
```