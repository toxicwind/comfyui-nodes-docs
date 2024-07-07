# Documentation
- Class name: PerpNeg
- Category: _for_testing
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The PerpNeg node is designed to manipulate the sampling process of the model by introducing negative conditions. It does so by changing the noise steps of the model to include negative proportionality factors, which help to lead the production process to more diverse outcomes.

# Input types
## Required
- model
    - Model parameters are essential for the PerpNeg node because they represent the machine learning model that will be modified. The function of the node is directly related to the ability of the model provided and affects how negative conditions are applied during the sampling.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- empty_conditioning
    - The empty condition is the placeholder for the input conditions that the model will use. It plays a key role in the operation of the node, as it determines how the negative ratio is applied during the sampling process and affects the final output.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
## Optional
- neg_scale
    - The neg_scale parameter is used to control the intensity of negative conditionality effects. It is particularly important because it directly affects the ability of nodes to diversify sampling results and provides a balance between positive and negative impacts.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- model
    - The output model of the PerpNeg node is a modified version of the input model, which now includes negative conditions. This modified model can then be used for sampling, which may lead to more diverse and creative results.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class PerpNeg:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'empty_conditioning': ('CONDITIONING',), 'neg_scale': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = '_for_testing'

    def patch(self, model, empty_conditioning, neg_scale):
        m = model.clone()
        nocond = comfy.sampler_helpers.convert_cond(empty_conditioning)

        def cfg_function(args):
            model = args['model']
            noise_pred_pos = args['cond_denoised']
            noise_pred_neg = args['uncond_denoised']
            cond_scale = args['cond_scale']
            x = args['input']
            sigma = args['sigma']
            model_options = args['model_options']
            nocond_processed = comfy.samplers.encode_model_conds(model.extra_conds, nocond, x, x.device, 'negative')
            (noise_pred_nocond,) = comfy.samplers.calc_cond_batch(model, [nocond_processed], x, sigma, model_options)
            cfg_result = x - perp_neg(x, noise_pred_pos, noise_pred_neg, noise_pred_nocond, neg_scale, cond_scale)
            return cfg_result
        m.set_model_sampler_cfg_function(cfg_function)
        return (m,)
```