# Documentation
- Class name: CR_RandomShapePattern
- Category: Comfyroll/Graphics/Shape
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_Random ShapePatten is a node used to generate images of randomly placed shapes. It provides a creative way to create visually diverse and structured patterns that apply to artistic expressions or data visualization purposes. The node uses randomity to select shapes, colours and locations to ensure that each output is unique.

# Input types
## Required
- width
    - Width determines the horizontal range of the output image. This is a key parameter because it determines the overall size of the pattern and the size of the individual shape in the pattern.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Height sets the vertical dimensions that generate the image and influences the vertical spacing and alignment of the shapes in the pattern.
    - Comfy dtype: INT
    - Python dtype: int
- num_rows
    - Lines determine the vertical structure of the grid of the pattern, influencing the distribution of shapes along image heights.
    - Comfy dtype: INT
    - Python dtype: int
- num_cols
    - The columns specify the horizontal structure of the grid of the pattern and determine the distribution of shapes over the width of the image.
    - Comfy dtype: INT
    - Python dtype: int
- color1
    - Colour 1 is one of the two colours used to randomly fill the shapes in the pattern. It helps the overall colour scheme and the visual contrast of the image.
    - Comfy dtype: COLORS
    - Python dtype: str
- color2
    - Colour 2 is the second colour option used to fill the shape of a drawing case. It is used with colour 1 to create a diverse and visually attractive combination of colours.
    - Comfy dtype: COLORS
    - Python dtype: str
## Optional
- color1_hex
    - The colour 16 system allows the use of custom hexadecimal colours for colour 1 to provide greater flexibility in the colour selection of the shape.
    - Comfy dtype: STRING
    - Python dtype: str
- color2_hex
    - The colour 26 system provides a method for assigning custom hexadecimal colours to colour 2 and enhances the ability of nodes to produce various colour combinations.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - Image output is the main result of nodes, showing images of randomly placed shapes of different colours and sizes.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL link to the document page to get more help and information about the use and functions of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_RandomShapePattern:

    @classmethod
    def INPUT_TYPES(cls):
        shapes = ['circle', 'oval', 'square', 'diamond', 'triangle', 'hexagon', 'octagon', 'half circle', 'quarter circle', 'starburst', 'star', 'cross']
        return {'required': {'width': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'num_rows': ('INT', {'default': 5, 'min': 1, 'max': 128}), 'num_cols': ('INT', {'default': 5, 'min': 1, 'max': 128}), 'color1': (COLORS,), 'color2': (COLORS,)}, 'optional': {'color1_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'color2_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'plot_random_shapes'
    CATEGORY = icons.get('Comfyroll/Graphics/Shape')

    def plot_random_shapes(self, num_rows, num_cols, width, height, color1, color2, color1_hex='#000000', color2_hex='#000000'):
        color1 = get_color_values(color1, color1_hex, color_mapping)
        color2 = get_color_values(color2, color2_hex, color_mapping)
        image = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(image)
        shape_functions = [draw_circle, draw_oval, draw_diamond, draw_square, draw_triangle, draw_hexagon, draw_octagon, draw_half_circle, draw_quarter_circle, draw_starburst, draw_star, draw_cross]
        for row in range(num_rows):
            for col in range(num_cols):
                shape_function = random.choice(shape_functions)
                color = random.choice([color1, color2])
                size = random.uniform(20, min(width, height) / 2)
                aspect_ratio = random.uniform(0.5, 2.0)
                center_x = col * (width / num_cols) + width / num_cols / 2
                center_y = row * (height / num_rows) + height / num_rows / 2
                shape_function(draw, center_x, center_y, size, aspect_ratio, color)
        image_out = pil2tensor(image)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pattern-Nodes-2#cr-random-shape-pattern'
        return (image_out, show_help)
```