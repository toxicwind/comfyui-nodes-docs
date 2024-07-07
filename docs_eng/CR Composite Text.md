# Documentation
- Class name: CR_CompositeText
- Category: Graphics/Text
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_CompositeText node is designed to add text to the image background. It provides a comprehensive set of functions from the look of the defined text, including font selection, size, alignment and rotation. The main purpose of the node is to create visually attractive composite images with text that can be used for various purposes, such as graphic design, brand promotion or social media content.

# Input types
## Required
- image_text
    - The image_text parameter is the source image, and the text will be synthesized to this image. It plays a key role in determining the final appearance of the output image, because the text will be placed on this image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image_background
    - The image_background parameter specifies the background image to be used in the synthesis. This is essential for setting the context in which the text appears.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- text
    - The text parameter contains the actual text that will render the image. It is a basic input, as it directly affects the message that the image ultimately synthesizes.
    - Comfy dtype: STRING
    - Python dtype: str
- font_name
    - The font_name parameter is used to select fonts for text. It is important to control the style and readability of text in synthetic images.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- font_size
    - The font_size parameter determines the size of the text. This is a key factor affecting the visual salience and readability of the text in synthesis.
    - Comfy dtype: INT
    - Python dtype: int
- margins
    - Margins parameters specify the space around the text. This is important to ensure that the text does not appear crowded and remains clean and professional.
    - Comfy dtype: INT
    - Python dtype: int
- line_spacing
    - Line_spacing parameters control the vertical space between text lines. It affects the overall layout and readability of multi-line text.
    - Comfy dtype: INT
    - Python dtype: int
- position_x
    - Position_x parameters set the horizontal position of the text on the image. This is essential for synthesizing the text to achieve the desired aesthetic effect.
    - Comfy dtype: INT
    - Python dtype: int
- position_y
    - Position_y parameters set the vertical position of the text on the image. It works with position_x to accurately place the text in the synthesis.
    - Comfy dtype: INT
    - Python dtype: int
- align
    - The align parameter determines the horizontal alignment of the text. This is essential for the visual balance of the overall picture and the text in the image.
    - Comfy dtype: STRING
    - Python dtype: str
- justify
    - Justify parameters control the distribution of text within the image and affect how the text unfolds across the available width.
    - Comfy dtype: STRING
    - Python dtype: str
- rotation_angle
    - Rotation_angle parameters specify the angle from which the text will rotate. This is an important feature for adding a dynamic look to the text in the synthetic image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- rotation_options
    - Rotation_options parameters determine the reference point for text rotation, which may be a text centre or an image centre.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - The IMAGE output provides the final synthetic image with text overlay. It is the main result of node operations and represents the combined result of all input parameters and settings.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL that links to a document page for further help or details about the use of relevant nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_CompositeText:

    @classmethod
    def INPUT_TYPES(s):
        font_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
        file_list = [f for f in os.listdir(font_dir) if os.path.isfile(os.path.join(font_dir, f)) and f.lower().endswith('.ttf')]
        return {'required': {'image_text': ('IMAGE',), 'image_background': ('IMAGE',), 'text': ('STRING', {'multiline': True, 'default': 'text'}), 'font_name': (file_list,), 'font_size': ('INT', {'default': 50, 'min': 1, 'max': 1024}), 'align': (ALIGN_OPTIONS,), 'justify': (JUSTIFY_OPTIONS,), 'margins': ('INT', {'default': 0, 'min': -1024, 'max': 1024}), 'line_spacing': ('INT', {'default': 0, 'min': -1024, 'max': 1024}), 'position_x': ('INT', {'default': 0, 'min': -4096, 'max': 4096}), 'position_y': ('INT', {'default': 0, 'min': -4096, 'max': 4096}), 'rotation_angle': ('FLOAT', {'default': 0.0, 'min': -360.0, 'max': 360.0, 'step': 0.1}), 'rotation_options': (ROTATE_OPTIONS,)}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'composite_text'
    CATEGORY = icons.get('Comfyroll/Graphics/Text')

    def composite_text(self, image_text, image_background, text, font_name, font_size, margins, line_spacing, position_x, position_y, align, justify, rotation_angle, rotation_options):
        image_text_3d = image_text[0, :, :, :]
        image_back_3d = image_background[0, :, :, :]
        text_image = tensor2pil(image_text_3d)
        back_image = tensor2pil(image_back_3d)
        text_mask = Image.new('L', back_image.size)
        rotated_text_mask = draw_masked_text(text_mask, text, font_name, font_size, margins, line_spacing, position_x, position_y, align, justify, rotation_angle, rotation_options)
        image_out = Image.composite(text_image, back_image, rotated_text_mask)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Text-Nodes#cr-composite-text'
        return (pil2tensor(image_out), show_help)
```