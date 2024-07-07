# Documentation
- Class name: APISR_ModelLoader_Zho
- Category: APISR
- Output node: False
- Repo Ref: https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR.git

APISR_ModelLoader_Zho is a node for loading and managing various images of ultra-resolution models. It abstractes the complexity of the initialization of models, enabling users to seamlessly integrate different ultra-resolution algorithms into their applications. The node emphasizes flexibility and ease of use, providing a unified interface for dealing with different model architectures.

# Input types
## Required
- apisr_model
    - The apisr_model parameter is essential to specify the model file to be loaded. It guides the node to the correct model structure and weight file, enabling the node to exemplify the appropriate hyper-resolution generator. This parameter is essential to the execution of the node and the quality of the results it produces.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- pipe
    - The output parameter 'pipe' means the super-resolution model generator that is loaded. It is important because it is the main output of the nodes, providing users with an i.e. a model for image magnification. The generator's performance directly affects the effectiveness of the hyper-resolution process.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class APISR_ModelLoader_Zho:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'apisr_model': (folder_paths.get_filename_list('apisr'),)}}
    RETURN_TYPES = ('APISRMODEL',)
    RETURN_NAMES = ('pipe',)
    FUNCTION = 'load_model'
    CATEGORY = '🔎APISR'

    def load_model(self, apisr_model):
        if not apisr_model:
            raise ValueError('Please provide the apisr_model parameter with the name of the model file.')
        apisr_path = folder_paths.get_full_path('apisr', apisr_model)
        if apisr_model == '4x_APISR_GRL_GAN_generator.pth':
            generator = load_grl(apisr_path, scale=4)
        elif apisr_model == '2x_APISR_RRDB_GAN_generator.pth':
            generator = load_rrdb(apisr_path, scale=2)
        else:
            raise gr.Error(error)
        return [generator]
```