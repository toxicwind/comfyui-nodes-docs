# Documentation
- Class name: LDSRModelLoader
- Category: Flowty LDSR
- Output node: False
- Repo Ref: https://github.com/flowtyone/ComfyUI-Flowty-LDSR.git

The node is designed to load and prepare a LDSR model for use, abstracting the complexity of model retrieval and initialization. It ensures that the model is ready for the sampling task by moving the model to the appropriate equipment and setting it up as an assessment model.

# Input types
## Required
- model
    - Model parameters are essential because they specify the LDSR model that you want to load. It affects the entire operation by determining the status dictionary and configuration of which model to be used in the sampling process.
    - Comfy dtype: COMBO[filename]
    - Python dtype: str

# Output types
- UPSCALE_MODEL
    - The output provides a fully initialized and prepared LDSR model, which is important for further image sampling tasks.
    - Comfy dtype: COMBO[LDSR]
    - Python dtype: LDSR

# Usage tips
- Infra type: CPU

# Source code
```
class LDSRModelLoader:

    @classmethod
    def INPUT_TYPES(s):
        model_list = get_filename_list('upscale_models')
        candidates = [name for name in model_list if 'last.ckpt' in name]
        if len(candidates) > 0:
            default_path = candidates[0]
        else:
            default_path = 'last.ckpt'
        return {'required': {'model': (model_list, {'default': default_path})}}
    RETURN_TYPES = ('UPSCALE_MODEL',)
    FUNCTION = 'load'
    CATEGORY = 'Flowty LDSR'

    def load(self, model):
        model_path = get_full_path('upscale_models', model)
        model = LDSR.load_model_from_path(model_path)
        model['model'].cpu()
        return (model,)
```