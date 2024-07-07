# Documentation
- Class name: LLLiteLoader
- Category: EasyUse/Loaders
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

LLLLiteLoader nodes are designed to facilitate the integration of lightweight models and to enhance the overall processing capacity of the system by adding additional model functions.

# Input types
## Required
- model
    - Model parameters are essential in defining the basic structure to be used and modified by nodes and significantly influencing the output and behaviour of nodes.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- model_name
    - This parameter is essential for selecting an appropriate model from the list and is the treatment of guiding nodes according to the characteristics of the selected model and the expected application.
    - Comfy dtype: COMBO
    - Python dtype: str
- cond_image
    - The cond_image parameter is important because it provides the context information needed for the model to adapt to its output to specific conditions and influences the final result.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
## Optional
- strength
    - The strength parameter adjustment model adjusts to the strength of the condition and can be used for the output of the microregulating point to meet different requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- steps
    - The Steps parameters define the number of overlaps that the model will experience, which has a direct impact on the complexity and accuracy of node processing.
    - Comfy dtype: INT
    - Python dtype: int
- start_percent
    - This parameter sets the starting point for the model adaptation process and affects progress in the implementation of the initial conditions and nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_percent
    - End_percent parameters determine the endpoint of model adaptation and influence the final state and results of node operations.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- model
    - The output model is the result of node processing and contains the characteristics and conditions of adaptation and is ready for use in the follow-up mission.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class LLLiteLoader:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        def get_file_list(filenames):
            return [file for file in filenames if file != 'put_models_here.txt' and 'lllite' in file]
        return {'required': {'model': ('MODEL',), 'model_name': (get_file_list(folder_paths.get_filename_list('controlnet')),), 'cond_image': ('IMAGE',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'steps': ('INT', {'default': 0, 'min': 0, 'max': 200, 'step': 1}), 'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 100.0, 'step': 0.1}), 'end_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 100.0, 'step': 0.1})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'load_lllite'
    CATEGORY = 'EasyUse/Loaders'

    def load_lllite(self, model, model_name, cond_image, strength, steps, start_percent, end_percent):
        model_path = os.path.join(folder_paths.get_full_path('controlnet', model_name))
        model_lllite = model.clone()
        patch = load_control_net_lllite_patch(model_path, cond_image, strength, steps, start_percent, end_percent)
        if patch is not None:
            model_lllite.set_model_attn1_patch(patch)
            model_lllite.set_model_attn2_patch(patch)
        return (model_lllite,)
```