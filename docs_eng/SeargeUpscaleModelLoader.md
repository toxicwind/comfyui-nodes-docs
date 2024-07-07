# Documentation
- Class name: SeargeUpscaleModelLoader
- Category: Searge/_deprecated_/Files
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergeUpscaleModel Loader node is designed to simplify the loading process of magnifying models in image enhancement missions. It abstractes the complexity of the model loading, making it possible to take samples on seamless integration in larger workflows. This node is essential for applications that require high-quality image scaling without going deep into the details of model processing.

# Input types
## Required
- upscaler_name
    - The parameter 'upscaler_name' is essential for identifying specific amplifier models to load. It plays a central role in the operation of nodes because it determines which models will be used for image sampling, directly affecting the quality and properties of the output.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- UPSCALE_MODEL
    - The 'UPSCALE_MODEL' output represents the model of the amplifier that has been loaded and is an essential part of the follow-up image processing task. It covers the model's structure and learning parameters and is prepared to be applied to image sampling in accordance with workflow requirements.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeUpscaleModelLoader:

    def __init__(self):
        self.upscale_model_loader = comfy_extras.nodes_upscale_model.UpscaleModelLoader()

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'upscaler_name': ('UPSCALER_NAME',)}}
    RETURN_TYPES = ('UPSCALE_MODEL',)
    FUNCTION = 'load_upscaler'
    CATEGORY = 'Searge/_deprecated_/Files'

    def load_upscaler(self, upscaler_name):
        return self.upscale_model_loader.load_model(upscaler_name)
```