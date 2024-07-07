# Documentation
- Class name: DiffusersLoader
- Category: advanced/loaders/deprecated
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The DiffusesLoader class is designed to simplify the process of loading and initializing the components of the diffusion model. It applies in particular to the different parts of the integration model itself, CLIP and VAE from the specified path. The load_checkpoint method is the main interface for this function, abstracting the complexity of file path resolution and model loading.

# Input types
## Required
- model_path
    - The model_path parameter is essential for the Diffuses Loader node because it specifies the path of the desired model file. It is used to search for and load the necessary components of the diffusion model.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- output_vae
    - The output_vae parameter determines whether the VAE component should be loaded with the model. It provides flexibility in the process of loading the model according to the specific needs of the application.
    - Comfy dtype: bool
    - Python dtype: bool
- output_clip
    - Output_clip parameters control the loading of the CLIP component. It allows the user to specify whether the CLIP model should be part of the loaded model component.
    - Comfy dtype: bool
    - Python dtype: bool

# Output types
- MODEL
    - MODEL output represents the proliferation model that Diffuses Loader loads. It is the central component of the application for further processing and analysis.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- CLIP
    - CLIP output is the text feature extractor part of the model, which is loaded conditionally according to the output_clip parameter. It plays an important role in the text-to-image generation task.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- VAE
    - The VAE output is a variable coder component of the diffusion model, which is loaded according to the output_vae parameter. It is essential for tasks involving potential space operations.
    - Comfy dtype: comfy.sd.VAE
    - Python dtype: comfy.sd.VAE

# Usage tips
- Infra type: CPU

# Source code
```
class DiffusersLoader:

    @classmethod
    def INPUT_TYPES(cls):
        paths = []
        for search_path in folder_paths.get_folder_paths('diffusers'):
            if os.path.exists(search_path):
                for (root, subdir, files) in os.walk(search_path, followlinks=True):
                    if 'model_index.json' in files:
                        paths.append(os.path.relpath(root, start=search_path))
        return {'required': {'model_path': (paths,)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE')
    FUNCTION = 'load_checkpoint'
    CATEGORY = 'advanced/loaders/deprecated'

    def load_checkpoint(self, model_path, output_vae=True, output_clip=True):
        for search_path in folder_paths.get_folder_paths('diffusers'):
            if os.path.exists(search_path):
                path = os.path.join(search_path, model_path)
                if os.path.exists(path):
                    model_path = path
                    break
        return comfy.diffusers_load.load_diffusers(model_path, output_vae=output_vae, output_clip=output_clip, embedding_directory=folder_paths.get_folder_paths('embeddings'))
```