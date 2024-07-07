# Documentation
- Class name: ControlNetClearSEGS
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The `doit' method of the ControlNetClearSEGs node is designed to treat SEG objects by creating a new SEG example with certain attributes set to None. It plays a key role in pre-processing or modifying segment data for further analysis or operating within the ImpactPack application package.

# Input types
## Required
- segs
    - The'segs' parameter is the set of SEG objects that the node will process. It is essential for the operation of the node because it defines the input data that will be converted to a new format.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[SEG, List[SEG]]

# Output types
- new_segs
    - The 'new_segs' output is a list of SEG objects modified by nodes. Each SEG object in this list has a specific attribute set to None, which may be important for some types of follow-up or analysis.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]

# Usage tips
- Infra type: CPU

# Source code
```
class ControlNetClearSEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',)}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, segs):
        new_segs = []
        for seg in segs[1]:
            new_seg = SEG(seg.cropped_image, seg.cropped_mask, seg.confidence, seg.crop_region, seg.bbox, seg.label, None)
            new_segs.append(new_seg)
        return ((segs[0], new_segs),)
```