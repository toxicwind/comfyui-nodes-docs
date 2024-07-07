# Documentation
- Class name: CR_MaskText
- Category: Graphics/Text
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_MaskText node is designed to add text to the image in a styled manner. It allows custom fonts, sizes, colours and locations to create visualally attractive text overlays. The node emphasizes the integration of text into graphic elements to enhance the overall beauty of the image.

# Input types
## Required
- image
    - The image will be masked. It will serve as the basis for the whole operation, and the text will be applied directly to it. The selection of the image will have an important effect on the final visual effect.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- text
    - The text content that you want to mask on the image. The content and structure of the text can significantly change the message that the final image conveys, making it the key parameter of the node function.
    - Comfy dtype: STRING
    - Python dtype: str
- font_name
    - A specific font file for rendering the text. Different fonts can significantly change the style and readability of the text, thus playing an important role in node execution.
    - Comfy dtype: STRING
    - Python dtype: str
- font_size
    - Font size for text. The font size directly influences the readability and visibility of the text in the image.
    - Comfy dtype: INT
    - Python dtype: int
- background_color
    - The colour of the background behind the text. This can be a predefined colour or a custom hexadecimal colour that affects the contrast of text cover and visual appeal.
    - Comfy dtype: STRING
    - Python dtype: str
- align
    - text is horizontally aligned. It determines the position of the text within the image width and affects the overall layout.
    - Comfy dtype: STRING
    - Python dtype: str
- justify
    - text alignment. It controls the spacing between words and affects the homogeneity of the face of the text block.
    - Comfy dtype: STRING
    - Python dtype: str
- margins
    - The space around the text, i.e., the margin. It adds a buffer area around the text, which may be important for the visibility of the text and for image mapping.
    - Comfy dtype: INT
    - Python dtype: int
- line_spacing
    - Vertical space between text lines. It affects the readability and overall compactness of multiple lines of text.
    - Comfy dtype: INT
    - Python dtype: int
- position_x
    - The horizontal position of the text from the left edge of the image. It is essential for the precise placement of the text in the image.
    - Comfy dtype: INT
    - Python dtype: int
- position_y
    - text from the vertical position of the top edge of the image. It is used in conjunction with the horizontal position to accurately place the text.
    - Comfy dtype: INT
    - Python dtype: int
- rotation_angle
    - The angle of the text rotates. It provides a method of locating the text in various directions, adding dynamic elements to the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- rotation_options
    - Determines the location of the rotor point, either the text centre or the image centre. This affects how the text is perceived in relation to the image.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- bg_color_hex
    - A custom hexadecimal colour for the background. It allows further custom text background and enhances the flexibility of the node function.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - The output image of the masked text is applied. It is the result of node processing and represents the final visual product.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - The URL link to the document is used for further help. It provides the user with additional resources to understand and remove malfunctions in node functions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_MaskText:

    @classmethod
    def INPUT_TYPES(s):
        font_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
        file_list = [f for f in os.listdir(font_dir) if os.path.isfile(os.path.join(font_dir, f)) and f.lower().endswith('.ttf')]
        return {'required': {'image': ('IMAGE',), 'text': ('STRING', {'multiline': True, 'default': 'text'}), 'font_name': (file_list,), 'font_size': ('INT', {'default': 50, 'min': 1, 'max': 1024}), 'background_color': (COLORS,), 'align': (ALIGN_OPTIONS,), 'justify': (JUSTIFY_OPTIONS,), 'margins': ('INT', {'default': 0, 'min': -1024, 'max': 1024}), 'line_spacing': ('INT', {'default': 0, 'min': -1024, 'max': 1024}), 'position_x': ('INT', {'default': 0, 'min': -4096, 'max': 4096}), 'position_y': ('INT', {'default': 0, 'min': -4096, 'max': 4096}), 'rotation_angle': ('FLOAT', {'default': 0.0, 'min': -360.0, 'max': 360.0, 'step': 0.1}), 'rotation_options': (ROTATE_OPTIONS,)}, 'optional': {'bg_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'mask_text'
    CATEGORY = icons.get('Comfyroll/Graphics/Text')

    def mask_text(self, image, text, font_name, font_size, margins, line_spacing, position_x, position_y, background_color, align, justify, rotation_angle, rotation_options, bg_color_hex='#000000'):
        bg_color = get_color_values(background_color, bg_color_hex, color_mapping)
        image_3d = image[0, :, :, :]
        text_image = tensor2pil(image_3d)
        text_mask = Image.new('L', text_image.size)
        background_image = Image.new('RGB', text_mask.size, bg_color)
        rotated_text_mask = draw_masked_text(text_mask, text, font_name, font_size, margins, line_spacing, position_x, position_y, align, justify, rotation_angle, rotation_options)
        text_mask = ImageOps.invert(rotated_text_mask)
        image_out = Image.composite(background_image, text_image, text_mask)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Text-Nodes#cr-mask-text'
        return (pil2tensor(image_out), show_help)
```