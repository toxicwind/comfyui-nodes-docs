# Documentation
- Class name: CR_FeatheredBorder
- Category: Comfyroll/Graphics/Layout
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_FeatheredBorder node is designed to add a feathered border to the image, providing a soft and visually attractive transition between the image and its surroundings. It allows custom borders to be thick and coloured, providing users with a high degree of control over the image's final appearance.

# Input types
## Required
- image
    - The image parameter is the core input of the node, which indicates the image that will be applied to the feather border. It is essential for the implementation of the node, as it determines the basis for adding the border effect.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- top_thickness
    - The top_tickness parameter specifies the border thickness that should be applied to the top edge of the image. It plays an important role in defining the overall size of the final image with a border.
    - Comfy dtype: INT
    - Python dtype: int
- bottom_thickness
    - Bottom_tickness parameters set the border thickness on the bottom edge of the image, which helps the overall border appearance and the ultimate size of the image.
    - Comfy dtype: INT
    - Python dtype: int
- left_thickness
    - The left_tickness parameter determines the thickness of the left border of the image and influences the final display of the image with the border.
    - Comfy dtype: INT
    - Python dtype: int
- right_thickness
    - The right_tickness parameter controls the thickness of the right border of the image and affects the total width of the image, including the border.
    - Comfy dtype: INT
    - Python dtype: int
- border_color
    - The border_color parameter is essential to define the border colour that will be applied to the image. It significantly affects the visual beauty of the final output.
    - Comfy dtype: COLOR
    - Python dtype: str
- feather_amount
    - The feed_amount parameter determines the softness of the border edge, creating a smooth transition between the image and the border. It is the key to professionality and fine appearance.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- border_color_hex
    - The border_color_hex parameter allows the use of custom hexadecimal colours for border use, providing additional flexibility for users to achieve a particular colour scheme.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- image
    - Image output parameters represent the final image of a feathered border. It is the main result of node execution and is the core of node purpose.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides URLs that point to the node document page, providing additional information and guidance to users on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_FeatheredBorder:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'top_thickness': ('INT', {'default': 0, 'min': 0, 'max': 4096}), 'bottom_thickness': ('INT', {'default': 0, 'min': 0, 'max': 4096}), 'left_thickness': ('INT', {'default': 0, 'min': 0, 'max': 4096}), 'right_thickness': ('INT', {'default': 0, 'min': 0, 'max': 4096}), 'border_color': (COLORS,), 'feather_amount': ('INT', {'default': 0, 'min': 0, 'max': 1024})}, 'optional': {'border_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('image', 'show_help')
    FUNCTION = 'make_border'
    CATEGORY = icons.get('Comfyroll/Graphics/Layout')

    def make_border(self, image, top_thickness, bottom_thickness, left_thickness, right_thickness, border_color, feather_amount, border_color_hex='#000000'):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Layout-Nodes#cr-feathered-border'
        images = []
        border_color = get_color_values(border_color, border_color_hex, color_mapping)
        for img in image:
            im = tensor2pil(img)
            RADIUS = feather_amount
            diam = 2 * RADIUS
            back = Image.new('RGB', (im.size[0] + diam, im.size[1] + diam), border_color)
            back.paste(im, (RADIUS, RADIUS))
            mask = Image.new('L', back.size, 0)
            draw = ImageDraw.Draw(mask)
            (x0, y0) = (0, 0)
            (x1, y1) = back.size
            for d in range(diam + RADIUS):
                (x1, y1) = (x1 - 1, y1 - 1)
                alpha = 255 if d < RADIUS else int(255 * (diam + RADIUS - d) / diam)
                draw.rectangle([x0, y0, x1, y1], outline=alpha)
                (x0, y0) = (x0 + 1, y0 + 1)
            blur = back.filter(ImageFilter.GaussianBlur(RADIUS / 2))
            back.paste(blur, mask=mask)
            if left_thickness > 0 or right_thickness > 0 or top_thickness > 0 or (bottom_thickness > 0):
                img = ImageOps.expand(back, (left_thickness, top_thickness, right_thickness, bottom_thickness), fill=border_color)
            else:
                img = back
            images.append(pil2tensor(img))
        images = torch.cat(images, dim=0)
        return (images, show_help)
```