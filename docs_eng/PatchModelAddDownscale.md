# Documentation
- Class name: PatchModelAddDownscale
- Category: _for_testing
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

PatchModelAddDownscale is designed to modify the behaviour of the given model by introducing sampling operations in the blocks specified in the model structure. It enhances the function of the model by allowing the resolution of the image to be adjusted during the processing phase, which is particularly useful for optimizing performance or achieving the required output quality.

# Input types
## Required
- model
    - Model parameters are necessary because it defines the basic model that will be modified by the node. It is the main input that determines the behaviour of the node and the nature of the output.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- block_number
    - Block number parameters are marked using specific blocks of sample operations in the model. It plays a key role in determining the change point in the model structure.
    - Comfy dtype: INT
    - Python dtype: int
- downscale_factor
    - The lower sampling factor parameter controls the level of below-sampling applied to the input. It is a key determinant in the conversion process that significantly influences the resolution of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_percent
    - Starts with a percentage parameter that specifies the size of the sigma that will be effective. It is an important factor in controlling the timing of the sampling in the model processing sequence.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_percent
    - Ends the sigma range of sampling operations under the percentage parameter. Together with the start-up percentage, it defines the operating window for sampling under the model workflow.
    - Comfy dtype: FLOAT
    - Python dtype: float
- downscale_after_skip
    - This determines the structural integrity of the model and the efficiency of the sub-sampling process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- downscale_method
    - The parameters of the sampling method determine the algorithm to be used for the input of the sample. This is a key option that affects the quality and properties of the sample output.
    - Comfy dtype: STRING
    - Python dtype: str
- upscale_method
    - The sampling method parameter determines the technology to be used for the sampling output. It plays an important role in the final resolution and visual authenticity of the model output.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- model
    - The output model is a modified version of the input model and is now equipped with an additional subsampling function. It represents the outcome of node processing and is ready for further use or analysis.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class PatchModelAddDownscale:
    upscale_methods = ['bicubic', 'nearest-exact', 'bilinear', 'area', 'bislerp']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'block_number': ('INT', {'default': 3, 'min': 1, 'max': 32, 'step': 1}), 'downscale_factor': ('FLOAT', {'default': 2.0, 'min': 0.1, 'max': 9.0, 'step': 0.001}), 'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_percent': ('FLOAT', {'default': 0.35, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'downscale_after_skip': ('BOOLEAN', {'default': True}), 'downscale_method': (s.upscale_methods,), 'upscale_method': (s.upscale_methods,)}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = '_for_testing'

    def patch(self, model, block_number, downscale_factor, start_percent, end_percent, downscale_after_skip, downscale_method, upscale_method):
        sigma_start = model.model.model_sampling.percent_to_sigma(start_percent)
        sigma_end = model.model.model_sampling.percent_to_sigma(end_percent)

        def input_block_patch(h, transformer_options):
            if transformer_options['block'][1] == block_number:
                sigma = transformer_options['sigmas'][0].item()
                if sigma <= sigma_start and sigma >= sigma_end:
                    h = comfy.utils.common_upscale(h, round(h.shape[-1] * (1.0 / downscale_factor)), round(h.shape[-2] * (1.0 / downscale_factor)), downscale_method, 'disabled')
            return h

        def output_block_patch(h, hsp, transformer_options):
            if h.shape[2] != hsp.shape[2]:
                h = comfy.utils.common_upscale(h, hsp.shape[-1], hsp.shape[-2], upscale_method, 'disabled')
            return (h, hsp)
        m = model.clone()
        if downscale_after_skip:
            m.set_model_input_block_patch_after_skip(input_block_patch)
        else:
            m.set_model_input_block_patch(input_block_patch)
        m.set_model_output_block_patch(output_block_patch)
        return (m,)
```