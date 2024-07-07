# Documentation
- Class name: LoraLoader
- Category: loaders
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The Lora Loader node is designed to manage loading and application of LoRA (low adaptation) modifications to models. It efficiently processes the integration of LoRA adjustments into models and clip components, allowing for minimal costing fine-tuning model behaviour. The node abstractes the complexity of LoRA applications and provides a simplified interface for model enhancement.

# Input types
## Required
- model
    - The model parameter is essential because it represents the basic model that will be modified through LoRA technology. It is important because it is the main object of enhancement and has a direct impact on the implementation of nodes and the results of model functions.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The clip parameter specifies a conditional phase model for the CLIP architecture, which may also be influenced by a LoRA modification. Its role is important because it determines how text information and visual models are handled together.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- lora_name
    - The lora_name parameter is marked with a specific LoRA configuration to be loaded. It is critical because it determines the adaptation behaviour of the node and the model that will be applied to the model.
    - Comfy dtype: folder_paths.get_filename_list('loras')
    - Python dtype: str
## Optional
- strength_model
    - Strength_model parameters are adjusted to the intensity of the model's LoRA modifications. It plays a key role in fine-tuning model behaviour and provides a balance between original models and post-adaptation modelling capabilities.
    - Comfy dtype: FLOAT
    - Python dtype: float
- strength_clip
    - Strength_clip parameters allow adjustments to the impact of LoRA modifications on the CLIP model. It is important because it controls the extent to which text information processing is influenced by LoRA technology.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- model_lora
    - The model_lora output represents a model that has been modified by LoRA. It is important because it is a direct result of node operations and includes the enhanced capabilities of the model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip_lora
    - The clip_lora output represents a CLIP model adjusted by LoRA. It is important to demonstrate how the technical text information processing through LoRA has been adapted.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class LoraLoader:

    def __init__(self):
        self.loaded_lora = None

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'clip': ('CLIP',), 'lora_name': (folder_paths.get_filename_list('loras'),), 'strength_model': ('FLOAT', {'default': 1.0, 'min': -20.0, 'max': 20.0, 'step': 0.01}), 'strength_clip': ('FLOAT', {'default': 1.0, 'min': -20.0, 'max': 20.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL', 'CLIP')
    FUNCTION = 'load_lora'
    CATEGORY = 'loaders'

    def load_lora(self, model, clip, lora_name, strength_model, strength_clip):
        if strength_model == 0 and strength_clip == 0:
            return (model, clip)
        lora_path = folder_paths.get_full_path('loras', lora_name)
        lora = None
        if self.loaded_lora is not None:
            if self.loaded_lora[0] == lora_path:
                lora = self.loaded_lora[1]
            else:
                temp = self.loaded_lora
                self.loaded_lora = None
                del temp
        if lora is None:
            lora = comfy.utils.load_torch_file(lora_path, safe_load=True)
            self.loaded_lora = (lora_path, lora)
        (model_lora, clip_lora) = comfy.sd.load_lora_for_models(model, clip, lora, strength_model, strength_clip)
        return (model_lora, clip_lora)
```