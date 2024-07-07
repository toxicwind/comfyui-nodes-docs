# Documentation
- Class name: DilateMaskInSEGS
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The Dilate Mask InSEGS node is designed to perform morphological inflating operations for partition masking. It enhances partitioning by extending the boundaries of divided areas. This process is particularly useful when the boundaries of divided areas are not clearly defined or require a more robust indication.

# Input types
## Required
- segs
    - The `segs' parameter is the grouping of split objects that the node is about to process. It is essential for the operation of the node, because it defines the input data that will be applied to the inflating operation. The quality and accuracy of the split directly influences the outcome of the inflating process.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
- dilation
    - The `dilation' parameter is specified to apply to the expansion of the partition mask. It is a key factor in determining the extent of the boundary expansion. The larger value will lead to a more significant expansion, which may be useful for some applications, but it may also introduce inaccuracies if overused.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- new_segs
    - `new_segs' output contains split objects modified by application inflation. These objects now have extended boundaries that can be used for further analysis or processing of next steps in the workflow.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]

# Usage tips
- Infra type: CPU

# Source code
```
class DilateMaskInSEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',), 'dilation': ('INT', {'default': 10, 'min': -512, 'max': 512, 'step': 1})}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, segs, dilation):
        new_segs = []
        for seg in segs[1]:
            mask = core.dilate_mask(seg.cropped_mask, dilation)
            seg = SEG(seg.cropped_image, mask, seg.confidence, seg.crop_region, seg.bbox, seg.label, seg.control_net_wrapper)
            new_segs.append(seg)
        return ((segs[0], new_segs),)
```