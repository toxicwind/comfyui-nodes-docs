# Documentation
- Class name: CR_StarburstLines
- Category: Comfyroll/Graphics/Pattern
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_StarbustLines is designed to create a visually attractive starstorm pattern consisting of lines that are evenly distributed from the centre point. It allows for the definition of parameters, such as number of lines, length and colour, to create a unique and symmetrical design.

# Input types
## Required
- width
    - The width parameters determine the width of the image generated. It is essential to set the overall size of a star storm pattern and to ensure that it adapts to the size of the canvas required.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters set the height of the image to determine the full canvas size of the star storm pattern with width.
    - Comfy dtype: INT
    - Python dtype: int
- num_lines
    - The number of lines determines the number of lines that will form a star storm, affecting the complexity and visual symmetry of the final pattern.
    - Comfy dtype: INT
    - Python dtype: int
- line_length
    - The length of the line specifies the length from which each line extends from the centre and contributes to the overall visual impact and direction of the star storm.
    - Comfy dtype: FLOAT
    - Python dtype: float
- line_width
    - Line width parameters control the thickness of each line in a star storm, affecting the visibility and detail of the image.
    - Comfy dtype: INT
    - Python dtype: int
- line_color
    - Line colours define the colour of line lines in a star storm and allow creative expression and visual comparison in the design.
    - Comfy dtype: COLORS
    - Python dtype: str
- background_color
    - The background colour sets the colour of the canvas behind the Star Trek, providing a background that complements the pattern and enhances its visibility.
    - Comfy dtype: COLORS
    - Python dtype: str
- center_x
    - Centre x designates the x-coordinate of the central point from the Star Trek Line to influence the alignment of the pattern on the canvas.
    - Comfy dtype: INT
    - Python dtype: int
- center_y
    - Centery determined the y-coordinate of the Star Trench Center and influenced the vertical position of the pattern.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- rotation
    - Rotation allows the direction of the pattern to be adjusted by the specified number of degrees, providing control over the direction of the pattern.
    - Comfy dtype: FLOAT
    - Python dtype: float
- line_color_hex
    - The line colour hexadecimal system provides a hexadecimal colour code that defines the colour of the line, making the colour selection of the line more accurate.
    - Comfy dtype: STRING
    - Python dtype: str
- bg_color_hex
    - The background colour hexadecimal system provides a hexadecimal colour code for custom background colours, allowing personalized canvas background.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - The IMAGE output contains a renderable star storm pattern as an image file for further use or display.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a link to the document to obtain additional information and guidance on the use of CR_StarbustLines nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_StarburstLines:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'num_lines': ('INT', {'default': 6, 'min': 1, 'max': 500}), 'line_length': ('FLOAT', {'default': 5, 'min': 0, 'max': 100, 'step': 0.1}), 'line_width': ('INT', {'default': 5, 'min': 1, 'max': 512}), 'line_color': (COLORS,), 'background_color': (COLORS,), 'center_x': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'center_y': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'rotation': ('FLOAT', {'default': 0, 'min': 0, 'max': 720})}, 'optional': {'line_color_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'bg_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'draw'
    CATEGORY = icons.get('Comfyroll/Graphics/Pattern')

    def draw(self, width, height, num_lines, line_length, line_width, line_color, background_color, center_x, center_y, rotation=0, line_color_hex='#000000', bg_color_hex='#000000'):
        if line_color == 'custom':
            line_color = line_color_hex
        else:
            line_color = line_color
        if background_color == 'custom':
            bgc = bg_color_hex
        else:
            bgc = background_color
        angle = 360 / num_lines
        (fig, ax) = plt.subplots(figsize=(width / 100, height / 100))
        plt.xlim(-width / 100, width / 100)
        plt.ylim(-height / 100, height / 100)
        plt.axis('off')
        plt.tight_layout(pad=0, w_pad=0, h_pad=0)
        plt.autoscale(False)
        center_x = center_x / 100
        center_y = center_y / 100
        for i in range(num_lines):
            x_unrotated = center_x + line_length * np.cos(np.radians(i * angle))
            y_unrotated = center_y + line_length * np.sin(np.radians(i * angle))
            x = center_x + x_unrotated * np.cos(np.radians(rotation)) - y_unrotated * np.sin(np.radians(rotation))
            y = center_y + x_unrotated * np.sin(np.radians(rotation)) + y_unrotated * np.cos(np.radians(rotation))
            fig.patch.set_facecolor(bgc)
            ax.plot([center_x, x], [center_y, y], color=line_color, linewidth=line_width)
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        img = Image.open(img_buf)
        image_out = pil2tensor(img.convert('RGB'))
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pattern-Nodes#cr-starburst-lines'
        return (image_out, show_help)
```