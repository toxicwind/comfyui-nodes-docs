# Documentation
- Class name: Dilate_SEG_ELT
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The Dilate_SEG_ELT node is designed to implement a morphological inflation of the partition mask, which is a key step in expanding the detection boundary of the object in image processing. The node enhances the partition mask by applying the expansion of the specified factor, which may improve the accuracy of the object detection during the subsequent phase.

# Input types
## Required
- seg_elt
    - The seg_elt parameter is the key input for the split elements to be processed. It contains the cropped image, mask, confidence score, crop area, boundary box, label and control net packagings, which are essential for correct expansionary operations.
    - Comfy dtype: SEG_ELT
    - Python dtype: SEG
## Optional
- dilation
    - The dilation parameter determines the extent of the expansion effect to be applied to the mask. Large values lead to a more significant expansion of the mask boundary, which may be important for some image analysis missions. Default values are set to ensure a balanced expansion effect.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- seg_elt
    - The output seg_elt is a treated partition element with an updated mask that reflects an inflated operation. This output is important because it forms the basis for further analysis or visualization in the image treatment stream.
    - Comfy dtype: SEG_ELT
    - Python dtype: SEG

# Usage tips
- Infra type: CPU

# Source code
```
class Dilate_SEG_ELT:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'seg_elt': ('SEG_ELT',), 'dilation': ('INT', {'default': 10, 'min': -512, 'max': 512, 'step': 1})}}
    RETURN_TYPES = ('SEG_ELT',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, seg, dilation):
        mask = core.dilate_mask(seg.cropped_mask, dilation)
        seg = SEG(seg.cropped_image, mask, seg.confidence, seg.crop_region, seg.bbox, seg.label, seg.control_net_wrapper)
        return (seg,)
```