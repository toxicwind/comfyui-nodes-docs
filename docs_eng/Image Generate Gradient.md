# Documentation
- Class name: WAS_Image_Generate_Gradient
- Category: WAS Suite/Image/Generate
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Generate_Gradient node is designed to stop producing seamless gradient textures from a given set of colours. It deals intelligently with the transition between colours to ensure smooth gradients that can be smoothed without visible seams. This is particularly useful in generating background textures for applications such as a game or a 3D model that requires a seamless pattern.

# Input types
## Required
- gradient_stops
    - Gradient_stops parameters define the colour stop for creating gradients. Each stop point is assigned a percentage of the length of the gradient, followed by the RGB colours, separated by a colon. This parameter is essential for determining the colour and distribution of the gradients.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- width
    - The width parameter sets the width of the gradient image generated. It is an important parameter because it determines the horizontal resolution of the output image.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The header parameter sets the height of the gradient image generated. It is an important parameter because it determines the vertical resolution of the output image.
    - Comfy dtype: INT
    - Python dtype: int
- direction
    - Direction parameters specify the direction of the gradient. It can be 'horizontal' or'vertical', affecting the colour gradient layout in the output image.
    - Comfy dtype: COMBO['horizontal', 'vertical']
    - Python dtype: str
- tolerance
    - The tolerance parameter is used to adjust the mixing of the edges of the gradient. A higher margin allows a smoother transition between colours, but it may result in less obvious gradients.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The output of the WAS_Image_Generate_Gradient node is a seamless gradient image that can be used as texture. It is important because it provides the final visual result of the node operation.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Generate_Gradient:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        gradient_stops = '0:255,0,0\n25:255,255,255\n50:0,255,0\n75:0,0,255'
        return {'required': {'width': ('INT', {'default': 512, 'max': 4096, 'min': 64, 'step': 1}), 'height': ('INT', {'default': 512, 'max': 4096, 'min': 64, 'step': 1}), 'direction': (['horizontal', 'vertical'],), 'tolerance': ('INT', {'default': 0, 'max': 255, 'min': 0, 'step': 1}), 'gradient_stops': ('STRING', {'default': gradient_stops, 'multiline': True})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_gradient'
    CATEGORY = 'WAS Suite/Image/Generate'

    def image_gradient(self, gradient_stops, width=512, height=512, direction='horizontal', tolerance=0):
        import io
        WTools = WAS_Tools_Class()
        colors_dict = {}
        stops = io.StringIO(gradient_stops.strip().replace(' ', ''))
        for stop in stops:
            parts = stop.split(':')
            colors = parts[1].replace('\n', '').split(',')
            colors_dict[parts[0].replace('\n', '')] = colors
        image = WTools.gradient((width, height), direction, colors_dict, tolerance)
        return (pil2tensor(image),)
```