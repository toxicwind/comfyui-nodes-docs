# Documentation
- Class name: CR_DrawPie
- Category: Comfyroll/Graphics/Shape
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_DrawPie is a node designed to generate visual expressions of pie charts. It allows the appearance of customized pie charts, including their dimensions, starting and ending angles, colours and rotations. The function of the node is concentrated on the graphical representation of the creation of a data segment, making it a multifunctional tool for visualizing scales and distributions.

# Input types
## Required
- width
    - The width determines the width of the pie map, which is the key parameter for setting the overall size of the output image. It directly affects the ratio of visualization to width.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Height sets the vertical range of the pie map to determine the scale of the chart with width. It plays an important role in the final look of the pie map, ensuring a balance of visual expression.
    - Comfy dtype: INT
    - Python dtype: int
- pie_start
    - The pie chart begins with the initial angle of the pie section. It is essential to define the starting position of the sub-section and helps with the structure of the entire pie.
    - Comfy dtype: FLOAT
    - Python dtype: float
- pie_stop
    - The end of the pie is the angle of the end of the pie. It works with the beginning of the pie to determine the size and scope of the pie.
    - Comfy dtype: FLOAT
    - Python dtype: float
- shape_color
    - Shape colours define the colour of the pie drawings and allow the user to customize the appearance of the data. This is a key aspect of visual design that conveys different meanings or categories.
    - Comfy dtype: COLORS
    - Python dtype: str
- back_color
    - Background colours set the background colours for the pie charts, providing contrasting or complementary colours for the shape colours. They are important parameters for enhancing the visual appeal and clarity of the charts.
    - Comfy dtype: COLORS
    - Python dtype: str
## Optional
- x_offset
    - X offsets are used to adjust the horizontal position of a clothed pie map. It can be used to align multiple charts or to locate charts for aesthetic purposes.
    - Comfy dtype: INT
    - Python dtype: int
- y_offset
    - Y offsets are used to adjust the vertical position of a clothed pie map. Similar to X offsets, it helps to display positioning charts for the best vision.
    - Comfy dtype: INT
    - Python dtype: int
- zoom
    - Scales are a ratio factor that adjusts the size of a pie against its original size. It can be used to emphasize a chart or adapt it to a specific space.
    - Comfy dtype: FLOAT
    - Python dtype: float
- rotation
    - Rotation allows you to rotate around the centre of the pie map. This can be used to direct the chart to a particular direction or to create dynamic visual effects.
    - Comfy dtype: FLOAT
    - Python dtype: float
- shape_color_hex
    - The shape colour hexadecimal system provides a hexadecimal colour code for the biscuits and provides precise control over the use of colours. It is an alternative to the shape colour parameters and applies to users who require a specific colour value.
    - Comfy dtype: STRING
    - Python dtype: str
- bg_color_hex
    - The background colour hexadecimal has assigned a hexadecimal colour code to the background of the pie map, allowing fine-tuning of the background colour to meet specific design requirements.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - The IMAGE output provides the pie charts generated as image files. This is the main result of the node operation and contains visual expressions of data input.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL link to the document page to obtain further help or information about the use and function of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_DrawPie:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'width': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'pie_start': ('FLOAT', {'default': 30.0, 'min': 0.0, 'max': 9999.0, 'step': 0.1}), 'pie_stop': ('FLOAT', {'default': 330.0, 'min': 0.0, 'max': 9999.0, 'step': 0.1}), 'shape_color': (COLORS,), 'back_color': (COLORS,), 'x_offset': ('INT', {'default': 0, 'min': -2048, 'max': 2048}), 'y_offset': ('INT', {'default': 0, 'min': -2048, 'max': 2048}), 'zoom': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.05}), 'rotation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 3600.0, 'step': 0.1})}, 'optional': {'shape_color_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'bg_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'make_shape'
    CATEGORY = icons.get('Comfyroll/Graphics/Shape')

    def make_shape(self, width, height, rotation, pie_start, pie_stop, shape_color, back_color, x_offset=0, y_offset=0, zoom=1.0, shape_color_hex='#000000', bg_color_hex='#000000'):
        bg_color = get_color_values(back_color, bg_color_hex, color_mapping)
        shape_color = get_color_values(shape_color, shape_color_hex, color_mapping)
        back_img = Image.new('RGB', (width, height), color=bg_color)
        shape_img = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(shape_img, 'RGBA')
        center_x = width // 2 + x_offset
        center_y = height // 2 + y_offset
        size = min(width - x_offset, height - y_offset) * zoom
        aspect_ratio = width / height
        num_rays = 16
        color = 'white'
        draw.pieslice([(center_x - size / 2, center_y - size / 2), (center_x + size / 2, center_y + size / 2)], start=pie_start, end=pie_stop, fill=color, outline=None)
        shape_img = shape_img.rotate(rotation, center=(center_x, center_y))
        result_image = Image.alpha_composite(back_img.convert('RGBA'), shape_img)
        image_out = pil2tensor(result_image.convert('RGB'))
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pattern-Nodes-2#cr-draw-pie'
        return (image_out, show_help)
```