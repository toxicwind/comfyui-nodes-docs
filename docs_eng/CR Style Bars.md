# Documentation
- Class name: CR_StyleBars
- Category: Comfyroll/Graphics/Pattern
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_StyleBars is a node for the creation of bar visual drawings that can be used for various graphic applications. It provides a way to create bar styles and direction ranges that can be customized through parameters such as mode, width, height, bar styles and frequency. The function of the node is focused on creating a styled image output that can be used for drawing design or as visual aids in other settings.

# Input types
## Required
- mode
    - The mode parameter determines the type of visual pattern that the node will generate. It can be set as 'collor bars','sin wave' or 'gradient bars', each producing a different visual effect. This parameter is essential because it determines the basic appearance of the output image.
    - Comfy dtype: COMBO['color bars', 'sin wave', 'gradient bars']
    - Python dtype: str
- width
    - The width parameter specifies the width of the image that is generated in pixels. It is an important aspect of the node function because it directly affects the size of the output image and affects its visual presentation.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters set the height at which the image is generated in pixels. Like width, it is a key determinant of image size and plays an important role in the way the final pattern is displayed.
    - Comfy dtype: INT
    - Python dtype: int
- bar_style
    - Bar style parameters define the colour map that should be used to generate bar shapes in the image. It affects the visual beauty of strips and allows various styles to be expressed.
    - Comfy dtype: STYLES
    - Python dtype: str
- orientation
    - The direction parameter determines whether the bar in the image is vertically or horizontally arranged. This selection affects the layout and flow of the pattern in the image.
    - Comfy dtype: COMBO['vertical', 'horizontal']
    - Python dtype: str
- bar_frequency
    - Bar frequency parameters control the frequency at which a bar appears in the image. It is an important factor in determining bar density and spacing and helps to form an overall visual texture.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - Image output provides a pattern of image creation. It is the main result of node operations and is essential for the subsequent use of the pattern in graphic design or other applications.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL link to the document for further help or guidance on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_StyleBars:

    @classmethod
    def INPUT_TYPES(s):
        modes = ['color bars', 'sin wave', 'gradient bars']
        return {'required': {'mode': (modes,), 'width': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'bar_style': (STYLES,), 'orientation': (['vertical', 'horizontal'],), 'bar_frequency': ('INT', {'default': 5, 'min': 1, 'max': 200, 'step': 1})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'draw'
    CATEGORY = icons.get('Comfyroll/Graphics/Pattern')

    def draw(self, mode, width, height, bar_style, orientation, bar_frequency):
        if orientation == 'vertical':
            x = np.linspace(0, 1, width)
            y = np.zeros((height, width))
        elif orientation == 'horizontal':
            x = np.zeros((height, width))
            y = np.linspace(0, 1, height)
        (X, Y) = np.meshgrid(x, y)
        if mode == 'color bars':
            bar_width = 1 / bar_frequency
            if orientation == 'vertical':
                colors = X // bar_width % 2
            elif orientation == 'horizontal':
                colors = Y // bar_width % 2
        elif mode == 'sin wave':
            if orientation == 'vertical':
                colors = np.sin(2 * np.pi * bar_frequency * X)
            elif orientation == 'horizontal':
                colors = np.sin(2 * np.pi * bar_frequency * Y)
        elif mode == 'gradient bars':
            if orientation == 'vertical':
                colors = X * bar_frequency * 2 % 2
            elif orientation == 'horizontal':
                colors = Y * bar_frequency * 2 % 2
        (fig, ax) = plt.subplots(figsize=(width / 100, height / 100))
        ax.imshow(colors, cmap=bar_style, aspect='auto')
        plt.axis('off')
        plt.tight_layout(pad=0, w_pad=0, h_pad=0)
        plt.autoscale(tight=True)
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        img = Image.open(img_buf)
        image_out = pil2tensor(img.convert('RGB'))
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pattern-Nodes#cr-style-bars'
        return (image_out, show_help)
```