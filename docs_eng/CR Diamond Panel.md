# Documentation
- Class name: CR_DiamondPanel
- Category: Graphics/Layout
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_DiamondPanel is a node used to create visual attractions from images. It enhances layout by providing graphic design that allows seamless integration into various graphic applications. This node focuses on the aesthetic display of images and allows free creation in panel formation and design.

# Input types
## Required
- image
    - The image parameter is the core input of the CR_DiamondPanel node used to generate the diamond panel. It is vital because it determines the visual content of the output panel.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- pattern
    - The pattern parameter determines the type of design to be applied to the panel. It is important because it allows users to select criteria or diamond-shaped patterns that affect the final appearance of the layout.
    - Comfy dtype: COMBO['none', 'diamond']
    - Python dtype: str
## Optional
- drop_percentage
    - The drop_percentage parameter adjusts the spacing between the diamond-shaped panels. It plays a vital role in the overall picture by controlling the density and the way the panels are arranged in the layout.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- image
    - The image output of the CR_DiamondPanel node represents the final diamond-shaped layout. It is a combination of the image and the selected pattern that can be further used or displayed.
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
class CR_DiamondPanel:

    @classmethod
    def INPUT_TYPES(s):
        patterns = ['none', 'diamond']
        return {'required': {'image': ('IMAGE',), 'pattern': (patterns,)}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('image', 'show_help')
    FUNCTION = 'make_panel'
    CATEGORY = icons.get('Comfyroll/Graphics/Layout')

    def make_panel(self, image, pattern, drop_percentage=0.5):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Layout-Nodes#cr-diamond-panel'
        if pattern == 'none':
            return (image, show_help)
        pil_img = tensor2pil(image)
        pil_img = pil_img.convert('RGBA')
        (x, y) = pil_img.size
        aspect_ratio = x / y
        d = int(drop_percentage * 100)
        panel_image = Image.new('RGBA', (x * 2, y * 2))
        if pattern == 'diamond':
            diamond_size = min(x, y)
            diamond_width = min(x, y * aspect_ratio)
            diamond_height = min(y, x / aspect_ratio)
            diamond_mask = Image.new('L', (x, y), 0)
            draw = ImageDraw.Draw(diamond_mask)
            draw.polygon([(x // 2, 0), (x, y // 2), (x // 2, y), (0, y // 2)], fill=255)
            diamond_image = pil_img.copy()
            diamond_image.putalpha(diamond_mask)
            panel_image.paste(diamond_image, (-x // 2, (d - 100) * y // 100), diamond_image)
            panel_image.paste(diamond_image, (-x // 2, d * y // 100), diamond_image)
            panel_image.paste(diamond_image, (-x // 2, y + d * y // 100), diamond_image)
            panel_image.paste(diamond_image, (0, 0), diamond_image)
            panel_image.paste(diamond_image, (0, y), diamond_image)
            panel_image.paste(diamond_image, (x // 2, (d - 100) * y // 100), diamond_image)
            panel_image.paste(diamond_image, (x // 2, d * y // 100), diamond_image)
            panel_image.paste(diamond_image, (x // 2, y + d * y // 100), diamond_image)
            panel_image.paste(diamond_image, (x, 0), diamond_image)
            panel_image.paste(diamond_image, (x, y), diamond_image)
            panel_image.paste(diamond_image, (3 * x // 2, (d - 100) * y // 100), diamond_image)
            panel_image.paste(diamond_image, (3 * x // 2, d * y // 100), diamond_image)
            panel_image.paste(diamond_image, (3 * x // 2, y + d * y // 100), diamond_image)
        image_out = pil2tensor(panel_image.convert('RGB'))
        return (image_out, show_help)
```