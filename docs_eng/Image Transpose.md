# Documentation
- Class name: WAS_Image_Transpose
- Category: WAS Suite/Image/Transform
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Image_Transpose nodes are designed to perform image operation tasks, especially to convert images by rotating and resizing them. It allows a single image to be added to another image, specifying the width and height of the output, the position of the stacking and the extent of the rotation. In addition, it provides a plume to soften the edges of the stacking layer in order to achieve a more natural mix. This node is essential for creating composite images with precise control of the position and appearance of the elements.

# Input types
## Required
- image
    - As the base image that will be applied in stacking. It will be a canvas created as a composite image. Select this image to significantly affect the final appearance of the output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image_overlay
    - The image that is superimposed on the base image. It is operated according to the specified parameters so that it is seamlessly integrated with the base image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- width
    - The expected width of the output image. It determines the base and the zoom of the image to fit the size specified.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The expected height of the output image. Together with width, it determines the size of the final synthetic image.
    - Comfy dtype: INT
    - Python dtype: int
- X
    - Adds the X coordinates of the position where the image is placed on the base image.
    - Comfy dtype: INT
    - Python dtype: int
- Y
    - Adds the Y coordinates of the position where the image is placed on the base image.
    - Comfy dtype: INT
    - Python dtype: int
- rotation
    - The number of rotations that you want to apply before superimposed images are placed on the base image.
    - Comfy dtype: INT
    - Python dtype: int
- feathering
    - The plume applied to the edge of the superimposed image to blend more smoothly with the underlying image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output_image
    - Based on the specified parameters, the final synthetic image is converted from the base image and the superimposed image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Transpose:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'image_overlay': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': -48000, 'max': 48000, 'step': 1}), 'height': ('INT', {'default': 512, 'min': -48000, 'max': 48000, 'step': 1}), 'X': ('INT', {'default': 0, 'min': -48000, 'max': 48000, 'step': 1}), 'Y': ('INT', {'default': 0, 'min': -48000, 'max': 48000, 'step': 1}), 'rotation': ('INT', {'default': 0, 'min': -360, 'max': 360, 'step': 1}), 'feathering': ('INT', {'default': 0, 'min': 0, 'max': 4096, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_transpose'
    CATEGORY = 'WAS Suite/Image/Transform'

    def image_transpose(self, image: torch.Tensor, image_overlay: torch.Tensor, width: int, height: int, X: int, Y: int, rotation: int, feathering: int=0):
        return (pil2tensor(self.apply_transpose_image(tensor2pil(image), tensor2pil(image_overlay), (width, height), (X, Y), rotation, feathering)),)

    def apply_transpose_image(self, image_bg, image_element, size, loc, rotate=0, feathering=0):
        image_element = image_element.rotate(rotate, expand=True)
        image_element = image_element.resize(size)
        if feathering > 0:
            mask = Image.new('L', image_element.size, 255)
            draw = ImageDraw.Draw(mask)
            for i in range(feathering):
                alpha_value = int(255 * (i + 1) / feathering)
                draw.rectangle((i, i, image_element.size[0] - i, image_element.size[1] - i), fill=alpha_value)
            alpha_mask = Image.merge('RGBA', (mask, mask, mask, mask))
            image_element = Image.composite(image_element, Image.new('RGBA', image_element.size, (0, 0, 0, 0)), alpha_mask)
        new_image = Image.new('RGBA', image_bg.size, (0, 0, 0, 0))
        new_image.paste(image_element, loc)
        image_bg = image_bg.convert('RGBA')
        image_bg.paste(new_image, (0, 0), new_image)
        return image_bg
```