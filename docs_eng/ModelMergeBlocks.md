# Documentation
- Class name: ModelMergeBlocks
- Category: advanced/model_merging
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The Model MergeBlocks function is designed to integrate two different models into a single structure. It achieves this by cloning the first model and then applying the key patches of the second model according to the specified scale. This process allows for the creation of a hybrid model that combines the advantages of the two original models and enhances their overall predictive capacity.

# Input types
## Required
- model1
    - The parameter'model1' is the first model to be cloned and used as the basis for the consolidation process. It is a key component because it determines the initial structure of the resulting hybrid model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- model2
    - The parameter'model2' represents the extraction of the key patches and their application to the second model of the cloning model. These patches are essential for integrating the features of the second model into the merged model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
## Optional
- input
    - The parameter 'input' is a floating point value used as the default ratio in the consolidation process. It determines the effect of the second model patch on the final model and can be adjusted to fine-tune the consolidation results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- middle
    - The parameter'middle' is another floating point value that can be used to specify different proportions of some patches during the consolidation process. It provides additional control over how models merge.
    - Comfy dtype: FLOAT
    - Python dtype: float
- out
    - The parameter 'out' is a floating point value used to define the output ratio of the consolidation process. It is used to balance the contribution of the original model to the ultimate hybrid model.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- merged_model
    - The output'merged_model' is the result of a consolidation process that combines the features of the input model into a single, tight structure. It represents the top of the node function and provides a new model with an enhanced capability set.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class ModelMergeBlocks:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model1': ('MODEL',), 'model2': ('MODEL',), 'input': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'middle': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'out': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'merge'
    CATEGORY = 'advanced/model_merging'

    def merge(self, model1, model2, **kwargs):
        m = model1.clone()
        kp = model2.get_key_patches('diffusion_model.')
        default_ratio = next(iter(kwargs.values()))
        for k in kp:
            ratio = default_ratio
            k_unet = k[len('diffusion_model.'):]
            last_arg_size = 0
            for arg in kwargs:
                if k_unet.startswith(arg) and last_arg_size < len(arg):
                    ratio = kwargs[arg]
                    last_arg_size = len(arg)
            m.add_patches({k: kp[k]}, 1.0 - ratio, ratio)
        return (m,)
```