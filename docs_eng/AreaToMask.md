# Documentation
- Class name: AreaToMask
- Category: ♾️Mixlab/Mask
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node converts images with the RGBA channel to a mask and focuses on separating specific areas of interest by removing transparency and applying cutting techniques. It emphasizes the conversion of visual data for further analysis or operation in the area of image processing.

# Input types
## Required
- RGBA
    - RGBA input is essential because it provides the raw image data needed for node execution to be converted to mask. It is the basis for node operations and determines the quality and extent of the result mask.
    - Comfy dtype: image
    - Python dtype: PIL.Image

# Output types
- MASK
    - The output mask is an important product of node operations and represents an area of isolation of interest in the input image. It is a key component of the follow-up image-processing task, making accurate operation and analysis possible.
    - Comfy dtype: tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class AreaToMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'RGBA': ('RGBA',)}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Mask'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)

    def run(self, RGBA):
        mask = AreaToMask_run(RGBA)
        return (mask,)
```