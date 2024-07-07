# Documentation
- Class name: CR_VignetteFilter
- Category: Comfyroll/Graphics/Filter
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_VignetteFilter is a node for the application of visual effects known as dizziness to images. This effect gradually dims the corner of the image, creating a soft focus transition between the center area and the edge. It increases visual depth and attracts attention to the centre of images, usually in photography and cinema.

# Input types
## Required
- image
    - Enter the image using the dizziness effect. This is the main data that the node will process, and the quality of the final output depends to a large extent on the properties of the input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- vignette_shape
    - Determines the shape of the faint shadow to be applied to the image. The choice of shape can significantly influence the aesthetic appeal of the final image and the emotional response to it.
    - Comfy dtype: COMBO['circle', 'oval', 'square', 'diamond']
    - Python dtype: str
- feather_amount
    - Controls the softness of the edge of the shadow. A higher plume makes the transition from the dark corner to the image centre more gradual, and a lower amount makes the transition even more sudden.
    - Comfy dtype: INT
    - Python dtype: int
- x_offset
    - Allows horizontally to adjust the center of the faint shadow. This changes the focus area of the image and creates subtle changes in the map.
    - Comfy dtype: INT
    - Python dtype: int
- y_offset
    - Allows vertically to adjust the center of the shadow. Similar to x_offset, it can be used to fine-tune the visual focus in the image.
    - Comfy dtype: INT
    - Python dtype: int
- zoom
    - This parameter adjusts the size of the dizziness effect. Higher zoom values increase the size of the dizziness and make it more prominent, while lower values reduce its size.
    - Comfy dtype: FLOAT
    - Python dtype: float
- reverse
    - If set as 'yes', the inverted dizziness effect. It's not darkening the edges, it's darkening the image center, creating contrasting visual styles.
    - Comfy dtype: COMBO['no', 'yes']
    - Python dtype: str

# Output types
- IMAGE
    - Applyes the result image of the dizziness effect. This is the main output, reflecting the creative adjustments made through node parameters.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- MASK
    - A alpha mask for dizziness transparency. It can be used for further image processing or as a selection tool in later production.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Provides document links to obtain further guidance on the use of nodes. This is very useful for users seeking more information on node functions and options.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_VignetteFilter:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'vignette_shape': (['circle', 'oval', 'square', 'diamond'],), 'feather_amount': ('INT', {'default': 100, 'min': 0, 'max': 1024}), 'x_offset': ('INT', {'default': 0, 'min': -2048, 'max': 2048}), 'y_offset': ('INT', {'default': 0, 'min': -2048, 'max': 2048}), 'zoom': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.1}), 'reverse': (['no', 'yes'],)}}
    RETURN_TYPES = ('IMAGE', 'MASK', 'STRING')
    RETURN_NAMES = ('IMAGE', 'MASK', 'show_help')
    FUNCTION = 'make_vignette'
    CATEGORY = icons.get('Comfyroll/Graphics/Filter')

    def make_vignette(self, image, feather_amount, reverse, vignette_shape='circle', x_offset=0, y_offset=0, zoom=1.0):
        images = []
        masks = []
        vignette_color = 'black'
        for img in image:
            im = tensor2pil(img)
            RADIUS = feather_amount
            alpha_mask = Image.new('L', im.size, 255)
            draw = ImageDraw.Draw(alpha_mask)
            center_x = im.size[0] // 2 + x_offset
            center_y = im.size[1] // 2 + y_offset
            radius = min(center_x, center_y) * zoom
            size_x = (im.size[0] - RADIUS) * zoom
            size_y = (im.size[1] - RADIUS) * zoom
            if vignette_shape == 'circle':
                if reverse == 'no':
                    draw.ellipse([(center_x - radius, center_y - radius), (center_x + radius, center_y + radius)], fill=0)
                elif reverse == 'yes':
                    draw.rectangle([(0, 0), im.size], fill=0)
                    draw.ellipse([(center_x - radius, center_y - radius), (center_x + radius, center_y + radius)], fill=255)
                else:
                    raise ValueError("Invalid value for reverse. Use 'yes' or 'no'.")
            elif vignette_shape == 'oval':
                if reverse == 'no':
                    draw.ellipse([(center_x - size_x / 2, center_y - size_y / 2), (center_x + size_x / 2, center_y + size_y / 2)], fill=0)
                elif reverse == 'yes':
                    draw.rectangle([(0, 0), im.size], fill=0)
                    draw.ellipse([(center_x - size_x / 2, center_y - size_y / 2), (center_x + size_x / 2, center_y + size_y / 2)], fill=255)
            elif vignette_shape == 'diamond':
                if reverse == 'no':
                    size = min(im.size[0] - x_offset, im.size[1] - y_offset) * zoom
                    draw.polygon([(center_x, center_y - size / 2), (center_x + size / 2, center_y), (center_x, center_y + size / 2), (center_x - size / 2, center_y)], fill=0)
                elif reverse == 'yes':
                    size = min(im.size[0] - x_offset, im.size[1] - y_offset) * zoom
                    draw.rectangle([(0, 0), im.size], fill=0)
                    draw.polygon([(center_x, center_y - size / 2), (center_x + size / 2, center_y), (center_x, center_y + size / 2), (center_x - size / 2, center_y)], fill=255)
            elif vignette_shape == 'square':
                if reverse == 'no':
                    size = min(im.size[0] - x_offset, im.size[1] - y_offset) * zoom
                    draw.rectangle([(center_x - size / 2, center_y - size / 2), (center_x + size / 2, center_y + size / 2)], fill=0)
                elif reverse == 'yes':
                    size = min(im.size[0] - x_offset, im.size[1] - y_offset) * zoom
                    draw.rectangle([(0, 0), im.size], fill=0)
                    draw.rectangle([(center_x - size / 2, center_y - size / 2), (center_x + size / 2, center_y + size / 2)], fill=255)
                else:
                    raise ValueError("Invalid value for reverse. Use 'yes' or 'no'.")
            else:
                raise ValueError("Invalid vignette_shape. Use 'circle', 'oval', or 'square'.")
            alpha_mask = alpha_mask.filter(ImageFilter.GaussianBlur(RADIUS))
            masks.append(pil2tensor(alpha_mask).unsqueeze(0))
            vignette_img = Image.new('RGBA', im.size, vignette_color)
            vignette_img.putalpha(alpha_mask)
            result_img = Image.alpha_composite(im.convert('RGBA'), vignette_img)
            images.append(pil2tensor(result_img.convert('RGB')))
        images = torch.cat(images, dim=0)
        masks = torch.cat(masks, dim=0)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Layout-Nodes#cr-vignette-filter'
        return (images, masks, show_help)
```