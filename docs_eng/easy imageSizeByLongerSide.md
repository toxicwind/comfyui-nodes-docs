# Documentation
- Class name: imageSizeByLongerSide
- Category: EasyUse/Image
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node class categorizes images according to their longer dimensions and provides a simplified method for image analysis and processing by focusing on the longer edges of the images.

# Input types
## Required
- image
    - The image parameter is essential because it is the main input for node operations. It affects the entire process by determining the basis for node output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray

# Output types
- resolution
    - Resolution output provides the long edge length of the image, which is essential for subsequent image processing tasks and analysis.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class imageSizeByLongerSide:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',)}}
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('resolution',)
    OUTPUT_NODE = True
    FUNCTION = 'image_longer_side'
    CATEGORY = 'EasyUse/Image'

    def image_longer_side(self, image):
        (_, raw_H, raw_W, _) = image.shape
        width = raw_W
        height = raw_H
        if width is not None and height is not None:
            if width > height:
                result = (width,)
            else:
                result = (height,)
        else:
            result = (0,)
        return {'ui': {'text': str(result[0])}, 'result': result}
```