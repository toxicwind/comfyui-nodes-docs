# Documentation
- Class name: WAS_Upscale_Model_Loader
- Category: WAS Suite/Loaders
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

Method `load_model'is responsible for loading and preparing models for image magnification tasks. It achieves this by locating the specified model in the specified directory, loading its parameters and initializing it for use. This method is essential for seamless integration of pre-training models into the workflow, ensuring that models are ready for deployment without manual intervention.

# Input types
## Required
- model_name
    - The parameter `model_name'is essential to identify the specific model to be loaded. It points the method to the correct file in the model catalogue, thus enabling the search and initialization of the required model. This parameter is essential to ensure the use of the correct model, which directly affects subsequent magnification and results.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- UPSCALE_MODEL
    - Output `UPSCALE_MODEL'represents a loaded and initialized model prepared for use in image magnification missions. It covers the model's structure and learning parameters, allowing the model to be applied to new data. This output is important because it forms the basis for all subsequent processing and analysis of the model.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- MODEL_NAME_TEXT
    - The output `MODEL_NAME_TEXT'provides the name of the loaded model, which is very useful for the purpose of log recording, tracking, or user interface displaying. It provides a human readable identifier for the model to communicate and refer to throughout the application.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Upscale_Model_Loader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model_name': (comfy_paths.get_filename_list('upscale_models'),)}}
    RETURN_TYPES = ('UPSCALE_MODEL', TEXT_TYPE)
    RETURN_NAMES = ('UPSCALE_MODEL', 'MODEL_NAME_TEXT')
    FUNCTION = 'load_model'
    CATEGORY = 'WAS Suite/Loaders'

    def load_model(self, model_name):
        model_path = comfy_paths.get_full_path('upscale_models', model_name)
        sd = comfy.utils.load_torch_file(model_path)
        out = model_loading.load_state_dict(sd).eval()
        return (out, model_name)
```