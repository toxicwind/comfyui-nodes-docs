# Documentation
- Class name: CR_ColorGradient
- Category: Comfyroll/Graphics/Pattern
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ColorGradient is designed to create smooth colour gradients between two specified colours that can cross the canvas horizontally or vertically. It allows custom gradient transitions and distances and provides users with a multifunctional tool to create visually attractive gradients for applications.

# Input types
## Required
- width
    - The width parameter determines the width of the gradient canvas. It is a key factor in setting the size of the output image, affecting the overall size of the gradient.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The height parameters set the vertical dimensions of the canvas, define the size of the canvas with width and directly influence the demonstration of the gradient.
    - Comfy dtype: INT
    - Python dtype: int
- start_color
    - The starting colour parameter specifies the initial colour of the gradient. It is a basic input that sets the tone for the beginning of the colour transition.
    - Comfy dtype: COLORS
    - Python dtype: str
- end_color
    - Ends the colour parameter that determines the final colour of the gradient. It works with the beginning colour to create a seamless transition between the two colors.
    - Comfy dtype: COLORS
    - Python dtype: str
- orientation
    - The direction parameter determines whether the gradient is horizontal or vertical. This option significantly changes the direction of the colour transition on the canvas.
    - Comfy dtype: COMBO['vertical', 'horizontal']
    - Python dtype: str
## Optional
- linear_transition
    - Linear transition parameters control the midpoint of the gradient transition and allow fine-tuning of the spread of the gradient on canvass.
    - Comfy dtype: FLOAT
    - Python dtype: float
- gradient_distance
    - Gradient distance parameters adjust the length of the gradient transition, affecting the smoothness and range of colour mixing.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_color_hex
    - The starting hexadecimal parameter allows the use of custom hexadecimal colours as the starting colour for gradients, providing greater flexibility in colour selection.
    - Comfy dtype: STRING
    - Python dtype: str
- end_color_hex
    - Ends the colour hexadecimal parameters allow a custom hexadecimal colour value to be specified for the end of the gradient, which enhances the ability of the user to define the colour range.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - Image output provides the colour gradients generated as images that can be used for further processing or presentation purposes.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Helps output provides a link to a document to obtain further guidance on how to use nodes and understand their functionality.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ColorGradient:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'start_color': (COLORS,), 'end_color': (COLORS,), 'gradient_distance': ('FLOAT', {'default': 1, 'min': 0, 'max': 2, 'step': 0.05}), 'linear_transition': ('FLOAT', {'default': 0.5, 'min': 0, 'max': 1, 'step': 0.05}), 'orientation': (['vertical', 'horizontal'],)}, 'optional': {'start_color_hex': ('STRING', {'multiline': False, 'default': '#000000'}), 'end_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'draw'
    CATEGORY = icons.get('Comfyroll/Graphics/Pattern')

    def draw(self, width, height, start_color, end_color, orientation, linear_transition=0.5, gradient_distance=1, start_color_hex='#000000', end_color_hex='#000000'):
        if start_color == 'custom':
            color1_rgb = hex_to_rgb(start_color_hex)
        else:
            color1_rgb = color_mapping.get(start_color, (255, 255, 255))
        if end_color == 'custom':
            color2_rgb = hex_to_rgb(end_color_hex)
        else:
            color2_rgb = color_mapping.get(end_color, (0, 0, 0))
        canvas = np.zeros((height, width, 3), dtype=np.uint8)
        transition_pixel = int(linear_transition * (width if orientation == 'horizontal' else height))

        def get_gradient_value(pos, length, linear_transition, gradient_distance):
            transition_length = length * gradient_distance
            transition_start = linear_transition * length - transition_length / 2
            transition_end = linear_transition * length + transition_length / 2
            if pos < transition_start:
                return 0
            elif pos > transition_end:
                return 1
            else:
                return (pos - transition_start) / transition_length
        if orientation == 'horizontal':
            x = [0, width * linear_transition - 0.5 * width * gradient_distance, width * linear_transition + 0.5 * width * gradient_distance, width]
            y = [0, 0, 1, 1]
            t_values = np.interp(np.arange(width), x, y)
            for (i, t) in enumerate(t_values):
                interpolated_color = [int(c1 * (1 - t) + c2 * t) for (c1, c2) in zip(color1_rgb, color2_rgb)]
                canvas[:, i] = interpolated_color
        elif orientation == 'vertical':
            x = [0, height * linear_transition - 0.5 * height * gradient_distance, height * linear_transition + 0.5 * height * gradient_distance, height]
            y = [0, 0, 1, 1]
            t_values = np.interp(np.arange(height), x, y)
            for (j, t) in enumerate(t_values):
                interpolated_color = [int(c1 * (1 - t) + c2 * t) for (c1, c2) in zip(color1_rgb, color2_rgb)]
                canvas[j, :] = interpolated_color
        (fig, ax) = plt.subplots(figsize=(width / 100, height / 100))
        ax.imshow(canvas)
        plt.axis('off')
        plt.tight_layout(pad=0, w_pad=0, h_pad=0)
        plt.autoscale(tight=True)
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        img = Image.open(img_buf)
        image_out = pil2tensor(img.convert('RGB'))
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pattern-Nodes#cr-color-gradient'
        return (image_out, show_help)
```