# Documentation
- Class name: PhotoMakerLoader
- Category: _for_testing/photomaker
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The PhotoMaker Loader class is responsible for loading and initializing the PhotoMaker model, which is a key component of the image processing process. It abstractes the complexity of the model loading and ensures that the model is properly initialized using the correct state dictionary.

# Input types
## Required
- photomaker_model_name
    - The photomaker_model_name parameter is essential for identifying a particular model to load. It guides the loader to the correct file path and ensures that the model is correctly exemplified for follow-up action.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- PHOTOMAKER
    - The PHOTOMAKER output represents the loaded PhotoMaker model, which is prepared for use in image-processing tasks. It marks the successful initialization of the parameters and status of the model associated with it.
    - Comfy dtype: PhotoMakerIDEncoder
    - Python dtype: PhotoMakerIDEncoder

# Usage tips
- Infra type: CPU

# Source code
```
class PhotoMakerLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'photomaker_model_name': (folder_paths.get_filename_list('photomaker'),)}}
    RETURN_TYPES = ('PHOTOMAKER',)
    FUNCTION = 'load_photomaker_model'
    CATEGORY = '_for_testing/photomaker'

    def load_photomaker_model(self, photomaker_model_name):
        photomaker_model_path = folder_paths.get_full_path('photomaker', photomaker_model_name)
        photomaker_model = PhotoMakerIDEncoder()
        data = comfy.utils.load_torch_file(photomaker_model_path, safe_load=True)
        if 'id_encoder' in data:
            data = data['id_encoder']
        photomaker_model.load_state_dict(data)
        return (photomaker_model,)
```