# Documentation
- Class name: CR_OverlayText
- Category: Comfyroll/Graphics/Text
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_OverlayText node is designed to add text to the picture and provides a range of custom options, such as font size, colour and rotation. It enhances the visual effects and information density of the picture by integrating text elements in a user-defined way.

# Input types
## Required
- image
    - To superimpose the base picture of the text. It is a visual canvas of the text.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- text
    - The text content that you want to superimpose on the picture. It can contain multi-line text, which is the core of the node function.
    - Comfy dtype: STRING
    - Python dtype: str
- font_name
    - Specifies the fonts that you want to add to the text. The font selection affects the style and readability of the text.
    - Comfy dtype: STRING
    - Python dtype: str
- font_size
    - Determines the font size of the text. A larger size makes the text more prominent, and a smaller size creates a subtle effect.
    - Comfy dtype: INT
    - Python dtype: int
- font_color
    - Sets the font colour for text stacking. The colour selection affects the contrast and visual impact of the text on the picture.
    - Comfy dtype: STRING
    - Python dtype: str
- align
    - Controls the horizontal alignment of the text on the picture. This is essential for positioning the text in an aesthetic way.
    - Comfy dtype: STRING
    - Python dtype: str
- justify
    - Determines the alignment of the text within the specified margin. It affects the spacing between words in each line.
    - Comfy dtype: STRING
    - Python dtype: str
- margins
    - Sets the margin around the text. A proper margin prevents the text from becoming crowded and improving readability.
    - Comfy dtype: INT
    - Python dtype: int
- line_spacing
    - Controls the spacing between text lines. A proper line spacing enhances the readability of the text.
    - Comfy dtype: INT
    - Python dtype: int
- position_x
    - Specifies the horizontal position (x coordinates) where the text starts on the picture.
    - Comfy dtype: INT
    - Python dtype: int
- position_y
    - Specifies the vertical position (y coordinates) where the text starts on the picture.
    - Comfy dtype: INT
    - Python dtype: int
- rotation_angle
    - Defines the rotation angle of the text. This can be used to position the text from a variety of angles to create creative effects.
    - Comfy dtype: FLOAT
    - Python dtype: float
- rotation_options
    - Determines the rotation point of the text. It can be the centre of the text or the centre of the picture.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- font_color_hex
    - Provides a hexadecimal colour code for fonts. This allows the use of custom colours that are not available in the predefined colour options.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - Applys the image of the result of the text stacking. It represents the final visual output of the node operation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Provides a document link to provide further guidance on how to use the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_OverlayText:

    @classmethod
    def INPUT_TYPES(s):
        font_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'fonts')
        file_list = [f for f in os.listdir(font_dir) if os.path.isfile(os.path.join(font_dir, f)) and f.lower().endswith('.ttf')]
        return {'required': {'image': ('IMAGE',), 'text': ('STRING', {'multiline': True, 'default': 'text'}), 'font_name': (file_list,), 'font_size': ('INT', {'default': 50, 'min': 1, 'max': 1024}), 'font_color': (COLORS,), 'align': (ALIGN_OPTIONS,), 'justify': (JUSTIFY_OPTIONS,), 'margins': ('INT', {'default': 0, 'min': -1024, 'max': 1024}), 'line_spacing': ('INT', {'default': 0, 'min': -1024, 'max': 1024}), 'position_x': ('INT', {'default': 0, 'min': -4096, 'max': 4096}), 'position_y': ('INT', {'default': 0, 'min': -4096, 'max': 4096}), 'rotation_angle': ('FLOAT', {'default': 0.0, 'min': -360.0, 'max': 360.0, 'step': 0.1}), 'rotation_options': (ROTATE_OPTIONS,)}, 'optional': {'font_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'overlay_text'
    CATEGORY = icons.get('Comfyroll/Graphics/Text')

    def overlay_text(self, image, text, font_name, font_size, font_color, margins, line_spacing, position_x, position_y, align, justify, rotation_angle, rotation_options, font_color_hex='#000000'):
        text_color = get_color_values(font_color, font_color_hex, color_mapping)
        image_3d = image[0, :, :, :]
        back_image = tensor2pil(image_3d)
        text_image = Image.new('RGB', back_image.size, text_color)
        text_mask = Image.new('L', back_image.size)
        rotated_text_mask = draw_masked_text(text_mask, text, font_name, font_size, margins, line_spacing, position_x, position_y, align, justify, rotation_angle, rotation_options)
        image_out = Image.composite(text_image, back_image, rotated_text_mask)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Text-Nodes#cr-overlay-text'
        return (pil2tensor(image_out), show_help)
```