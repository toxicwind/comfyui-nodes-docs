# Documentation
- Class name: StyleModelLoader
- Category: loaders
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The StyleModelLoader node is designed to efficiently manage and load style models. It is a key component of a model deployment line, ensuring that appropriate style models are retrieved and ready for use. The node abstractes the complexity of file path management and model loading and provides seamless interfaces for downstream tasks.

# Input types
## Required
- style_model_name
    - Parameters'style_model_name' are essential for identifying particular style models to load. It plays a key role in running nodes, by guiding nodes to the correct file path in the style model directory. Values of parameters directly influence the eventual loading and use of models in subsequent processes.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- STYLE_MODEL
    - Output 'STYLE_MODEL' represents the installed style model and is a key element for further processing and analysis. It covers features and parameters learned by the style model so that it can be applied to a variety of tasks, such as style migration or feature extraction.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class StyleModelLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'style_model_name': (folder_paths.get_filename_list('style_models'),)}}
    RETURN_TYPES = ('STYLE_MODEL',)
    FUNCTION = 'load_style_model'
    CATEGORY = 'loaders'

    def load_style_model(self, style_model_name):
        style_model_path = folder_paths.get_full_path('style_models', style_model_name)
        style_model = comfy.sd.load_style_model(style_model_path)
        return (style_model,)
```