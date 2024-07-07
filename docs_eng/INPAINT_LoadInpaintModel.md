# Documentation
- Class name: LoadInpaintModel
- Category: inpaint
- Output node: False
- Repo Ref: https://github.com/Acly/comfyui-inpaint-nodes

The LoadInpaintModel class is designed to facilitate the loading of repair models, which are neural network structures designed to fill missing or damaged parts of the image. It abstractes the complexity of the loading of the model, ensuring that the loading process is fluid and reliable. The function of the node is essential for the initialization of the restoration process and provides the basis for further image operations.

# Input types
## Required
- model_name
    - The parameter'model_name' is important because it identifies a specific repair model to be loaded. It influences the execution of the node by determining the neural network structure that will be used to restore the task. The correct model name is essential for achieving the required image recovery results.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- INPAINT_MODEL
    - Output 'INPAINT_MODEL' represents the installed repair model that can be used for subsequent image processing tasks. It encapsifies the model's trained weights and architecture, marks the completion of the loading process and enables the model to perform its assigned functions.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class LoadInpaintModel:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model_name': (folder_paths.get_filename_list('inpaint'),)}}
    RETURN_TYPES = ('INPAINT_MODEL',)
    CATEGORY = 'inpaint'
    FUNCTION = 'load'

    def load(self, model_name: str):
        model_file = folder_paths.get_full_path('inpaint', model_name)
        if model_file is None:
            raise RuntimeError(f'Model file not found: {model_name}')
        if model_file.endswith('.pt'):
            sd = torch.jit.load(model_file, map_location='cpu').state_dict()
        else:
            sd = comfy.utils.load_torch_file(model_file, safe_load=True)
        if 'synthesis.first_stage.conv_first.conv.resample_filter' in sd:
            model = mat.load(sd)
        else:
            model = comfy_extras.chainner_models.model_loading.load_state_dict(sd)
        model = model.eval()
        return (model,)
```