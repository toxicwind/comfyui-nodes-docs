# Documentation
- Class name: WeightAdjustAllMultNode
- Category: Animate Diff 🎭🅐🅓/ad settings/weight adjust
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The `get_weight_adjust' method of the WeightAdjustAllMultNode class is designed to apply a uniform multiplier to ownership in the model so as to fine-tune its parameters without changing the bottom structure. It is a key tool for adjusting the overall size of the weight of the model, particularly for scenarios that require calibration of the model according to different input ranges or sensitivity levels.

# Input types
## Required
- all_MULT
    - The parameter 'all_MULT' is essential for determining the uniform multiplier that will be applied to the weight of ownership in the model. It allows a simple scaling of the weight of the model, which can significantly influence the performance and behaviour of the model. This parameter is critical for adjusting the sensitivity of the model to input data.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- print_adjustment
    - Parameter 'print_adjustment' is an optional sign that allows details of recording weight adjustments when set to True. This is very useful for users who want to track adjustments to model weights during debugging or during the adjustment process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- prev_weight_adjust
    - Parameters'prev_weight_adjust' allow the user to provide a previous weight adjustment group, which will then be constructed on that basis. This is very useful for incremental adjustments, some of which can continue from the pre-established state, rather than starting from the beginning.
    - Comfy dtype: WEIGHT_ADJUST
    - Python dtype: AdjustGroup

# Output types
- WEIGHT_ADJUST
    - The output of the 'get_weight_adjust' method is a 'WEIGHT_ADJUST' object, which covers adjustments to model weights. This object is important because it represents the state of update of model parameters after weight adjustment process and is prepared for further model training or reasoning.
    - Comfy dtype: WEIGHT_ADJUST
    - Python dtype: AdjustGroup

# Usage tips
- Infra type: CPU

# Source code
```
class WeightAdjustAllMultNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'all_MULT': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 2.0, 'step': 1e-06}), 'print_adjustment': ('BOOLEAN', {'default': False})}, 'optional': {'prev_weight_adjust': ('WEIGHT_ADJUST',)}}
    RETURN_TYPES = ('WEIGHT_ADJUST',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/ad settings/weight adjust'
    FUNCTION = 'get_weight_adjust'

    def get_weight_adjust(self, all_MULT: float, print_adjustment: bool, prev_weight_adjust: AdjustGroup=None):
        if prev_weight_adjust is None:
            prev_weight_adjust = AdjustGroup()
        prev_weight_adjust = prev_weight_adjust.clone()
        adjust = AdjustWeight(all_MULT=all_MULT, print_adjustment=print_adjustment)
        prev_weight_adjust.add(adjust)
        return (prev_weight_adjust,)
```