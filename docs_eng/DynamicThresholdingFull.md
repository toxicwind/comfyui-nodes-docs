# Documentation
- Class name: DynamicThresholdingComfyNode
- Category: advanced/mcmonkey
- Output node: False
- Repo Ref: https://github.com/mcmonkeyprojects/sd-dynamic-thresholding

The node dynamically adjusts the model's threshold process to achieve the desired imitation level and controls the output generated. It refines the model's response by explaining the scale and variation measures, thereby optimizing the generation process according to the specified parameters.

# Input types
## Required
- model
    - Model parameters are essential and define the basis for node operations. They are the basis for the application of dynamic threshold processing processes, the characteristics of which directly affect the output results.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- mimic_scale
    - The mimic_scale parameter is essential for controlling imitation in the output. It adjusts the intensity of the threshold processing process, thus affecting the final quality and resemblance of the content generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- threshold_percentile
    - The xreshold_percentile parameter plays an important role in determining the variability of the content that is generated. It sets a threshold based on the bits, which are used to control the dynamic scaling of features.
    - Comfy dtype: FLOAT
    - Python dtype: float
- mimic_mode
    - The mimic_mode parameter sets out the scaling pattern during the threshold processing process. It plays a key role in defining how the model adapts to input and adjusts its output accordingly.
    - Comfy dtype: ENUM
    - Python dtype: str
- cfg_mode
    - The cfg_mode parameter specifies the configuration model for the dynamic threshold. It is essential to guide how nodes interpret and apply the zoom factors for feature adjustments.
    - Comfy dtype: ENUM
    - Python dtype: str

# Output types
- model
    - The output model is the result of a dynamic threshold processing process. It has been optimized and adjusted to input parameters, providing optimization and controlled output that meets desired imitation and quality standards.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class DynamicThresholdingComfyNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'mimic_scale': ('FLOAT', {'default': 7.0, 'min': 0.0, 'max': 100.0, 'step': 0.5}), 'threshold_percentile': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'mimic_mode': (DynThresh.Modes,), 'mimic_scale_min': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 100.0, 'step': 0.5}), 'cfg_mode': (DynThresh.Modes,), 'cfg_scale_min': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 100.0, 'step': 0.5}), 'sched_val': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01}), 'separate_feature_channels': (['enable', 'disable'],), 'scaling_startpoint': (DynThresh.Startpoints,), 'variability_measure': (DynThresh.Variabilities,), 'interpolate_phi': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = 'advanced/mcmonkey'

    def patch(self, model, mimic_scale, threshold_percentile, mimic_mode, mimic_scale_min, cfg_mode, cfg_scale_min, sched_val, separate_feature_channels, scaling_startpoint, variability_measure, interpolate_phi):
        dynamic_thresh = DynThresh(mimic_scale, threshold_percentile, mimic_mode, mimic_scale_min, cfg_mode, cfg_scale_min, sched_val, 0, 999, separate_feature_channels == 'enable', scaling_startpoint, variability_measure, interpolate_phi)

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