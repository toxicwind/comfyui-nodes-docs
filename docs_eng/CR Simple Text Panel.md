# Documentation
- Class name: CR_SimpleTextPanel
- Category: Comfyroll/Graphics/Layout
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SimpleTextPanel is designed to create a visually attractive text panel with customable fonts, colours and layout options. It allows text to be rendered to the image background and has various style functions, such as font contour and alignment, to enhance the presentation of text information.

# Input types
## Required
- panel_width
    - The width of the text panel determines the horizontal range of the output image. This is a key parameter because it determines the space available for text content and affects the overall layout and appearance.
    - Comfy dtype: INT
    - Python dtype: int
- panel_height
    - The vertical size of the panel is set at the height of the text panel, which is essential to control the vertical space of the text and to ensure that the text adapts to the image boundary.
    - Comfy dtype: INT
    - Python dtype: int
- text
    - Text parameters are the actual content to be displayed on the panel. It can contain multi-line text, which is particularly useful for longer paragraphs or when more complex layouts are needed.
    - Comfy dtype: STRING
    - Python dtype: str
- font_name
    - Font name parameters specify the type of font that you want to use for text. The font selection significantly affects the style and readability of the text in the panel.
    - Comfy dtype: STRING
    - Python dtype: str
- font_color
    - The font colour determines the colour of the text, allowing the user to match the text to the background or to a particular design theme. It plays a crucial role in ensuring that the text is readable and visual contrasts are made.
    - Comfy dtype: STRING
    - Python dtype: str
- font_size
    - Font size controls the size of the text, which is an important factor for readability and for adjusting the text to fit the size of the panel specified.
    - Comfy dtype: INT
    - Python dtype: int
- font_outline_thickness
    - The thickness of the font contour increases the emphasis of the text and enhances its visibility in a complex context. This is an optional style selection that enhances the appearance of the text.
    - Comfy dtype: INT
    - Python dtype: int
- font_outline_color
    - The font colour provides a comparative boundary that enhances the definition of the text and makes it out of the background, especially when the font colour and background are similar.
    - Comfy dtype: STRING
    - Python dtype: str
- background_color
    - The background colour sets the basic colour for the text panel, which affects the overall atmosphere and beauty of the design. It is a key element in creating a harmonious visual combination.
    - Comfy dtype: STRING
    - Python dtype: str
- align
    - Alignment parameters determine the horizontal alignment of the text within the panel, which can influence the symmetry and balance of the design.
    - Comfy dtype: STRING
    - Python dtype: str
- justify
    - The alignment option controls the spacing between words and characters, ensuring that text is evenly aligned along the right and left edges.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- image
    - The result is that the image is the main output of the CR_SimpleTextPanel node and contains a styled text that is layoutd on the specified background. It represents the final visual product of the node function.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL link to the document page to obtain further help or information about the use and function of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SimpleTextPanel:

    @classmethod
    def INPUT_TYPES(s):
        font_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
        file_list = [f for f in os.listdir(font_dir) if os.path.isfile(os.path.join(font_dir, f)) and f.lower().endswith('.ttf')]
        return {'required': {'panel_width': ('INT', {'default': 512, 'min': 8, 'max': 4096}), 'panel_height': ('INT', {'default': 512, 'min': 8, 'max': 4096}), 'text': ('STRING', {'multiline': True, 'default': 'text'}), 'font_name': (file_list,), 'font_color': (COLORS,), 'font_size': ('INT', {'default': 100, 'min': 0, 'max': 1024}), 'font_outline_thickness': ('INT', {'default': 0, 'min': 0, 'max': 50}), 'font_outline_color': (COLORS,), 'background_color': (COLORS,), 'align': (ALIGN_OPTIONS,), 'justify': (JUSTIFY_OPTIONS,)}, 'optional': {'font_color_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'bg_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('image', 'show_help')
    FUNCTION = 'layout'
    CATEGORY = icons.get('Comfyroll/Graphics/Layout')

    def layout(self, panel_width, panel_height, text, align, justify, font_name, font_color, font_size, font_outline_thickness, font_outline_color, background_color, font_color_hex='#000000', font_outline_color_hex='#000000', bg_color_hex='#000000'):
        font_color = get_color_values(font_color, font_color_hex, color_mapping)
        outline_color = get_color_values(font_outline_color, font_outline_color_hex, color_mapping)
        bg_color = get_color_values(background_color, bg_color_hex, color_mapping)
        margins = 50
        line_spacing = 0
        position_x = 0
        position_y = 0
        rotation_angle = 0
        rotation_options = 'image center'
        panel = text_panel(panel_width, panel_height, text, font_name, font_size, font_color, font_outline_thickness, outline_color, bg_color, margins, line_spacing, position_x, position_y, align, justify, rotation_angle, rotation_options)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Layout-Nodes#cr-simple-text-panel'
        return (pil2tensor(panel), show_help)
```