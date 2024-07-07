# Documentation
- Class name: CR_RandomRGBGradient
- Category: Comfyroll/Utils/Random
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_RandomRGBGradient is a node used to generate random RGB gradients. It operates from one colour to the next by creating a series of smooth transition RGB values, ensuring a visually attractive gradient effect. This node applies in particular to designers and developers who need to provide dynamic and diverse colour options for the project.

# Input types
## Required
- seed
    - The “seed” parameter is essential to the random number generation process of nodes. It ensures that the RGB values generated are recreated and allow for consistent results in different operations. This is particularly important in the need to produce the same gradient over and over again.
    - Comfy dtype: INT
    - Python dtype: int
- rows
    - The “rows” parameter determines the number of colour stops in which the gradient is generated. Higher values lead to more detailed gradients, which include more intermediate colours, while lower values lead to simpler gradients and less colour transitions.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- multiline_text
    - The " multiline_text " output contains RGB gradient data generated in a multi-line format. Each line represents a colour that stops and the RGB value is separated by comma. This format is easily used in applications that require line-by-line input of gradient data.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The Show_help output provides a URL link to the node document page. This is very useful for users who need additional information or guidance to use node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_RandomRGBGradient:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'rows': ('INT', {'default': 5, 'min': 1, 'max': 2048})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('multiline_text', 'show_help')
    FUNCTION = 'generate'
    CATEGORY = icons.get('Comfyroll/Utils/Random')

    def generate(self, rows, seed):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-random-RGB-gradient'
        random.seed(seed)
        temp = 0
        multiline_text = ''
        for i in range(1, rows + 1):
            print(temp)
            if temp <= 99 - rows + i:
                upper_bound = min(99, temp + (99 - temp) // (rows - i + 1))
                current_value = random.randint(temp, upper_bound)
                multiline_text += f'{current_value}:{random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)}\n'
                temp = current_value + 1
        return (multiline_text, show_help)
```