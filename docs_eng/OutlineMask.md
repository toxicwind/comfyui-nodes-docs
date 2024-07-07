# Documentation
- Class name: OutlineMask
- Category: ♾️Mixlab/Mask
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The Outline Mask node is designed to create contour effects by using an inflated or corrosive process to manipulate the image mask. It enhances the visual differentiation on the surface of the mask, which is essential for the application of the mask boundary that needs to be clear and well defined.

# Input types
## Required
- mask
    - The `mask' parameter is an essential input to the Outline Mask node, representing the original image mask to be processed. It plays a key role in determining the final contours, as it determines the shape and content of the initial mask.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- outline_width
    - The `outline_width' parameter specifies the extent to which the contour extension or contraction should be applied to the mask. It is a key factor in controlling the contour generated, thus affecting the visual impact of the margin of the mask.
    - Comfy dtype: INT
    - Python dtype: int
- tapered_corners
    - When set to True, the 'tapered_corners' parameter applies a conical effect to the corner of the mask, creating a more subtle and visually attractive contour. This feature enhances the aesthetic quality of the final output.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- mask
    - The `mask' output of the Outline Mask node is a processed image mask with contour effects. It is important because it represents the final product of node operations and is prepared for further use or visualization.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class OutlineMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'outline_width': ('INT', {'default': 10, 'min': 1, 'max': MAX_RESOLUTION, 'step': 1}), 'tapered_corners': ('BOOLEAN', {'default': True})}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Mask'

    def run(self, mask, outline_width, tapered_corners):
        m1 = grow(mask, outline_width, tapered_corners)
        m2 = grow(mask, -outline_width, tapered_corners)
        m3 = combine(m1, m2, 0, 0)
        return (m3,)
```