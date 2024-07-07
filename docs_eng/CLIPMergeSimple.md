# Documentation
- Class name: CLIPMergeSimple
- Category: advanced/model_merging
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The CLIP MergeSimple node is designed to integrate the two stand-alone CLIP models seamlessly into a single expression. It does so by combining the key patches of one model into another, which determines the effect of each model on the final combined output, based on a given ratio. This node is particularly suitable for advanced applications, where the insights of the two models need to be combined without starting to train a new model from the beginning.

# Input types
## Required
- clip1
    - The first CLIP model that will be used as the basis for the merger. As its main structure, the patches of the second model will be integrated.
    - Comfy dtype: CLIP
    - Python dtype: CLIP model object
- clip2
    - The key patch will be merged into the second CLIP model in the base model. The selection of the patch will help to consolidate the final results of the model.
    - Comfy dtype: CLIP
    - Python dtype: CLIP model object
- ratio
    - The scale parameters control the impact of the patches of the second model on the merged model. The higher ratio increases the impact of the second model, while the lower ratio favours the properties of the first model.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- merged_clip
    - The output of the CLIP MergeSimple node is a consolidated CLIP model, which contains a combination of two input models and provides a more refined representation of downstream tasks.
    - Comfy dtype: CLIP
    - Python dtype: CLIP model object

# Usage tips
- Infra type: CPU

# Source code
```
class CLIPMergeSimple:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip1': ('CLIP',), 'clip2': ('CLIP',), 'ratio': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('CLIP',)
    FUNCTION = 'merge'
    CATEGORY = 'advanced/model_merging'

    def merge(self, clip1, clip2, ratio):
        m = clip1.clone()
        kp = clip2.get_key_patches()
        for k in kp:
            if k.endswith('.position_ids') or k.endswith('.logit_scale'):
                continue
            m.add_patches({k: kp[k]}, 1.0 - ratio, ratio)
        return (m,)
```