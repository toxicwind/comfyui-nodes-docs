# Documentation
- Class name: PCSplitSampling
- Category: promptcontrol
- Output node: False
- Repo Ref: https://github.com/asagi4/comfyui-prompt-control.git

The PCSplitSampling node is designed to modify the given model by enabling or disallowing a specific sampling technique called the hint to control the partition of the sample. This technology is essential to control the process of model generation and allows for more fine and targeted output. By applying this node, the user can easily switch the sampling method to achieve the desired result without changing the structure of the bottom model.

# Input types
## Required
- model
    - The `model' parameter is essential because it represents a machine learning model to be adjusted by sampling technology. It is the core component of node operations, and its modification will have a direct impact on the ability of the model to generate.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- split_sampling
    - The `split_sampling' parameter decides whether to activate the hint control sampling technique for the model. This switch directly affects the way data are sampled, which may be critical to achieving a particular result in the model prediction or generation.
    - Comfy dtype: COMBO['enable', 'disable']
    - Python dtype: str

# Output types
- model
    - Output `model' is a modified version of the input model that uses the user-selected hint control to split the sampling function. This allows the model to use the required sampling behaviour in the follow-up task.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class PCSplitSampling:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'split_sampling': (['enable', 'disable'],)}}
    RETURN_TYPES = ('MODEL',)
    CATEGORY = 'promptcontrol'
    FUNCTION = 'apply'

    def apply(self, model, split_sampling):
        model = clone_model(model)
        model.model_options['pc_split_sampling'] = split_sampling == 'enable'
        return (model,)
```