# Documentation
- Class name: CR_RandomHexColor
- Category: Comfyroll/Utils/Random
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_RandomHexColor node is designed to generate random hexadecimal code. It is designed to provide users with a unique and randomly generated set of colours that can be used in various graphic designs or visual applications. The node emphasizes the creation of diversity in colour selection without manual specification, thus simplifying the design process and providing a convenient way to try color changes.

# Input types
## Required
- seed
    - The "seed" parameter is essential for the operation of the node, as it initializes the random number generator to ensure that the colours generated are recreated. This feature is particularly important for consistency in different operations or for debugging purposes.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- hex_color1
    - The 'hex_color1'output provides the first randomly generated hexadecimal colour code. It is important because it represents one of the diverse colour options that nodes can generate and applies to applications directly related to colour.
    - Comfy dtype: STRING
    - Python dtype: str
- hex_color2
    - The "hex_color2 " output provides a second unique hexadecimal colour code. Like "hex_color1 ", it is designed to provide users with different colour options and expand the range of colours available to them.
    - Comfy dtype: STRING
    - Python dtype: str
- hex_color3
    - The "hex_color3 " output generates a third different hexadecimal colour code. This output further enhances the diversity of colours available and provides more options for creative work.
    - Comfy dtype: STRING
    - Python dtype: str
- hex_color4
    - The 'hex_color4'output represents the fourth randomly generated hexadecimal colour code. It continues to expand the range of colour selections to ensure that users have multiple options in their design needs.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The Show_help output provides a URL link to the document page for further help. This is a useful resource for users who may need additional guidance or information about node functions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_RandomHexColor:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('STRING', 'STRING', 'STRING', 'STRING', 'STRING')
    RETURN_NAMES = ('hex_color1', 'hex_color2', 'hex_color3', 'hex_color4', 'show_help')
    FUNCTION = 'get_colors'
    CATEGORY = icons.get('Comfyroll/Utils/Random')

    def get_colors(self, seed):
        random.seed(seed)
        hex_color1 = random_hex_color()
        hex_color2 = random_hex_color()
        hex_color3 = random_hex_color()
        hex_color4 = random_hex_color()
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-random-hex-color'
        return (hex_color1, hex_color2, hex_color3, hex_color4, show_help)
```