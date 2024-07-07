# Documentation
- Class name: ModelAdd
- Category: advanced/model_merging
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ModelAdd node's `merge' method is designed to combine two different models into a single, unified model. By cloning a model, it integrates the key patches of the second model to ensure that the models produced reflect the characteristics of the two original models. This process is essential for integrating advanced applications of model functions.

# Input types
## Required
- model1
    - The'model1' parameter is the first model to be cloned and to be used as a basis for the consolidation process. It is an essential component, as it determines the initial structure and attributes of the eventual merger model.
    - Comfy dtype: MODEL
    - Python dtype: ModelPatcher or a similar type representing a model structure
- model2
    - The'model2' parameter represents the second model from which the key patches will be extracted and applied to'model1'. These patches help to enhance the merged model through additional functionality and capacity.
    - Comfy dtype: MODEL
    - Python dtype: ModelPatcher or a similar type representing a model structure

# Output types
- merged_model
    - The output of the'merge' method is a single model that combines input models. The model now covers the combined advantages and functions of the two original models.
    - Comfy dtype: MODEL
    - Python dtype: ModelPatcher or a similar type representing the merged model structure

# Usage tips
- Infra type: CPU

# Source code
```
class ModelAdd:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model1': ('MODEL',), 'model2': ('MODEL',)}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'merge'
    CATEGORY = 'advanced/model_merging'

    def merge(self, model1, model2):
        m = model1.clone()
        kp = model2.get_key_patches('diffusion_model.')
        for k in kp:
            m.add_patches({k: kp[k]}, 1.0, 1.0)
        return (m,)
```