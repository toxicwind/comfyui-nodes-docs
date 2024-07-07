# Documentation
- Class name: LoadOOTDPipeline
- Category: OOTD
- Output node: False
- Repo Ref: https://github.com/AuroBit/ComfyUI-OOTDiffusion.git

The node is intended to exemplify and provide access to the OOTDiffusion model, which can generate fashion-related images based on text descriptions. It abstractes the complexity of the model's loading and setting, ensuring that the model is ready for a reasoning task, without having to have a detailed understanding of the bottom structure or the training process.

# Input types
## Required
- type
    - The `type' parameter is essential for determining the specific configuration of the OOTDiffusion model that is to be loaded. It determines whether the model is optimized to produce images of half-body or full body clothing. This selects the performance and output quality of the significant impact model.
    - Comfy dtype: COMBO['Half body', 'Full body']
    - Python dtype: str
- path
    - The 'path' parameter is essential because it points to the directory where the OOTDiffusion model and its associated files are stored. This includes model weights, configuration files, and any other necessary data. The right path ensures that nodes are successfully loaded and initialized for image generation tasks.
    - Comfy dtype: string
    - Python dtype: str

# Output types
- pipe
    - The `pipe' output is a loaded OOTTDiffusion model to be used to generate fashion images. It covers the functions of the model and allows seamless interaction with the rest of the system to perform various image generation tasks.
    - Comfy dtype: object
    - Python dtype: OOTDiffusion

# Usage tips
- Infra type: GPU

# Source code
```
class LoadOOTDPipeline:
    display_name = 'Load OOTDiffusion Local'

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'type': (['Half body', 'Full body'],), 'path': (['/data/app/aigc-worker-v3/models/OOTDiffusion'], {'default': '/data/app/aigc-worker-v3/models/OOTDiffusion'})}}
    RETURN_TYPES = ('MODEL',)
    RETURN_NAMES = ('pipe',)
    FUNCTION = 'load'
    CATEGORY = 'OOTD'

    @staticmethod
    def load_impl(type, path):
        if type == 'Half body':
            type = 'hd'
        elif type == 'Full body':
            type = 'dc'
        else:
            raise ValueError(f"unknown input type {type} must be 'Half body' or 'Full body'")
        if not os.path.isdir(path):
            raise ValueError(f'input path {path} is not a directory')
        return OOTDiffusion(path, model_type=type)

    def load(self, type, path):
        return (self.load_impl(type, path),)
```