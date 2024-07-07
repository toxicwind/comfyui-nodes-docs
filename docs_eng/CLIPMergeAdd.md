# Documentation
- Class name: CLIPAdd
- Category: advanced/model_merging
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The CLIPAdd node is designed to integrate two stand-alone CLIP models seamlessly into a unified structure. It does so effectively by combining key patches from one CLIP model into another. This node plays a key role in advanced model consolidation techniques, allowing the creation of new models that are more complex and capable by taking advantage of the advantages of the two component models.

# Input types
## Required
- clip1
    - The first CLIP model, which will serve as the basis for the consolidation process, is crucial because it determines the infrastructure architecture that will be integrated into the patches of the second CLIP model.
    - Comfy dtype: CLIP
    - Python dtype: An instance of a CLIP model class.
- clip2
    - Provides a second CLIP model of key patches to be merged into the first CLIP model. Selecting this model is important because it contributes additional functionality to the merged model.
    - Comfy dtype: CLIP
    - Python dtype: An instance of a CLIP model class.

# Output types
- merged_clip
    - The output is a consolidated CLIP model, which now contains two features that enter the CLIP model. The new model is ready for further use or deployment for various tasks.
    - Comfy dtype: CLIP
    - Python dtype: An instance of a CLIP model class representing the merged model.

# Usage tips
- Infra type: CPU

# Source code
```
class CLIPAdd:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip1': ('CLIP',), 'clip2': ('CLIP',)}}
    RETURN_TYPES = ('CLIP',)
    FUNCTION = 'merge'
    CATEGORY = 'advanced/model_merging'

    def merge(self, clip1, clip2):
        m = clip1.clone()
        kp = clip2.get_key_patches()
        for k in kp:
            if k.endswith('.position_ids') or k.endswith('.logit_scale'):
                continue
            m.add_patches({k: kp[k]}, 1.0, 1.0)
        return (m,)
```