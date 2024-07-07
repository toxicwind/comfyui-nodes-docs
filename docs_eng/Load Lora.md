# Documentation
- Class name: WAS_Lora_Loader
- Category: WAS Suite/Loaders
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Lora_Loader node is designed to manage the loading and application of the Lora model in the WAS package. It ensures efficient processing of the Loa file, reduces redundancy and improves performance by cacheing the models previously loaded. This node is essential for integrating advanced custom features into workflows.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes, as they represent the main objects that will be applied to Lora enhancements. They have a direct impact on the performance of nodes and the ability of result models.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The clip parameter is essential to define the context in which the Lora model operates. It affects how the model is integrated with the rest of the system and the end result.
    - Comfy dtype: CLIP
    - Python dtype: Union[torch.Tensor, comfy.models.CLIPModel]
- lora_name
    - The lora_name parameter specifies the Lora model that you want to load. It is the key determinant of the customization process because it determines which Lora model will be used.
    - Comfy dtype: STRING
    - Python dtype: str
- strength_model
    - Strength_model parameters adjust the intensity of the impact of the Lora model on the underlying model. It is a key factor in fine-tuning model performance.
    - Comfy dtype: FLOAT
    - Python dtype: float
- strength_clip
    - Strength_clip parameters control the impact of the CLIP model on the process as a whole. It is important in forming the final output according to the required specification.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- MODEL
    - The output model represents an enhanced model tailored to Lora. It marks the completion of node processing and is at the core of the next steps in the workflow.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- CLIP
    - The output CLIP model reflects the adjustments made through integration with the Lora model. It is an important part of further processing or analysis.
    - Comfy dtype: CLIP
    - Python dtype: Union[torch.Tensor, comfy.models.CLIPModel]
- NAME_STRING
    - The NAME_STRING output provides the name of the loaded Lora model, which is very useful for tracking and referencing within the system.
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