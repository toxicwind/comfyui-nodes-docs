# Documentation
- Class name: WeightAdjustAllAddNode
- Category: Animate Diff 🎭🅐🅓/ad settings/weight adjust
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

In the `WeightAdjustAllAddNode'category, the `get_weight_adjust'method is designed to apply uniform adjustments to ownership weights in models. This is achieved by accepting an added value and selectively printing the details of adjustments. It is essential that this method fine-tunes the weight of models in animating differences, ensuring that adjustments are applied consistently throughout the model.

# Input types
## Required
- all_ADD
    - The parameter `all_ADD' specifies the amount of ownership weight in the model that should be adjusted. This is a key input because it directly affects the size of the weight adjustment and thus the performance of the adjusted model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- print_adjustment
    - The logo `print_adjustment'determines whether to print details of weighting adjustments. This is useful for debugging or monitoring adjustments to model weights.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- prev_weight_adjust
    - The parameter `prev_weight_adjust'allows the provision of prior weight adjustment groups that can be used to create or modify existing weight adjustments. This parameter is optional, but it enhances the flexibility of the weight adjustment process.
    - Comfy dtype: WEIGHT_ADJUST
    - Python dtype: AdjustGroup

# Output types
- WEIGHT_ADJUST
    - The output of the `get_weight_adjust'method is an `AdjustGroup'object that contains a weighting of the result after the application of the specified `all_AD' value. This object is important because it represents an update of the weight of the adjusted model.
    - Comfy dtype: WEIGHT_ADJUST
    - Python dtype: AdjustGroup

# Usage tips
- Infra type: CPU

# Source code
```
class WeightAdjustAllAddNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'all_ADD': ('FLOAT', {'default': 0.0, 'min': -2.0, 'max': 2.0, 'step': 1e-06}), 'print_adjustment': ('BOOLEAN', {'default': False})}, 'optional': {'prev_weight_adjust': ('WEIGHT_ADJUST',)}}
    RETURN_TYPES = ('WEIGHT_ADJUST',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/ad settings/weight adjust'
    FUNCTION = 'get_weight_adjust'

    def get_weight_adjust(self, all_ADD: float, print_adjustment: bool, prev_weight_adjust: AdjustGroup=None):
        if prev_weight_adjust is None:
            prev_weight_adjust = AdjustGroup()
        prev_weight_adjust = prev_weight_adjust.clone()
        adjust = AdjustWeight(all_ADD=all_ADD, print_adjustment=print_adjustment)
        prev_weight_adjust.add(adjust)
        return (prev_weight_adjust,)
```