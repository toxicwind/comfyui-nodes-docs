# Documentation
- Class name: CLIPSubtract
- Category: advanced/model_merging
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The CLIPSubtrust node is designed to reduce the behaviour of two CLIP models. It merges the key patches of one CLIP model into another, allowing fine-tuning of model features by adjusting the impact of a particular patch. This node is essential in advanced model consolidation techniques, with the objective of refining or modifying the behaviour of existing models.

# Input types
## Required
- clip1
    - The first CLIP model, which will receive patches from the second model, is critical because it defines the underlying model that will be integrated and modified.
    - Comfy dtype: CLIP
    - Python dtype: An instance of a CLIP model class.
- clip2
    - The second CLIP model, which provides key patches, will be subtracted from the first model. It plays an important role in determining which aspects of the model will be changed.
    - Comfy dtype: CLIP
    - Python dtype: An instance of a CLIP model class.
## Optional
- multiplier
    - A floating point value is used to adjust the strength of patches that are merged from the second CLIP model to the first model. It is important to control the extent of the effect of patches on the result model.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- resulting_clip
    - The output of the CLIPSubtract node is a modified CLAIP model, which now includes patches subtracted from the second model and adjusted according to the specified multipliers.
    - Comfy dtype: CLIP
    - Python dtype: An instance of a modified CLIP model class.

# Usage tips
- Infra type: CPU

# Source code
```
class CLIPSubtract:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip1': ('CLIP',), 'clip2': ('CLIP',), 'multiplier': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01})}}
    RETURN_TYPES = ('CLIP',)
    FUNCTION = 'merge'
    CATEGORY = 'advanced/model_merging'

    def merge(self, clip1, clip2, multiplier):
        m = clip1.clone()
        kp = clip2.get_key_patches()
        for k in kp:
            if k.endswith('.position_ids') or k.endswith('.logit_scale'):
                continue
            m.add_patches({k: kp[k]}, -multiplier, multiplier)
        return (m,)
```