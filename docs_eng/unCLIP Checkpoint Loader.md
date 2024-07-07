# Documentation
- Class name: WAS_unCLIP_Checkpoint_Loader
- Category: WAS Suite/Loaders
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The node is intended to load and manage inspection points for the WAS package, including models, CLIP and VAE components. It is essential for the initialization of the components required for further processing and analysis within the WAS framework.

# Input types
## Required
- ckpt_name
    - The name of the check point is a necessary parameter, which specifies the name of the check point to be loaded. This is essential to identify and retrieve the correct check point for the operation of the WAS package.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- output_vae
    - The 'output_vae'parameter determines whether to include the VAE component in the loaded checkpoint. It affects the composition of the object returned at the node.
    - Comfy dtype: bool
    - Python dtype: bool
- output_clip
    - 'output_clip'indicates whether the CLIP model should be used as part of a loaded check point. It influences the output of the node by including or excluding the CLIP model.
    - Comfy dtype: bool
    - Python dtype: bool

# Output types
- MODEL
    - MODEL output represents the machine learning model components that are loaded from the checkpoint. It is important for carrying out tasks that require model reasoning or processing.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- CLIP
    - The CLIP output is a loaded CLIP model component used for text-to-image matching and other related tasks in the WAS package.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- VAE
    - VAE output represents the variable coder components in the check point. It is essential for tasks involving the generation of models and potential space operations.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- CLIP_VISION
    - The CLIP_VISION output is a visual component of the CLIP model and is responsible for image-related operations within the WAS package.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- NAME_STRING
    - The NAME_STRING output provides the basic name of the loading check point without a file extension. It is very useful for reference and identification purposes.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_unCLIP_Checkpoint_Loader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (comfy_paths.get_filename_list('checkpoints'),)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE', 'CLIP_VISION', 'STRING')
    RETURN_NAMES = ('MODEL', 'CLIP', 'VAE', 'CLIP_VISION', 'NAME_STRING')
    FUNCTION = 'load_checkpoint'
    CATEGORY = 'WAS Suite/Loaders'

    def load_checkpoint(self, ckpt_name, output_vae=True, output_clip=True):
        ckpt_path = comfy_paths.get_full_path('checkpoints', ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, output_clipvision=True, embedding_directory=comfy_paths.get_folder_paths('embeddings'))
        return (out[0], out[1], out[2], out[3], os.path.splitext(os.path.basename(ckpt_name))[0])
```