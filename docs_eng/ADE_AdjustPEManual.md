# Documentation
- Class name: ManualAdjustPENode
- Category: Animate Diff 🎭🅐🅓/ad settings/pe adjust
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The node is designed to manually adjust the parameters associated with the PE (personal energy) in the animation workflow. It allows fine-tuning of the initial and final PE index, inserting values to a specific length, and provides options for printing adjustments. Node plays a key role in defining the energy level in the animation to achieve the desired effect.

# Input types
## Required
- cap_initial_pe_length
    - This parameter defines the initial length of the PE to be limited, which is essential for controlling the initial energy level in the animation. It directly affects energy dynamics and the overall sense of the animation sequence.
    - Comfy dtype: INT
    - Python dtype: int
- interpolate_pe_to_length
    - Plug-in parameters allow PE to smooth the transition to a specified length, ensuring a harmonious flow of energy in animation. This is a key factor in achieving natural progress in energy levels.
    - Comfy dtype: INT
    - Python dtype: int
- initial_pe_idx_offset
    - This deviation parameter is used to adjust the beginning index of the PE, which significantly changes the initial energy state of the animation. It provides a method of fine-tuning energy input at the beginning of the sequence.
    - Comfy dtype: INT
    - Python dtype: int
- final_pe_idx_offset
    - The final PE index deviation is essential to define the end-energy state of the animation. It allows accurate control over the resolution of energy at the end of the animation sequence.
    - Comfy dtype: INT
    - Python dtype: int
- print_adjustment
    - The Boolean logo determines whether the adjustment made to the PE will be printed. This is very useful for debugging and understanding the impact of the adjustment on the animation.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- prev_pe_adjust
    - The former PE adjustment group provides a method of building on existing adjustments that allows for cumulative effects in animations. It is an optional parameter that enhances the flexibility of node functions.
    - Comfy dtype: PE_ADJUST
    - Python dtype: AdjustGroup

# Output types
- PE_ADJUST
    - The output of the node is an AdjustGroup object that contains a manual adjustment of the PE. It is important because it directly affects the final energy level and the overall results of the animation.
    - Comfy dtype: PE_ADJUST
    - Python dtype: AdjustGroup

# Usage tips
- Infra type: CPU

# Source code
```
class ManualAdjustPENode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'cap_initial_pe_length': ('INT', {'default': 0, 'min': 0, 'step': 1}), 'interpolate_pe_to_length': ('INT', {'default': 0, 'min': 0, 'step': 1}), 'initial_pe_idx_offset': ('INT', {'default': 0, 'min': 0, 'step': 1}), 'final_pe_idx_offset': ('INT', {'default': 0, 'min': 0, 'step': 1}), 'print_adjustment': ('BOOLEAN', {'default': False})}, 'optional': {'prev_pe_adjust': ('PE_ADJUST',)}}
    RETURN_TYPES = ('PE_ADJUST',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/ad settings/pe adjust'
    FUNCTION = 'get_pe_adjust'

    def get_pe_adjust(self, cap_initial_pe_length: int, interpolate_pe_to_length: int, initial_pe_idx_offset: int, final_pe_idx_offset: int, print_adjustment: bool, prev_pe_adjust: AdjustGroup=None):
        if prev_pe_adjust is None:
            prev_pe_adjust = AdjustGroup()
        prev_pe_adjust = prev_pe_adjust.clone()
        adjust = AdjustPE(cap_initial_pe_length=cap_initial_pe_length, interpolate_pe_to_length=interpolate_pe_to_length, initial_pe_idx_offset=initial_pe_idx_offset, final_pe_idx_offset=final_pe_idx_offset, print_adjustment=print_adjustment)
        prev_pe_adjust.add(adjust)
        return (prev_pe_adjust,)
```