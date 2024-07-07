# Documentation
- Class name: CR_StarburstColors
- Category: Comfyroll/Graphics/Pattern
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_StarbustColors is designed to generate attractive starstorm patterns with customable colours and geometric properties. It provides a creative way to create complex designs that can be used for various graphic applications.

# Input types
## Required
- width
    - Width parameters determine the width of the image generated, which is essential for setting the overall size of a star storm pattern.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The altimeter sets the vertical range of the image and works with the width to create the canvas size of the Star Trek pattern.
    - Comfy dtype: INT
    - Python dtype: int
- num_triangles
    - The number of triangles determines the complexity and detail of star storm patterns and affects overall visual effects.
    - Comfy dtype: INT
    - Python dtype: int
- color_1
    - The first colour parameter allows users to choose the main colour of a star storm, which significantly affects the ultimate beauty of the pattern.
    - Comfy dtype: COLORS
    - Python dtype: str
- color_2
    - The second colour parameter is used to define secondary colours in a star storm and to provide comparative elements for design.
    - Comfy dtype: COLORS
    - Python dtype: str
- center_x
    - Center_x determines the x-coordinate of the centre of the Star Trek, which is essential for locating patterns within the image.
    - Comfy dtype: INT
    - Python dtype: int
- center_y
    - Enter_y Sets the y-coordinate of the Star Trek Center to ensure that the pattern is aligned vertically on the canvas.
    - Comfy dtype: INT
    - Python dtype: int
- bbox_factor
    - The boundary box factor determines the scale of the star storm pattern and influences the size of the triangle within the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- rotation
    - Rotation into a star storm pattern has been added to allow dynamic changes in the design.
    - Comfy dtype: FLOAT
    - Python dtype: float
- color1_hex
    - color1_hex is an optional parameter that allows a custom hexadecimal colour to be entered for the first colour of a star storm and provides advanced colour customization.
    - Comfy dtype: STRING
    - Python dtype: str
- color2_hex
    - color2_hex is an optional parameter to specify a custom hexadecimal colour for the second colour of a star storm and to enhance design flexibility.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - The IMAGE output provides a renderable pattern of a star storm as an image that can be further processed or displayed.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL link to the document to further guide how to use the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_StarburstColors:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'num_triangles': ('INT', {'default': 6, 'min': 1, 'max': 512}), 'color_1': (COLORS,), 'color_2': (COLORS,), 'center_x': ('INT', {'default': 0, 'min': 0, 'max': 512}), 'center_y': ('INT', {'default': 0, 'min': 0, 'max': 512}), 'rotation': ('FLOAT', {'default': 0, 'min': 0, 'max': 720}), 'bbox_factor': ('FLOAT', {'default': 2, 'min': 0, 'max': 2, 'step': 0.01})}, 'optional': {'color1_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'color2_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'draw'
    CATEGORY = icons.get('Comfyroll/Graphics/Pattern')

    def draw(self, width, height, num_triangles, color_1, color_2, center_x, center_y, bbox_factor, rotation=0, color1_hex='#000000', color2_hex='#000000'):
        if color_1 == 'custom':
            color_1 = color1_hex
        else:
            color_1 = color_1
        if color_2 == 'custom':
            color_2 = color2_hex
        else:
            color_2 = color_2
        (fig, ax) = plt.subplots()
        x = width / 100
        y = height / 100
        (fig, ax) = plt.subplots(figsize=(x, y))
        plt.xlim(-x / 2, x / 2)
        plt.ylim(-y / 2, y / 2)
        plt.axis('off')
        plt.tight_layout(pad=0, w_pad=0, h_pad=0)
        plt.autoscale(False)
        box_width = bbox_factor * x
        box_height = bbox_factor * y
        colors = [color_1, color_2]
        tri = num_triangles
        for i in range(tri):
            x1 = center_x / 100
            y1 = center_y / 100
            x2_unrotated = box_width / 2 * np.cos(np.radians(i * 360 / tri))
            y2_unrotated = box_height / 2 * np.sin(np.radians(i * 360 / tri))
            x3_unrotated = box_width / 2 * np.cos(np.radians((i + 1) * 360 / tri))
            y3_unrotated = box_height / 2 * np.sin(np.radians((i + 1) * 360 / tri))
            x2 = x2_unrotated * np.cos(np.radians(rotation)) - y2_unrotated * np.sin(np.radians(rotation))
            y2 = x2_unrotated * np.sin(np.radians(rotation)) + y2_unrotated * np.cos(np.radians(rotation))
            x3 = x3_unrotated * np.cos(np.radians(rotation)) - y3_unrotated * np.sin(np.radians(rotation))
            y3 = x3_unrotated * np.sin(np.radians(rotation)) + y3_unrotated * np.cos(np.radians(rotation))
            ax.fill([x1, x2, x3, x1], [y1, y2, y3, y1], color=colors[i % 2])
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        img = Image.open(img_buf)
        image_out = pil2tensor(img.convert('RGB'))
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pattern-Nodes#cr-starburst-colors'
        return (image_out, show_help)
```