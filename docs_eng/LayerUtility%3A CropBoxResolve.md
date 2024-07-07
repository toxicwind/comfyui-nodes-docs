# Documentation
- Class name: CropBoxResolve
- Category: 😺dzNodes/LayerMask
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Resolve corp_box as x, y, width, height.

# Input types
## Required

- crop_box
    - Crop frames.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types

- x
    - Crop the top left corner x coordinate.
    - Comfy dtype: INT
    - Python dtype: int

- y
    - Crop frame top left corner y coordinates.
    - Comfy dtype: INT
    - Python dtype: int

- width
    - Crop frame width.
    - Comfy dtype: INT
    - Python dtype: int

- height
    - Crop frame height.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: GPU

# Source code
```
class CropBoxResolve:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):

        return {
            "required": {
                "crop_box": ("BOX",),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT")
    RETURN_NAMES = ("x", "y", "width", "height")
    FUNCTION = 'crop_box_resolve'
    CATEGORY = '😺dzNodes/LayerUtility'

    def crop_box_resolve(self, crop_box
                  ):

        (x1, y1, x2, y2) = crop_box
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        return (x1, y1, x2 - x1, y2 - y1,)
```