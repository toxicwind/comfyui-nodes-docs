# Documentation
- Class name: ModelSamplingStableCascade
- Category: advanced/model
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ModelSamplingStableCascade node is designed to enhance the sampling process for modelling by integrating stable cascades. It allows users to customize the sampling process through the 'patch' method, adapting model behaviour to advanced sampling techniques. This node is critical for users wishing to achieve complex sampling strategies that may improve the quality and diversity of generating output.

# Input types
## Required
- model
    - The `model' parameter is essential because it represents the generation model to be modified by the node. It is the basis for the application of advanced sampling techniques and directly affects the execution of the node and the quality of the output generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- shift
    - The `shift' parameter plays a key role in the sampling variance in the control cascade model. It adjusts the sampling distribution to achieve different levels of detail or diversity in the generation of images, thus significantly influencing the results of nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- modified_model
    - The `modified_model' output represents the production model that has been enhanced by stabilization cascade sampling techniques. It is important because it contains node modifications and is used to further process or directly generate high-quality images.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class ModelSamplingStableCascade:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'shift': ('FLOAT', {'default': 2.0, 'min': 0.0, 'max': 100.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = 'advanced/model'

    def patch(self, model, shift):
        m = model.clone()
        sampling_base = comfy.model_sampling.StableCascadeSampling
        sampling_type = comfy.model_sampling.EPS

        class ModelSamplingAdvanced(sampling_base, sampling_type):
            pass
        model_sampling = ModelSamplingAdvanced(model.model.model_config)
        model_sampling.set_parameters(shift)
        m.add_object_patch('model_sampling', model_sampling)
        return (m,)
```