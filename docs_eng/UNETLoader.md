# Documentation
- Class name: UNETLoader
- Category: advanced/loaders
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The `load_unet'method is designed to retrieve and load the pre-trained U-Net model from the specified directory. It is a key component of the model deployment process, ensuring that the correct model is loaded and ready for reasoning tasks.

# Input types
## Required
- unet_name
    - The parameter `unet_name'is essential to identify the specific U-Net model that you want to load. It guides the loader to the correct file path, making it possible to retrieve the model required for follow-up operations.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- MODEL
    - The output of the `load_unet'method is a U-Net model, which represents the PyTorch module. The model can be used to split tasks across images, using pre-trained weights for accurate predictions.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class UNETLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'unet_name': (folder_paths.get_filename_list('unet'),)}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'load_unet'
    CATEGORY = 'advanced/loaders'

    def load_unet(self, unet_name):
        unet_path = folder_paths.get_full_path('unet', unet_name)
        model = comfy.sd.load_unet(unet_path)
        return (model,)
```