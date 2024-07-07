# Documentation
- Class name: BitwiseAndMaskForEach
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The `doit' method at Bitwise And MaskForEach node calculates the segment by using a mask to determine the area of overlap. It handles each base segment with a mask section, identifying the area of overlap and applying a mask to the area of non-overlapping to eliminate it. This method is essential to fine-tune the split result, ensuring that only the area of real overlap is preserved.

# Input types
## Required
- base_segs
    - The 'base_segs' parameter is a series of split objects that are to be processed by nodes. It is vital because it forms the basis for the biting exercise with the mask segment. The parameter directly influences the results of the node implementation and determines which paragraphs are considered for overlapping testing.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
- mask_segs
    - The'mask_segs' parameter consists of a split object that serves as a proxy for biting operations. It is essential because it defines the area to be retained after operation. The parameter plays an important role in shaping the final output of nodes by specifying the area to be considered for overlap and should be retained after operation.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]

# Output types
- result
    - The'redult' output is a list of split objects processed by bits. It contains only those that overlap between base and mask segments. This output is important because it represents the detailed split data after the operation.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[str, List[SEG]]

# Usage tips
- Infra type: CPU

# Source code
```
class BitwiseAndMaskForEach:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'base_segs': ('SEGS',), 'mask_segs': ('SEGS',)}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Operation'

    def doit(self, base_segs, mask_segs):
        result = []
        for bseg in base_segs[1]:
            cropped_mask1 = bseg.cropped_mask.copy()
            crop_region1 = bseg.crop_region
            for mseg in mask_segs[1]:
                cropped_mask2 = mseg.cropped_mask
                crop_region2 = mseg.crop_region
                intersect_region = (max(crop_region1[0], crop_region2[0]), max(crop_region1[1], crop_region2[1]), min(crop_region1[2], crop_region2[2]), min(crop_region1[3], crop_region2[3]))
                overlapped = False
                for i in range(intersect_region[0], intersect_region[2]):
                    for j in range(intersect_region[1], intersect_region[3]):
                        if cropped_mask1[j - crop_region1[1], i - crop_region1[0]] == 1 and cropped_mask2[j - crop_region2[1], i - crop_region2[0]] == 1:
                            overlapped = True
                            pass
                        else:
                            cropped_mask1[j - crop_region1[1], i - crop_region1[0]] = 0
                if overlapped:
                    item = SEG(bseg.cropped_image, cropped_mask1, bseg.confidence, bseg.crop_region, bseg.bbox, bseg.label, None)
                    result.append(item)
        return ((base_segs[0], result),)
```