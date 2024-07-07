# Documentation
- Class name: WAS_Image_Rotate_Hue
- Category: WAS Suite/Image/Adjustment
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Rotate_Hue node is designed to adjust the colour of the image and provides a way to change the overall colour of the image without changing the brightness or saturation of the image. It is particularly suitable for creating a variant of the image for visual effects or colour correction purposes.

# Input types
## Required
- image
    - The image parameter is essential for the operation of the node because it is an input that will be colour-adjusted. It is the primary data that the node will process to achieve the required colour conversion.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
## Optional
- hue_shift
    - Hue_ship parameters allow fine-tuning colour rotations in the image. It is a floating number that affects the degree of colour deviation, and thus the ultimate visual effect of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- rotated_image
    - The model_image output represents the result of a colour-phase rotation applied to the input image. It is a colour-adjusted conversion image that can be further processed or displayed.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Rotate_Hue:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'hue_shift': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'rotate_hue'
    CATEGORY = 'WAS Suite/Image/Adjustment'

    def rotate_hue(self, image, hue_shift=0.0):
        if hue_shift > 1.0 or hue_shift < 0.0:
            cstr(f'The hue_shift `{cstr.color.LIGHTYELLOW}{hue_shift}{cstr.color.END}` is out of range. Valid range is {cstr.color.BOLD}0.0 - 1.0{cstr.color.END}').error.print()
            hue_shift = 0.0
        shifted_hue = pil2tensor(self.hue_rotation(image, hue_shift))
        return (shifted_hue,)

    def hue_rotation(self, image, hue_shift=0.0):
        import colorsys
        if hue_shift > 1.0 or hue_shift < 0.0:
            print(f"The hue_shift '{hue_shift}' is out of range. Valid range is 0.0 - 1.0")
            hue_shift = 0.0
        pil_image = tensor2pil(image)
        (width, height) = pil_image.size
        rotated_image = Image.new('RGB', (width, height))
        for x in range(width):
            for y in range(height):
                (r, g, b) = pil_image.getpixel((x, y))
                (h, l, s) = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
                h = (h + hue_shift) % 1.0
                (r, g, b) = colorsys.hls_to_rgb(h, l, s)
                (r, g, b) = (int(r * 255), int(g * 255), int(b * 255))
                rotated_image.putpixel((x, y), (r, g, b))
        return rotated_image
```