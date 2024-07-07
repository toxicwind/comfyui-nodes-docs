# Documentation
- Class name: CR_HalfDropPanel
- Category: Comfyroll/Graphics/Layout
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_HalfDropPanel is a node used to operate and convert images according to the specified mode, creating the fate effect of a self-defined percentage value. It enhances the visual presentation of images by applying half-draw, one-quarter or customd drop patterns, providing users with a flexible way to adjust their image layout and aesthetics for various design purposes.

# Input types
## Required
- image
    - The image parameter is necessary because it is the basic input for node processing. It determines the source material for the effect of the drop panel and is essential for node execution.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- pattern
    - Model parameters determine the type of destination effect to be applied to the image. It is essential to define the particular visual transformation that the node will perform.
    - Comfy dtype: COMBO['none', 'half drop', 'quarter drop', 'custom drop %']
    - Python dtype: str
## Optional
- drop_percentage
    - The drop_percentage parameter is optional, but is very important when choosing a custom-defined drop mode. It allows users to control the range of the drop effect and provides a certain degree of customization for image conversion.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- image
    - The converted image output is the main result of the node operation. It represents a visual output that applies the drop pattern to further use or display.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a link to the document for further help. This is a useful resource for users seeking to use nodes or solve malfunctions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_HalfDropPanel:

    @classmethod
    def INPUT_TYPES(s):
        patterns = ['none', 'half drop', 'quarter drop', 'custom drop %']
        return {'required': {'image': ('IMAGE',), 'pattern': (patterns,)}, 'optional': {'drop_percentage': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('image', 'show_help')
    FUNCTION = 'make_panel'
    CATEGORY = icons.get('Comfyroll/Graphics/Layout')

    def make_panel(self, image, pattern, drop_percentage=0.5):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Layout-Nodes#cr-half-drop-panel'
        if pattern == 'none':
            return (image, show_help)
        pil_img = tensor2pil(image)
        pil_img = pil_img.convert('RGBA')
        (x, y) = pil_img.size
        aspect_ratio = x / y
        d = int(drop_percentage * 100)
        panel_image = Image.new('RGBA', (x * 2, y * 2))
        if pattern == 'half drop':
            panel_image.paste(pil_img, (0, 0))
            panel_image.paste(pil_img, (0, y))
            panel_image.paste(pil_img, (x, -y // 2))
            panel_image.paste(pil_img, (x, y // 2))
            panel_image.paste(pil_img, (x, 3 * y // 2))
        elif pattern == 'quarter drop':
            panel_image.paste(pil_img, (0, 0))
            panel_image.paste(pil_img, (0, y))
            panel_image.paste(pil_img, (x, -3 * y // 4))
            panel_image.paste(pil_img, (x, y // 4))
            panel_image.paste(pil_img, (x, 5 * y // 4))
        elif pattern == 'custom drop %':
            panel_image.paste(pil_img, (0, 0))
            panel_image.paste(pil_img, (0, y))
            panel_image.paste(pil_img, (x, (d - 100) * y // 100))
            panel_image.paste(pil_img, (x, d * y // 100))
            panel_image.paste(pil_img, (x, y + d * y // 100))
        image_out = pil2tensor(panel_image.convert('RGB'))
        return (image_out, show_help)
```