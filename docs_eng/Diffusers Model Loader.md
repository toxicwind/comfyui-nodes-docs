# Documentation
- Class name: WAS_Diffusers_Loader
- Category: WAS Suite/Loaders/Advanced
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

Method `load_checkpoint'aims to load and manage the pre-training model from the specified directory. It allows intelligent access to file systems to locate and load the required models, and ensures that essential components such as VAE and CLIP are also available if required. This method is essential for initializing the model infrastructure in the application, providing seamless integration of model components for downstream tasks.

# Input types
## Required
- model_path
    - The parameter `model_path'is essential for identifying specific models to load in the file system. It guides the node to the right location so that the model's data and structure can be retrieved and used. This parameter is essential for the implementation of the node, as it determines the source of the model to be used in subsequent operations.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- output_vae
    - The parameter `output_vae'decides whether the model's VAE component should be loaded with the main model. This decision affects the function of the node, especially if the downstream task requires VAE to be generated. Therefore, the inclusion or exclusion of VAE can be a strategic choice, depending on the specific needs of the application.
    - Comfy dtype: bool
    - Python dtype: bool
- output_clip
    - Parameter `output_clip'controls the loading of the CLIP component, which is usually used for image-text matching tasks. Enables or disables this parameter to affect the ability of nodes to perform such tasks, as required by the application. It is an important consideration to ensure that nodes are consistent with the broader objectives of the project.
    - Comfy dtype: bool
    - Python dtype: bool

# Output types
- MODEL
    - The output `MODEL'represents the core structure of the loaded model and is the main component of the machine learning mission. It encapsulates the structure of the model and the parameters learned, so it is the basic output of any subsequent model-based operation in the system.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- CLIP
    - When an `CLIP'output exists, it provides an interface to the image-text matching function. It is an optional component that can be loaded according to the needs of the application and provides additional capabilities for tasks involving linking images to text descriptions.
    - Comfy dtype: Optional[torch.nn.Module]
    - Python dtype: Optional[torch.nn.Module]
- VAE
    - The output `VAE'is the variable-based encoder part of the model, which is responsible for the generation of the model. It is an optional output that can be included depending on whether or not the mission is capable of generating it.
    - Comfy dtype: Optional[torch.nn.Module]
    - Python dtype: Optional[torch.nn.Module]
- NAME_STRING
    - The output `NAME_STRING'provides the basic name of the loaded model, which is very useful for log recording, recognition or reference in the application. As a human readable label, it helps to track and manage the use of the model.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Diffusers_Loader:

    @classmethod
    def INPUT_TYPES(cls):
        paths = []
        for search_path in comfy_paths.get_folder_paths('diffusers'):
            if os.path.exists(search_path):
                paths += next(os.walk(search_path))[1]
        return {'required': {'model_path': (paths,)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE', TEXT_TYPE)
    RETURN_NAMES = ('MODEL', 'CLIP', 'VAE', 'NAME_STRING')
    FUNCTION = 'load_checkpoint'
    CATEGORY = 'WAS Suite/Loaders/Advanced'

    def load_checkpoint(self, model_path, output_vae=True, output_clip=True):
        for search_path in comfy_paths.get_folder_paths('diffusers'):
            if os.path.exists(search_path):
                paths = next(os.walk(search_path))[1]
                if model_path in paths:
                    model_path = os.path.join(search_path, model_path)
                    break
        out = comfy.diffusers_convert.load_diffusers(model_path, fp16=comfy.model_management.should_use_fp16(), output_vae=output_vae, output_clip=output_clip, embedding_directory=comfy_paths.get_folder_paths('embeddings'))
        return (out[0], out[1], out[2], os.path.basename(model_path))
```