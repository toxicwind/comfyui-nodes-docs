# Documentation
- Class name: imageInsetCrop
- Category: EasyUse/Image
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node facilitates the accurate cropping of the image by allowing the user to define the area in pixel values or percentage size of the image. It enhances the image processing workflow to ensure that the cropped image meets specific requirements by operating the image without complex calculations.

# Input types
## Required
- image
    - The image parameter is essential because it is the source from which the crop operation is to be performed. It directly influences the output of the node and determines the visual content and dimensions of the result image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- measurement
    - The measurement parameters determine whether the cut value is entered as an absolute pixel or as a relative percentage. This significantly affects the way the area is calculated, and thus the final size of the crop image.
    - Comfy dtype: COMBO['Pixels', 'Percentage']
    - Python dtype: str
- left
    - The left-hand margin parameter specifies the distance from the left edge of the image to the crop area. It plays a key role in determining the horizontal position of the area in the image.
    - Comfy dtype: INT
    - Python dtype: int
- right
    - The right distance parameter defines the distance from the right edge of the image to the end of the crop area. It works with the left distance parameter to determine the total width of the crop.
    - Comfy dtype: INT
    - Python dtype: int
- top
    - The upper margin parameter sets the distance from the top of the image to the crop area. It is essential to determine the vertical position of the area in the image.
    - Comfy dtype: INT
    - Python dtype: int
- bottom
    - The lower margin parameter specifies the distance from the bottom of the image to the end of the crop area. Together with the upper margin parameter, it defines the height of the crop.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The output image is the result of the crop operation. It represents the remainder of the original image after the application of the specified inner margin and captures the required visual content.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class imageInsetCrop:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'measurement': (['Pixels', 'Percentage'],), 'left': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'right': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'top': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'bottom': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'crop'
    CATEGORY = 'EasyUse/Image'

    def crop(self, measurement, left, right, top, bottom, image=None):
        """Does the crop."""
        (_, height, width, _) = image.shape
        if measurement == 'Percentage':
            left = int(width - width * (100 - left) / 100)
            right = int(width - width * (100 - right) / 100)
            top = int(height - height * (100 - top) / 100)
            bottom = int(height - height * (100 - bottom) / 100)
        left = left // 8 * 8
        right = right // 8 * 8
        top = top // 8 * 8
        bottom = bottom // 8 * 8
        if left == 0 and right == 0 and (bottom == 0) and (top == 0):
            return (image,)
        (inset_left, inset_right, inset_top, inset_bottom) = get_new_bounds(width, height, left, right, top, bottom)
        if inset_top > inset_bottom:
            raise ValueError(f'Invalid cropping dimensions top ({inset_top}) exceeds bottom ({inset_bottom})')
        if inset_left > inset_right:
            raise ValueError(f'Invalid cropping dimensions left ({inset_left}) exceeds right ({inset_right})')
        log_node_info('Image Inset Crop', f'Cropping image {width}x{height} width inset by {inset_left},{inset_right}, ' + f'and height inset by {inset_top}, {inset_bottom}')
        image = image[:, inset_top:inset_bottom, inset_left:inset_right, :]
        return (image,)
```