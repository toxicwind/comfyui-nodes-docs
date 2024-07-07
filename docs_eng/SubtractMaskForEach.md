# Documentation
- Class name: SubtractMaskForEach
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method at SubtrustMaskForEach node is designed to treat the split data by subtracting the mask partition from the base partition. It operates by identifying the overlap area between the base partition and the mask partition and modifying the base partition accordingly. This method is essential to fine-tune the split result and to ensure that the overlap area is accurately identified.

# Input types
## Required
- base_segs
    - The 'base_segs' parameter is the collection of split data to be processed by the node. It is essential because it forms the basis for the subtraction exercise performed by the node. This parameter directly affects the outcome of the split process and determines which parts of the image will be retained or modified.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
- mask_segs
    - The'mask_segs' parameter contains a mask split that will be subtracted from the base partition. This parameter is essential for defining the partition area that will be modified. It works with 'base_segs' to ensure that only the specified area is affected by the subtraction operation.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]

# Output types
- result
    - The'redult' output is a list of splits that are modified after the subtraction operation. Each item represents a base split adjusted by the mask split. This output is important because it provides the final, refined split data for further use or analysis.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[str, List[SEG]]

# Usage tips
- Infra type: CPU

# Source code
```
class SubtractMaskForEach:

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
                changed = False
                for i in range(intersect_region[0], intersect_region[2]):
                    for j in range(intersect_region[1], intersect_region[3]):
                        if cropped_mask1[j - crop_region1[1], i - crop_region1[0]] == 1 and cropped_mask2[j - crop_region2[1], i - crop_region2[0]] == 1:
                            changed = True
                            cropped_mask1[j - crop_region1[1], i - crop_region1[0]] = 0
                        else:
                            pass
                if changed:
                    item = SEG(bseg.cropped_image, cropped_mask1, bseg.confidence, bseg.crop_region, bseg.bbox, bseg.label, None)
                    result.append(item)
                else:
                    result.append(bseg)
        return ((base_segs[0], result),)
```