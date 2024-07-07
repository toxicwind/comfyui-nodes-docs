# Documentation
- Class name: WAS_Load_Cache
- Category: WAS Suite/IO
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Load_Cache node aims to efficiently manage the loading of cache data from a given path, such as potential vectors, images, and conditional data. It ensures that data are loaded only when a cache file exists on a given path, providing an important data retrieval mechanism for the workstream of the SAS package.

# Input types
## Required
- latent_path
    - The latent_path parameter specifies the file path for the potential data cache. Its existence is essential because it guides nodes to the right location to load the potential data, which is essential for the follow-up steps in the WAS package.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- image_path
    - The image_path parameter is used to indicate the location of the image data cache. This is an optional parameter that allows nodes to load and use the image data from the specified path when provided, thereby enhancing the functionality of the system as a whole.
    - Comfy dtype: STRING
    - Python dtype: Optional[str]
- conditioning_path
    - Convention_path parameters point to the file path for storage conditions data caches. This optional parameter is important when nodees need to be loaded to influence the generation or processing of other data in the WAS package.
    - Comfy dtype: STRING
    - Python dtype: Optional[str]

# Output types
- LATENT
    - LATENT output provides the potential data to be loaded from the specified cache path. It is a key component of a model in the WAS package that is potentially indicative of the operation.
    - Comfy dtype: LATENT
    - Python dtype: Union[torch.Tensor, None]
- IMAGE
    - The IMAGE output contains loaded image data that can be used for visualization or further analysis in the WAS package. It is an optional output that occurs only when the corresponding image_path input is provided and the image data is successfully loaded.
    - Comfy dtype: IMAGE
    - Python dtype: Union[PIL.Image, None]
- CONDITIONING
    - The CONDITIONING output provides the loaded condition data, which is essential for some modeling operations within the SAS package. It allows custom and fine-tuning model behaviour to be entered in accordance with the conditions.
    - Comfy dtype: CONDITIONING
    - Python dtype: Union[torch.Tensor, None]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Load_Cache:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'latent_path': ('STRING', {'default': '', 'multiline': False}), 'image_path': ('STRING', {'default': '', 'multiline': False}), 'conditioning_path': ('STRING', {'default': '', 'multiline': False})}}
    RETURN_TYPES = ('LATENT', 'IMAGE', 'CONDITIONING')
    RETURN_NAMES = ('LATENT', 'IMAGE', 'CONDITIONING')
    FUNCTION = 'load_cache'
    CATEGORY = 'WAS Suite/IO'

    def load_cache(self, latent_path=None, image_path=None, conditioning_path=None):
        if 'joblib' not in packages():
            install_package('joblib')
        import joblib
        input_path = os.path.join(WAS_SUITE_ROOT, 'cache')
        latent = None
        image = None
        conditioning = None
        if latent_path not in ['', None]:
            if os.path.exists(latent_path):
                latent = joblib.load(latent_path)
            else:
                cstr(f'Unable to locate cache file {latent_path}').error.print()
        if image_path not in ['', None]:
            if os.path.exists(image_path):
                image = joblib.load(image_path)
            else:
                cstr(f'Unable to locate cache file {image_path}').msg.print()
        if conditioning_path not in ['', None]:
            if os.path.exists(conditioning_path):
                conditioning = joblib.load(conditioning_path)
            else:
                cstr(f'Unable to locate cache file {conditioning_path}').error.print()
        return (latent, image, conditioning)
```