# Documentation
- Class name: RGB_Picker
- Category: 😺dzNodes/WordCloud
- Output node: True
- Repo Ref: https://github.com/chflame163/ComfyUI_WordCloud.git

RGB_Picker nodes are designed to facilitate the conversion and selection of colour values. It handles colour input in various formats and focuses on providing users with flexibility to process colours in hexadecimal and decimal expressions.

# Input types
## Required
- color
    - The 'color' parameter is necessary because it defines the initial colour input for node operations. It is the basis for all subsequent colour conversions and is essential for determining the final output.
    - Comfy dtype: COLOR
    - Python dtype: str
## Optional
- mode
    - The `mode' parameter determines the process of conversion of colour input. It affects the way the colour is interpreted and the result format of the output, enhancing the adaptability of the node to the different colours required.
    - Comfy dtype: COMBO[mode_list]
    - Python dtype: str

# Output types
- value
    - The `value' output represents the post-processing colour under the required format and contains the main functions for node colour conversion and selection.
    - Comfy dtype: STRING
    - Python dtype: tuple

# Usage tips
- Infra type: CPU

# Source code
```
class RGB_Picker:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {'required': {'color': ('COLOR', {'default': 'white'}), 'mode': (mode_list,)}, 'optional': {}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('value',)
    FUNCTION = 'picker'
    CATEGORY = '😺dzNodes/WordCloud'
    OUTPUT_NODE = True

    def picker(self, color, mode):
        ret = color
        if mode == 'DEC':
            ret = hex_to_dec(color)
        return (ret,)
```