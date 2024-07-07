# Documentation
- Class name: WAS_Inset_Image_Bounds
- Category: WAS Suite/Image/Bound
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Inset_Image_Bounds node is designed to ensure that the modified image retains its structural integrity by inserting value. It operates by adding or reducing the specified boundary, with care to verify that the generated image boundary is logically reasonable and does not exceed the original dimensions.

# Input types
## Required
- image_bounds
    - The image_bounds parameter defines the initial boundary of the image that will be applied to the inserted value. This is essential to determine the starting point of the image size modification.
    - Comfy dtype: IMAGE_BOUNDS
    - Python dtype: List[Tuple[int, int, int, int]]
- inset_left
    - The inset_left parameter specifies the amount of boundary to be inserted on the left side of the image. It plays an important role in determining the new left edge of the processed image.
    - Comfy dtype: INT
    - Python dtype: int
- inset_right
    - The inset_right parameter specifies the number of boundaries to be inserted on the right side of the image. This is important for creating a new right edge for the adjusted image.
    - Comfy dtype: INT
    - Python dtype: int
- inset_top
    - The inset_top parameter indicates the number of boundaries that should be inserted at the top of the image. It is important to set a new top edge of the image after applying the insertion.
    - Comfy dtype: INT
    - Python dtype: int
- inset_bottom
    - The inset_bottom parameter determines the number of boundaries that should be inserted at the bottom of the image. This is essential to define the new bottom edge of the adjusted image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- inset_bounds
    - The inset_bounds output indicates a new boundary that applies the inserted image. It is important because it reflects the final size of the processed image.
    - Comfy dtype: IMAGE_BOUNDS
    - Python dtype: List[Tuple[int, int, int, int]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Inset_Image_Bounds:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {'required': {'image_bounds': ('IMAGE_BOUNDS',), 'inset_left': ('INT', {'default': 64, 'min': 0, 'max': 18446744073709551615}), 'inset_right': ('INT', {'default': 64, 'min': 0, 'max': 18446744073709551615}), 'inset_top': ('INT', {'default': 64, 'min': 0, 'max': 18446744073709551615}), 'inset_bottom': ('INT', {'default': 64, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('IMAGE_BOUNDS',)
    FUNCTION = 'inset_image_bounds'
    CATEGORY = 'WAS Suite/Image/Bound'

    def inset_image_bounds(self, image_bounds, inset_left, inset_right, inset_top, inset_bottom):
        inset_bounds = []
        for (rmin, rmax, cmin, cmax) in image_bounds:
            rmin += inset_top
            rmax -= inset_bottom
            cmin += inset_left
            cmax -= inset_right
            if rmin > rmax or cmin > cmax:
                raise ValueError('Invalid insets provided. Please make sure the insets do not exceed the image bounds.')
            inset_bounds.append((rmin, rmax, cmin, cmax))
        return (inset_bounds,)
```