# Documentation
- Class name: ImageResizeCalculator
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The ImageResizeCalculator node is designed to intelligently resize the image while maintaining its horizontal ratio to meet specific requirements, such as target dimensions and multiples of alignment to eight, which are essential for certain image processing tasks.

# Input types
## Required
- image
    - The image parameter is necessary because it is the main input to the node operation. It determines the source material to be processed and affects the output size and calculation of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- target_size
    - The target size parameter specifies the desired size of the adjusted image. It plays a vital role in the process of resizing, directly affecting the final size and scaling calculation.
    - Comfy dtype: INT
    - Python dtype: int
- force_8x
    - Force_8x parameters determine whether the adjusted size should be aligned to a multiple of 8. This is particularly important for some image processing algorithms that benefit from this alignment.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- width
    - The width output provides a new width of the adjusted image, which is the direct result of the node resize calculation.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The high output corresponds to the new height of the adjusted image, which is another key result of the process of resizing.
    - Comfy dtype: INT
    - Python dtype: int
- min
    - A smaller dimension of two dimensions after the minimum value output instruction adjustment provides insight into the width ratio of the adjusted image.
    - Comfy dtype: INT
    - Python dtype: int
- scale
    - Scale output represents the zoom factor from the original width to the new width, which is a key value for understanding the resize change.
    - Comfy dtype: FLOAT
    - Python dtype: float
- scale_r
    - The scale_r output represents the penultimate of the zoom factor from the original altitude to the new altitude, providing a comprehensive understanding of vertical resizeing.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class ImageResizeCalculator:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE', {}), 'target_size': ('INT', {'default': 512, 'min': 1, 'step': 1}), 'force_8x': ('BOOLEAN', {'default': True})}}
    RETURN_TYPES = ('INT', 'INT', 'INT', 'FLOAT', 'FLOAT')
    RETURN_NAMES = ('width', 'height', 'min', 'scale', 'scale_r')
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, image: Tensor, target_size: int, force_8x: bool):
        w = image[0].shape[1]
        h = image[0].shape[0]
        ratio = h * 1.0 / w
        if w >= h:
            w_new = target_size
            h_new = target_size * ratio
            if force_8x:
                w_new = int(w_new / 8) * 8
                h_new = int(h_new / 8) * 8
            return (w_new, int(h_new), h_new, w_new * 1.0 / w, w * 1.0 / w_new)
        else:
            w_new = target_size / ratio
            h_new = target_size
            if force_8x:
                w_new = int(w_new / 8) * 8
                h_new = int(h_new / 8) * 8
            return (int(w_new), h_new, w_new, h_new * 1.0 / h, h * 1.0 / h_new)
```