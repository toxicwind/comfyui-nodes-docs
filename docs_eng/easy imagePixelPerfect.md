# Documentation
- Class name: imagePixelPerfect
- Category: EasyUse/Image
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node class is designed to optimize the resolution of the image by calculating the ideal number of pixels that maintain the image's vertical ratio within the specified size. It emphasizes the visual integrity of the image in the larger hours when the image is adjusted.

# Input types
## Required
- image
    - The image parameter is essential because it is the source of node operations. It influences the process by determining the initial size and quality of the node to be processed.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
## Optional
- resize_mode
    - Adjusts the pattern parameters to influence the way the image is adjusted, either maximizing or minimizing the horizontal and vertical ratio to suit the given constraints. This is important for achieving the desired visual result after adjusting the size.
    - Comfy dtype: COMBO[ResizeMode.RESIZE.value, ResizeMode.INNER_FIT.value, ResizeMode.OUTER_FIT.value]
    - Python dtype: Union[str, ResizeMode]

# Output types
- resolution
    - The resolution output provides the ideal number of pixels to be calculated, which is the result of node processing. It is important because it determines the final size of the image after scaling.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class imagePixelPerfect:

    @classmethod
    def INPUT_TYPES(s):
        RESIZE_MODES = [ResizeMode.RESIZE.value, ResizeMode.INNER_FIT.value, ResizeMode.OUTER_FIT.value]
        return {'required': {'image': ('IMAGE',), 'resize_mode': (RESIZE_MODES, {'default': ResizeMode.RESIZE.value})}}
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('resolution',)
    OUTPUT_NODE = True
    FUNCTION = 'execute'
    CATEGORY = 'EasyUse/Image'

    def execute(self, image, resize_mode):
        (_, raw_H, raw_W, _) = image.shape
        width = raw_W
        height = raw_H
        k0 = float(height) / float(raw_H)
        k1 = float(width) / float(raw_W)
        if resize_mode == ResizeMode.OUTER_FIT.value:
            estimation = min(k0, k1) * float(min(raw_H, raw_W))
        else:
            estimation = max(k0, k1) * float(min(raw_H, raw_W))
        result = int(np.round(estimation))
        text = f'Width:{str(width)}\nHeight:{str(height)}\nPixelPerfect:{str(result)}'
        return {'ui': {'text': text}, 'result': (result,)}
```