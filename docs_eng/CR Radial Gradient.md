# Documentation
- Class name: CR_RadialGradient
- Category: Comfyroll/Graphics/Pattern
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_RadialGradient is designed to generate a gradient image with a diameter. It provides a seamless way to evolve from the beginning colour to the end colour at the specified width and altitude, and to customize the path to the centre and gradient distance.

# Input types
## Required
- width
    - The width parameter defines the width of the output image. It is vital because it determines the horizontal range of the gradient pattern.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters set the height of the output image. It is critical because it determines the vertical range of the gradient.
    - Comfy dtype: INT
    - Python dtype: int
- start_color
    - The starting colour parameter specifies the initial colour of the gradient in the diameter. It plays an important role in determining the overall appearance of the gradient effect.
    - Comfy dtype: COLORS
    - Python dtype: str
- end_color
    - Ends the colour parameter to determine the final color of the gradient. It is important when setting the color of the destination in the gradient transition.
    - Comfy dtype: COLORS
    - Python dtype: str
## Optional
- radial_center_x
    - Radius x parameters adjust to the horizontal position of the gradient centre. It affects the distribution of colours on the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- radial_center_y
    - The longitudinal y-parameter sets the vertical position of the gradient centre. It affects how the gradient colour spreads over the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- gradient_distance
    - Gradient distance parameters control the spread of the gradient and determine the speed of the colour transition from the initial to the end colour.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_color_hex
    - The starting colour hexadecimal parameter allows a custom hexadecimal colour to be set as the starting colour, providing flexibility for precise colour specifications.
    - Comfy dtype: STRING
    - Python dtype: str
- end_color_hex
    - End colour hexadecimal parameters allow a custom hexadecimal colour to be specified for end colours, providing control over the exact colour used by the gradient endpoint.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - The IMAGE output provides the resulting image of a gradient in diameter, which is the main result of node execution.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_Help
    - Show_Help output provides a link to the document to obtain further guidance on the use of this node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_RadialGradient:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'start_color': (COLORS,), 'end_color': (COLORS,), 'gradient_distance': ('FLOAT', {'default': 1, 'min': 0, 'max': 2, 'step': 0.05}), 'radial_center_x': ('FLOAT', {'default': 0.5, 'min': 0, 'max': 1, 'step': 0.05}), 'radial_center_y': ('FLOAT', {'default': 0.5, 'min': 0, 'max': 1, 'step': 0.05})}, 'optional': {'start_color_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'end_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_Help')
    FUNCTION = 'draw'
    CATEGORY = icons.get('Comfyroll/Graphics/Pattern')

    def draw(self, width, height, start_color, end_color, radial_center_x=0.5, radial_center_y=0.5, gradient_distance=1, start_color_hex='#000000', end_color_hex='#000000'):
        if start_color == 'custom':
            color1_rgb = hex_to_rgb(start_color_hex)
        else:
            color1_rgb = color_mapping.get(start_color, (255, 255, 255))
        if end_color == 'custom':
            color2_rgb = hex_to_rgb(end_color_hex)
        else:
            color2_rgb = color_mapping.get(end_color, (0, 0, 0))
        canvas = np.zeros((height, width, 3), dtype=np.uint8)
        center_x = int(radial_center_x * width)
        center_y = int(radial_center_y * height)
        max_distance = np.sqrt(max(center_x, width - center_x) ** 2 + max(center_y, height - center_y) ** 2) * gradient_distance
        for i in range(width):
            for j in range(height):
                distance_to_center = np.sqrt((i - center_x) ** 2 + (j - center_y) ** 2)
                t = distance_to_center / max_distance
                t = max(0, min(t, 1))
                interpolated_color = [int(c1 * (1 - t) + c2 * t) for (c1, c2) in zip(color1_rgb, color2_rgb)]
                canvas[j, i] = interpolated_color
        (fig, ax) = plt.subplots(figsize=(width / 100, height / 100))
        ax.imshow(canvas)
        plt.axis('off')
        plt.tight_layout(pad=0, w_pad=0, h_pad=0)
        plt.autoscale(tight=True)
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        img = Image.open(img_buf)
        image_out = pil2tensor(img.convert('RGB'))
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pattern-Nodes#cr-radial-gradiant'
        return (image_out, show_help)
```