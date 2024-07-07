# Documentation
- Class name: SEG_ELT_BBOX_ScaleBy
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

SEG_ELT_BBOX_ScaleBy node is designed to adjust the size of the partition element (SEG_ELT) by the specified factor. By scaling the border box of SEG_ELT, it then uses zero filling on the mask to preserve the integrity of the partition. This node is essential to adjust the size of the split without losing any detail or introducing a false picture.

# Input types
## Required
- seg
    - The'seg' parameter is the scalable split element (SEG_ELT). It is important because it defines input data for node operations and directly affects the size and properties of the output partition.
    - Comfy dtype: SEG_ELT
    - Python dtype: SEG_ELT
- scale_by
    - The'scale_by' parameter determines the zoom factor of the SEG_ELT boundary box. It is a floating number that adjusts the size of the split element and has an impact on the resolution and coverage of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- scaled_seg
    - The'scaled_seg'output is the result of applying the zoom operation to SEG_ELT. It includes the scaled boundary box and the adjusted mask to ensure that the split is correctly resized and the information is not lost during the process.
    - Comfy dtype: SEG_ELT
    - Python dtype: SEG_ELT

# Usage tips
- Infra type: CPU

# Source code
```
class SEG_ELT_BBOX_ScaleBy:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'seg': ('SEG_ELT',), 'scale_by': ('FLOAT', {'default': 1.0, 'min': 0.01, 'max': 8.0, 'step': 0.01})}}
    RETURN_TYPES = ('SEG_ELT',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    @staticmethod
    def fill_zero_outside_bbox(mask, crop_region, bbox):
        (cx1, cy1, _, _) = crop_region
        (x1, y1, x2, y2) = bbox
        (x1, y1, x2, y2) = (x1 - cx1, y1 - cy1, x2 - cx1, y2 - cy1)
        (h, w) = mask.shape
        x1 = min(w - 1, max(0, x1))
        x2 = min(w - 1, max(0, x2))
        y1 = min(h - 1, max(0, y1))
        y2 = min(h - 1, max(0, y2))
        mask_cropped = mask.copy()
        mask_cropped[:, :x1] = 0
        mask_cropped[:, x2:] = 0
        mask_cropped[:y1, :] = 0
        mask_cropped[y2:, :] = 0
        return mask_cropped

    def doit(self, seg, scale_by):
        (x1, y1, x2, y2) = seg.bbox
        w = x2 - x1
        h = y2 - y1
        dw = int((w * scale_by - w) / 2)
        dh = int((h * scale_by - h) / 2)
        bbox = (x1 - dw, y1 - dh, x2 + dw, y2 + dh)
        cropped_mask = SEG_ELT_BBOX_ScaleBy.fill_zero_outside_bbox(seg.cropped_mask, seg.crop_region, bbox)
        seg = SEG(seg.cropped_image, cropped_mask, seg.confidence, seg.crop_region, bbox, seg.label, seg.control_net_wrapper)
        return (seg,)
```