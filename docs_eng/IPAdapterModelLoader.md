# Documentation
- Class name: IPAdapterModelLoader
- Category: ipadapter/loaders
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

IPAdapterModelLoader aims to efficiently load and integrate the IPAdapter model into the system to ensure compatibility and seamless functionality of the model with the frame.

# Input types
## Required
- ipadapter_file
    - ipadapter_file is a key parameter that specifies the path of the IPAdapter model file. It is essential for the correct loading and processing of the model at nodes, affecting the overall performance and accuracy of the system.
    - Comfy dtype: COMBO[string]
    - Python dtype: str

# Output types
- ipadapter
    - The output provided a structured representation of the loaded IPAdapter model, which is essential for follow-up and analysis within the system.
    - Comfy dtype: dict
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class IPAdapterModelLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ipadapter_file': (folder_paths.get_filename_list('ipadapter'),)}}
    RETURN_TYPES = ('IPADAPTER',)
    FUNCTION = 'load_ipadapter_model'
    CATEGORY = 'ipadapter/loaders'

    def load_ipadapter_model(self, ipadapter_file):
        ipadapter_file = folder_paths.get_full_path('ipadapter', ipadapter_file)
        return (ipadapter_model_loader(ipadapter_file),)
```