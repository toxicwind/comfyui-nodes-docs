# Documentation
- Class name: WAS_FreeU_V2
- Category: _for_testing
- Output node: False
- Repo Ref: https://github.com/WASasquatch/FreeU_Advanced

This node class is designed to use patch mechanisms for block application of the model to enhance the performance of the model by adjusting input, intermediate or output blocks by providing parameters. It focuses on the internal representation of the model through multiscale adjustment and slice techniques.

# Input types
## Required
- model
    - Model parameters are essential because it defines the neural network structure that will be modified by the patching process. It is the main object of node operations, the characteristics of which directly affect the patch result.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- multiscale_mode
    - Multiscale_mode parameters are essential for defining the multiscale method used in patches. They influence how model features are adjusted at different scales, which is essential for fine-tuning model performance.
    - Comfy dtype: LIST
    - Python dtype: list
- multiscale_strength
    - The multiscale_strength parameter controls the strength of multiscale adjustments. It is a key factor in determining the validity of the patch process and the adaptability of the results model to the various data scales.
    - Comfy dtype: FLOAT
    - Python dtype: float
- slice_b1
    - The slick_b1 parameter defines the size of the slice to be adjusted in the first dimension of the model's hidden layer. It is important to concentrate patch work on the specific area of the model, thereby optimizing its internal feature extraction mechanism.
    - Comfy dtype: INT
    - Python dtype: int
- slice_b2
    - The slick_b2 parameter sets the size of the slice in the second dimension of the hidden layer of the model. This parameter is important in refining the ability of the model to perform by targeting specific features within the layer.
    - Comfy dtype: INT
    - Python dtype: int
- b1
    - b1 parameter effects apply to the zoom factor of the first dimension of the hidden layer. It is a key factor in controlling the degree of conversion applied to the internal features of the model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- b2
    - The b2 parameter determines the zoom factor of the second dimension of the hidden layer. Adjusting this parameter can have a significant impact on the ability of the model to capture and process features within this dimension.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s1
    - The s1 parameter sets the threshold of the first dimension of the Fourier filter used in patching. It plays a key role in filtering unrelated frequencies and retaining only the most relevant features.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s2
    - The s2 parameter defines the threshold of the second dimension of the Fourier filter. By adjusting this parameter, you can control the level of detail that the model retains in the data expression.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- input_block
    - The input_block parameter determines whether the patch should be applied to the input block of the model. It plays a key role in the initial phase of data processing and can significantly affect the overall performance of the post-painting model.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- middle_block
    - Middle_block parameters specify whether patches should be applied to the middle layers of the model. These layers are essential to the learning process of the model and their adjustments can improve the performance of the model.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- output_block
    - The output_block parameter indicates whether the patch target should be positioned in the model's output block. Modifying this block directly affects the quality and accuracy of model predictions.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- threshold
    - Threshold parameters are used to determine the sensitivity of Fourier filters. Higher thresholds can lead to more radical filters, may remove more noise, but may also discard important information.
    - Comfy dtype: INT
    - Python dtype: int
- use_override_scales
    - Use_override_scales parameters allow the application of custom scaling instead of default values. This provides flexibility to customize the patching process according to specific requirements or experimental settings.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- override_scales
    - When using_override_scales is set to True, the override_scales parameter contains a string of custom scaling values to overwrite the default values. It allows users to fine-tune model responses under specific data features, which is very useful for fine particle size adjustments.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- model
    - The patch-up model is the main output of the node, representing the neural network that has been modified. This output is very important because it reflects the enhancement of the post-painting model and the adjusted internal mechanism.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class WAS_FreeU_V2:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'input_block': ('BOOLEAN', {'default': False}), 'middle_block': ('BOOLEAN', {'default': False}), 'output_block': ('BOOLEAN', {'default': False}), 'multiscale_mode': (list(mscales.keys()),), 'multiscale_strength': ('FLOAT', {'default': 1.0, 'max': 1.0, 'min': 0, 'step': 0.001}), 'slice_b1': ('INT', {'default': 640, 'min': 64, 'max': 1280, 'step': 1}), 'slice_b2': ('INT', {'default': 320, 'min': 64, 'max': 640, 'step': 1}), 'b1': ('FLOAT', {'default': 1.1, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'b2': ('FLOAT', {'default': 1.2, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 's1': ('FLOAT', {'default': 0.9, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 's2': ('FLOAT', {'default': 0.2, 'min': 0.0, 'max': 10.0, 'step': 0.001})}, 'optional': {'threshold': ('INT', {'default': 1.0, 'max': 10, 'min': 1, 'step': 1}), 'use_override_scales': (['false', 'true'],), 'override_scales': ('STRING', {'default': '# OVERRIDE SCALES\n\n# Sharpen\n# 10, 1.5', 'multiline': True})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = '_for_testing'

    def patch(self, model, input_block, middle_block, output_block, multiscale_mode, multiscale_strength, slice_b1, slice_b2, b1, b2, s1, s2, threshold=1.0, use_override_scales='false', override_scales=''):
        min_slice = 64
        max_slice_b1 = 1280
        max_slice_b2 = 640
        slice_b1 = max(min(max_slice_b1, slice_b1), min_slice)
        slice_b2 = max(min(min(slice_b1, max_slice_b2), slice_b2), min_slice)
        scales_list = []
        if use_override_scales == 'true':
            if override_scales.strip() != '':
                scales_str = override_scales.strip().splitlines()
                for line in scales_str:
                    if not line.strip().startswith('#') and (not line.strip().startswith('!')) and (not line.strip().startswith('//')):
                        scale_values = line.split(',')
                        if len(scale_values) == 2:
                            scales_list.append((int(scale_values[0]), float(scale_values[1])))
        if use_override_scales == 'true' and (not scales_list):
            print('No valid override scales found. Using default scale.')
            scales_list = None
        scales = mscales[multiscale_mode] if use_override_scales == 'false' else scales_list

        def _hidden_mean(h):
            hidden_mean = h.mean(1).unsqueeze(1)
            B = hidden_mean.shape[0]
            (hidden_max, _) = torch.max(hidden_mean.view(B, -1), dim=-1, keepdim=True)
            (hidden_min, _) = torch.min(hidden_mean.view(B, -1), dim=-1, keepdim=True)
            hidden_mean = (hidden_mean - hidden_min.unsqueeze(2).unsqueeze(3)) / (hidden_max - hidden_min).unsqueeze(2).unsqueeze(3)
            return hidden_mean

        def block_patch(h, transformer_options):
            if h.shape[1] == 1280:
                hidden_mean = _hidden_mean(h)
                h[:, :slice_b1] = h[:, :slice_b1] * ((b1 - 1) * hidden_mean + 1)
            if h.shape[1] == 640:
                hidden_mean = _hidden_mean(h)
                h[:, :slice_b2] = h[:, :slice_b2] * ((b2 - 1) * hidden_mean + 1)
            return h

        def block_patch_hsp(h, hsp, transformer_options):
            if h.shape[1] == 1280:
                h = block_patch(h, transformer_options)
                hsp = Fourier_filter(hsp, threshold=threshold, scale=s1, scales=scales, strength=multiscale_strength)
            if h.shape[1] == 640:
                h = block_patch(h, transformer_options)
                hsp = Fourier_filter(hsp, threshold=threshold, scale=s2, scales=scales, strength=multiscale_strength)
            return (h, hsp)
        m = model.clone()
        if output_block:
            print('Patching output block')
            m.set_model_output_block_patch(block_patch_hsp)
        if input_block:
            print('Patching input block')
            m.set_model_input_block_patch(block_patch)
        if middle_block:
            print('Patching middle block')
            m.set_model_patch(block_patch, 'middle_block_patch')
        return (m,)
```