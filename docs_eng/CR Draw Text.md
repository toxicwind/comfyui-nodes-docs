# Documentation
- Class name: CR_DrawText
- Category: Comfyroll/Graphics/Text
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_DrawText node is designed to render the text to the image. It allows custom fonts, colours and locations to create visualally attractive text overlays. This node has a variety of functions that can be used in applications that need to add text dynamics to the image.

# Input types
## Required
- image_width
    - Text will be drawn with the width of the image on it. This is a key parameter that determines the overall size of the output image.
    - Comfy dtype: INT
    - Python dtype: int
- image_height
    - The height of the image. It works with the width and sets the size of the canvas that the text will render.
    - Comfy dtype: INT
    - Python dtype: int
- text
    - The actual text content that you want to draw on the image. It can contain multiple lines of text to fit the paragraph or list.
    - Comfy dtype: STRING
    - Python dtype: str
- font_name
    - font name for the text. It must be a valid.ttf font file available in the font directory.
    - Comfy dtype: STRING
    - Python dtype: str
- font_size
    - font. It affects the readability and visual visibility of the text in the image.
    - Comfy dtype: INT
    - Python dtype: int
- font_color
    - font. It is specified by a name that corresponds to a colour in the predefined colour map.
    - Comfy dtype: STRING
    - Python dtype: str
- background_color
    - The background colour of the text area. It is used to create a background in contrast to the text, making the text more prominent.
    - Comfy dtype: STRING
    - Python dtype: str
- align
    - Text is horizontally aligned. It determines how the text is distributed over the width of the image.
    - Comfy dtype: STRING
    - Python dtype: str
- justify
    - text. It controls the spacing between words and characters in the text.
    - Comfy dtype: STRING
    - Python dtype: str
- margins
    - The space around the text is in pixels. It adds a buffer zone between the text and the image edge.
    - Comfy dtype: INT
    - Python dtype: int
- line_spacing
    - The space between text lines affects the overall readability and layout of multiple lines.
    - Comfy dtype: INT
    - Python dtype: int
- position_x
    - Text will begin horizontal positions. It is calculated in pixels, starting at the left edge of the image.
    - Comfy dtype: INT
    - Python dtype: int
- position_y
    - Text will start with a vertical position. It is calculated in pixels from the top edge of the image.
    - Comfy dtype: INT
    - Python dtype: int
- rotation_angle
    - Text will rotate the angle. It can be used to create a styled effect by tilting the text.
    - Comfy dtype: FLOAT
    - Python dtype: float
- rotation_options
    - Determines the feed point for the rotation of the text. It can be the centre of the text or the centre of the image.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - Draws the result images of the text. It is the main output of the nodes and represents the final visual product.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- show_help
    - is the URL link to the node document. It provides additional information and guidance on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_DrawText:

    @classmethod
    def INPUT_TYPES(s):
        font_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
        file_list = [f for f in os.listdir(font_dir) if os.path.isfile(os.path.join(font_dir, f)) and f.lower().endswith('.ttf')]
        return {'required': {'image_width': ('INT', {'default': 512, 'min': 64, 'max': 2048}), 'image_height': ('INT', {'default': 512, 'min': 64, 'max': 2048}), 'text': ('STRING', {'multiline': True, 'default': 'text'}), 'font_name': (file_list,), 'font_size': ('INT', {'default': 50, 'min': 1, 'max': 1024}), 'font_color': (COLORS,), 'background_color': (COLORS,), 'align': (ALIGN_OPTIONS,), 'justify': (JUSTIFY_OPTIONS,), 'margins': ('INT', {'default': 0, 'min': -1024, 'max': 1024}), 'line_spacing': ('INT', {'default': 0, 'min': -1024, 'max': 1024}), 'position_x': ('INT', {'default': 0, 'min': -4096, 'max': 4096}), 'position_y': ('INT', {'default': 0, 'min': -4096, 'max': 4096}), 'rotation_angle': ('FLOAT', {'default': 0.0, 'min': -360.0, 'max': 360.0, 'step': 0.1}), 'rotation_options': (ROTATE_OPTIONS,)}, 'optional': {'font_color_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'bg_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'draw_text'
    CATEGORY = icons.get('Comfyroll/Graphics/Text')

    def draw_text(self, image_width, image_height, text, font_name, font_size, font_color, background_color, margins, line_spacing, position_x, position_y, align, justify, rotation_angle, rotation_options, font_color_hex='#000000', bg_color_hex='#000000'):
        text_color = get_color_values(font_color, font_color_hex, color_mapping)
        bg_color = get_color_values(background_color, bg_color_hex, color_mapping)
        size = (image_width, image_height)
        text_image = Image.new('RGB', size, text_color)
        back_image = Image.new('RGB', size, bg_color)
        text_mask = Image.new('L', back_image.size)
        rotated_text_mask = draw_masked_text(text_mask, text, font_name, font_size, margins, line_spacing, position_x, position_y, align, justify, rotation_angle, rotation_options)
        image_out = Image.composite(text_image, back_image, rotated_text_mask)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Text-Nodes#cr-draw-text'
        return (pil2tensor(image_out), show_help)
```