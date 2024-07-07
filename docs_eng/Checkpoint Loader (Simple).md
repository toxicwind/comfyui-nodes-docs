# Documentation
- Class name: WAS_Checkpoint_Loader_Simple
- Category: WAS Suite/Loaders
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The load_checkpoint method is designed to efficiently retrieve and initialize the components of the designated checkpoint to facilitate seamless integration in the workflow. It serves as a key link between the storage model and the application, ensuring that the necessary elements for follow-up operations are readily available.

# Input types
## Required
- ckpt_name
    - The check point name parameter is essential to identify a particular check point to load. It guides the node to find the correct file, and thus retrieves the relevant models and configurations.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- output_vae
    - The output_vae parameter determines whether to load the VAE component from the check point. It allows the component to be loaded selectively according to the needs of the current task.
    - Comfy dtype: bool
    - Python dtype: bool
- output_clip
    - The output_clip parameter determines whether the CLIP model should be loaded in the search check point process. It provides flexibility to include or exclude the CLIP model in the loaded component.
    - Comfy dtype: bool
    - Python dtype: bool

# Output types
- MODEL
    - MODEL output represents the main neural network structure loaded from the checkpoint, which is essential for subsequent processing and analysis tasks.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- CLIP
    - The CLIP output represents the condition language-image pre-training model loaded with the main model, which enhances the ability of nodes to handle multi-module tasks.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- VAE
    - VAE output represents a searchable variable coder component that provides a powerful generation model and data coding tool within the operating range of nodes.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- NAME_STRING
    - The NAME_STRING output provides the name of the check point as a string, which is very useful for further processing in log records, recognition or workflows.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Checkpoint_Loader_Simple:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (comfy_paths.get_filename_list('checkpoints'),)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE', TEXT_TYPE)
    RETURN_NAMES = ('MODEL', 'CLIP', 'VAE', 'NAME_STRING')
    FUNCTION = 'load_checkpoint'
    CATEGORY = 'WAS Suite/Loaders'

    def load_checkpoint(self, ckpt_name, output_vae=True, output_clip=True):
        ckpt_path = comfy_paths.get_full_path('checkpoints', ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=comfy_paths.get_folder_paths('embeddings'))
        return (out[0], out[1], out[2], os.path.splitext(os.path.basename(ckpt_name))[0])
```