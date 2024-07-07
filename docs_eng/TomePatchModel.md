# Documentation
- Class name: TomePatchModel
- Category: _for_testing
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The TomePatchModel class is designed to modify and enhance the function of the given model by applying patch technology. This method, called 'patch ', allows custom model attention mechanisms that may enhance its performance on specific tasks without significantly changing the bottom structure.

# Input types
## Required
- model
    - The'model' parameter is essential because it represents a machine learning model that will be patched. The patching process customizes the behaviour of the model to make it more appropriate for the intended application.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ratio
    - The 'ratio' parameter determines the proportion of the model attention mechanism that is patched. It is essential to control the scope of the changes and to balance performance with computational efficiency.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- modified_model
    - Output'modified_model' is the result of the application of patches to input models. It is important because it represents an enhanced model that is prepared for deployment or further training.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class TomePatchModel:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'ratio': ('FLOAT', {'default': 0.3, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = '_for_testing'

    def patch(self, model, ratio):
        self.u = None

        def tomesd_m(q, k, v, extra_options):
            (m, self.u) = get_functions(q, ratio, extra_options['original_shape'])
            return (m(q), k, v)

        def tomesd_u(n, extra_options):
            return self.u(n)
        m = model.clone()
        m.set_model_attn1_patch(tomesd_m)
        m.set_model_attn1_output_patch(tomesd_u)
        return (m,)
```