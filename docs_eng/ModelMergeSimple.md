# Documentation
- Class name: ModelMergeSimple
- Category: advanced/model_merging
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The Model MergeSimple node is designed to integrate two different models seamlessly into a single, unified module. It does so by combining the key patches of one model with another, allowing a balanced mix based on the specified scale. This node is particularly relevant in advanced applications where models need to be integrated to enhance performance or functionality.

# Input types
## Required
- model1
    - The'model1' parameter represents the main model that will be merged with another model. It is the key element in the consolidation process, as it forms the basis for the final combination model. The implementation and results of the node are largely influenced by the characteristics and structure of'model1'.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- model2
    - The'model2' parameter is a secondary model that provides patches that are to be merged with'model1'. Its role is important because it provides differentiated elements that will be integrated into the final model, thus influencing the functionality and performance of the whole.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ratio
    - The 'ratio' parameter determines the effect of'model2' on the merger model. It is a floating point value ranging from 0.0 to 1.0, of which 1.0 indicates that'model2' has a full impact. This parameter is essential for controlling the balance between the two models in the consolidation process.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- merged_model
    - The'merged_model' output represents a combination of'model1' and'model2' results based on the designated 'ratio'. It covers the combined functions and characteristics of the two models and provides a uniform model for further use or analysis.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class ModelMergeSimple:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model1': ('MODEL',), 'model2': ('MODEL',), 'ratio': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'merge'
    CATEGORY = 'advanced/model_merging'

    def merge(self, model1, model2, ratio):
        m = model1.clone()
        kp = model2.get_key_patches('diffusion_model.')
        for k in kp:
            m.add_patches({k: kp[k]}, 1.0 - ratio, ratio)
        return (m,)
```