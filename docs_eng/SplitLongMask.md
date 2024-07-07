# Documentation
- Class name: SplitLongMask
- Category: ♾️Mixlab/Mask
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The SplitLongMask node is designed to divide a single large mask into several smaller masks depending on the number or height specified. This process enhances the managementability and applicability of the mask in various scenarios, such as image partitioning or target tracking, and prefers to use smaller and easier-to-manage modules.

# Input types
## Required
- long_mask
    - Long_mask parameters are the main input for the SpringLongmask node. It represents a large mask that needs to be separated. The quality and size of the mask directly influences the output and determines the properties of the smaller mask in the result.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- count
    - The count parameter specifies the number of smaller masks that you want to export. It plays a crucial role in determining the size and quantity of the mask, which is essential for the application of the mask that requires a particular distribution.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- masks
    - The output of the SpringLongMask node, masks, is a small list of masks derived from the original long_mask. These masks are essential for applications that benefit from block mask input, such as image processing or machine learning tasks involving mask-based operations.
    - Comfy dtype: MASK
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class SplitLongMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'long_mask': ('MASK',), 'count': ('INT', {'default': 1, 'min': 1, 'max': 1024, 'step': 1})}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Mask'
    OUTPUT_IS_LIST = (True,)

    def run(self, long_mask, count):
        masks = []
        nh = long_mask.shape[0] // count
        if nh * count == long_mask.shape[0]:
            masks = split_mask_by_new_height(long_mask, nh)
        else:
            masks = split_mask_by_new_height(long_mask, long_mask.shape[0])
        return (masks,)
```