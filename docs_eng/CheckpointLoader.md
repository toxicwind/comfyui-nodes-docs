# Documentation
- Class name: CheckpointLoader
- Category: advanced/loaders
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The CheckpointLoader node is designed to efficiently manage search model check points. It ensures that the correct model state is restored for further processing or reasoning by using configuration and check point filenames to locate and load the complexity of pre-training models in abstract terms.

# Input types
## Required
- config_name
    - The config_name parameter is essential for identifying specific configurations associated with the desired model checkpoint. It guides the node to the correct configuration file, which contains the settings required for the model to work as expected.
    - Comfy dtype: str
    - Python dtype: str
- ckpt_name
    - The ckpt_name parameter specifies the name of the check point file that you want to load. It is essential to position the node and restore to the model status that is saved in the given check point.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- output_vae
    - The output_vae parameter determines whether to load the model's variable coder (VAE) component. It provides flexibility when only specific parts of the model are needed for the task at hand.
    - Comfy dtype: bool
    - Python dtype: bool
- output_clip
    - Output_clip parameters indicate whether the checkpoints loaded should contain the model's comparative language-image pre-training (CLIP) components. It allows the model components to be loaded selectively according to the application's needs.
    - Comfy dtype: bool
    - Python dtype: bool

# Output types
- MODEL
    - MODEL output provides a loaded model check point that can be used for follow-up tasks, such as reasoning or further training.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- CLIP
    - When requested, the CLIP output provides a comparative language-image pre-training component of the loaded model, applicable to tasks involving text and image analysis.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- VAE
    - If specified, VAE output includes the model's variable fractional encoder section, which is very useful for generating tasks or decomposition dimensions.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class CheckpointLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'config_name': (folder_paths.get_filename_list('configs'),), 'ckpt_name': (folder_paths.get_filename_list('checkpoints'),)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE')
    FUNCTION = 'load_checkpoint'
    CATEGORY = 'advanced/loaders'

    def load_checkpoint(self, config_name, ckpt_name, output_vae=True, output_clip=True):
        config_path = folder_paths.get_full_path('configs', config_name)
        ckpt_path = folder_paths.get_full_path('checkpoints', ckpt_name)
        return comfy.sd.load_checkpoint(config_path, ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths('embeddings'))
```