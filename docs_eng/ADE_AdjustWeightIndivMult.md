# Documentation
- Class name: WeightAdjustIndivMultNode
- Category: Animate Diff 🎭🅐🅓/ad settings/weight adjust
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The WeightAdjustIndivMultNode class aims to modify the weight of the model individually by multiplying it. It provides a method by which the weights of different parts of the model can be adjusted according to predefined multipliers (e.g. p_MULT, antn_MULT and other_MULT), allowing fine-tuning of model parameters without changing their underlying structure. If necessary, the node also supports printing the details of the adjustment, providing transparency in the weight modification process.

# Input types
## Required
- pe_MULT
    - The p_MULT parameter is a multiplier to adjust the weight of the model associated with the position encoding (PE). It plays a key role in fine-tuning the sensitivity of the model to input the sequence of elements, which can significantly influence the performance of the model in tasks that depend on the sequence.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_MULT
    - The antn_MULT parameter is a multiplier of the weight of the attention mechanism in the model. By adjusting this value, the effect of the attention mechanism on model output can be controlled, which is essential for a task that requires a careful understanding of the relationship between context and elements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- other_MULT
    - The other_MULT parameter is a generic multiplier that can be applied to other weights in the model that are not covered by p_MULT or attn_MULT. It provides flexibility to adjust model behaviour in specific cases or experimental settings.
    - Comfy dtype: FLOAT
    - Python dtype: float
- print_adjustment
    - The print_adjustment parameter is a boolean symbol that enables records weight adjustment details when set as True. This is useful for developers to track and validate changes to model weights during the adjustment process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- prev_weight_adjust
    - The prev_weight_adjust parameter allows for previous weight adjustment groups to be constructed or modified on the basis of the existing weight adjustment. This parameter is particularly useful when it is necessary to retain the status of the previous adjustment step in the iterative adjustment and to further improve it.
    - Comfy dtype: WEIGHT_ADJUST
    - Python dtype: AdjustGroup

# Output types
- WEIGHT_ADJUST
    - The output of WeightAdjustIndivMultNode is an AdjustGroup object that seals the weighting of the results applied to the model. This object can be used to further refine the model or apply the adjustment to another example of the model.
    - Comfy dtype: WEIGHT_ADJUST
    - Python dtype: AdjustGroup

# Usage tips
- Infra type: CPU

# Source code
```
class WeightAdjustIndivMultNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pe_MULT': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 2.0, 'step': 1e-06}), 'attn_MULT': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 2.0, 'step': 1e-06}), 'other_MULT': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 2.0, 'step': 1e-06}), 'print_adjustment': ('BOOLEAN', {'default': False})}, 'optional': {'prev_weight_adjust': ('WEIGHT_ADJUST',)}}
    RETURN_TYPES = ('WEIGHT_ADJUST',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/ad settings/weight adjust'
    FUNCTION = 'get_weight_adjust'

    def get_weight_adjust(self, pe_MULT: float, attn_MULT: float, other_MULT: float, print_adjustment: bool, prev_weight_adjust: AdjustGroup=None):
        if prev_weight_adjust is None:
            prev_weight_adjust = AdjustGroup()
        prev_weight_adjust = prev_weight_adjust.clone()
        adjust = AdjustWeight(pe_MULT=pe_MULT, attn_MULT=attn_MULT, other_MULT=other_MULT, print_adjustment=print_adjustment)
        prev_weight_adjust.add(adjust)
        return (prev_weight_adjust,)
```