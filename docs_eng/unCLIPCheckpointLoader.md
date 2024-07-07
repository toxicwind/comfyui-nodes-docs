# Documentation
- Class name: unCLIPCheckpointLoader
- Category: loaders
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The unCLIPheckpoint Loader node is designed to efficiently manage and load the checkpoint for the unCLIP model. It abstracts the complexity of the checkpoint search and ensures that the appropriate components, such as models, CLIP and VAE, are properly initialized from the stored state. The node plays a key role in model deployment and reasoning workflows, and is achieved by simplifying the check point loading process.

# Input types
## Required
- ckpt_name
    - The ckpt_name parameter is essential to identify the particular check point that you want to load. It points the node to the correct file path in the checkpoint directory, thus enabling the relevant model status to be retrieved. This parameter is essential for node implementation, as it determines the starting point for model recovery.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- output_vae
    - The output_vae parameter decides whether to load the VAE component from the check point. It provides flexibility in node operations to allow users to load only the required components selectively, depending on their particular usage or calculation.
    - Comfy dtype: bool
    - Python dtype: bool
- output_clip
    - The output_clip parameter specifies whether the model should be loaded with the CLIP component. It is an important setting for an application that requires text to an image or image to a text function, ensuring that nodes are adapted to different operational needs.
    - Comfy dtype: bool
    - Python dtype: bool

# Output types
- MODEL
    - MODEL output provides a model that is loaded from the checkpoint. It is the basic output of any follow-up or reasoning task as the core component of the model function.
    - Comfy dtype: COMBO[str, torch.nn.Module]
    - Python dtype: torch.nn.Module
- CLIP
    - The CLIP output represents text-to-image-to-text components of the model, which are particularly useful for applications involving natural language processing and computer visualization.
    - Comfy dtype: COMBO[str, torch.nn.Module]
    - Python dtype: torch.nn.Module
- VAE
    - VAE output is the variable coder part of the model and is responsible for generating new data samples from the learning to distribution. It is a key component of the task that requires data generation or operation.
    - Comfy dtype: COMBO[str, torch.nn.Module]
    - Python dtype: torch.nn.Module
- CLIP_VISION
    - CLIP_VISION output relates to the visual aspects of the CLIP model, focusing on image-related functions. It is important for a task dedicated to image processing and analysis.
    - Comfy dtype: COMBO[str, torch.nn.Module]
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class unCLIPCheckpointLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (folder_paths.get_filename_list('checkpoints'),)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE', 'CLIP_VISION')
    FUNCTION = 'load_checkpoint'
    CATEGORY = 'loaders'

    def load_checkpoint(self, ckpt_name, output_vae=True, output_clip=True):
        ckpt_path = folder_paths.get_full_path('checkpoints', ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, output_clipvision=True, embedding_directory=folder_paths.get_folder_paths('embeddings'))
        return out
```