# Documentation
- Class name: SegsToCombinedMask
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The `SegsToCombined Mask' node is designed to combine multiple splits into a single mask. It operates by combining the fragments into a comprehensive binary mask, which can be used for further analysis or visualization. This node is essential in applications that need to be uniform in indicating partition areas, such as medical imaging or autopilot vehicle perception systems.

# Input types
## Required
- segs
    - The `segs' parameter is the collection of split objects that the node will process to create a combination mask. It is essential for the operation of the node, because it directly affects the composition of the output mask. Each split object should contain a crop mask and a crop area that determines the location of the mask in the final combination mask.
    - Comfy dtype: COMBO[torch.Tensor]
    - Python dtype: List[core.SEG]

# Output types
- mask
    - The `mask' output is a 3D binary volume, representing a combination mask made from input splits. It is important because it binds the group into a single, coherent structure that can be used for downstream tasks, such as target detection or partition analysis.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class SegsToCombinedMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',)}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Operation'

    def doit(self, segs):
        mask = core.segs_to_combined_mask(segs)
        mask = utils.make_3d_mask(mask)
        return (mask,)
```