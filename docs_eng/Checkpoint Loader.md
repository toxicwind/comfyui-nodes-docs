# Documentation
- Class name: WAS_Checkpoint_Loader
- Category: WAS Suite/Loaders/Advanced
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

Methodology `load_checkpoint'aims to efficiently retrieve and load pre-training models, CLIP models and VAE models for designated inspection points. It is a key component of the workflow for initializing complex machine learning structures and their corresponding configuration and weighting.

# Input types
## Required
- config_name
    - The parameter `config_name'is essential because it identifies the specific configurations required for the model. It ensures that the correct model architecture and hyper-parameters are applied during loading.
    - Comfy dtype: str
    - Python dtype: str
- ckpt_name
    - The parameter `ckpt_name'is essential for the location of the checkpoint file containing model learning weights. It is a key input that guides the loading process to the correct weight set of models.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- output_vae
    - The logo `output_vae'determines whether the model should be loaded with the VAE component. It provides flexibility during loading according to the specific needs of the task on hand.
    - Comfy dtype: bool
    - Python dtype: bool
- output_clip
    - The symbol `output_clip'controls the loading of the CLIP model components. It allows the loading of model components selectively according to the application or analysis needs.
    - Comfy dtype: bool
    - Python dtype: bool

# Output types
- MODEL
    - Output `MODEL'provides a loaded model structure. It is important because it represents the core components needed for further processing or reasoning tasks.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- CLIP
    - When requested, the output `CLIP'provides a CLIP model component. It is essential for tasks involving text to image or image to text functions.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- VAE
    - If specified, the output `VAE'includes the variable self-codifier part of the model. It is essential for tasks requiring capacity generation or potential space operations.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- NAME_STRING
    - Output `NAME_STRING'returns the basic name of the checkpoint without a file extension. It is very useful as the identifier of the checkpoint for the purposes of log recording or record-keeping.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Checkpoint_Loader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'config_name': (comfy_paths.get_filename_list('configs'),), 'ckpt_name': (comfy_paths.get_filename_list('checkpoints'),)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE', TEXT_TYPE)
    RETURN_NAMES = ('MODEL', 'CLIP', 'VAE', 'NAME_STRING')
    FUNCTION = 'load_checkpoint'
    CATEGORY = 'WAS Suite/Loaders/Advanced'

    def load_checkpoint(self, config_name, ckpt_name, output_vae=True, output_clip=True):
        config_path = comfy_paths.get_full_path('configs', config_name)
        ckpt_path = comfy_paths.get_full_path('checkpoints', ckpt_name)
        out = comfy.sd.load_checkpoint(config_path, ckpt_path, output_vae=True, output_clip=True, embedding_directory=comfy_paths.get_folder_paths('embeddings'))
        return (out[0], out[1], out[2], os.path.splitext(os.path.basename(ckpt_name))[0])
```