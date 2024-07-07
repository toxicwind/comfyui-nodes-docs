# Documentation
- Class name: MasksToMaskList
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The MasksToMaskList node is designed to process a series of mask images and convert them to a 3D masked sheet for further operation in the image-processing task. By applying the necessary conversions, it ensures that each mask is in the correct format, regardless of its initial size.

# Input types
## Required
- masks
    - The'masks' parameter is the mask image that the node will process. This is essential for the operation of the node, as it determines the input data that will be converted to a 3D mask bar list.
    - Comfy dtype: MASK
    - Python dtype: List[torch.Tensor]

# Output types
- mask_list
    - The'mask_list' output is a series of 3D mask loads that are processed and ready for follow-up image processing tasks. Each load in the list corresponds to a conversion mask in the input.
    - Comfy dtype: MASK
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class MasksToMaskList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'masks': ('MASK',)}}
    RETURN_TYPES = ('MASK',)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Operation'

    def doit(self, masks):
        if masks is None:
            empty_mask = torch.zeros((64, 64), dtype=torch.float32, device='cpu')
            return ([empty_mask],)
        res = []
        for mask in masks:
            res.append(mask)
        print(f'mask len: {len(res)}')
        res = [make_3d_mask(x) for x in res]
        return (res,)
```