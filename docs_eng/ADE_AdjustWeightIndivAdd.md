# Documentation
- Class name: WeightAdjustIndivAddNode
- Category: Animate Diff 🎭🅐🅓/ad settings/weight adjust
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

WeightAdjustIndivAddNode aims to adjust the weight of the model individually by adding specific values to different types of parameters. It encapsulates the logic of the changes made according to the specified criteria and ensures that the adjustments are applied in a structured and modular manner.

# Input types
## Required
- pe_ADD
    - The p_ADD parameter allows for the resetting of position encoded weights. It plays a crucial role in fine-tuning the model's understanding of the input sequence structure, which is essential for tasks that depend on the sequence of elements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_ADD
    - The antn_ADD parameter is used to modify the weight of the attention mechanism. By adjusting the parameter, it enhances the ability of different parts of the model's focus input and may help to improve the performance of the model in tasks that require a fine understanding of the context.
    - Comfy dtype: FLOAT
    - Python dtype: float
- other_ADD
    - The other_ADD parameter is used to adjust weights that do not fall within the predefined category. It provides flexibility to fine-tune models to cover a wider range of adjustments that are not covered by other parameters.
    - Comfy dtype: FLOAT
    - Python dtype: float
- print_adjustment
    - This is very useful for debugging and understanding the effects of the adjustment on model behaviour.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- prev_weight_adjust
    - The prev_weight_adjust parameter is an optional pre-adjustment group that can be applied to the model. This allows for the continuation of a series of adjustments or the application of a predefined set of changes.
    - Comfy dtype: WEIGHT_ADJUST
    - Python dtype: AdjustGroup

# Output types
- weight_adjust
    - The output of WeightAdjustIndivAddNode is a WEIGHT_ADJUST object that represents a collective adjustment of model weights. This object can be used to further refine the model or apply the adjustment to another model example.
    - Comfy dtype: WEIGHT_ADJUST
    - Python dtype: AdjustGroup

# Usage tips
- Infra type: CPU

# Source code
```
class WeightAdjustIndivAddNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pe_ADD': ('FLOAT', {'default': 0.0, 'min': -2.0, 'max': 2.0, 'step': 1e-06}), 'attn_ADD': ('FLOAT', {'default': 0.0, 'min': -2.0, 'max': 2.0, 'step': 1e-06}), 'other_ADD': ('FLOAT', {'default': 0.0, 'min': -2.0, 'max': 2.0, 'step': 1e-06}), 'print_adjustment': ('BOOLEAN', {'default': False})}, 'optional': {'prev_weight_adjust': ('WEIGHT_ADJUST',)}}
    RETURN_TYPES = ('WEIGHT_ADJUST',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/ad settings/weight adjust'
    FUNCTION = 'get_weight_adjust'

    def get_weight_adjust(self, pe_ADD: float, attn_ADD: float, other_ADD: float, print_adjustment: bool, prev_weight_adjust: AdjustGroup=None):
        if prev_weight_adjust is None:
            prev_weight_adjust = AdjustGroup()
        prev_weight_adjust = prev_weight_adjust.clone()
        adjust = AdjustWeight(pe_ADD=pe_ADD, attn_ADD=attn_ADD, other_ADD=other_ADD, print_adjustment=print_adjustment)
        prev_weight_adjust.add(adjust)
        return (prev_weight_adjust,)
```