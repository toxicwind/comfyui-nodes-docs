# Documentation
- Class name: GetImageSize_
- Category: ♾️Mixlab/Image
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node is designed to extract and select the size of the image to ensure that it meets the minimum width requirement. It processes the image to maintain its width ratio and returns the original size and adjusted size, which helps to understand image properties comprehensively in the workflow.

# Input types
## Required
- image
    - An image parameter is necessary because it is the main input for node operations. It is the source of the node's information about width and height and may be resized to meet the specified minimum width criteria.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
## Optional
- min_width
    - Min_width parameters are important because they set minimum width requirements for the image. If the width of the image is less than this value, the node will resize to meet this criterion to ensure a consistent starting point for further image processing.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- width
    - Width output represents the original width of the image entered. This is the basic information for understanding the size of the image and is essential for any subsequent image operation or analysis.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The high output corresponds to the original height of the image entered, providing an important background for the image size and width ratio, which is essential for maintaining image integrity in the processing process.
    - Comfy dtype: INT
    - Python dtype: int
- min_width
    - Min_width output instruction adjusts the minimum width of the image. It ensures that the image meets the size required for further processing or displaying and meets the workflow specifications.
    - Comfy dtype: INT
    - Python dtype: int
- min_height
    - Min_height output indicates that the image height is adjusted to meet the minimum width standard. This is important to understand how the image is adjusted and to ensure that it is correctly displayed or further processed.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class GetImageSize_:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',)}, 'optional': {'min_width': ('INT', {'default': 512, 'min': 1, 'max': 2048, 'step': 8, 'display': 'number'})}}
    RETURN_TYPES = ('INT', 'INT', 'INT', 'INT')
    RETURN_NAMES = ('width', 'height', 'min_width', 'min_height')
    FUNCTION = 'get_size'
    CATEGORY = '♾️Mixlab/Image'

    def get_size(self, image, min_width):
        (_, height, width, _) = image.shape
        if min_width > width:
            im = tensor2pil(image)
            im = resize_image(im, 'width', min_width, min_width, 'white')
            im = im.convert('RGB')
            (min_width, min_height) = im.size
        else:
            min_width = width
            min_height = height
        return (width, height, min_width, min_height)
```