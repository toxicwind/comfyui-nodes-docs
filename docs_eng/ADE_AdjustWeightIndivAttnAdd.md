# Documentation
- Class name: WeightAdjustIndivAttnAddNode
- Category: Animate Diff 🎭🅐🅓/ad settings/weight adjust
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The WeightAdjustIndivAttnAddNode class is designed to adjust the weight of attention mechanisms in neural network models. It provides a method to fine-tune attention parameters, such as query (q), key (k) and value (v) vectors, and output weights and deviations. This node allows these parameters to be adapted to specific cases or experimental requirements to customize model behaviour.

# Input types
## Required
- pe_ADD
    - The p_ADD parameter is used to adjust the position encoded weight of the model. It plays a crucial role in interpreting the sequence of the model, which may significantly affect the performance of the model in tasks that are sensitive to the order of input data.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_ADD
    - The antn_ADD parameter allows adjustment of the general focus weight within the model. This helps to highlight or dilute certain aspects of the input data, thereby influencing the focus of the model and may enhance its ability to capture relevant information.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_q_ADD
    - The attn_q_ADD parameter is specific to the query weight of the attention mechanism. By fine-tuning the parameter, the model can be guided to pay more attention to certain input features, which are particularly useful for tasks that require in-depth understanding of the context.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_k_ADD
    - The antn_k_ADD parameter is responsible for adjusting the key weights of the attention mechanism. Modifying this parameter changes the ability of the model to align with the relevant parts of the input data, which is essential for a task that relies on accurate contextual alignment.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_v_ADD
    - The antn_v_ADD parameter influences the weight of the value in the attention mechanism. It is important for determining the contribution of each input element to the final output, which is essential for the task of accurately indicating the input data.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_out_weight_ADD
    - Attn_out_weight_ADD parameters are used to adjust the output weights of the attention mechanism. This helps to refine the output of the model and bring it closer to the desired results, which is particularly important for the task of requiring a high level of accuracy in the output layer.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_out_bias_ADD
    - Attn_out_bias_ADD parameters allow for adjustment of output deviations within the attention mechanism. This is useful for adjusting model predictions to better match expected results, especially for tasks requiring precise output adjustments.
    - Comfy dtype: FLOAT
    - Python dtype: float
- other_ADD
    - The other_ADD parameter provides general adjustments to other weights not specified in the model. It can be used to make extensive adjustments to model behaviour that are not specific to the other parameters.
    - Comfy dtype: FLOAT
    - Python dtype: float
- print_adjustment
    - The print_adjustment parameter is a boolean symbol that enables detailed information on record weight adjustments when set to True. This is useful for debugging and understanding how adjustments affect model parameters.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- prev_weight_adjust
    - The prev_weight_adjust parameter is an optional pre-weight adjustment group that can be applied to the model. This allows for the continuation of a series of adjustments or the application of a predefined set of adjustments.
    - Comfy dtype: WEIGHT_ADJUST
    - Python dtype: Union[AdjustGroup, None]

# Output types
- weight_adjust
    - The output of weight_adjust provides the results of the application of various attention adjustments to the model. It contains the combined effect of all input parameters on the weight of the model and provides a structured representation of the adjusted weight.
    - Comfy dtype: WEIGHT_ADJUST
    - Python dtype: AdjustGroup

# Usage tips
- Infra type: CPU

# Source code
```
class WeightAdjustIndivAttnAddNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pe_ADD': ('FLOAT', {'default': 0.0, 'min': -2.0, 'max': 2.0, 'step': 1e-06}), 'attn_ADD': ('FLOAT', {'default': 0.0, 'min': -2.0, 'max': 2.0, 'step': 1e-06}), 'attn_q_ADD': ('FLOAT', {'default': 0.0, 'min': -2.0, 'max': 2.0, 'step': 1e-06}), 'attn_k_ADD': ('FLOAT', {'default': 0.0, 'min': -2.0, 'max': 2.0, 'step': 1e-06}), 'attn_v_ADD': ('FLOAT', {'default': 0.0, 'min': -2.0, 'max': 2.0, 'step': 1e-06}), 'attn_out_weight_ADD': ('FLOAT', {'default': 0.0, 'min': -2.0, 'max': 2.0, 'step': 1e-06}), 'attn_out_bias_ADD': ('FLOAT', {'default': 0.0, 'min': -2.0, 'max': 2.0, 'step': 1e-06}), 'other_ADD': ('FLOAT', {'default': 0.0, 'min': -2.0, 'max': 2.0, 'step': 1e-06}), 'print_adjustment': ('BOOLEAN', {'default': False})}, 'optional': {'prev_weight_adjust': ('WEIGHT_ADJUST',)}}
    RETURN_TYPES = ('WEIGHT_ADJUST',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/ad settings/weight adjust'
    FUNCTION = 'get_weight_adjust'

    def get_weight_adjust(self, pe_ADD: float, attn_ADD: float, attn_q_ADD: float, attn_k_ADD: float, attn_v_ADD: float, attn_out_weight_ADD: float, attn_out_bias_ADD: float, other_ADD: float, print_adjustment: bool, prev_weight_adjust: AdjustGroup=None):
        if prev_weight_adjust is None:
            prev_weight_adjust = AdjustGroup()
        prev_weight_adjust = prev_weight_adjust.clone()
        adjust = AdjustWeight(pe_ADD=pe_ADD, attn_ADD=attn_ADD, attn_q_ADD=attn_q_ADD, attn_k_ADD=attn_k_ADD, attn_v_ADD=attn_v_ADD, attn_out_weight_ADD=attn_out_weight_ADD, attn_out_bias_ADD=attn_out_bias_ADD, other_ADD=other_ADD, print_adjustment=print_adjustment)
        prev_weight_adjust.add(adjust)
        return (prev_weight_adjust,)
```