# Documentation
- Class name: RemoveImageFromSEGS
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The `RemoveImageFromSEGS’ node is designed to separate the data by removing the original image components from the `SEGS' object. It focuses on preserving basic properties such as the mask after the crop, confidence, area, boundary frame, label and control net packaging, thus allowing for a simplified version of the split data that does not contain the image itself.

# Input types
## Required
- segs
    - The `segs' parameter is an important input to the node because it represents the split data that needs to be processed. The node operates on this data to create a new version of the `SEGS' object without the original image, which is necessary for some applications that only divide properties.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[SEG, List[SEG]]

# Output types
- result
    - The `result' output contains processed `SEGS' objects, in which the original image has been removed. This output is important because it provides users with a data set that can be used for further analysis or processing without necessarily modifying the image data.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[SEG, List[SEG]]

# Usage tips
- Infra type: CPU

# Source code
```
class RemoveImageFromSEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',)}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, segs):
        results = []
        if len(segs[1]) > 0:
            for seg in segs[1]:
                new_seg = SEG(None, seg.cropped_mask, seg.confidence, seg.crop_region, seg.bbox, seg.label, seg.control_net_wrapper)
                results.append(new_seg)
            return ((segs[0], results),)
        else:
            return (segs,)
```