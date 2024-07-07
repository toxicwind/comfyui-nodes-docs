# Documentation
- Class name: RatioAdvanced
- Category: Mikey/Utils
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The RatioAdvanced node is designed to perform advanced scale calculations and conversions. It can handle preset scales, custom input sizes, and various scaling operations to determine the optimal dimensions of the different phases of the image processing stream. The node emphasizes flexibility and accuracy in the scale processing to ensure that the output size meets specific criteria or binding conditions.

# Input types
## Required
- preset
    - Preset parameters allow users to select a predefined scale configuration. This option significantly simplifys the application of known scales to images, ensures consistency and reduces manual calculations.
    - Comfy dtype: STRING
    - Python dtype: str
- swap_axis
    - The swap_axis parameters enable the exchange of width and height when necessary. This is very useful for adjusting the image's direction without changing the inherent width ratio of the image.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- custom_latent_w
    - When choosing a custom scale, thecustom_latent_w parameter specifies the width of the potential image. This allows fine-tuning of the image size at a given processing stage, which is essential for achieving the required visual effects or meeting the output requirements.
    - Comfy dtype: INT
    - Python dtype: int
- custom_latent_h
    - This parameter provides control over the vertical dimensions of the image and allows precise adjustments to be made to meet specific processing objectives.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- latent_w
    - The output of latent_w represents the width of a potential image calculated on the basis of the ratio of input parameters and nodes. This value is essential for determining the horizontal dimensions of the image at a particular stage of the flow line.
    - Comfy dtype: INT
    - Python dtype: int
- latent_h
    - The output of latent_h corresponds to the height of the calculated potential image. Together with latent_w, it defines the overall size of the potential phase image, which is essential for further processing and analysis.
    - Comfy dtype: INT
    - Python dtype: int
- cte_w
    - cte_w output means considering the image width of the constant time evolution (CTE) scale. This parameter is important for maintaining the time consistency of the image in different processing steps.
    - Comfy dtype: INT
    - Python dtype: int
- cte_h
    - The cte_h output is the height of the image when applying the CTE scale. It works with cte_w to ensure that the image is appropriately resized while maintaining its long-width ratio and time integrity.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class RatioAdvanced:

    @classmethod
    def INPUT_TYPES(s):
        (s.ratio_sizes, s.ratio_dict) = read_ratios()
        default_ratio = s.ratio_sizes[0]
        s.ratio_sizes.insert(0, 'custom')
        (s.ratio_presets, s.ratio_config) = read_ratio_presets()
        if 'none' not in s.ratio_presets:
            s.ratio_presets.append('none')
        return {'required': {'preset': (s.ratio_presets, {'default': 'none'}), 'swap_axis': (['true', 'false'], {'default': 'false'}), 'select_latent_ratio': (s.ratio_sizes, {'default': default_ratio}), 'custom_latent_w': ('INT', {'default': 0, 'min': 0, 'max': 8192, 'step': 1}), 'custom_latent_h': ('INT', {'default': 0, 'min': 0, 'max': 8192, 'step': 1}), 'select_cte_ratio': (s.ratio_sizes, {'default': default_ratio}), 'cte_w': ('INT', {'default': 0, 'min': 0, 'max': 8192, 'step': 1}), 'cte_h': ('INT', {'default': 0, 'min': 0, 'max': 8192, 'step': 1}), 'cte_mult': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 100.0, 'step': 0.01}), 'cte_res': ('INT', {'default': 0, 'min': 0, 'max': 8192, 'step': 1}), 'cte_fit_size': ('INT', {'default': 0, 'min': 0, 'max': 8192, 'step': 1}), 'select_target_ratio': (s.ratio_sizes, {'default': default_ratio}), 'target_w': ('INT', {'default': 0, 'min': 0, 'max': 8192, 'step': 1}), 'target_h': ('INT', {'default': 0, 'min': 0, 'max': 8192, 'step': 1}), 'target_mult': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 100.0, 'step': 0.01}), 'target_res': ('INT', {'default': 0, 'min': 0, 'max': 8192, 'step': 1}), 'target_fit_size': ('INT', {'default': 0, 'min': 0, 'max': 8192, 'step': 1}), 'crop_w': ('INT', {'default': 0, 'min': 0, 'max': 8192, 'step': 1}), 'crop_h': ('INT', {'default': 0, 'min': 0, 'max': 8192, 'step': 1}), 'use_preset_seed': (['true', 'false'], {'default': 'false'}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}, 'hidden': {'unique_id': 'UNIQUE_ID', 'extra_pnginfo': 'EXTRA_PNGINFO', 'prompt': 'PROMPT'}}
    RETURN_TYPES = ('INT', 'INT', 'INT', 'INT', 'INT', 'INT', 'INT', 'INT')
    RETURN_NAMES = ('latent_w', 'latent_h', 'cte_w', 'cte_h', 'target_w', 'target_h', 'crop_w', 'crop_h')
    CATEGORY = 'Mikey/Utils'
    FUNCTION = 'calculate'

    def mult(self, width, height, mult):
        return (int(width * mult), int(height * mult))

    def fit(self, width, height, fit_size):
        if width > height:
            return (fit_size, int(height * fit_size / width))
        else:
            return (int(width * fit_size / height), fit_size)

    def res(self, width, height, res):
        return find_latent_size(width, height, res)

    def calculate(self, preset, swap_axis, select_latent_ratio, custom_latent_w, custom_latent_h, select_cte_ratio, cte_w, cte_h, cte_mult, cte_res, cte_fit_size, select_target_ratio, target_w, target_h, target_mult, target_res, target_fit_size, crop_w, crop_h, use_preset_seed, seed, unique_id=None, extra_pnginfo=None, prompt=None):
        if use_preset_seed == 'true' and len(self.ratio_presets) > 1:
            offset = seed % len(self.ratio_presets - 1)
            presets = [p for p in self.ratio_presets if p != 'none']
            preset = presets[offset]
        if preset != 'none':
            latent_width = self.ratio_config[preset]['custom_latent_w']
            latent_height = self.ratio_config[preset]['custom_latent_h']
            cte_w = self.ratio_config[preset]['cte_w']
            cte_h = self.ratio_config[preset]['cte_h']
            target_w = self.ratio_config[preset]['target_w']
            target_h = self.ratio_config[preset]['target_h']
            crop_w = self.ratio_config[preset]['crop_w']
            crop_h = self.ratio_config[preset]['crop_h']
            if swap_axis == 'true':
                (latent_width, latent_height) = (latent_height, latent_width)
                (cte_w, cte_h) = (cte_h, cte_w)
                (target_w, target_h) = (target_h, target_w)
                (crop_w, crop_h) = (crop_h, crop_w)
            '\n            example user_ratio_presets.json\n            {\n                "ratio_presets": {\n                    "all_1024": {\n                        "custom_latent_w": 1024,\n                        "custom_latent_h": 1024,\n                        "cte_w": 1024,\n                        "cte_h": 1024,\n                        "target_w": 1024,\n                        "target_h": 1024,\n                        "crop_w": 0,\n                        "crop_h": 0\n                    },\n                }\n            }\n            '
            return (latent_width, latent_height, cte_w, cte_h, target_w, target_h, crop_w, crop_h)
        if select_latent_ratio != 'custom':
            latent_width = self.ratio_dict[select_latent_ratio]['width']
            latent_height = self.ratio_dict[select_latent_ratio]['height']
        else:
            latent_width = custom_latent_w
            latent_height = custom_latent_h
        if select_cte_ratio != 'custom':
            cte_w = self.ratio_dict[select_cte_ratio]['width']
            cte_h = self.ratio_dict[select_cte_ratio]['height']
        else:
            cte_w = cte_w
            cte_h = cte_h
        if cte_mult != 0.0:
            (cte_w, cte_h) = self.mult(cte_w, cte_h, cte_mult)
        if cte_res != 0:
            (cte_w, cte_h) = self.res(cte_w, cte_h, cte_res)
        if cte_fit_size != 0:
            (cte_w, cte_h) = self.fit(cte_w, cte_h, cte_fit_size)
        if select_target_ratio != 'custom':
            target_w = self.ratio_dict[select_target_ratio]['width']
            target_h = self.ratio_dict[select_target_ratio]['height']
        else:
            target_w = target_w
            target_h = target_h
        if target_mult != 0.0:
            (target_w, target_h) = self.mult(target_w, target_h, target_mult)
        if target_res != 0:
            (target_w, target_h) = self.res(target_w, target_h, target_res)
        if target_fit_size != 0:
            (target_w, target_h) = self.fit(target_w, target_h, target_fit_size)
        return (latent_width, latent_height, cte_w, cte_h, target_w, target_h, crop_w, crop_h)
```