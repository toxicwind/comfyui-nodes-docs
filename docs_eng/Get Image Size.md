# Documentation
- Class name: GetImageSize
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The GetImageSize node is designed to extract the size of the image and to provide width and height as an output. It plays a key role in the image-processing task, in which the spatial dimensions of the image are essential for further operation (e.g. resizeing, cropping or data analysis).

# Input types
## Required
- image
    - The image parameter is essential for the node because it is the source of the dimensions to be determined. The node relies on this input to calculate and return the width and height of the image, which can significantly influence subsequent image operations and analysis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- width
    - The width output provides the horizontal dimensions of the post-processed image. This is a key information that can be used for a variety of purposes, such as determining horizontal and horizontal comparisons or compatibility checks with other image processing systems.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - High output represents the vertical dimensions of the image. This is a basic parameter for tasks that require an understanding of the image's spatial structure, such as resizing to suit a given frame or display purpose.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class GetImageSize:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',)}}
    RETURN_TYPES = ('INT', 'INT')
    RETURN_NAMES = ('width', 'height')
    FUNCTION = 'get_size'
    CATEGORY = 'Masquerade Nodes'

    def get_size(self, image):
        image_size = image.size()
        image_width = int(image_size[2])
        image_height = int(image_size[1])
        return (image_width, image_height)
```