# Documentation
- Class name: ImageBatch
- Category: image
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The "batch" method of the ImageBatch node is designed to efficiently process and group two images into a batch. It ensures that both images have the same size (if necessary) by performing sampling operations and then connects them along the batch dimensions. This node plays a key role in preparing data for further image processing tasks, such as neural network training or batch image operations.

# Input types
## Required
- image1
    - The 'image1'parameter represents the first image in the batch. It is essential for the operation of the node, because it is one of the two images to be processed and combined. The size and content of the image have a significant impact on the output and subsequent processing steps of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image2
    - The 'image2' parameter indicates that the second image will be included in the batch. It is required for node function and is treated with 'image1'. If the 'image2' size is different from 'image1', the size will be adjusted to match 'image1' to ensure consistency in the batch to allow consistent processing.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- batched_images
    - The 'batched_images' output is a mass of images that combine 'image1' and 'image2'. It is the main result of node operations and represents a batch of images prepared for downstream tasks, such as model reasoning or further image analysis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageBatch:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image1': ('IMAGE',), 'image2': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'batch'
    CATEGORY = 'image'

    def batch(self, image1, image2):
        if image1.shape[1:] != image2.shape[1:]:
            image2 = comfy.utils.common_upscale(image2.movedim(-1, 1), image1.shape[2], image1.shape[1], 'bilinear', 'center').movedim(1, -1)
        s = torch.cat((image1, image2), dim=0)
        return (s,)
```