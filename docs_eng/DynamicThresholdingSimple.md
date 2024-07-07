# Documentation
- Class name: DynamicThresholdingSimpleComfyNode
- Category: advanced/mcmonkey
- Output node: False
- Repo Ref: https://github.com/mcmonkeyprojects/sd-dynamic-thresholding

The node is set on the basis of the thresholds of the specified percentage and the zoom factor dynamic adjustment model, enabling model output to match the desired characteristics.

# Input types
## Required
- model
    - Model parameters are essential because they define the basic structure and parameters of the neural network that will be set for the dynamic threshold of its output.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- mimic_scale
    - This parameter adjusts the extent to which the model output is modified to match the characteristics of the target, which has a significant impact on the overall effect of the node.
    - Comfy dtype: FLOAT
    - Python dtype: float
- threshold_percentile
    - The threshold percentage sets the relative threshold for adjusting model output, which is essential for achieving the desired output distribution.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- model
    - The output model is a modified version of the input model and now has threshold parameters adjusted to the characteristics of the specified target.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class DynamicThresholdingSimpleComfyNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'mimic_scale': ('FLOAT', {'default': 7.0, 'min': 0.0, 'max': 100.0, 'step': 0.5}), 'threshold_percentile': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = 'advanced/mcmonkey'

    def patch(self, model, mimic_scale, threshold_percentile):
        dynamic_thresh = DynThresh(mimic_scale, threshold_percentile, 'CONSTANT', 0, 'CONSTANT', 0, 0, 0, 999, False, 'MEAN', 'AD', 1)

        def sampler_dyn_thresh(args):
            input = args['input']
            cond = input - args['cond']
            uncond = input - args['uncond']
            cond_scale = args['cond_scale']
            time_step = model.model.model_sampling.timestep(args['sigma'])
            time_step = time_step[0].item()
            dynamic_thresh.step = 999 - time_step
            return input - dynamic_thresh.dynthresh(cond, uncond, cond_scale, None)
        m = model.clone()
        m.set_model_sampler_cfg_function(sampler_dyn_thresh)
        return (m,)
```