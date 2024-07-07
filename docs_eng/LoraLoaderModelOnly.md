# Documentation
- Class name: LoraLoaderModelOnly
- Category: Model Loading
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The Lora Loader ModelOnly node is designed to efficiently load and integrate the Lora model into the existing model architecture. It enhances the capability of the underlying model by applying the Lora adjustment, allowing for specific modifications without reloading the complete model.

# Input types
## Required
- model
    - The'model' parameter is critical, because it represents the basic model that will integrate the Lora adjustment. It is essential for the implementation of the node, because it determines the model that will be modified.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- lora_name
    - The 'lora_name' parameter specifies the name of the Lora file to be loaded. It is essential to identify the correct Lora model that needs to be applied to the underlying model.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- strength_model
    - The'strength_model' parameter allows users to control the intensity of the Lora adjustment applied to the model. It plays an important role in fine-tuning model performance.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- model
    - The'model' output represents a modified model with an integrated Lora adjustment. It is the result of node function and provides an enhanced model modified by the specified Lora.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class LoraLoaderModelOnly(LoraLoader):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'lora_name': (folder_paths.get_filename_list('loras'),), 'strength_model': ('FLOAT', {'default': 1.0, 'min': -20.0, 'max': 20.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'load_lora_model_only'

    def load_lora_model_only(self, model, lora_name, strength_model):
        return (self.load_lora(model, None, lora_name, strength_model, 0)[0],)
```