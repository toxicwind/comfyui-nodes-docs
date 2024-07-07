# Documentation
- Class name: CropMask
- Category: mask
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

Cropmask node is designed to extract the specified interest area from the larger masked image. It operates by defining a rectangular area using the coordinates and dimensions provided, allowing accurate cropping. This node is essential to focus analysis on a particular area of the image and to improve the efficiency and relevance of subsequent processing steps.

# Input types
## Required
- mask
    - The'mask'parameter is the input mask image from which the area is to be trimmed. It is the basic data for node operations, and the output of the node depends directly on the content and structure of the input.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- x
    - The 'x' parameter specifies a horizontal starting point for the crop operation. It is essential to determine the exact location within the mask where the crop will start.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - The 'y' parameter defines the vertical starting point of the crop operation. It works with the 'x' parameter to specify precisely the top left corner of the crop rectangle.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The `width' parameter sets the width of the rectangular. It determines the horizontal range of the area to be extracted from the mask image.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height'parameter establishes the vertical dimensions of the cropRect. It is essential to define the vertical range of the area to be cut from the mask.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- cropped_mask
    - The `cropped_mask' output is the result of the crop operation, showing a smaller part of the original mask, which is specified by the input parameter. This output is important for further processing or analysis that requires a focused view of a particular area within the mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class CropMask:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mask': ('MASK',), 'x': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1}), 'y': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1}), 'width': ('INT', {'default': 512, 'min': 1, 'max': MAX_RESOLUTION, 'step': 1}), 'height': ('INT', {'default': 512, 'min': 1, 'max': MAX_RESOLUTION, 'step': 1})}}
    CATEGORY = 'mask'
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'crop'

    def crop(self, mask, x, y, width, height):
        mask = mask.reshape((-1, mask.shape[-2], mask.shape[-1]))
        out = mask[:, y:y + height, x:x + width]
        return (out,)
```