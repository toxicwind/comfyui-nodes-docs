# Documentation
- Class name: MaskToSEGS
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The MaskToSEGS node is designed to convert the binary mask to a series of sub-objects expressed for SEG objects. It handles the input mask to identify different areas and output them into a group of sub-objects that can be further used for various image processing tasks.

# Input types
## Required
- mask
    - The mask parameter is a binary mask that defines the area of interest in the image. It is essential for the operation of the node, as it directly affects the split process and the SEG object generated.
    - Comfy dtype: MASK
    - Python dtype: np.ndarray
## Optional
- combined
    - The cobined parameter determines whether the node should merge the overlapping area in the mask into a single SEG object. This may be important to simplify the indication of a complex scenario.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- crop_factor
    - The crop_factor parameter controls the size of the cropped area around the boundary box of each mask segment. It affects the detail level of the SEG object by determining the number of contexts around each segment.
    - Comfy dtype: FLOAT
    - Python dtype: float
- bbox_fill
    - The bbox_fill parameter specifies whether the boundary box should be filled with a solid value in the crop area. This can be used to highlight or isolate a specific area within a SEG object.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- drop_size
    - The drop_size parameter setting will contain the minimum dimensions of the mask segment in the output. Smaller segments that do not meet this size threshold will be discarded, which may reduce the noise in the split.
    - Comfy dtype: INT
    - Python dtype: int
- contour_fill
    - The contour_fill parameter indicates whether the node should fill the area in the mask. This can be used to create a solid SEG object from a contour-based mask.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- SEGS
    - The SEGS output consists of a series of SEG objects, each of which represents a segment area derived from the input mask. These objects are structured so that they can be further analysed or operated in the image processing workflow.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[int, List[core.SEG]]

# Usage tips
- Infra type: CPU

# Source code
```
class MaskToSEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'combined': ('BOOLEAN', {'default': False, 'label_on': 'True', 'label_off': 'False'}), 'crop_factor': ('FLOAT', {'default': 3.0, 'min': 1.0, 'max': 100, 'step': 0.1}), 'bbox_fill': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'drop_size': ('INT', {'min': 1, 'max': MAX_RESOLUTION, 'step': 1, 'default': 10}), 'contour_fill': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'})}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Operation'

    def doit(self, mask, combined, crop_factor, bbox_fill, drop_size, contour_fill=False):
        mask = make_2d_mask(mask)
        result = core.mask_to_segs(mask, combined, crop_factor, bbox_fill, drop_size, is_contour=contour_fill)
        return (result,)
```