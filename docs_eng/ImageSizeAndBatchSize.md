# Documentation
- Class name: ImageSizeAndBatchSize
- Category: Animate Diff/Utils
- Output node: False
- Repo Ref: https://github.com/ArtVentureX/comfyui-animatediff.git

Such nodes are intended to extract and return key image properties, such as size and bulk dimensions, for further processing and analysis within the system.

# Input types
## Required
- image
    - The image parameter is essential because it is the primary input for the function of the node execution. It influences the operation of the node by determining the size and volume of the output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- width
    - Width parameters represent the horizontal dimensions of the image and are an essential aspect of image analysis and processing.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - High parameters represent the vertical dimensions of the image and play a key role in structural understanding and the operation of image data.
    - Comfy dtype: INT
    - Python dtype: int
- batch_size
    - Batch size parameters indicate the number of images in a batch of images, which is essential to optimize computational efficiency and manage resources during image processing.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class ImageSizeAndBatchSize:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}
    CATEGORY = 'Animate Diff/Utils'
    RETURN_TYPES = ('INT', 'INT', 'INT')
    RETURN_NAMES = ('width', 'height', 'batch_size')
    FUNCTION = 'batch_size'

    def batch_size(self, image: Tensor):
        (batch_size, height, width) = image.shape[0:3]
        return (width, height, batch_size)
```