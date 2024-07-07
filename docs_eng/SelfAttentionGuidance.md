# Documentation
- Class name: SelfAttentionGuidance
- Category: _for_testing
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The SelfAttentionGuidance class is designed to enhance the focus mechanism in the model by providing self-direction-based guidance. It can improve the model’s ability to focus on the relevant parts of the data input by adapting the model’s attention to the additional context.

# Input types
## Required
- model
    - Model parameters are essential for the SelfAttentionGuidance node because they represent the machine learning model that the node will modify and guide. The function of the node is directly linked to the structure and capacity of the model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- scale
    - The scale parameter adjusts from attention guidance on the impact on model output. It is a key component that allows the impact of the microregulating point on the model attention process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- blur_sigma
    - The blur_sigma parameter defines the degree of ambiguity applied in the post-configuration function of the model. It is important because it affects the visual quality and preservation of the details of the model output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- modified_model
    - The modified_model output is the result of the application of the SelfAttentionGuidance patch to the input model. It represents a model with an enhanced attention mechanism for further use or evaluation.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class SelfAttentionGuidance:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'scale': ('FLOAT', {'default': 0.5, 'min': -2.0, 'max': 5.0, 'step': 0.1}), 'blur_sigma': ('FLOAT', {'default': 2.0, 'min': 0.0, 'max': 10.0, 'step': 0.1})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = '_for_testing'

    def patch(self, model, scale, blur_sigma):
        m = model.clone()
        attn_scores = None

        def attn_and_record(q, k, v, extra_options):
            nonlocal attn_scores
            heads = extra_options['n_heads']
            cond_or_uncond = extra_options['cond_or_uncond']
            b = q.shape[0] // len(cond_or_uncond)
            if 1 in cond_or_uncond:
                uncond_index = cond_or_uncond.index(1)
                (out, sim) = attention_basic_with_sim(q, k, v, heads=heads)
                n_slices = heads * b
                attn_scores = sim[n_slices * uncond_index:n_slices * (uncond_index + 1)]
                return out
            else:
                return optimized_attention(q, k, v, heads=heads)

        def post_cfg_function(args):
            nonlocal attn_scores
            uncond_attn = attn_scores
            sag_scale = scale
            sag_sigma = blur_sigma
            sag_threshold = 1.0
            model = args['model']
            uncond_pred = args['uncond_denoised']
            uncond = args['uncond']
            cfg_result = args['denoised']
            sigma = args['sigma']
            model_options = args['model_options']
            x = args['input']
            if min(cfg_result.shape[2:]) <= 4:
                return cfg_result
            degraded = create_blur_map(uncond_pred, uncond_attn, sag_sigma, sag_threshold)
            degraded_noised = degraded + x - uncond_pred
            (sag,) = comfy.samplers.calc_cond_batch(model, [uncond], degraded_noised, sigma, model_options)
            return cfg_result + (degraded - sag) * sag_scale
        m.set_model_sampler_post_cfg_function(post_cfg_function, disable_cfg1_optimization=True)
        m.set_model_attn1_replace(attn_and_record, 'middle', 0, 0)
        return (m,)
```