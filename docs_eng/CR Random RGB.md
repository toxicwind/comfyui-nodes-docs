# Documentation
- Class name: CR_RandomRGB
- Category: Comfyroll/Utils/Random
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_RandomRGB node is designed to generate random RGB colour code. It serves as a practical tool for applications that require random colour generation, for example in graphic design or visual effects. The node ensures that each execution produces a unique set of colours that enhances the diversity and randomity of colour selection.

# Input types
## Required
- seed
    - Seed parameters are essential to initialize the random number generator to ensure that random RGB colours are produced for repeatability. It allows users to control randomity and to obtain the same colour set when needed, which is essential for a consistent colour scheme in different implementations.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- rgb_1
    - The first output parameter'rgb_1' provides a randomly generated string for the RGB colour code. It is formatted into a comma-separated list of three integer numbers, each range from 0 to 255, representing the red, green and blue components of the colour.
    - Comfy dtype: STRING
    - Python dtype: str
- rgb_2
    - The second output parameter'rgb_2' provides a string for another randomly generated RGB colour code, similar to 'rgb_1' but with different values to ensure diversity of colour selection.
    - Comfy dtype: STRING
    - Python dtype: str
- rgb_3
    - The third output parameter'rgb_3' provides a string for another unique randomly generated RGB colour code, which further enhances the diversity of colours available for different applications.
    - Comfy dtype: STRING
    - Python dtype: str
- rgb_4
    - The fourth output parameter'rgb_4' provides another string for different RGB colour codes, adding a random collection of colours that can be used in various scenarios.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The'show_help' output parameter provides a URL link to the document page for further help and information about node functions and uses.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_RandomRGB:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('STRING', 'STRING', 'STRING', 'STRING', 'STRING')
    RETURN_NAMES = ('rgb_1', 'rgb_2', 'rgb_3', 'rgb_4', 'show_help')
    FUNCTION = 'get_colors'
    CATEGORY = icons.get('Comfyroll/Utils/Random')

    def get_colors(self, seed):
        random.seed(seed)
        rgb_1 = random_rgb()
        rgb_2 = random_rgb()
        rgb_3 = random_rgb()
        rgb_4 = random_rgb()
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-random-rgb'
        return (rgb_1, rgb_2, rgb_3, rgb_4, show_help)
```