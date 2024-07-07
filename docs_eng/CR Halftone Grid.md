# Documentation
- Class name: CR_HalftoneGrid
- Category: Comfyroll/Graphics/Pattern
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_HalftoneGrid is a node used to create a semi-coloured grid pattern, with custom-made parameters. It allows users to set the width, height, point style, frequency and location of the grid and provides a multifunctional way for graphic design purposes to generate visually attractive patterns. The function of the node is concentrated on producing a semi-colour effect, which is an image rendering that uses different points of size and spacing to simulate different grey shadows.

# Input types
## Required
- width
    - Width determines the horizontal range of the semi-coloured grid. This is a key parameter because it directly affects the overall size and proportion of the pattern generated.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The vertical size of the grid is set at altitude, which is essential to control the vertical dimensions of the pattern and ensure its adaptation to the layout required.
    - Comfy dtype: INT
    - Python dtype: int
- dot_style
    - The point style defines the visual appearance of the inner grid and allows for the aesthetic characteristics of the drawings.
    - Comfy dtype: STYLES
    - Python dtype: str
- reverse_dot_style
    - Reverse point styles provide an option to reverse point patterns and create a mirror effect that enhances the visual interest of the grid.
    - Comfy dtype: COMBO['No', 'Yes']
    - Python dtype: str
- dot_frequency
    - Point frequency controls the number of cells in the grid, affecting the particle size and detail level of the semi-colour pattern.
    - Comfy dtype: INT
    - Python dtype: int
- background_color
    - The background colour sets the background colour of the grid, which can be customised or set as the default colour to supplement the pattern.
    - Comfy dtype: COLORS
    - Python dtype: str
- x_pos
    - The X position determines the horizontal position of the pattern in the grid and allows for precise control over the alignment of the pattern.
    - Comfy dtype: FLOAT
    - Python dtype: float
- y_pos
    - The Y position sets the vertical position of the point pattern, which is important for aligning the pattern within the vertical space of the grid.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- bg_color_hex
    - The background colour hexadecimal system allows the use of custom hexadecimal colours for the background of the grid, providing additional flexibility on colour selection.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - The IMAGE output provided the resulting semi-coloured grid pattern as an image that could be further processed or displayed.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL link to the document page for further help and guidance on the use of CR_HalftoneGrid node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_HalftoneGrid:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 4096}), 'dot_style': (STYLES,), 'reverse_dot_style': (['No', 'Yes'],), 'dot_frequency': ('INT', {'default': 50, 'min': 1, 'max': 200, 'step': 1}), 'background_color': (COLORS,), 'x_pos': ('FLOAT', {'default': 0.5, 'min': 0, 'max': 1, 'step': 0.01}), 'y_pos': ('FLOAT', {'default': 0.5, 'min': 0, 'max': 1, 'step': 0.01})}, 'optional': {'bg_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'halftone'
    CATEGORY = icons.get('Comfyroll/Graphics/Pattern')

    def halftone(self, width, height, dot_style, reverse_dot_style, dot_frequency, background_color, x_pos, y_pos, bg_color_hex='#000000'):
        if background_color == 'custom':
            bgc = bg_color_hex
        else:
            bgc = background_color
        reverse = ''
        if reverse_dot_style == 'Yes':
            reverse = '_r'
        (fig, ax) = plt.subplots(figsize=(width / 100, height / 100))
        dotsx = np.linspace(0, 1, dot_frequency)
        dotsy = np.linspace(0, 1, dot_frequency)
        (X, Y) = np.meshgrid(dotsx, dotsy)
        dist = np.sqrt((X - x_pos) ** 2 + (Y - y_pos) ** 2)
        fig.patch.set_facecolor(bgc)
        ax.scatter(X, Y, c=dist, cmap=dot_style + reverse)
        plt.axis('off')
        plt.tight_layout(pad=0, w_pad=0, h_pad=0)
        plt.autoscale(tight=True)
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        img = Image.open(img_buf)
        image_out = pil2tensor(img.convert('RGB'))
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pattern-Nodes#cr-halftone-grid'
        return (image_out, show_help)
```