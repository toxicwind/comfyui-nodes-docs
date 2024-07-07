# Documentation
- Class name: SEGSToMaskList
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

SEGSToMaskList is designed to convert the split object into a mask list. It is a tool in the ImpactPack/Util category to help transform the split data into a format that is easier to visualize or further analyse.

# Input types
## Required
- segs
    - The parameter'segs' is essential for the operation of the node, because it provides split data that need to be converted to a mask. The significance of this parameter is that it determines the output of the node as its main input.
    - Comfy dtype: SEGS
    - Python dtype: List[core.SEG]

# Output types
- masks
    - Output'masks' is a mask list from which you enter split data. Each mask represents a different segment, and this output is important because it allows further processing or analysis of split areas.
    - Comfy dtype: MASK
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class SEGSToMaskList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',)}}
    RETURN_TYPES = ('MASK',)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, segs):
        masks = core.segs_to_masklist(segs)
        if len(masks) == 0:
            empty_mask = torch.zeros(segs[0], dtype=torch.float32, device='cpu')
            masks = [empty_mask]
        masks = [utils.make_3d_mask(mask) for mask in masks]
        return (masks,)
```