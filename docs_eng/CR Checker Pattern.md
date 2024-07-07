# Documentation
- Class name: CR_CheckerPattern
- Category: Comfyroll/Graphics/Pattern
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_CheckerPatten is a node to generate a board mode for customable parameters. It allows the user to define the pattern of the pattern, the size of the output image, and the colour used in the pattern. The node focuses on creating a visual grid pattern with alternate colours, indicating that it provides a multifunctional tool for graphic design and visualization.

# Input types
## Required
- mode
    - Model parameters determine the layout of the pattern, which can be a'regular' standard chess board or'stepped' deviation mode. This option significantly influences the visual output of nodes and allows different design options.
    - Comfy dtype: MODE
    - Python dtype: str
- width
    - The width parameter sets the width of the image generated in pixels. It is a key factor in determining the size and resolution of the pattern as a whole, affecting its display and use in various applications.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The altimeter sets the height at which the image is generated, in pixels. It defines the size of the canvas with width, which is essential for the scale and width ratio of the pattern.
    - Comfy dtype: INT
    - Python dtype: int
- color_1
    - Color_1 is used to define the first colour of the board pattern. It plays an important role in the overall look of the pattern, allowing creative control over the aesthetics of the design.
    - Comfy dtype: COLOR
    - Python dtype: str
- color_2
    - Color_2 is used to define the second colour of the board pattern. It is used in conjunction with Color_1 to create contrast blocks that are unique to the board design.
    - Comfy dtype: COLOR
    - Python dtype: str
- grid_frequency
    - The grid_frequency parameter indicates the number of squares per row/column in the board chart. It is the key determinant of pattern density and individual square size.
    - Comfy dtype: INT
    - Python dtype: int
- step
    - Long march parameters are used in the'stepped' mode to control the misallocation of the grid. It affects the complexity of the pattern and the visual rhythm of the board.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- color1_hex
    - The color1_hex parameter allows the use of custom hexadecimal colours for Color_1. This provides additional flexibility for users who need to use specific colour shades that are not available in the predefined colour options.
    - Comfy dtype: STRING
    - Python dtype: str
- color2_hex
    - The color2_hex parameter allows the use of custom hexadecimal colours for Color_2. It provides users with the ability to fine-tune minor colours to meet their design requirements.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - The IMAGE output provides a chart of the board that generates points as an image file. This is the main result of the node operation and the heart of the node to create a visual pattern.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL link to the node document page for more guidance and information. This is a useful resource for users seeking relevant node functions and using detailed information.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_CheckerPattern:

    @classmethod
    def INPUT_TYPES(s):
        modes = ['regular', 'stepped']
        return {'required': {'mode': (modes,), 'width': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'color_1': (COLORS,), 'color_2': (COLORS,), 'grid_frequency': ('INT', {'default': 8, 'min': 1, 'max': 200, 'step': 1}), 'step': ('INT', {'default': 2, 'min': 2, 'max': 200, 'step': 1})}, 'optional': {'color1_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'color2_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'draw'
    CATEGORY = icons.get('Comfyroll/Graphics/Pattern')

    def draw(self, mode, width, height, color_1, color_2, grid_frequency, step, color1_hex='#000000', color2_hex='#000000'):
        if color_1 == 'custom':
            color1_rgb = hex_to_rgb(color1_hex)
        else:
            color1_rgb = color_mapping.get(color_1, (255, 255, 255))
        if color_2 == 'custom':
            color2_rgb = hex_to_rgb(color2_hex)
        else:
            color2_rgb = color_mapping.get(color_2, (0, 0, 0))
        canvas = np.zeros((height, width, 3), dtype=np.uint8)
        grid_size = width / grid_frequency
        for i in range(width):
            for j in range(height):
                if mode == 'regular':
                    if i // grid_size % 2 == j // grid_size % 2:
                        canvas[j, i] = color1_rgb
                    else:
                        canvas[j, i] = color2_rgb
                elif mode == 'stepped':
                    if i // grid_size % step != j // grid_size % step:
                        canvas[j, i] = color1_rgb
                    else:
                        canvas[j, i] = color2_rgb
        (fig, ax) = plt.subplots(figsize=(width / 100, height / 100))
        ax.imshow(canvas)
        plt.axis('off')
        plt.tight_layout(pad=0, w_pad=0, h_pad=0)
        plt.autoscale(tight=True)
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        img = Image.open(img_buf)
        image_out = pil2tensor(img.convert('RGB'))
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pattern-Nodes#cr-checker-pattern'
        return (image_out, show_help)
```