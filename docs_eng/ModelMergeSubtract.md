# Documentation
- Class name: ModelSubtract
- Category: advanced/model_merging
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ModelSubtrade node's `merge' method is designed to combine two models by subtracting a model's key patches and using specified multipliers. It performs a complex operation that integrates the characteristics of the two models and allows fine adjustments to their contribution.

# Input types
## Required
- model1
    - The parameter'model1' is the main model from which to subtract patches. It plays a key role in the consolidation process, as it forms the basic structure for the generation of models.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- model2
    - The parameter'model2' provides key patches that will be subtracted from the model1. It is essential to determine the particular differences that will be integrated into the final model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
## Optional
- multiplier
    - The parameter'multiplier' adjusts the strength of the patch subtracted from model1. It's important because it allows fine-tuning of the model2 effect on the merger model.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- merged_model
    - The output'merged_model' represents the results of the model consolidation process. It covers a combination of two input models and provides a new model with adjusted properties.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class ModelSubtract:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model1': ('MODEL',), 'model2': ('MODEL',), 'multiplier': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'merge'
    CATEGORY = 'advanced/model_merging'

    def merge(self, model1, model2, multiplier):
        m = model1.clone()
        kp = model2.get_key_patches('diffusion_model.')
        for k in kp:
            m.add_patches({k: kp[k]}, -multiplier, multiplier)
        return (m,)
```