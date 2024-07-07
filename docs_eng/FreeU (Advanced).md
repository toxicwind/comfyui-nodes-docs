# Documentation
- Class name: WAS_FreeU
- Category: _for_testing
- Output node: False
- Repo Ref: https://github.com/WASasquatch/FreeU_Advanced

The WAS_FreeU category includes a method to modify and enhance model behaviour by applying patching techniques. The method is called 'patch', which aims to improve the performance of models or adjust their output characteristics according to predefined parameters and models. The function of the node is concentrated on the internal expression of the manipulation model, allowing for a more detailed and targeted approach to model optimization.

# Input types
## Required
- model
    - Model parameters are necessary because it defines the infrastructure and weights that will be applied to the patching process. It is the main input and its characteristics and performance will be changed by the operation of the node.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- target_block
    - The target_block parameter determines which part of the model will be concentrated in patching operations. It is critical in determining the scope and impact of the changes made at the node.
    - Comfy dtype: COMBO[output_block, middle_block, input_block, all]
    - Python dtype: str
- multiscale_mode
    - Multiscale_mode parameters influence the complexity and particle size of patching processes. It plays an important role in how nodes adjust their behaviour to different scales of model characteristics.
    - Comfy dtype: FLOAT
    - Python dtype: float
- multiscale_strength
    - This parameter controls the strength of multiscale patches. It is important because it directly affects the extent to which nodes modify model features at different scales.
    - Comfy dtype: FLOAT
    - Python dtype: float
- slice_b1
    - The slick_b1 parameter specifies the size of the first piece of the patch. It is a key factor in determining the component of the model that will be modified.
    - Comfy dtype: INT
    - Python dtype: int
- slice_b2
    - This parameter defines the size of the second piece involved in the patch. It works with slice_b1 to create the model feature range to which the node will be directed.
    - Comfy dtype: INT
    - Python dtype: int
- b1
    - b1 parameter is used to adjust the impact of the first part of the patch. It is important because it allows node control to be applied to the extent of modification of model characteristics.
    - Comfy dtype: FLOAT
    - Python dtype: float
- b2
    - This parameter is responsible for adjusting the impact of the second film during patches. It is critical in shaping how nodes change model features within the specified range.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s1
    - The s1 parameter is essential for setting the size of the first filter operation. It determines how the node emphasizes or suppresses certain features of the model according to its importance.
    - Comfy dtype: FLOAT
    - Python dtype: float
- s2
    - This parameter determines the size of the second filtering operation. It plays a key role in the ability of the microreconciliation point to improve model features within the target range.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- b1_mode
    - The b1_mode parameter sets out the first hybrid mode. It is important to define how the patch operation integrates the changes into the existing features of the model.
    - Comfy dtype: COMBO[add, subtract, multiply, divide, average, max, min]
    - Python dtype: str
- b1_blend
    - This parameter adjusts the mixing strength of the first section. It is important because it allows nodes to control the smoothness of the transition between the original feature and the modified feature.
    - Comfy dtype: FLOAT
    - Python dtype: float
- b2_mode
    - The b2_mode parameter sets out a hybrid model for the second film. It is essential to determine how the patched features of the node are aligned with the rest of the model.
    - Comfy dtype: COMBO[add, subtract, multiply, divide, average, max, min]
    - Python dtype: str
- b2_blend
    - This parameter fine-tunes the mixing strength of the second film. It is essential to ensure that nodes are seamlessly integrated into the existing structure of the model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- threshold
    - Threshold parameters are used to define areas of interest for filtering operations. It is important for the focus of attention on nodes in terms of the specific characteristics of the model.
    - Comfy dtype: INT
    - Python dtype: int
- use_override_scales
    - Use_override_scales parameters allow custom scaling of Fourier filters. It is important because it provides flexibility for nodes to adjust the filtering process to specific needs.
    - Comfy dtype: COMBO[false, true]
    - Python dtype: str
- override_scales
    - This parameter provides a manual method for assigning proportional values to the Fourier filter. It is important for applying the user-defined filter criteria to the characteristics of the model.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- MODEL
    - The output is a modified model that applies patch operations. It represents an enhanced or modified version of the input model and reflects the changes made at the node.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class WAS_FreeU:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'target_block': (['output_block', 'middle_block', 'input_block', 'all'],), 'multiscale_mode': (list(mscales.keys()),), 'multiscale_strength': ('FLOAT', {'default': 1.0, 'max': 1.0, 'min': 0, 'step': 0.001}), 'slice_b1': ('INT', {'default': 640, 'min': 64, 'max': 1280, 'step': 1}), 'slice_b2': ('INT', {'default': 320, 'min': 64, 'max': 640, 'step': 1}), 'b1': ('FLOAT', {'default': 1.1, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'b2': ('FLOAT', {'default': 1.2, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 's1': ('FLOAT', {'default': 0.9, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 's2': ('FLOAT', {'default': 0.2, 'min': 0.0, 'max': 10.0, 'step': 0.001})}, 'optional': {'b1_mode': (list(blending_modes.keys()),), 'b1_blend': ('FLOAT', {'default': 1.0, 'max': 100, 'min': 0, 'step': 0.001}), 'b2_mode': (list(blending_modes.keys()),), 'b2_blend': ('FLOAT', {'default': 1.0, 'max': 100, 'min': 0, 'step': 0.001}), 'threshold': ('INT', {'default': 1.0, 'max': 10, 'min': 1, 'step': 1}), 'use_override_scales': (['false', 'true'],), 'override_scales': ('STRING', {'default': '# OVERRIDE SCALES\n\n# Sharpen\n# 10, 1.5', 'multiline': True})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = '_for_testing'

    def patch(self, model, target_block, multiscale_mode, multiscale_strength, slice_b1, slice_b2, b1, b2, s1, s2, b1_mode='add', b1_blend=1.0, b2_mode='add', b2_blend=1.0, threshold=1.0, use_override_scales='false', override_scales=''):
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
        print(f'FreeU Plate Portions: {slice_b1} over {slice_b2}')
        print(f'FreeU Multi-Scales: {scales}')

        def block_patch(h, transformer_options):
            if h.shape[1] == 1280:
                h_t = h[:, :slice_b1]
                h_r = h_t * b1
                h[:, :slice_b1] = blending_modes[b1_mode](h_t, h_r, b1_blend)
            if h.shape[1] == 640:
                h_t = h[:, :slice_b2]
                h_r = h_t * b2
                h[:, :slice_b2] = blending_modes[b2_mode](h_t, h_r, b2_blend)
            return h

        def block_patch_hsp(h, hsp, transformer_options):
            if h.shape[1] == 1280:
                h = block_patch(h, transformer_options)
                hsp = Fourier_filter(hsp, threshold=threshold, scale=s1, scales=scales, strength=multiscale_strength)
            if h.shape[1] == 640:
                h = block_patch(h, transformer_options)
                hsp = Fourier_filter(hsp, threshold=threshold, scale=s2, scales=scales, strength=multiscale_strength)
            return (h, hsp)
        print(f'Patching {target_block}')
        m = model.clone()
        if target_block == 'all' or target_block == 'output_block':
            m.set_model_output_block_patch(block_patch_hsp)
        if target_block == 'all' or target_block == 'input_block':
            m.set_model_input_block_patch(block_patch)
        if target_block == 'all' or target_block == 'middle_block':
            m.set_model_patch(block_patch, 'middle_block_patch')
        return (m,)
```