# Documentation
- Class name: CR_BinaryPattern
- Category: Comfyroll/Graphics/Pattern
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_BinaryPatten node is designed to generate visual patterns from binary strings. It accepts binary mode input, rendering it into a grid of coloured squares, and provides a way to visualize binary data in graphic format. This node is particularly suitable for creating complex designs and patterns based on binary sequences and provides a unique way of visualizing data.

# Input types
## Required
- binary_pattern
    - Binary mode input is the key parameter of the node because it directly determines the visual output. This is a multi-line string that represents a series of binary numbers used to construct the mode. The complexity and design of the final model are largely influenced by this input.
    - Comfy dtype: STRING
    - Python dtype: str
- width
    - The width parameter determines the width of the output image in pixels, which is essential for setting the overall size of the pattern. It works in conjunction with the height parameter to ensure that the pattern is scalded appropriately to fit the required width ratio.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters set the vertical dimensions of the output image, determining the size of the pattern with the width parameters. It is a key factor in controlling the image's overall appearance and scalability.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- background_color
    - Background colour parameters allow the background of a custom pattern to affect the overall visual appeal and contrast of the rendering pattern. It can be set to predefined colours or custom hexadecimal colours.
    - Comfy dtype: COLORS
    - Python dtype: str
- outline_color
    - An outline colour parameter defines the colour of the contour of a square, adds a layer of detail and enhances the visibility of the pattern and the background. It can be adjusted to match or contrast the colour of the pattern to achieve the purpose of style.
    - Comfy dtype: COLORS
    - Python dtype: str

# Output types
- IMAGE
    - The IMAGE output provides a renderable binary mode as an image that can be used for further processing or displaying. It represents the top of the node function and shows the visual representation of the input binary mode.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides URLs that point to node document pages, and provides users with additional information and guidance on how to use nodes effectively. It is a useful resource for understanding node capabilities and potential cases.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_BinaryPattern:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'binary_pattern': ('STRING', {'multiline': True, 'default': '10101'}), 'width': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'background_color': (COLORS,), 'color_0': (COLORS,), 'color_1': (COLORS,), 'outline_thickness': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'outline_color': (COLORS,), 'jitter_distance': ('INT', {'default': 0, 'min': 0, 'max': 1024}), 'bias': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.05})}, 'optional': {'bg_color_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'color0_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'color1_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'outline_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'draw_pattern'
    CATEGORY = icons.get('Comfyroll/Graphics/Pattern')

    def draw_pattern(self, binary_pattern, width, height, background_color, outline_color, color_0='white', color_1='black', outline_thickness=0, color0_hex='#000000', color1_hex='#000000', bg_color_hex='#000000', outline_color_hex='#000000', jitter_distance=0, bias=0.5):
        color0 = get_color_values(color_0, color0_hex, color_mapping)
        color1 = get_color_values(color_1, color1_hex, color_mapping)
        bg_color = get_color_values(background_color, bg_color_hex, color_mapping)
        outline_color = get_color_values(outline_color, outline_color_hex, color_mapping)
        rows = binary_pattern.strip().split('\n')
        grid = [[int(bit) for bit in row.strip()] for row in rows]
        square_width = width / len(rows[0])
        square_height = height / len(rows)
        image = Image.new('RGB', (width, height), color=bg_color)
        draw = ImageDraw.Draw(image)
        x_jitter = 0
        y_jitter = 0
        for (row_index, row) in enumerate(grid):
            for (col_index, bit) in enumerate(row):
                if jitter_distance != 0:
                    x_jitter = random.uniform(0, jitter_distance)
                    y_jitter = random.uniform(0, jitter_distance)
                x1 = col_index * square_width + x_jitter
                y1 = row_index * square_height + y_jitter
                x2 = x1 + square_width + x_jitter
                y2 = y1 + square_height + y_jitter
                if random.uniform(0, 1) < abs(bias):
                    color = color1
                else:
                    color = color0
                draw.rectangle([x1, y1, x2, y2], fill=color, outline=outline_color, width=outline_thickness)
        image_out = pil2tensor(image)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pattern-Nodes-2#cr-binary-pattern'
        return (image_out, show_help)
```