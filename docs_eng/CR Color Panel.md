# Documentation
- Class name: CR_ColorPanel
- Category: Comfyroll/Graphics/Layout
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ColorPanel is a node used to generate a pure colour panel. It allows the user to specify the size and colour of the panel, which can then be used as an image output. This node is very multifunctional and can serve as a basis for a more complex image combination or as an independent visual effect element.

# Input types
## Required
- panel_width
    - The panel_width parameter defines the width of the colour panel. It is essential for setting the horizontal dimensions of the output image and influencing the overall structure when used in conjunction with other visual elements.
    - Comfy dtype: INT
    - Python dtype: int
- panel_height
    - The panel_height parameter determines the height of the colour panel. Together with panel_width, it determines the overall size of the image, which is essential for creating a visually balanced layout.
    - Comfy dtype: INT
    - Python dtype: int
- fill_color
    - The fill_color parameter determines the colour of the filled panel. It is a key aspect of the node function and allows custom panels to be designed to meet specific design requirements.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- fill_color_hex
    - Fill_color_hex parameters provide another way to specify a fill colour using hexadecimal values. This allows for precise control of colours, especially when a particular tone is required, which may not be directly available in the predefined colour options.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- image
    - An image output is a colour panel that is rendered as a volume. It represents the visual result of the node operation, which can be used for input or direct display for further image processing.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL link to the node document. This is very useful for users seeking additional guidance or information on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ColorPanel:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'panel_width': ('INT', {'default': 512, 'min': 8, 'max': 4096}), 'panel_height': ('INT', {'default': 512, 'min': 8, 'max': 4096}), 'fill_color': (COLORS,)}, 'optional': {'fill_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('image', 'show_help')
    FUNCTION = 'make_panel'
    CATEGORY = icons.get('Comfyroll/Graphics/Layout')

    def make_panel(self, panel_width, panel_height, fill_color, fill_color_hex='#000000'):
        fill_color = get_color_values(fill_color, fill_color_hex, color_mapping)
        size = (panel_width, panel_height)
        panel = Image.new('RGB', size, fill_color)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Layout-Nodes#cr-color-panel'
        return (pil2tensor(panel), show_help)
```