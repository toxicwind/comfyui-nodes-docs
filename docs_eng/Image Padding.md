# Documentation
- Class name: WAS_Image_Padding
- Category: WAS Suite/Image/Transform
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Padding node is designed to enhance images by adding fill to the edge of the image, which is very useful for a variety of image processing tasks (e.g. data enhancement or the preparation of images for machine learning models). It provides an advanced feature that allows the addition of fills and the optional application of plume effects, smoothly mixing the filling edges with the original images.

# Input types
## Required
- image
    - The image parameter is the input image that the node will process. It plays a central role in the operation of the node, as the entire filling and feathering process is applied to the image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- feathering
    - The plume parameter determines the extent of the plume effect applied to the edge of the image fill. This is an optional parameter that enhances the visual smoothness of the fill.
    - Comfy dtype: INT
    - Python dtype: int
- feather_second_pass
    - Feed_second_pass parameters control whether to apply a second plume to the image. This can add an additional smoothness layer to the edge of the fill.
    - Comfy dtype: COMBO[true, false]
    - Python dtype: bool
- left_padding
    - The left_pading parameter specifies the fill to be added to the left side of the image. It is an important parameter because it directly affects the final size of the image.
    - Comfy dtype: INT
    - Python dtype: int
- right_padding
    - The right_pading parameter specifies the fill to be added to the right side of the image. It is essential to control the total width of the filled image.
    - Comfy dtype: INT
    - Python dtype: int
- top_padding
    - The top_padding parameter determines the fill to be added to the top of the image. It is the key parameter for adjusting the vertical size of the image.
    - Comfy dtype: INT
    - Python dtype: int
- bottom_padding
    - Bottom_padding parameters are set to add to the fill at the bottom of the image. It is essential to modify the total height of the image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- padded_image
    - The Padded_image parameter is the output of the node, i.e. the original image specified for filling. It represents the end result of the image filling process.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- padding_mask
    - The padding_mask parameter is an additional output that provides a visual indication of the filling that should be applied to the image. It can be used for further processing or visual examination.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Padding:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'feathering': ('INT', {'default': 120, 'min': 0, 'max': 2048, 'step': 1}), 'feather_second_pass': (['true', 'false'],), 'left_padding': ('INT', {'default': 512, 'min': 8, 'max': 48000, 'step': 1}), 'right_padding': ('INT', {'default': 512, 'min': 8, 'max': 48000, 'step': 1}), 'top_padding': ('INT', {'default': 512, 'min': 8, 'max': 48000, 'step': 1}), 'bottom_padding': ('INT', {'default': 512, 'min': 8, 'max': 48000, 'step': 1})}}
    RETURN_TYPES = ('IMAGE', 'IMAGE')
    FUNCTION = 'image_padding'
    CATEGORY = 'WAS Suite/Image/Transform'

    def image_padding(self, image, feathering, left_padding, right_padding, top_padding, bottom_padding, feather_second_pass=True):
        padding = self.apply_image_padding(tensor2pil(image), left_padding, right_padding, top_padding, bottom_padding, feathering, second_pass=True)
        return (pil2tensor(padding[0]), pil2tensor(padding[1]))

    def apply_image_padding(self, image, left_pad=100, right_pad=100, top_pad=100, bottom_pad=100, feather_radius=50, second_pass=True):
        mask = Image.new('L', image.size, 255)
        draw = ImageDraw.Draw(mask)
        draw.rectangle((0, 0, feather_radius * 2, image.height), fill=0)
        draw.rectangle((image.width - feather_radius * 2, 0, image.width, image.height), fill=0)
        draw.rectangle((0, 0, image.width, feather_radius * 2), fill=0)
        draw.rectangle((0, image.height - feather_radius * 2, image.width, image.height), fill=0)
        mask = mask.filter(ImageFilter.GaussianBlur(radius=feather_radius))
        if second_pass:
            mask2 = Image.new('L', image.size, 255)
            draw2 = ImageDraw.Draw(mask2)
            feather_radius2 = int(feather_radius / 4)
            draw2.rectangle((0, 0, feather_radius2 * 2, image.height), fill=0)
            draw2.rectangle((image.width - feather_radius2 * 2, 0, image.width, image.height), fill=0)
            draw2.rectangle((0, 0, image.width, feather_radius2 * 2), fill=0)
            draw2.rectangle((0, image.height - feather_radius2 * 2, image.width, image.height), fill=0)
            mask2 = mask2.filter(ImageFilter.GaussianBlur(radius=feather_radius2))
            feathered_im = Image.new('RGBA', image.size, (0, 0, 0, 0))
            feathered_im.paste(image, (0, 0), mask)
            feathered_im.paste(image, (0, 0), mask)
            feathered_im.paste(image, (0, 0), mask2)
            feathered_im.paste(image, (0, 0), mask2)
        else:
            feathered_im = Image.new('RGBA', image.size, (0, 0, 0, 0))
            feathered_im.paste(image, (0, 0), mask)
        new_size = (feathered_im.width + left_pad + right_pad, feathered_im.height + top_pad + bottom_pad)
        new_im = Image.new('RGBA', new_size, (0, 0, 0, 0))
        new_im.paste(feathered_im, (left_pad, top_pad))
        padding_mask = Image.new('L', new_size, 0)
        gradient = [int(255 * (1 - p[3] / 255)) if p[3] != 0 else 255 for p in new_im.getdata()]
        padding_mask.putdata(gradient)
        return (new_im, padding_mask.convert('RGB'))
```