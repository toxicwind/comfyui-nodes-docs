# Documentation
- Class name: CR_SimpleTextWatermark
- Category: Comfyroll/Graphics/Text
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SimpleTextWatermark node is designed to add text to the image as a watermark. It allows custom text properties, such as alignment, opacity and font styles, so that watermarks are seamlessly integrated with image content.

# Input types
## Required
- image
    - The image parameter is essential because it defines the basic medium that will be applied to the watermark text. The image selected directly affects the final appearance of the watermark in the image context.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- text
    - Text parameters specify the contents of the watermark that will be superimposed on the image. The information and styles of the text are essential to convey the desired message or brand to the audience.
    - Comfy dtype: STRING
    - Python dtype: str
- align
    - Aligning parameters determines the position of the water print text vis-à-vis the image. This is essential to ensure that the text is placed in a visually attractive and appropriate position.
    - Comfy dtype: STRING
    - Python dtype: str
- font_name
    - Font name parameters select the type of font for the watermark text. The font selection significantly affects the readability and visual attractiveness of the text in the image.
    - Comfy dtype: STRING
    - Python dtype: str
- font_size
    - Font size parameters set the size of the watermark text. This attribute is important because it affects the prominence and readability of the text when it is displayed on the image.
    - Comfy dtype: INT
    - Python dtype: int
- font_color
    - The font colour parameter defines the colour of the watermark text. It plays a key role in ensuring that the text emerges from the image background while maintaining a consistent visual theme.
    - Comfy dtype: STRING
    - Python dtype: str
- opacity
    - The opacity parameter adjusts the level of transparency of the water print text. It is important because it allows the text to be visible and does not override the bottom image content.
    - Comfy dtype: FLOAT
    - Python dtype: float
- x_margin
    - The x_margin parameter specifies the horizontal spacing between the edge of the image and the watermark text. This is important to achieve a balanced layout and prevent the text from appearing too close to the edge of the image.
    - Comfy dtype: INT
    - Python dtype: int
- y_margin
    - The y_margin parameter specifies the vertical spacing between the edge of the image and the watermark text. This is essential to maintain a visually attractive layout and to ensure that the text is not overshadowed by other image elements.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- font_color_hex
    - The font_color_hex parameter allows the use of custom hexadecimal colours for water-printing text. This may be important for exact colour matching with brands or design specifications.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - The IMAGE output provides the final image of the application of the watermark. It is the result of all node parameters working together to produce the required visual effects.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides URLs that point to node documents for further guidance or help. This is a valuable resource for users seeking more information on how to use node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SimpleTextWatermark:

    @classmethod
    def INPUT_TYPES(s):
        font_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
        file_list = [f for f in os.listdir(font_dir) if os.path.isfile(os.path.join(font_dir, f)) and f.lower().endswith('.ttf')]
        ALIGN_OPTIONS = ['center', 'top left', 'top center', 'top right', 'bottom left', 'bottom center', 'bottom right']
        return {'required': {'image': ('IMAGE',), 'text': ('STRING', {'multiline': False, 'default': '@ your name'}), 'align': (ALIGN_OPTIONS,), 'opacity': ('FLOAT', {'default': 0.3, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'font_name': (file_list,), 'font_size': ('INT', {'default': 50, 'min': 1, 'max': 1024}), 'font_color': (COLORS,), 'x_margin': ('INT', {'default': 20, 'min': -1024, 'max': 1024}), 'y_margin': ('INT', {'default': 20, 'min': -1024, 'max': 1024})}, 'optional': {'font_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'overlay_text'
    CATEGORY = icons.get('Comfyroll/Graphics/Text')

    def overlay_text(self, image, text, align, font_name, font_size, font_color, opacity, x_margin, y_margin, font_color_hex='#000000'):
        text_color = get_color_values(font_color, font_color_hex, color_mapping)
        total_images = []
        for img in image:
            img = tensor2pil(img)
            textlayer = Image.new('RGBA', img.size)
            draw = ImageDraw.Draw(textlayer)
            font_file = os.path.join('fonts', str(font_name))
            resolved_font_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), font_file)
            font = ImageFont.truetype(str(resolved_font_path), size=font_size)
            textsize = get_text_size(draw, text, font)
            if align == 'center':
                textpos = [(img.size[0] - textsize[0]) // 2, (img.size[1] - textsize[1]) // 2]
            elif align == 'top left':
                textpos = [x_margin, y_margin]
            elif align == 'top center':
                textpos = [(img.size[0] - textsize[0]) // 2, y_margin]
            elif align == 'top right':
                textpos = [img.size[0] - textsize[0] - x_margin, y_margin]
            elif align == 'bottom left':
                textpos = [x_margin, img.size[1] - textsize[1] - y_margin]
            elif align == 'bottom center':
                textpos = [(img.size[0] - textsize[0]) // 2, img.size[1] - textsize[1] - y_margin]
            elif align == 'bottom right':
                textpos = [img.size[0] - textsize[0] - x_margin, img.size[1] - textsize[1] - y_margin]
            draw.text(textpos, text, font=font, fill=text_color)
            if opacity != 1:
                textlayer = reduce_opacity(textlayer, opacity)
            out_image = Image.composite(textlayer, img, textlayer)
            out_image = np.array(out_image.convert('RGB')).astype(np.float32) / 255.0
            out_image = torch.from_numpy(out_image).unsqueeze(0)
            total_images.append(out_image)
        images_out = torch.cat(total_images, 0)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Text-Nodes#cr-simple-text-watermark'
        return (images_out, show_help)
```