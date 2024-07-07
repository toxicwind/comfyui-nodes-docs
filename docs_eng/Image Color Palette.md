# Documentation
- Class name: WAS_Image_Color_Palette
- Category: WAS Suite/Image/Analyze
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Color_Palette node is designed to analyse and process image data to generate colour palettes. It accepts an image as input and returns a converted image and a list of colour palettes extracted from the original image. This node is particularly suitable for applications where colour data are extracted and expressed from the image, such as design, image editing or any process that requires image colour data.

# Input types
## Required
- image
    - To generate an input image of the colour palette. The image will be processed by nodes to extract colour information and create visual expressions of the colour palette.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
## Optional
- colors
    - Generates the number of colours to be included in the palette. It provides a method of controlling the particle size of the colour formula derived from the image.
    - Comfy dtype: INT
    - Python dtype: int
- mode
    - Colour palette display mode. It determines the visual presentation of the palette and provides options such as a chart or back to back.
    - Comfy dtype: COMBO['Chart', 'back_to_back']
    - Python dtype: str

# Output types
- image
    - Converted images, in which colour palettes are embedded or changed in a visual manner according to the input image and the parameters provided.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- color_palettes
    - A list of colour palettes that are extracted from the input image. Each entry in the list represents a colour and is expressed as a hexadecimal code for a string.
    - Comfy dtype: LIST
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Color_Palette:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'colors': ('INT', {'default': 16, 'min': 8, 'max': 256, 'step': 1}), 'mode': (['Chart', 'back_to_back'],)}}
    RETURN_TYPES = ('IMAGE', 'LIST')
    RETURN_NAMES = ('image', 'color_palettes')
    FUNCTION = 'image_generate_palette'
    CATEGORY = 'WAS Suite/Image/Analyze'

    def image_generate_palette(self, image, colors=16, mode='chart'):
        WTools = WAS_Tools_Class()
        res_dir = os.path.join(WAS_SUITE_ROOT, 'res')
        font = os.path.join(res_dir, 'font.ttf')
        if not os.path.exists(font):
            font = None
        elif mode == 'Chart':
            cstr(f'Found font at `{font}`').msg.print()
        if len(image) > 1:
            palette_strings = []
            palette_images = []
            for img in image:
                img = tensor2pil(img)
                (palette_image, palette) = WTools.generate_palette(img, colors, 128, 10, font, 15, mode.lower())
                palette_images.append(pil2tensor(palette_image))
                palette_strings.append(palette)
            palette_images = torch.cat(palette_images, dim=0)
            return (palette_images, palette_strings)
        else:
            image = tensor2pil(image)
            (palette_image, palette) = WTools.generate_palette(image, colors, 128, 10, font, 15, mode.lower())
            return (pil2tensor(palette_image), [palette])
```