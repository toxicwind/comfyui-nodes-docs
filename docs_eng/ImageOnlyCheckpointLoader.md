# Documentation
- Class name: ImageOnlyCheckpointLoader
- Category: loaders/video_models
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The node is responsible for loading the checkpoint from the specified directory and returning the relevant models, the CLIP visual module and the VAE component. It is designed to handle the complexity of loading and extracting the check point, abstract details, and provides a direct interface for downstream tasks.

# Input types
## Required
- ckpt_name
    - The name of the check point file that you want to load. It is essential for identifying a particular check point in the directory, as it directly affects the operation of the node and the model components generated.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- MODEL
    - Model components loaded from inspection points can be used for various downstream tasks, such as reasoning or further training.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- CLIP_VISION
    - The CLIP visual module extracted from the check point is essential for tasks involving text to image generation or image text matching.
    - Comfy dtype: CLIP
    - Python dtype: CLIP
- VAE
    - The VAE component, which is loaded from the check point, is usually used for potential space operations and generation tasks.
    - Comfy dtype: AutoencoderKL
    - Python dtype: AutoencoderKL

# Usage tips
- Infra type: CPU

# Source code
```
class ImageOnlyCheckpointLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (folder_paths.get_filename_list('checkpoints'),)}}
    RETURN_TYPES = ('MODEL', 'CLIP_VISION', 'VAE')
    FUNCTION = 'load_checkpoint'
    CATEGORY = 'loaders/video_models'

    def load_checkpoint(self, ckpt_name, output_vae=True, output_clip=True):
        ckpt_path = folder_paths.get_full_path('checkpoints', ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=False, output_clipvision=True, embedding_directory=folder_paths.get_folder_paths('embeddings'))
        return (out[0], out[3], out[2])
```