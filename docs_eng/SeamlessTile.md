# Documentation
- Class name: SeamlessTile
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/spinagon/ComfyUI-seamless-tiling

SeamlessTile is a node used to modify model filling and volume behaviour in order to achieve seamlessly flattening. It adjusts the filling mode and filling values of the Conv2d layer in order to achieve a “circle” effect, which is particularly useful in image processing tasks that require seamless flooring.

# Input types
## Required
- model
    - Model parameters are essential because they represent the neural network that will be modified to achieve seamlessly flattening. They are the core components of node operations to achieve the required levelling effect.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- tiling
    - Tiling parameter instructions apply to the flatten type of the model. It controls whether to use the sheeting, limiting it to x-axis, y-axis, or to disable it completely, affecting the ability of the model to produce a seamless pattern.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- copy_model
    - The copy_model parameter determines whether the original model should be copied or changed locally before it is modified. This affects implementation by retaining or modifying the original model status.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- MODEL
    - The output MODEL is a modified neural network with adjusted filling and volume settings to support seamlessly flattened. It is important because it directly affects the follow-up and output quality of the image.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class SeamlessTile:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'tiling': (['enable', 'x_only', 'y_only', 'disable'],), 'copy_model': (['Make a copy', 'Modify in place'],)}}
    CATEGORY = 'conditioning'
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'run'

    def run(self, model, copy_model, tiling):
        if copy_model == 'Modify in place':
            model_copy = model
        else:
            model_copy = copy.deepcopy(model)
        if tiling == 'enable':
            make_circular_asymm(model_copy.model, True, True)
        elif tiling == 'x_only':
            make_circular_asymm(model_copy.model, True, False)
        elif tiling == 'y_only':
            make_circular_asymm(model_copy.model, False, True)
        else:
            make_circular_asymm(model_copy.model, False, False)
        return (model_copy,)
```