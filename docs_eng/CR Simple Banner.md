# Documentation
- Class name: CR_SimpleBanner
- Category: Comfyroll/Graphics/Template
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SimpleBanner node is designed to create visually attractive banners from the images and text provided. It is intelligently resizes the text and its location, ensures that the banners are easy to read and beautiful, and provides custom options for fonts, colours and contours to meet different design needs.

# Input types
## Required
- image
    - The image parameter is essential to the process of creating the banner because it forms the visual basis for the output. It determines the canvas that the text will be rendered.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- banner_text
    - The banner text is a key input that conveys messages or messages intended to reach the audience. This is the main element that will be styled and displayed on the banner.
    - Comfy dtype: STRING
    - Python dtype: str
- font_name
    - The font name parameter determines the style of the text on the banner and affects the overall sense of the end output. It is a key factor in setting the tone for the banner message.
    - Comfy dtype: STRING
    - Python dtype: str
- max_font_size
    - The maximum font size parameter ensures that the text is appropriate to the size of the banner while remaining readable. This is a key factor in the layout and design of the banner text.
    - Comfy dtype: INT
    - Python dtype: int
- font_color
    - The font colour parameter allows custom text to look at and ensure that it is highlighted in the banner background in order to achieve maximum visual impact.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- outline_thickness
    - The contour thickness parameter adds a border around the text, increases its visibility and gives it a clearer look. This is an optional feature that can be adjusted according to design preferences.
    - Comfy dtype: INT
    - Python dtype: int
- outline_color
    - Outline colour parameters supplement the text by defining the colour of the text border and contribute to the overall aesthetic appeal of the banner.
    - Comfy dtype: STRING
    - Python dtype: str
- margin_size
    - The margin size parameters adjust the distance around the text, provide a balanced look and ensure that the text does not appear to be overcrowded or too thin on the banners.
    - Comfy dtype: INT
    - Python dtype: int
- font_color_hex
    - Font colour hexadecimal parameters allow precise colour customization of text using hexadecimal values, providing a wide range of colour options for the text of banners.
    - Comfy dtype: STRING
    - Python dtype: str
- outline_color_hex
    - An outline colour hexadecimal parameter specifies a hexadecimal colour value for the text's contour, allows detailed colour adjustments and enhances the visual design of the banner.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- image
    - The output image is the final banner, which combines styled text and design elements. It represents all input parameters and custom-made results for banners.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Displays the help parameters to provide a link to the document for further guidance and help on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SimpleBanner:

    @classmethod
    def INPUT_TYPES(s):
        font_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
        file_list = [f for f in os.listdir(font_dir) if os.path.isfile(os.path.join(font_dir, f)) and f.lower().endswith('.ttf')]
        return {'required': {'image': ('IMAGE',), 'banner_text': ('STRING', {'multiline': True, 'default': 'text'}), 'font_name': (file_list,), 'max_font_size': ('INT', {'default': 150, 'min': 20, 'max': 2048}), 'font_color': (COLORS,), 'outline_thickness': ('INT', {'default': 0, 'min': 0, 'max': 500}), 'outline_color': (COLORS,), 'margin_size': ('INT', {'default': 0, 'min': 0, 'max': 500})}, 'optional': {'font_color_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'outline_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('image', 'show_help')
    FUNCTION = 'make_banner'
    CATEGORY = icons.get('Comfyroll/Graphics/Template')

    def make_banner(self, image, banner_text, font_name, max_font_size, font_color, outline_thickness, outline_color, margin_size, font_color_hex='#000000', outline_color_hex='#000000'):
        text_color = get_color_values(font_color, font_color_hex, color_mapping)
        outline_color = get_color_values(outline_color, outline_color_hex, color_mapping)
        total_images = []
        for img in image:
            back_image = tensor2pil(img).convert('RGBA')
            size = (back_image.width, back_image.height)
            font_file = os.path.join('fonts', font_name)
            resolved_font_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), font_file)
            draw = ImageDraw.Draw(back_image)
            area_width = back_image.width - margin_size * 2
            area_height = back_image.width - margin_size * 2
            font = get_font_size(draw, banner_text, area_width, area_height, resolved_font_path, max_font_size)
            x = back_image.width // 2
            y = back_image.height // 2
            if outline_thickness > 0:
                draw.text((x, y), banner_text, fill=text_color, font=font, anchor='mm', stroke_width=outline_thickness, stroke_fill=outline_color)
            else:
                draw.text((x, y), banner_text, fill=text_color, font=font, anchor='mm')
            out_image = np.array(back_image.convert('RGB')).astype(np.float32) / 255.0
            out_image = torch.from_numpy(out_image).unsqueeze(0)
            total_images.append(out_image)
        images_out = torch.cat(total_images, 0)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Template-Nodes#cr-simple-banner'
        return (images_out, show_help)
```