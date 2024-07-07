# Documentation
- Class name: LatentCompositeMasked
- Category: latent
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The `composite' method at the LatentComposite Masked node is designed to mix potential source samples to the designated location of the target potential sample. It is intelligently managing synthetic operations to achieve seamless integration by considering optional masking and adjusting size parameters.

# Input types
## Required
- destination
    - The “destination” parameter indicates that the source sample will be synthesized as a potential sample. It is essential for the operation of nodes, as it defines the basis for the source sample mix.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- source
    - The "source" parameter is intended to be a potential sample of the target. It plays a key role in the function of the node, as it provides the content to be synthesized.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- x
    - The "x" parameter specifies the horizontal position where the source sample will be placed in the target. It is important because it determines the exact location of the synthesis operation.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - The " y " parameter defines the vertical position where the source sample will be placed in the target. It is an important factor in node execution, as it determines the vertical placement of composite content.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- resize_source
    - The "resize_source" parameter is an optional symbol, and when set to True, the source is resized to match the size of the target before the synthesis operation. It increases the flexibility of nodes in dealing with different potential sizes.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- mask
    - The " mask " parameter is an optional mass that defines the mask of the source sample. It is used to control which parts of the post-synthetic source are visible, adding a layer of control to the final output.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- composited_latent
    - The "composited_latet" output represents the final potential sample after the synthesis operation. It encapsifies the result of using optional masking and resizeing the source to the target at a given location.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class LatentCompositeMasked:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'destination': ('LATENT',), 'source': ('LATENT',), 'x': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'y': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'resize_source': ('BOOLEAN', {'default': False})}, 'optional': {'mask': ('MASK',)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'composite'
    CATEGORY = 'latent'

    def composite(self, destination, source, x, y, resize_source, mask=None):
        output = destination.copy()
        destination = destination['samples'].clone()
        source = source['samples']
        output['samples'] = composite(destination, source, x, y, mask, 8, resize_source)
        return (output,)
```