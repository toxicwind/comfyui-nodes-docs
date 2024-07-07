# Documentation
- Class name: CLIPLoader
- Category: advanced/loaders
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The CLIPLoader node is designed to efficiently manage and load the integration of CLIP models based on the specified type, contributing to the stabilization of diffusion or stabilization of cascade models. It abstractes the complexity of file path management and model loading and ensures seamless experience for users in using the CLIP model.

# Input types
## Required
- clip_name
    - The clip_name parameter is essential to identify the specific CLIP model that you want to load. It influences the implementation of the node by determining from which file path to retrieve the model, thereby influencing the results of the process of loading the model.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- type
    - The type is used to specify the type of CLIP model that you want to load, which can be 'table_discussion' or 'table_case'. It plays an important role in the function of the node by guiding the selection of the appropriate model type for the current task.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- CLIP
    - The output CLIP parameter represents the loaded CLIP model, which is the main result of node operations. It marks the model's successful loading and preparation for the follow-up task.
    - Comfy dtype: CLIP
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class CLIPLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip_name': (folder_paths.get_filename_list('clip'),), 'type': (['stable_diffusion', 'stable_cascade'],)}}
    RETURN_TYPES = ('CLIP',)
    FUNCTION = 'load_clip'
    CATEGORY = 'advanced/loaders'

    def load_clip(self, clip_name, type='stable_diffusion'):
        clip_type = comfy.sd.CLIPType.STABLE_DIFFUSION
        if type == 'stable_cascade':
            clip_type = comfy.sd.CLIPType.STABLE_CASCADE
        clip_path = folder_paths.get_full_path('clip', clip_name)
        clip = comfy.sd.load_clip(ckpt_paths=[clip_path], embedding_directory=folder_paths.get_folder_paths('embeddings'), clip_type=clip_type)
        return (clip,)
```