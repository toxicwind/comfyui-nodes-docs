# Documentation
- Class name: CR_ComicPanelTemplates
- Category: Comfyroll/Graphics/Template
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ComicPanelTemplates is a node used to create comic panel layouts from a group of pictures. It allows custom panel layouts, reading directions, and colours of borders, contours and background. This node can handle predefined and custom panel layouts to create comic strip effects.

# Input types
## Required
- page_width
    - The page_width parameter determines the width of the comic panel layout. It is essential to set the overall size of the output and influences the spacing and alignment of the internal panels in the layout.
    - Comfy dtype: INT
    - Python dtype: int
- page_height
    - Page_height parameters set the height of the comic panel layout. It works with page_width to determine the overall canvas size of the comic strip.
    - Comfy dtype: INT
    - Python dtype: int
- template
    - The template parameter specifies the predefined or custom layout of the comic panel. It is a key input that determines the structure of the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- reading_direction
    - Reading_direaction parameters determine the flow of comic panel reading, which can be from left to right or from right to left, which is essential for reading the panel in the correct order.
    - Comfy dtype: STRING
    - Python dtype: str
- border_thickness
    - The border_tickness parameter defines the thickness of the border around each comic panel. It helps to improve the beauty and clarity of each panel.
    - Comfy dtype: INT
    - Python dtype: int
- outline_thickness
    - The outline_tickness parameter sets the thickness of the contour around each panel and enhances the visual differentiation between panels.
    - Comfy dtype: INT
    - Python dtype: int
- outline_color
    - The outline_color parameter specifies the colour of the contour around each cartoon panel, which plays a role in the overall visual style of the layout.
    - Comfy dtype: STRING
    - Python dtype: str
- panel_color
    - The panel_color parameter determines the background colour of each comic panel and sets the tone for internal works of art.
    - Comfy dtype: STRING
    - Python dtype: str
- background_color
    - Background_color parameters set the background colour for the entire cartoon panel layout, providing a background canvas for the panel.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- images
    - The image parameters are an optional list of image lengths that will be used to fill comic panels. It allows dynamic content to be filled in layouts.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
- custom_panel_layout
    - Custom_panel_layout parameters accept a string that defines the custom grid layout of the panel. Use when selecting 'custom' templates.
    - Comfy dtype: STRING
    - Python dtype: str
- outline_color_hex
    - The outline_color_hex parameters provide a hexadecimal colour value for the contour and another way to specify the colour of the contour.
    - Comfy dtype: STRING
    - Python dtype: str
- panel_color_hex
    - The panel_color_hex parameter allows a hexadecimal colour value to be assigned to the panel background, providing flexibility in colour selection.
    - Comfy dtype: STRING
    - Python dtype: str
- bg_color_hex
    - The bg_color_hex parameter sets the hexadecimal colour value for the entire layout background and provides a direct method for entering the background colour.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- image
    - The Image output contains a renderable comic panel layout that can be further processed or displayed as an image billing.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL that points to the document page to obtain additional guidance on using this node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ComicPanelTemplates:

    @classmethod
    def INPUT_TYPES(s):
        directions = ['left to right', 'right to left']
        templates = ['custom', 'G22', 'G33', 'H2', 'H3', 'H12', 'H13', 'H21', 'H23', 'H31', 'H32', 'V2', 'V3', 'V12', 'V13', 'V21', 'V23', 'V31', 'V32']
        return {'required': {'page_width': ('INT', {'default': 512, 'min': 8, 'max': 4096}), 'page_height': ('INT', {'default': 512, 'min': 8, 'max': 4096}), 'template': (templates,), 'reading_direction': (directions,), 'border_thickness': ('INT', {'default': 5, 'min': 0, 'max': 1024}), 'outline_thickness': ('INT', {'default': 2, 'min': 0, 'max': 1024}), 'outline_color': (COLORS,), 'panel_color': (COLORS,), 'background_color': (COLORS,)}, 'optional': {'images': ('IMAGE',), 'custom_panel_layout': ('STRING', {'multiline': False, 'default': 'H123'}), 'outline_color_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'panel_color_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'bg_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('image', 'show_help')
    FUNCTION = 'layout'
    CATEGORY = icons.get('Comfyroll/Graphics/Template')

    def layout(self, page_width, page_height, template, reading_direction, border_thickness, outline_thickness, outline_color, panel_color, background_color, images=None, custom_panel_layout='G44', outline_color_hex='#000000', panel_color_hex='#000000', bg_color_hex='#000000'):
        panels = []
        k = 0
        len_images = 0
        if images is not None:
            images = [tensor2pil(image) for image in images]
            len_images = len(images)
        outline_color = get_color_values(outline_color, outline_color_hex, color_mapping)
        panel_color = get_color_values(panel_color, panel_color_hex, color_mapping)
        bg_color = get_color_values(background_color, bg_color_hex, color_mapping)
        size = (page_width - 2 * border_thickness, page_height - 2 * border_thickness)
        page = Image.new('RGB', size, bg_color)
        draw = ImageDraw.Draw(page)
        if template == 'custom':
            template = custom_panel_layout
        first_char = template[0]
        if first_char == 'G':
            rows = int(template[1])
            columns = int(template[2])
            panel_width = (page.width - 2 * columns * (border_thickness + outline_thickness)) // columns
            panel_height = (page.height - 2 * rows * (border_thickness + outline_thickness)) // rows
            for i in range(rows):
                for j in range(columns):
                    create_and_paste_panel(page, border_thickness, outline_thickness, panel_width, panel_height, page.width, panel_color, bg_color, outline_color, images, i, j, k, len_images, reading_direction)
                    k += 1
        elif first_char == 'H':
            rows = len(template) - 1
            panel_height = (page.height - 2 * rows * (border_thickness + outline_thickness)) // rows
            for i in range(rows):
                columns = int(template[i + 1])
                panel_width = (page.width - 2 * columns * (border_thickness + outline_thickness)) // columns
                for j in range(columns):
                    create_and_paste_panel(page, border_thickness, outline_thickness, panel_width, panel_height, page.width, panel_color, bg_color, outline_color, images, i, j, k, len_images, reading_direction)
                    k += 1
        elif first_char == 'V':
            columns = len(template) - 1
            panel_width = (page.width - 2 * columns * (border_thickness + outline_thickness)) // columns
            for j in range(columns):
                rows = int(template[j + 1])
                panel_height = (page.height - 2 * rows * (border_thickness + outline_thickness)) // rows
                for i in range(rows):
                    create_and_paste_panel(page, border_thickness, outline_thickness, panel_width, panel_height, page.width, panel_color, bg_color, outline_color, images, i, j, k, len_images, reading_direction)
                    k += 1
        if border_thickness > 0:
            page = ImageOps.expand(page, border_thickness, bg_color)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Template-Nodes#cr-comic-panel-templates'
        return (pil2tensor(page), show_help)
```