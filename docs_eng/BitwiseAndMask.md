# Documentation
- Class name: BitwiseAndMask
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method at Bitwise And Mask node is designed to perform position and operation for two input masks. It is essential for applications that require a combination of masking layers, for example, during image partitioning or data filtering. This method ensures that only two masked common elements are retained in the output, which helps to obtain more refined and accurate results.

# Input types
## Required
- mask1
    - The parameter'mask1' is the first input mask by location and operation. By contributing its structure and content, it plays a key role in determining the final mask. Node execution is directly influenced by the'mask1' attribute, which must be aligned to'mask2' in order to operate effectively by location.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- mask2
    - The parameter'mask2' is the second input mask that'mask1' is used in position and operation. It is equivalent to'mask1' because it also defines the common area that will appear in the result mask. The function of the node depends on the compatibility of the shape between'mask1' and'mask2'.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- mask
    - The'mask' output is the result of location and operation between'mask1' and'mask2'. It indicates that a common area exists in both input masks and is essential for further processing or analysis, as indicated by the need for a single combination mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class BitwiseAndMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask1': ('MASK',), 'mask2': ('MASK',)}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Operation'

    def doit(self, mask1, mask2):
        mask = bitwise_and_masks(mask1, mask2)
        return (mask,)
```