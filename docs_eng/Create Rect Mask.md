# Documentation
- Class name: CreateRectMask
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The CreativeRectmask node is designed to generate rectangular maskes based on the parameters specified. It calculates the coordinates of the corner of the mask, taking into account the measurement mode (percentages or pixels), the origin of the rectangular and the size provided. The node is flexible, allowing custom mask to be defined relative to the location and size of the application image. It also provides an option for copying image sizes to allow dynamic mask creation.

# Input types
## Required
- mode
    - The mode parameter determines the unit of measure of the mask size. It may be 'percent' for the coordinates based on percentages, or 'pixels' for absolute pixels.
    - Comfy dtype: str
    - Python dtype: str
- origin
    - The origin parameter determines the reference point for calculating the position of the mask. It can be one of 'topleft', 'bottomleft', 'topleft' or 'bottomright'.
    - Comfy dtype: str
    - Python dtype: str
- x
    - x The parameter specifies the horizontal position of the starting point of the mask. It is used with the mode and the original to determine the location of the mask.
    - Comfy dtype: float
    - Python dtype: float
- y
    - y Arguments specify the vertical position of the starting point of the mask. It works with x parameters and other settings to create the coordinates of the mask.
    - Comfy dtype: float
    - Python dtype: float
- width
    - Width parameters set the width of the mask. This is a critical dimension, defining the shape and coverage of the mask with altitude.
    - Comfy dtype: float
    - Python dtype: float
- height
    - The header parameter sets the vertical range of the mask. It is critical in determining the overall size of the mask and the area it contains.
    - Comfy dtype: float
    - Python dtype: float
- image_width
    - The image_width parameter defines the width of the image that will apply the mask. If the pattern is set to 'percent', it is important to ensure that the mask size is correctly scaled.
    - Comfy dtype: int
    - Python dtype: int
- image_height
    - The image_height parameter defines the height of the image. It is similar to the image_width and plays a similar role in scaling the size of the mask according to the size of the image.
    - Comfy dtype: int
    - Python dtype: int
## Optional
- copy_image_size
    - The optional copy_image_size parameter allows a mask to use the size of the image provided. This is very useful for creating a mask based on the dynamic size of the image applied.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor

# Output types
- mask
    - Output mask is a binary image that indicates a rectangular area defined by input parameters. It is a key component of various image processing tasks (e.g. object split or mask).
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class CreateRectMask:
    """
    Creates a rectangle mask. If copy_image_size is provided, the image_width and image_height parameters are ignored and the size of the given images will be used instead.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mode': (['percent', 'pixels'],), 'origin': (['topleft', 'bottomleft', 'topright', 'bottomright'],), 'x': ('FLOAT', {'default': 0, 'min': 0, 'max': VERY_BIG_SIZE, 'step': 1}), 'y': ('FLOAT', {'default': 0, 'min': 0, 'max': VERY_BIG_SIZE, 'step': 1}), 'width': ('FLOAT', {'default': 50, 'min': 0, 'max': VERY_BIG_SIZE, 'step': 1}), 'height': ('FLOAT', {'default': 50, 'min': 0, 'max': VERY_BIG_SIZE, 'step': 1}), 'image_width': ('INT', {'default': 512, 'min': 64, 'max': VERY_BIG_SIZE, 'step': 64}), 'image_height': ('INT', {'default': 512, 'min': 64, 'max': VERY_BIG_SIZE, 'step': 64})}, 'optional': {'copy_image_size': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'create_mask'
    CATEGORY = 'Masquerade Nodes'

    def create_mask(self, mode, origin, x, y, width, height, image_width, image_height, copy_image_size=None):
        min_x = x
        min_y = y
        max_x = min_x + width
        max_y = min_y + height
        if copy_image_size is not None:
            size = copy_image_size.size()
            image_width = size[2]
            image_height = size[1]
        if mode == 'percent':
            min_x = min_x / 100.0 * image_width
            max_x = max_x / 100.0 * image_width
            min_y = min_y / 100.0 * image_height
            max_y = max_y / 100.0 * image_height
        if origin == 'bottomleft' or origin == 'bottomright':
            (min_y, max_y) = (image_height - max_y, image_height - min_y)
        if origin == 'topright' or origin == 'bottomright':
            (min_x, max_x) = (image_width - max_x, image_width - min_x)
        mask = torch.zeros((image_height, image_width))
        mask[int(min_y):int(max_y) + 1, int(min_x):int(max_x) + 1] = 1
        return (mask.unsqueeze(0),)
```