# Documentation
- Class name: Pixelize
- Category: postprocessing/Effects
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

Pixelize nodes are designed to apply pixelization to input images and convert them into styled, massive expressions. They do so by assigning colour values in grids with an average pixel size definition, thereby reducing the resolution of the image to more abstract forms. This node is particularly suitable for the creation of retrogent or artistic appearances, as well as for image processing that protects privacy.

# Input types
## Required
- image
    - The image parameter is the input to be processed by the Pixelize node. It is vital because it determines the visual content to be treated with pixels. The operation of the node is directly influenced by image size and pixel data, which is essential for the pixelization effect.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- pixel_size
    - The pixel_size parameter determines the particle size of the pixel effect. It specifies the size of each pixel block in the output image. The larger pixel_size value leads to more obvious pixelization, while the smaller value retains more detail. This parameter plays a key role in controlling the stylized results processed by the nodes.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- pixelized_image
    - The pixelized_image output represents the end result of the pixel processing process. It is an image of each pixel block being averaged to create a styled, pixel-like look. This output is important because it reflects the main function of the node and the creative intent behind the pixelization effect.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class Pixelize:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'pixel_size': ('INT', {'default': 8, 'min': 2, 'max': 128, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'apply_pixelize'
    CATEGORY = 'postprocessing/Effects'

    def apply_pixelize(self, image: torch.Tensor, pixel_size: int):
        pixelized_image = self.pixelize_image(image, pixel_size)
        pixelized_image = torch.clamp(pixelized_image, 0, 1)
        return (pixelized_image,)

    def pixelize_image(self, image: torch.Tensor, pixel_size: int):
        (batch_size, height, width, channels) = image.shape
        new_height = height // pixel_size
        new_width = width // pixel_size
        image = image.permute(0, 3, 1, 2)
        image = F.avg_pool2d(image, kernel_size=pixel_size, stride=pixel_size)
        image = F.interpolate(image, size=(height, width), mode='nearest')
        image = image.permute(0, 2, 3, 1)
        return image
```