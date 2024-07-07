# Documentation
- Class name: LLLiteLoader
- Category: loaders
- Output node: False
- Repo Ref: https://github.com/kohya-ss/ControlNet-LLLite-ComfyUI.git

The LLLLiteLoader class is designed to efficiently load and process models, enabling the integration of control mechanisms into the model architecture. It abstractes the complexity of model loading and reconciliation and focuses on seamless adaptation of models to specific conditions and requirements.

# Input types
## Required
- model
    - Model parameters are essential because they define the basic architecture that will be regulated and modified. They are the starting point for the LLLiteLoader function and determine the type of model to be addressed.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- model_name
    - Model name parameters are essential for identifying specific model files to load. They guide LLLLiteLoader to find the right model in the file system and ensure that the right model is selected for processing.
    - Comfy dtype: STRING
    - Python dtype: str
- cond_image
    - Cond_image parameters affect the behaviour and output of the model as a regulatory input. It is a key component of the model adaptation process and allows fine-tuning based on the visual context.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- strength
    - Strength parameter adjusts the strength of the adjustment effect on the model. It plays an important role in determining the extent of the effect of the adjustment input on the model's final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- steps
    - The Steps parameter defines the number of intervals to be used in the reconciliation process. It is important for the progress of the model and for the distribution of the adjustment effects throughout the process.
    - Comfy dtype: INT
    - Python dtype: int
- start_percent
    - The start_percent parameter specifies the start of the reconciliation interval and determines when the model begins to adapt to the adjustment input. It is a key factor in controlling the response time of the model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_percent
    - End_percent parameters mark the end of the reconciliation interval and define the end time of the model adaptation adjustment input. It is the key to determining the duration of the model response.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- model
    - The output model is the result of the LLLLiteLoader process and contains the reconciliation input and adjustment. It represents the final state of the model after the entire reconciliation process and is prepared for further use or evaluation.
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
        return {'required': {'model': ('MODEL',), 'model_name': (get_file_list(os.path.join(CURRENT_DIR, 'models')),), 'cond_image': ('IMAGE',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'steps': ('INT', {'default': 0, 'min': 0, 'max': 200, 'step': 1}), 'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 100.0, 'step': 0.1}), 'end_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 100.0, 'step': 0.1})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'load_lllite'
    CATEGORY = 'loaders'

    def load_lllite(self, model, model_name, cond_image, strength, steps, start_percent, end_percent):
        model_path = os.path.join(CURRENT_DIR, os.path.join(CURRENT_DIR, 'models', model_name))
        model_lllite = model.clone()
        patch = load_control_net_lllite_patch(model_path, cond_image, strength, steps, start_percent, end_percent)
        if patch is not None:
            model_lllite.set_model_attn1_patch(patch)
            model_lllite.set_model_attn2_patch(patch)
        return (model_lllite,)
```