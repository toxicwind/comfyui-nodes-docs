# Documentation
- Class name: WAS_Mask_Invert
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_Invert node is designed to reverse input mask, providing a means to manipulate image masking in certain image-processing tasks. It is an indispensable tool in applications and applies to situations where binary mask data are required, such as in image partitioning or synthesis.

# Input types
## Required
- masks
    - The'masks' parameter is essential for the operation of the node, as it defines the binary mask to be reversed. Its correct use is essential for achieving the desired results in the image processing workflow.
    - Comfy dtype: MASK
    - Python dtype: Union[PIL.Image.Image, np.ndarray]

# Output types
- MASKS
    - The MASKS output represents a reverse binary mask, which is a direct result of the main function of the node. It is important for downstream processes that rely on the invert mask for further image operations.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Invert:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'masks': ('MASK',)}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'add_masks'

    def add_masks(self, masks):
        return (1.0 - masks,)
```