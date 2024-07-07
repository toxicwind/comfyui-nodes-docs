# Documentation
- Class name: MaskToSEGS_for_AnimateDiff
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The MaskToSEGS_for_AnimatéDiff node is designed to convert the binary mask into a group of sub-objects called SEGS. It is implemented using the core functionality of the system to identify and separate different areas within the mask. This node is particularly useful for applications that need to convert the mask data into a format that can be further processed or analysed for detailed operations.

# Input types
## Required
- mask
    - The mask parameter is the key input for the node because it defines the binary mask from which the partition is to be performed. The quality and accuracy of the mask directly influences the partition of the result, making it an important part of the node execution.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- combined
    - Combined parameters determine whether the node should be treated as a single entity or as a separate paragraph. This decision affects the treatment of splits and may lead to different outcomes depending on the specific needs of different mandates.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- crop_factor
    - The crop_factor parameter is used to define the size of the area in the mask. It plays an important role in the partition process by controlling the size of the details extracted from the mask.
    - Comfy dtype: FLOAT
    - Python dtype: float
- bbox_fill
    - The bbox_fill parameter is an optional setting that, when enabled, fills the boundary box area within the mask. In some applications, the existence of the filled boundary box is necessary for further analysis or processing, which may be important.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- drop_size
    - The drop_size parameter specifies the minimum size of the area to be considered for partition. It ensures that only areas larger than a size threshold are included in the final partition, which helps filter out noise or irrelevant details.
    - Comfy dtype: INT
    - Python dtype: int
- contour_fill
    - The contour_fill parameter indicates whether the node should be filled with the contour in the mask. This is useful for applications that need to be physically filled in the area in a follow-up operation.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- SEGS
    - The SEGS output represents the results of the split process and provides detailed breakdowns of different areas within the original mask. This output is essential for further analysis or operation of the split data.
    - Comfy dtype: SEGS
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class MaskToSEGS_for_AnimateDiff:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'combined': ('BOOLEAN', {'default': False, 'label_on': 'True', 'label_off': 'False'}), 'crop_factor': ('FLOAT', {'default': 3.0, 'min': 1.0, 'max': 100, 'step': 0.1}), 'bbox_fill': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'drop_size': ('INT', {'min': 1, 'max': MAX_RESOLUTION, 'step': 1, 'default': 10}), 'contour_fill': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'})}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Operation'

    def doit(self, mask, combined, crop_factor, bbox_fill, drop_size, contour_fill=False):
        mask = make_2d_mask(mask)
        segs = core.mask_to_segs(mask, combined, crop_factor, bbox_fill, drop_size, is_contour=contour_fill)
        all_masks = SEGSToMaskList().doit(segs)[0]
        result_mask = (all_masks[0] * 255).to(torch.uint8)
        for mask in all_masks[1:]:
            result_mask |= (mask * 255).to(torch.uint8)
        result_mask = (result_mask / 255.0).to(torch.float32)
        result_mask = utils.to_binary_mask(result_mask, 0.1)[0]
        return MaskToSEGS().doit(result_mask, False, crop_factor, False, drop_size, contour_fill)
```