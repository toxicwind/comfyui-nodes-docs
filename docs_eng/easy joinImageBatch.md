# Documentation
- Class name: JoinImageBatch
- Category: EasyUse/Image
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node can combine multiple images into a large image, which can be done vertically or horizontally. It is designed to simplify the process of creating image collating or comparing and analysing with visual data.

# Input types
## Required
- images
    - The Images parameter is the key input to the image batch that you want to merge. It is a numbery array containing the image batch, each of which is a multi-dimensional array of pixel values.
    - Comfy dtype: COMBO[numpy.ndarray]
    - Python dtype: numpy.ndarray
## Optional
- mode
    - The mode parameter determines the direction of the merged image, which can be 'horizontal' or'vertical'. It affects the way the image is arranged in the final consolidation image.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- image
    - The output image is the result of the batch merge of the input. It represents a single large image that contains all input images, horizontally or vertically.
    - Comfy dtype: numpy.ndarray
    - Python dtype: numpy.ndarray

# Usage tips
- Infra type: CPU

# Source code
```
class JoinImageBatch:
    """Turns an image batch into one big image."""

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'mode': (('horizontal', 'vertical'), {'default': 'horizontal'})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    FUNCTION = 'join'
    CATEGORY = 'EasyUse/Image'

    def join(self, images, mode):
        (n, h, w, c) = images.shape
        image = None
        if mode == 'vertical':
            image = images.reshape(1, n * h, w, c)
        elif mode == 'horizontal':
            image = torch.transpose(torch.transpose(images, 1, 2).reshape(1, n * w, h, c), 1, 2)
        return (image,)
```