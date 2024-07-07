# Documentation
- Class name: ImagePadForOutpaint
- Category: image
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ImagePadForOutpaint node is designed to expand the boundaries of the image, which is particularly useful in the context of an extended (outpinting) mission. It allows each side of the image to be expanded by the number of pixels specified and can selectively add a feather effect to smooth the integration of the new edge with the original image.

# Input types
## Required
- image
    - The image parameter is the input image that will be filled. It is essential for the operation of the node, as it determines the content that will be expanded.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- left
    - The left parameter specifies the number of pixels that you want to add to the left side of the image. It plays an important role in determining the final size of the extended image.
    - Comfy dtype: INT
    - Python dtype: int
- top
    - The top parameter specifies the number of pixels that you want to add to the top of the image. It is an important factor in controlling the vertical extension of the image.
    - Comfy dtype: INT
    - Python dtype: int
- right
    - The parameter specifies the number of pixels that you want to add to the right side of the image. It affects the ultimate width of the extended image.
    - Comfy dtype: INT
    - Python dtype: int
- bottom
    - The bottom parameter specifies the number of pixels to be added at the bottom of the image. It is essential to control the horizontal expansion of the image.
    - Comfy dtype: INT
    - Python dtype: int
- feathering
    - Feathering parameters control the smoothness of the transition between the original image area and the newly added image area. The higher the value, the more gradual the transition.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- new_image
    - New_image output is the result of the extension process, showing original images filled on each side in specified quantities.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - The mask output is a binary image that divides the original image area from the newly added area, mainly for hybrid purposes.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ImagePadForOutpaint:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'left': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'top': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'right': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'bottom': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'feathering': ('INT', {'default': 40, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1})}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'expand_image'
    CATEGORY = 'image'

    def expand_image(self, image, left, top, right, bottom, feathering):
        (d1, d2, d3, d4) = image.size()
        new_image = torch.ones((d1, d2 + top + bottom, d3 + left + right, d4), dtype=torch.float32) * 0.5
        new_image[:, top:top + d2, left:left + d3, :] = image
        mask = torch.ones((d2 + top + bottom, d3 + left + right), dtype=torch.float32)
        t = torch.zeros((d2, d3), dtype=torch.float32)
        if feathering > 0 and feathering * 2 < d2 and (feathering * 2 < d3):
            for i in range(d2):
                for j in range(d3):
                    dt = i if top != 0 else d2
                    db = d2 - i if bottom != 0 else d2
                    dl = j if left != 0 else d3
                    dr = d3 - j if right != 0 else d3
                    d = min(dt, db, dl, dr)
                    if d >= feathering:
                        continue
                    v = (feathering - d) / feathering
                    t[i, j] = v * v
        mask[top:top + d2, left:left + d3] = t
        return (new_image, mask)
```