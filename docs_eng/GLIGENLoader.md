# Documentation
- Class name: GLIGENLoader
- Category: loaders
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The GLIGENLoader node is designed to efficiently load and process GLIGEN data. It plays a key role in the data preparation phase to ensure that GLIGEN data is properly retrieved and made available for subsequent processing steps.

# Input types
## Required
- gligen_name
    - The parameter'gligen_name' is essential for identifying specific GLIGEN data that you want to load. Node uses it to locate and retrieve the corresponding data files and then process them for workflow use.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- GLIGEN
    - Output GLIGEN data represents the information that is loaded and processed from the specified GLIGEN file. It is prepared for downstream tasks such as analysis or further data operations.
    - Comfy dtype: GLIGEN
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class GLIGENLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'gligen_name': (folder_paths.get_filename_list('gligen'),)}}
    RETURN_TYPES = ('GLIGEN',)
    FUNCTION = 'load_gligen'
    CATEGORY = 'loaders'

    def load_gligen(self, gligen_name):
        gligen_path = folder_paths.get_full_path('gligen', gligen_name)
        gligen = comfy.sd.load_gligen(gligen_path)
        return (gligen,)
```