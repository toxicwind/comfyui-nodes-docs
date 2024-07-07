# Documentation
- Class name: WAS_Lora_Loader
- Category: WAS Suite/Loaders
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Lora_Loader node is designed to manage and apply the Lora model to enhance the functionality of the basic model and the editing. It ensures efficient processing of the Loa file through the cache of previously loaded models, thereby optimizing performance and resource use.

# Input types
## Required
- model
    - The `model' parameter is essential because it represents the base model that will be applied to Lora-enhanced. It directly influences the output of nodes by determining the model that will be modified.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The `clip' parameter is essential to provide the clip components that will be influenced by the Lora model. It is a key element of node operations, as it defines the clips that will be enhanced.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- lora_name
    - The `lora_name' parameter specifies the Lora model file to be loaded. It is a key input because it determines the Lora model to be enhanced and influences the final output of the node.
    - Comfy dtype: STRING
    - Python dtype: str
- strength_model
    - The `strength_model' parameter adjusts the intensity of the impact of the Lora model on the base model. It plays an important role in the microregulating point output to achieve the required level of enhancement.
    - Comfy dtype: FLOAT
    - Python dtype: float
- strength_clip
    - The'strength_clip' parameter controls the intensity of the impact of the Lora model on the editing. It is important for adjusting the output of nodes to meet the specific enhancement requirements of the editing component.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- MODEL
    - The `MODEL' output represents an enhanced model following the application of the Lora model. It is the main result of node operations and is important for further processing or analysis.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- CLIP
    - The 'CLIP'output is a editing component modified by the Lora model. It is an important part of the node function and provides enhanced clips for downstream tasks.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- NAME_STRING
    - The output `NAME_STRING' provides the name of the Lora model that is loaded and applied. It serves as a reference for the specific Lora model used in the enhancement process.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Lora_Loader:

    def __init__(self):
        self.loaded_lora = None

    @classmethod
    def INPUT_TYPES(s):
        file_list = comfy_paths.get_filename_list('loras')
        file_list.insert(0, 'None')
        return {'required': {'model': ('MODEL',), 'clip': ('CLIP',), 'lora_name': (file_list,), 'strength_model': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'strength_clip': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL', 'CLIP', TEXT_TYPE)
    RETURN_NAMES = ('MODEL', 'CLIP', 'NAME_STRING')
    FUNCTION = 'load_lora'
    CATEGORY = 'WAS Suite/Loaders'

    def load_lora(self, model, clip, lora_name, strength_model, strength_clip):
        if strength_model == 0 and strength_clip == 0:
            return (model, clip)
        lora_path = comfy_paths.get_full_path('loras', lora_name)
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
        return (model_lora, clip_lora, os.path.splitext(os.path.basename(lora_name))[0])
```