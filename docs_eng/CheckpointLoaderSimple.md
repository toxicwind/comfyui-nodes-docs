# Documentation
- Class name: CheckpointLoaderSimple
- Category: loaders
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The CheckpointLoaderSimple node is designed to load and manage the checkpoint of the machine learning model. It retrieves the model from the designated checkpoint and ensures that the model is prepared for reasoning or further training. The node abstractes the complexity of loading the check point and provides a simplified interface for model deployment and utilization.

# Input types
## Required
- ckpt_name
    - The check point name is the key parameter for the Checkpoint Loader Simple node, as it identifies the particular check point to be loaded on. This parameter directly affects the operation of the node and influences subsequent model performance and behaviour by determining the model status to be retrieved.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- output_vae
    - This optional parameter allows flexibility in loading the necessary components of the model, thereby optimizing the use of resources and simplifying the loading process.
    - Comfy dtype: bool
    - Python dtype: bool
- output_clip
    - The output_clip parameter determines whether the CLIP model should be loaded with the main model check point. This option may be important for applications that require text-image matching functions, thereby enhancing the model's functionality.
    - Comfy dtype: bool
    - Python dtype: bool

# Output types
- MODEL
    - MODEL output represents the loaded machine learning model. It is a key component because it contains the model's learning parameters and architecture that enable it to perform tasks such as classification or regression based on input data.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- CLIP
    - When requested, the CLIP output provides a comparative language-image pre-training model that can understand and generate images from text descriptions. This output is important for applications involving text to image generation or image-text matching.
    - Comfy dtype: CLIP
    - Python dtype: CLIP
- VAE
    - VAE output refers to the model's variable coder component, which produces new data samples similar to the distribution of input data. This is an important part of the task that requires data generation or noise.
    - Comfy dtype: AutoencoderKL
    - Python dtype: AutoencoderKL

# Usage tips
- Infra type: CPU

# Source code
```
class CheckpointLoaderSimple:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (folder_paths.get_filename_list('checkpoints'),)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE')
    FUNCTION = 'load_checkpoint'
    CATEGORY = 'loaders'

    def load_checkpoint(self, ckpt_name, output_vae=True, output_clip=True):
        ckpt_path = folder_paths.get_full_path('checkpoints', ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths('embeddings'))
        return out[:3]
```