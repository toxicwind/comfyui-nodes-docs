# Documentation
- Class name: ColorPicker
- Category: 😺dzNodes/LayerUtility
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Selects the colours on the panels and produces them. Reproduces from mtb nodes' web extensions, thanks to the original author.

# Input types

## Required

- color
    - The colour that you enter.
    - Comfy dtype: COLOR
    - Python dtype: str
    - Options: {"default": "#FFFFFF"}

- mode
    - Output Mode
    - Comfy dtype: STRING
    - Python dtype: str
    - Options: ['HEX', 'DEC']

# Output types

- value
    - Colour of the output.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: GPU

# Source code
```
class ColorPicker:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        mode_list = ['HEX', 'DEC']
        return {
            "required": {
                "color": ("COLOR", {"default": "#FFFFFF"},),
                "mode": (mode_list, # output mode)
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("value",)
    FUNCTION = 'picker'
    CATEGORY = '😺dzNodes/LayerUtility'

    def picker(self, color, mode):
        ret = color
        if mode == 'DEC':
            ret = Hex_to_RGB(ret)
        return (ret,)
```