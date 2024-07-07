# Documentation
- Class name: InstantIDModelLoader
- Category: InstantID
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_InstantID.git

The node is intended to efficiently load and manage particular InstantID models, ensure that appropriate models are retrieved and prepared for use in the system.

# Input types
## Required
- instantid_file
    - This parameter is essential to specify the exact InstantID model file that you want to load. It determines the identity and version of the model to be used in subsequent operations.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- INSTANTID
    - The output represents the loaded InstantID model, which is essential for the system to carry out tasks related to model functions.
    - Comfy dtype: DICTIONARY
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class InstantIDModelLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'instantid_file': (folder_paths.get_filename_list('instantid'),)}}
    RETURN_TYPES = ('INSTANTID',)
    FUNCTION = 'load_model'
    CATEGORY = 'InstantID'

    def load_model(self, instantid_file):
        ckpt_path = folder_paths.get_full_path('instantid', instantid_file)
        model = comfy.utils.load_torch_file(ckpt_path, safe_load=True)
        if ckpt_path.lower().endswith('.safetensors'):
            st_model = {'image_proj': {}, 'ip_adapter': {}}
            for key in model.keys():
                if key.startswith('image_proj.'):
                    st_model['image_proj'][key.replace('image_proj.', '')] = model[key]
                elif key.startswith('ip_adapter.'):
                    st_model['ip_adapter'][key.replace('ip_adapter.', '')] = model[key]
            model = st_model
        return (model,)
```