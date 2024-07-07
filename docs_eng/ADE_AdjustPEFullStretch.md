# Documentation
- Class name: FullStretchPENode
- Category: Animate Diff 🎭🅐🅓/ad settings/pe adjust
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The FullStretchPENode class is designed to modify the character of the private part of the role in the animation. It does so by applying various adjustments, such as stretching, deflecting and limiting the initial length. The main function of the node is to enhance the visual effects and details of the animation through these changes.

# Input types
## Required
- pe_stretch
    - The 'pe_stretch' parameter controls the degree of stretching applied to the private part of the role. This is essential to define the visual scope and detail of the animation in the area.
    - Comfy dtype: INT
    - Python dtype: int
- print_adjustment
    - The 'print_adjustment' parameter decides whether to export the adjustment details to the console. This is useful for debugging and understanding the adjustments that are being made.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- prev_pe_adjust
    - The 'prev_pe_adjust' parameter allows adjustments to previous private settings. This is important to improve animations based on previous adjustments.
    - Comfy dtype: PE_ADJUST
    - Python dtype: Union[AdjustGroup, None]

# Output types
- PE_ADJUST
    - Output 'PE_ADJUST' represents the final set of adjustments made to character privacy. It covers visual enhancement applied to animations.
    - Comfy dtype: PE_ADJUST
    - Python dtype: AdjustGroup

# Usage tips
- Infra type: CPU

# Source code
```
class FullStretchPENode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pe_stretch': ('INT', {'default': 0, 'min': 0, 'max': BIGMAX}), 'print_adjustment': ('BOOLEAN', {'default': False})}, 'optional': {'prev_pe_adjust': ('PE_ADJUST',)}}
    RETURN_TYPES = ('PE_ADJUST',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/ad settings/pe adjust'
    FUNCTION = 'get_pe_adjust'

    def get_pe_adjust(self, pe_stretch: int, print_adjustment: bool, prev_pe_adjust: AdjustGroup=None):
        if prev_pe_adjust is None:
            prev_pe_adjust = AdjustGroup()
        prev_pe_adjust = prev_pe_adjust.clone()
        adjust = AdjustPE(motion_pe_stretch=pe_stretch, print_adjustment=print_adjustment)
        prev_pe_adjust.add(adjust)
        return (prev_pe_adjust,)
```