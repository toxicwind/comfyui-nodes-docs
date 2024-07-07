# Documentation
- Class name: CR_PageLayout
- Category: Comfyroll/Graphics/Layout
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_PageLayout Node is designed to create a structured layout of the image by adding a custom title and footer text. It allows the font properties, colours, and borders to be added to create a visually attractive combination.

# Input types
## Required
- layout_options
    - The layout option defines the parts that will be included in the final image. This option affects the overall structure and composition of the output.
    - Comfy dtype: COMBO['header', 'footer', 'header and footer', 'no header or footer']
    - Python dtype: str
- image_panel
    - The main image panel, which is the central component of the layout. It is the image that will be added to the title and footer.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- header_height
    - Specifies the height of the header section. This parameter is essential for determining the spacing and size of the header in the layout.
    - Comfy dtype: INT
    - Python dtype: int
- header_text
    - The text content of the title section. It affects the visual presentation of the title and the message it conveys.
    - Comfy dtype: STRING
    - Python dtype: str
- header_align
    - Determines the text alignment of the title. It affects the location of the title text within the title section.
    - Comfy dtype: JUSTIFY_OPTIONS
    - Python dtype: str
- footer_height
    - Specifies the height of the footer section. It is an important parameter for setting the length and size of the footer in the layout.
    - Comfy dtype: INT
    - Python dtype: int
- footer_text
    - Text content of the footer section. It determines the information and visual style of the footer.
    - Comfy dtype: STRING
    - Python dtype: str
- footer_align
    - Defines the text alignment of the footer. It controls the position of the footer text in the footer section.
    - Comfy dtype: JUSTIFY_OPTIONS
    - Python dtype: str
- font_name
    - Select the font for the title and footer text. The font selection significantly affects the overall beauty of the layout.
    - Comfy dtype: FONT_LIST
    - Python dtype: str
- font_color
    - Sets the font colour of the title and footer text. It plays a key role in the readability and visual appeal of the text.
    - Comfy dtype: COLORS
    - Python dtype: str
- header_font_size
    - Defines the font size of the title text. It affects the prominence and readability of the title in the layout.
    - Comfy dtype: INT
    - Python dtype: int
- footer_font_size
    - Specifies the font size of the footer text. It is important for the visibility and prominence of the footer in the layout.
    - Comfy dtype: INT
    - Python dtype: int
- border_thickness
    - Determines the thickness of the border around the layout. It helps to define the overall frame and the edge of the layout.
    - Comfy dtype: INT
    - Python dtype: int
- border_color
    - Sets the colour of the border around the layout. It plays an important role in the visual boundary and style of the layout.
    - Comfy dtype: COLORS
    - Python dtype: str
- background_color
    - Defines the background colour of the layout. It provides the basic visual background for all other elements.
    - Comfy dtype: COLORS
    - Python dtype: str

# Output types
- image
    - The final grouping of images, including any headings, footers and borders specified according to the input parameters.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Provides a document link for further help and detailed information on node functions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_PageLayout:

    @classmethod
    def INPUT_TYPES(s):
        font_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
        file_list = [f for f in os.listdir(font_dir) if os.path.isfile(os.path.join(font_dir, f)) and f.lower().endswith('.ttf')]
        layout_options = ['header', 'footer', 'header and footer', 'no header or footer']
        return {'required': {'layout_options': (layout_options,), 'image_panel': ('IMAGE',), 'header_height': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'header_text': ('STRING', {'multiline': True, 'default': 'text'}), 'header_align': (JUSTIFY_OPTIONS,), 'footer_height': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'footer_text': ('STRING', {'multiline': True, 'default': 'text'}), 'footer_align': (JUSTIFY_OPTIONS,), 'font_name': (file_list,), 'font_color': (COLORS,), 'header_font_size': ('INT', {'default': 150, 'min': 0, 'max': 1024}), 'footer_font_size': ('INT', {'default': 50, 'min': 0, 'max': 1024}), 'border_thickness': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'border_color': (COLORS,), 'background_color': (COLORS,)}, 'optional': {'font_color_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'border_color_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'bg_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('image', 'show_help')
    FUNCTION = 'layout'
    CATEGORY = icons.get('Comfyroll/Graphics/Layout')

    def layout(self, layout_options, image_panel, border_thickness, border_color, background_color, header_height, header_text, header_align, footer_height, footer_text, footer_align, font_name, font_color, header_font_size, footer_font_size, font_color_hex='#000000', border_color_hex='#000000', bg_color_hex='#000000'):
        font_color = get_color_values(font_color, font_color_hex, color_mapping)
        border_color = get_color_values(border_color, border_color_hex, color_mapping)
        bg_color = get_color_values(background_color, bg_color_hex, color_mapping)
        main_panel = tensor2pil(image_panel)
        image_width = main_panel.width
        image_height = main_panel.height
        margins = 50
        line_spacing = 0
        position_x = 0
        position_y = 0
        align = 'center'
        rotation_angle = 0
        rotation_options = 'image center'
        font_outline_thickness = 0
        font_outline_color = 'black'
        images = []
        if layout_options == 'header' or layout_options == 'header and footer':
            header_panel = text_panel(image_width, header_height, header_text, font_name, header_font_size, font_color, font_outline_thickness, font_outline_color, bg_color, margins, line_spacing, position_x, position_y, align, header_align, rotation_angle, rotation_options)
            images.append(header_panel)
        images.append(main_panel)
        if layout_options == 'footer' or layout_options == 'header and footer':
            footer_panel = text_panel(image_width, footer_height, footer_text, font_name, footer_font_size, font_color, font_outline_thickness, font_outline_color, bg_color, margins, line_spacing, position_x, position_y, align, footer_align, rotation_angle, rotation_options)
            images.append(footer_panel)
        combined_image = combine_images(images, 'vertical')
        if border_thickness > 0:
            combined_image = ImageOps.expand(combined_image, border_thickness, border_color)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Layout-Nodes#cr-page-layout'
        return (pil2tensor(combined_image), show_help)
```