# Documentation
- Class name: CheckpointSave
- Category: advanced/model_merging
- Output node: True
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The CheckpointSave node is designed to facilitate the preservation of a model check point. It encapsifies the process of sequencing and storing the model's state (including its parameters and any associated metadata) into the document. This node is essential for the sustainability of the model, allowing training or reasoning to resume at a later stage without losing progress.

# Input types
## Required
- model
    - Model parameters are essential for the CheckpointSave node because it means the machine learning model that you want to save. It influences the node by determining the specific model state that you want to sequence and store.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The clip parameter needs to integrate the CLIP model status to the check point. It plays an important role in the function of the node by including the relevant features of the model reconstruction.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- vae
    - The vae parameter specifies the variable encoder that is to be included in the check point. It is important for the node because it ensures that the parameters and status of VAE are included for future use.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- filename_prefix
    - The filename_prefix parameters determine the basic name of the stored check point file. It is important because it provides an identifiable and consistent naming protocol for the check point, which helps to organize and retrieve it.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- prompt
    - The optional prompt parameter can be used to include a description or comment associated with the check point. This is useful for adding context to the saved model state.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - Extra_pnginfo parameters allow additional metadata to be saved with the checkpoint. This may include any additional information that may be relevant for model operations or analysis.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, Any]

# Output types

# Usage tips
- Infra type: CPU

# Source code
```
class CheckpointSave:

    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'clip': ('CLIP',), 'vae': ('VAE',), 'filename_prefix': ('STRING', {'default': 'checkpoints/ComfyUI'})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    FUNCTION = 'save'
    OUTPUT_NODE = True
    CATEGORY = 'advanced/model_merging'

    def save(self, model, clip, vae, filename_prefix, prompt=None, extra_pnginfo=None):
        save_checkpoint(model, clip=clip, vae=vae, filename_prefix=filename_prefix, output_dir=self.output_dir, prompt=prompt, extra_pnginfo=extra_pnginfo)
        return {}
```