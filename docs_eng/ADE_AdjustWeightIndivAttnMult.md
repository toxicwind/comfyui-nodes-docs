# Documentation
- Class name: WeightAdjustIndivAttnMultNode
- Category: Animate Diff 🎭🅐🅓/ad settings/weight adjust
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The WeightAdjustIndivAttnMultNode class is designed to adjust the weight of attention mechanisms in neural network models individually. It allows fine-tuning of location codes and attention components by multiplying them to specified factors. This node is essential to optimize model performance by adjusting attention processes to meet specific mission needs.

# Input types
## Required
- pe_MULT
    - The p_MULT parameter is essential for scaling position encoded weights. It directly affects the ability of the model to capture the sequence of input, which is essential for tasks such as language translation or text generation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_MULT
    - The antn_MULT parameter adjusts the overall weight of attention to influences the focus of the model on different parts of the input sequence. This is particularly useful for highlighting or diluting certain input features.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_q_MULT
    - The attn_q_MULT parameter is specific to query weights in the attention mechanism and allows changes to be made in the way model queries enter different elements of the data.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_k_MULT
    - The antn_k_MULT parameter influences the key weight in the attention mechanism, which determines how the model aligns the input sequence to the context.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_v_MULT
    - The antn_v_MULT parameter changes the weight of the value in the attention mechanism, which is essential for the model to measure the importance of different input elements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_out_weight_MULT
    - The antn_out_weight_MULT parameter has shrunk the output weight of the attention mechanism, which is important for the ultimate expression of the sequence entered in the model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_out_bias_MULT
    - An attn_out_bias_MULT parameter adjusts the bias of the output of the attention mechanism, which helps to fine-tune model predictions.
    - Comfy dtype: FLOAT
    - Python dtype: float
- other_MULT
    - Other_MULT parameters provide a common scaling factor for other rights reorganizations that are not clearly classified in the model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- print_adjustment
    - The print_adjustment parameter determines whether the node should output a log detailing the adjustments to weights. This is very helpful for debugging and understanding the effects of the adjustments.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- prev_weight_adjust
    - Prev_weight_adjust parameters allow for previous weight adjustment groups to enable nodes to be constructed on the basis of existing adjustments, or to be reset and recommenced.
    - Comfy dtype: WEIGHT_ADJUST
    - Python dtype: Union[AdjustGroup, None]

# Output types
- weight_adjust
    - The output of the node is a WEIGHT_ADJUST object that covers adjustments to model weights. This object can be used to apply these adjustments to models or to fine-tune adjustments in subsequent nodes.
    - Comfy dtype: WEIGHT_ADJUST
    - Python dtype: AdjustGroup

# Usage tips
- Infra type: CPU

# Source code
```
class WeightAdjustIndivAttnMultNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pe_MULT': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 2.0, 'step': 1e-06}), 'attn_MULT': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 2.0, 'step': 1e-06}), 'attn_q_MULT': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 2.0, 'step': 1e-06}), 'attn_k_MULT': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 2.0, 'step': 1e-06}), 'attn_v_MULT': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 2.0, 'step': 1e-06}), 'attn_out_weight_MULT': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 2.0, 'step': 1e-06}), 'attn_out_bias_MULT': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 2.0, 'step': 1e-06}), 'other_MULT': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 2.0, 'step': 1e-06}), 'print_adjustment': ('BOOLEAN', {'default': False})}, 'optional': {'prev_weight_adjust': ('WEIGHT_ADJUST',)}}
    RETURN_TYPES = ('WEIGHT_ADJUST',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/ad settings/weight adjust'
    FUNCTION = 'get_weight_adjust'

    def get_weight_adjust(self, pe_MULT: float, attn_MULT: float, attn_q_MULT: float, attn_k_MULT: float, attn_v_MULT: float, attn_out_weight_MULT: float, attn_out_bias_MULT: float, other_MULT: float, print_adjustment: bool, prev_weight_adjust: AdjustGroup=None):
        if prev_weight_adjust is None:
            prev_weight_adjust = AdjustGroup()
        prev_weight_adjust = prev_weight_adjust.clone()
        adjust = AdjustWeight(pe_MULT=pe_MULT, attn_MULT=attn_MULT, attn_q_MULT=attn_q_MULT, attn_k_MULT=attn_k_MULT, attn_v_MULT=attn_v_MULT, attn_out_weight_MULT=attn_out_weight_MULT, attn_out_bias_MULT=attn_out_bias_MULT, other_MULT=other_MULT, print_adjustment=print_adjustment)
        prev_weight_adjust.add(adjust)
        return (prev_weight_adjust,)
```