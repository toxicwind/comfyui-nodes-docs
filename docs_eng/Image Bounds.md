# Documentation
- Class name: WAS_Image_Bounds
- Category: WAS Suite/Image/Bound
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Bounds'method is designed to calculate the boundaries of images and to provide basic spatial information for various image processing tasks. It ensures that images are properly formatted before they are determined, so that follow-up actions can be performed accurately.

# Input types
## Required
- image
    - The 'image'parameter is essential to the operation of the node because it is the node that will be processed to determine the data source of the boundary. It is the basis for the node function, without which the node cannot perform its intended task.
    - Comfy dtype: IMAGE
    - Python dtype: Union[torch.Tensor, PIL.Image.Image]

# Output types
- image_bounds
    - The 'image_bounds' output provides the spatial coordinates that define the boundaries of the input image. This information is essential for tasks that require space perception, such as cropping, resizing or locating elements within the image.
    - Comfy dtype: COMBO[Tuple[int, int, int, int]]
    - Python dtype: List[Tuple[int, int, int, int]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Bounds:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {'required': {'image': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE_BOUNDS',)
    FUNCTION = 'image_bounds'
    CATEGORY = 'WAS Suite/Image/Bound'

    def image_bounds(self, image):
        image = image.unsqueeze(0) if image.dim() == 3 else image
        return ([(0, img.shape[0] - 1, 0, img.shape[1] - 1) for img in image],)
```