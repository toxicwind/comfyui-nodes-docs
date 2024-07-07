# Documentation
- Class name: SweetspotStretchPENode
- Category: Animate Diff 🎭🅐🅓/ad settings/pe adjust
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The Sweetspot StretchPENode class adjusts the maximum effect of the animation by stretching or compressing the peak effect (PE). This node allows fine-tuning of the dynamics of the animation to ensure that the PE is best positioned and scaled to achieve the required visual effect.

# Input types
## Required
- sweetspot
    - The'sweespot' parameter defines the initial length of the peak effect in the animation. This is essential to determine the starting point of the PE adjustment process.
    - Comfy dtype: INT
    - Python dtype: int
- new_sweetspot
    - The 'new_sweetspot' parameter specifies the target length to be adjusted for peak effects. It is a key factor in controlling the final appearance of animated PE.
    - Comfy dtype: INT
    - Python dtype: int
- print_adjustment
    - The 'print_adjustment' parameter is a boolean symbol, and when set to True, the indicator node prints details of the PE adjustment process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- prev_pe_adjust
    - The 'prev_pe_adjust' parameter is an optional previously adjusted group that can be applied to the current PE adjustment. It allows the chain processing of complex animation scenarios to be adjusted.
    - Comfy dtype: PE_ADJUST
    - Python dtype: Union[AdjustGroup, None]

# Output types
- PE_ADJUST
    - The output of a node is an AdjustGroup object that contains new PE adjustments and any previous adjustments. This object is used to apply PE adjustments to animations.
    - Comfy dtype: PE_ADJUST
    - Python dtype: AdjustGroup

# Usage tips
- Infra type: CPU

# Source code
```
class SweetspotStretchPENode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'sweetspot': ('INT', {'default': 16, 'min': 0, 'max': BIGMAX}), 'new_sweetspot': ('INT', {'default': 16, 'min': 0, 'max': BIGMAX}), 'print_adjustment': ('BOOLEAN', {'default': False})}, 'optional': {'prev_pe_adjust': ('PE_ADJUST',)}}
    RETURN_TYPES = ('PE_ADJUST',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/ad settings/pe adjust'
    FUNCTION = 'get_pe_adjust'

    def get_pe_adjust(self, sweetspot: int, new_sweetspot: int, print_adjustment: bool, prev_pe_adjust: AdjustGroup=None):
        if prev_pe_adjust is None:
            prev_pe_adjust = AdjustGroup()
        prev_pe_adjust = prev_pe_adjust.clone()
        adjust = AdjustPE(cap_initial_pe_length=sweetspot, interpolate_pe_to_length=new_sweetspot, print_adjustment=print_adjustment)
        prev_pe_adjust.add(adjust)
        return (prev_pe_adjust,)
```