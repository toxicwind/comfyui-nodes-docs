# Documentation
- Class name: SEGSPicker
- Category: ImpactPack/Util
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

SEGSPicker nodes are designed to process and select segments in a series of subparagraphs. It receives a list of selected items that correspond to the index of the item to be selected, as well as a set of subparagraphs. If backup images are provided, the nodes zoom in to match the backup images, apply a mask to the cropped images, and then return a new set of selected subparagraphs as selected. It plays a key role in simplifying the selection process and ensuring that the output meets the specific requirements of the application.

# Input types
## Required
- picks
    - The 'nicks' parameter is a string that contains a comma-separated list of indexes indicating the parts to be selected. It is essential for the function of the node, as it determines which parts of the input pool are to be processed and returned for output.
    - Comfy dtype: STRING
    - Python dtype: str
- segs
    - The `segs' parameter is the grouping of the objects of the subparagraphs that the node will process. This is the required input, because the node is intended to operate and select these subparagraphs according to different choices.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
## Optional
- fallback_image_opt
    - The `fallback_image_opt' parameter is an optional image, and if this parameter is provided, the node will be used to zoom in. It can influence the output of the node by ensuring that the part is appropriate in size so that it can be further processed or displayed.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- unique_id
    - The `unique_id' parameter is a hidden field that is used within the node to track and manage the segment. It does not directly affect the execution of the node, but it is important to maintain the integrity of the data.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- segs
    - The `segs' output parameter represents a new selection cluster based on the selection of nodes to receive. It is the final result of node processing and is important because it represents the final output for further use or analysis.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[List[SEG], List[SEG]]

# Usage tips
- Infra type: CPU

# Source code
```
class SEGSPicker:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'picks': ('STRING', {'multiline': True, 'dynamicPrompts': False, 'pysssss.autocomplete': False}), 'segs': ('SEGS',)}, 'optional': {'fallback_image_opt': ('IMAGE',)}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('SEGS',)
    OUTPUT_NODE = True
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, picks, segs, fallback_image_opt=None, unique_id=None):
        if fallback_image_opt is not None:
            segs = core.segs_scale_match(segs, fallback_image_opt.shape)
        cands = []
        for seg in segs[1]:
            if seg.cropped_image is not None:
                cropped_image = seg.cropped_image
            elif fallback_image_opt is not None:
                cropped_image = crop_image(fallback_image_opt, seg.crop_region)
            else:
                cropped_image = empty_pil_tensor()
            mask_array = seg.cropped_mask.copy()
            mask_array[mask_array < 0.3] = 0.3
            mask_array = mask_array[None, ..., None]
            cropped_image = cropped_image * mask_array
            cands.append(cropped_image)
        impact.impact_server.segs_picker_map[unique_id] = cands
        pick_ids = set()
        for pick in picks.split(','):
            try:
                pick_ids.add(int(pick) - 1)
            except Exception:
                pass
        new_segs = []
        for i in pick_ids:
            if 0 <= i < len(segs[1]):
                new_segs.append(segs[1][i])
        return ((segs[0], new_segs),)
```