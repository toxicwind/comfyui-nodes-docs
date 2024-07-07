# Documentation
- Class name: GrowMask
- Category: mask
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

GrowMask nodes are designed to operate binary masks by expanding or eroding their boundaries. It provides advanced functionality for masking changes, which are essential for applications that require precise control over the shape and size of the masked area.

# Input types
## Required
- mask
    - The'mask' parameter is a binary mask that is extended or eroded. It plays a central role in the operation of the node because it directly affects the shape and quality of the mask's output.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- expand
    - The `expand' parameter determines the amount of extension or erosion to be applied to the mask. Positive values lead to inflation, while negative values lead to erosion. It significantly affects the size and detail of the ultimate mask.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- tapered_corners
    - When set as True, the 'tapered_corners' parameter applies a particular erosion pattern to the corner of the mask. This is important for achieving a visual appeal mask shape with a rounded angle.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- expanded_mask
    - The `expanded_mask' output is the result of a mask extension or erosion process. It is important because it represents the final state of the mask after node operations.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class GrowMask:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mask': ('MASK',), 'expand': ('INT', {'default': 0, 'min': -MAX_RESOLUTION, 'max': MAX_RESOLUTION, 'step': 1}), 'tapered_corners': ('BOOLEAN', {'default': True})}}
    CATEGORY = 'mask'
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'expand_mask'

    def expand_mask(self, mask, expand, tapered_corners):
        c = 0 if tapered_corners else 1
        kernel = np.array([[c, 1, c], [1, 1, 1], [c, 1, c]])
        mask = mask.reshape((-1, mask.shape[-2], mask.shape[-1]))
        out = []
        for m in mask:
            output = m.numpy()
            for _ in range(abs(expand)):
                if expand < 0:
                    output = scipy.ndimage.grey_erosion(output, footprint=kernel)
                else:
                    output = scipy.ndimage.grey_dilation(output, footprint=kernel)
            output = torch.from_numpy(output)
            out.append(output)
        return (torch.stack(out, dim=0),)
```