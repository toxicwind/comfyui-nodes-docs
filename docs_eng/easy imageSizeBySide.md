# Documentation
- Class name: imageSizeBySide
- Category: EasyUse/Image
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node classifies the image according to the specified border length criteria and provides a simplified resolution value based on the user's preference for longer or shorter edges of the image.

# Input types
## Required
- image
    - The image parameter is necessary because it is the main input for node operations. It influences the entire processing process by deciding the size to be assessed and compared to the specified edge.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- side
    - The margin parameters determine the criteria for a resolution assessment, either focusing on the longest edge of the image or on the shortest edge. It significantly influences the results of node functions.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- resolution
    - The resolution output provides a single integer value, representing the image dimensions selected on the basis of the border parameters. It is the core result of the node operation, summarizing the size of the image according to the user's preferences.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class imageSizeBySide:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'side': (['Longest', 'Shortest'],)}}
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('resolution',)
    OUTPUT_NODE = True
    FUNCTION = 'image_side'
    CATEGORY = 'EasyUse/Image'

    def image_side(self, image, side):
        (_, raw_H, raw_W, _) = image.shape
        width = raw_W
        height = raw_H
        if width is not None and height is not None:
            if side == 'Longest':
                result = (width,) if width > height else (height,)
            elif side == 'Shortest':
                result = (width,) if width < height else (height,)
        else:
            result = (0,)
        return {'ui': {'text': str(result[0])}, 'result': result}
```