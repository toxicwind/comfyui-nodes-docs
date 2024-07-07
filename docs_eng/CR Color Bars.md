# Documentation
- Class name: CR_ColorBars
- Category: Comfyroll/Graphics/Pattern
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_ColorBars node is designed to generate visualization expressions of colour bars with customable parameters. It allows users to specify the direction, frequency and colour of bars and provides a multifunctional tool to create patterns or test display devices. This node contributes to the entire workflow by providing a simple method for generating and operating colour bar models.

# Input types
## Required
- mode
    - The mode parameter determines the type of colour bar that you want to generate. It is essential for setting the initial style of the pattern and influencing the overall appearance of the output.
    - Comfy dtype: COMBO['2-color']
    - Python dtype: str
- width
    - The width parameter sets the width of the colour bar pattern. It is an important aspect of the node function because it directly affects the size of the output image.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters define the height of the colour bar pattern. Similar to width, it is a key factor in determining the size and proportion of the image generated.
    - Comfy dtype: INT
    - Python dtype: int
- color_1
    - The colour 1 parameter specifies the first colour used in the colour bar. It plays an important role in the visual results of the pattern, allowing creative control of the colour scheme.
    - Comfy dtype: COLORS
    - Python dtype: str
- color_2
    - The colour 2 parameter sets the second colour of the colour bar. It works in conjunction with the colour 1 to create a contrast that enhances the visual impact of the pattern.
    - Comfy dtype: COLORS
    - Python dtype: str
- orientation
    - The direction parameter determines the direction of the colour bar. It is a basic setting that determines the layout of the pattern.
    - Comfy dtype: COMBO['vertical', 'horizontal', 'diagonal', 'alt_diagonal']
    - Python dtype: str
- bar_frequency
    - A frequency parameter controls the frequency of the colour bars. It is an important factor in determining the density and spacing of the bars.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- offset
    - Offsets the parameter to adjust the starting position of the colour bar to allow fine-tuning of the pattern.
    - Comfy dtype: FLOAT
    - Python dtype: float
- color1_hex
    - The colour 16-digit parameter allows the user to enter a custom hexadecimal colour value for the first colour, providing greater flexibility and accuracy in colour selection.
    - Comfy dtype: STRING
    - Python dtype: str
- color2_hex
    - Colour 26 parameters enable the user to assign a custom hexadecimal colour value to the second colour, which enhances the ability of nodes to produce a broad colour mix.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - Image output provides a colour bar pattern that is generated as an image. It is the main result of node execution and is essential for the purpose of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a link to the document to obtain further help and guidance on the use of nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ColorBars:

    @classmethod
    def INPUT_TYPES(s):
        modes = ['2-color']
        return {'required': {'mode': (modes,), 'width': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'color_1': (COLORS,), 'color_2': (COLORS,), 'orientation': (['vertical', 'horizontal', 'diagonal', 'alt_diagonal'],), 'bar_frequency': ('INT', {'default': 5, 'min': 1, 'max': 200, 'step': 1}), 'offset': ('FLOAT', {'default': 0, 'min': 0, 'max': 20, 'step': 0.05})}, 'optional': {'color1_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'color2_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'draw'
    CATEGORY = icons.get('Comfyroll/Graphics/Pattern')

    def draw(self, mode, width, height, color_1, color_2, orientation, bar_frequency, offset=0, color1_hex='#000000', color2_hex='#000000'):
        if color_1 == 'custom':
            color1_rgb = hex_to_rgb(color1_hex)
        else:
            color1_rgb = color_mapping.get(color_1, (255, 255, 255))
        if color_2 == 'custom':
            color2_rgb = hex_to_rgb(color2_hex)
        else:
            color2_rgb = color_mapping.get(color_2, (0, 0, 0))
        canvas = np.zeros((height, width, 3), dtype=np.uint8)
        bar_width = width / bar_frequency
        bar_height = height / bar_frequency
        offset_pixels = int(offset * max(width, height))
        if orientation == 'vertical':
            for j in range(height):
                for i in range(width):
                    if (i + offset_pixels) // bar_width % 2 == 0:
                        canvas[j, i] = color1_rgb
                    else:
                        canvas[j, i] = color2_rgb
        elif orientation == 'horizontal':
            for j in range(height):
                for i in range(width):
                    if (j + offset_pixels) // bar_height % 2 == 0:
                        canvas[j, i] = color1_rgb
                    else:
                        canvas[j, i] = color2_rgb
        elif orientation == 'diagonal':
            bar_width = int(bar_height / np.tan(np.pi / 4)) * 2
            for j in range(height):
                for i in range(width):
                    bar_number = (i + j + offset_pixels) // bar_width
                    if bar_number % 2 == 0:
                        canvas[j, i] = color1_rgb
                    else:
                        canvas[j, i] = color2_rgb
        elif orientation == 'alt_diagonal':
            bar_width = int(bar_height / np.tan(np.pi / 4)) * 2
            for j in range(height):
                for i in range(width):
                    bar_number = (i - j + width + offset_pixels) // bar_width
                    if bar_number % 2 == 0:
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
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pattern-Nodes#cr-color-bars'
        return (image_out, show_help)
```