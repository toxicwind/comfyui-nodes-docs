# Documentation
- Class name: TextImage
- Category: ♾️Mixlab/Image
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

This node facilitates the creation of images with text content and provides a range of custom options, such as font style, size and colour. It combines text data with visual expressions, enabling the generation of custom visual output that integrates text and design elements. This node is particularly suitable for applications where text information needs to be synthesized into image formats.

# Input types
## Required
- text
    - Text parameters are essential, defining the text content to be rendered to the image. They are the main input for node operations and determine the information or message to be visualized.
    - Comfy dtype: STRING
    - Python dtype: str
- font_path
    - The font_path parameter specifies the font source for the text. It is essential to determine the style of the text in the image, affecting overall beauty and readability.
    - Comfy dtype: STRING
    - Python dtype: str
- font_size
    - The font_size parameter adjusts the size of the text, directly affecting the prominence and readability of the text in the image. It is a key factor in the final output of visual effects.
    - Comfy dtype: INT
    - Python dtype: int
- spacing
    - The spacing parameter defines the distance between the character and the text line, which enhances or reduces the clarity and visual appeal of the image. It plays an important role in the organization and presentation of the text content.
    - Comfy dtype: INT
    - Python dtype: int
- text_color
    - The text_color parameter sets the colour of the text, which affects the contrast of the image and the visual dynamic effect. It is an important aspect of the design and contributes to the overall visual effect.
    - Comfy dtype: STRING
    - Python dtype: str
- vertical
    - The vertical parameter determines the direction of the text, whether horizontally or vertically. This option affects the layout and structure of the text in the image, as well as structure and mobility.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- stroke
    - Stroke parameters apply borders or contours around the text, which enhances the definition of the text and separation from the background. This adds additional visual details and depth to the text.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- IMAGE
    - Image output is the main result of the node, representing the visual expression of the input text. It covers design selection and text layout and provides a physical output that can be used for various applications.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- MASK
    - The MASK output provides a alpha channel for text images, which can be used for advanced image processing and synthesis tasks. It provides a level of control over text transparency and mixing with other visual elements.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class TextImage:

    @classmethod
    def INPUT_TYPES(s):
        {required': {STRING', {multilline': True, 'default': `Long Horse spiritual aging', 'dynamic Prompts': False}, 'font_path': (`STRING', {multiline': False, 'default': `default', `int_size': `INT', {deminin':100,'min','max:000,'step':1, 'display': `numer','spacing': {int', {dnefault': False': 12 -200, 'Bumax:200', falt:ft: 200'
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Image'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False, False)

    def run(self, text, font_path, font_size, spacing, text_color, vertical, stroke):
        (img, mask) = generate_text_image(text, font_path, font_size, text_color, vertical, stroke, (0, 0, 0), 1, spacing)
        img = pil2tensor(img)
        mask = pil2tensor(mask)
        return (img, mask)
```