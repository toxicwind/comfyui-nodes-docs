# Documentation
- Class name: PresetRatioSelector
- Category: Mikey/Utils
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The PresetRadioSelector node is designed to calculate and select the size of the image according to its predefined design. It allows customizing potential dimensions, content-to-margin ratio, target size, and crop parameters. The main function of the node is to automatically select the proportion of the image according to the default defined by the user, ensuring consistency and ease of use in the image operation task.

# Input types
## Required
- select_preset
    - The select_preset parameter is essential for determining which proportion is to be applied. It determines the starting point of the node calculation process and is essential for achieving the required image size.
    - Comfy dtype: STRING
    - Python dtype: str
- swap_axis
    - The swap_axis parameter allows the user to exchange the preset width and height size. This may be important in the scenario where the image is to be reoriented.
    - Comfy dtype: STRING
    - Python dtype: str
- use_preset_seed
    - Use_preset_seed parameters to decide whether to use a torrent value to select the preset. This can introduce variability in the selection process and allow for the selection of a more diverse image scale.
    - Comfy dtype: STRING
    - Python dtype: str
- seed
    - Seed parameters are used in conjunction with the use_preset_seed logo to influence the selection of preset ratios. It adds a control layer for randomity during the selection process.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- unique_id
    - The unique_id parameter is used for the only identification operation in the system. It may be important to track and manage the implementation of nodes in the larger workflow.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
- extra_pnginfo
    - Extra_pnginfo parameters provide additional information relevant to the PNG image format. This may be useful for processing specific image properties associated with node operations.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: str
- prompt
    - The prompt parameter can be used to provide descriptive text that guides the operation of the node. It may affect the preset selection depending on the context provided by the text.
    - Comfy dtype: PROMPT
    - Python dtype: str

# Output types
- latent_w
    - This is the key parameter for determining the horizontal dimensions of the image in the potential expression.
    - Comfy dtype: INT
    - Python dtype: int
- latent_h
    - The output indicates the altitude of the potential space. It is the key parameter for determining the vertical dimensions of the image in the potential expression.
    - Comfy dtype: INT
    - Python dtype: int
- cte_w
    - cte_w output indicates the width of the calculated content to the margin ratio. It is important to maintain the vertical and proportional ratio of the image.
    - Comfy dtype: INT
    - Python dtype: int
- cte_h
    - cte_h output indicates the height of the calculated content to the margin ratio. It plays a similar role to cte_w in maintaining the vertical and proportional ratio of the image.
    - Comfy dtype: INT
    - Python dtype: int
- target_w
    - Target_w output indicates the target width of the calculated image. It is used to guide the process of resizing or scaling in order to achieve the required dimensions.
    - Comfy dtype: INT
    - Python dtype: int
- target_h
    - Target_h output indicates the target height of the calculated image. It works with Target_w to ensure that the image size meets the specified requirements.
    - Comfy dtype: INT
    - Python dtype: int
- crop_w
    - Crop_w output represents the width of the calculated image cropping process. It is essential to define the area in which the image will be visible after the clipping.
    - Comfy dtype: INT
    - Python dtype: int
- crop_h
    - Crop_h output indicates the height of the calculated image cropping process. It works with Crop_w to determine the final visible range of the cropped image.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class PresetRatioSelector:

    @classmethod
    def INPUT_TYPES(s):
        (s.ratio_presets, s.ratio_config) = read_ratio_presets()
        return {'required': {'select_preset': (s.ratio_presets, {'default': 'none'}), 'swap_axis': (['true', 'false'], {'default': 'false'}), 'use_preset_seed': (['true', 'false'], {'default': 'false'}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}, 'hidden': {'unique_id': 'UNIQUE_ID', 'extra_pnginfo': 'EXTRA_PNGINFO', 'prompt': 'PROMPT'}}
    RETURN_TYPES = ('INT', 'INT', 'INT', 'INT', 'INT', 'INT', 'INT', 'INT')
    RETURN_NAMES = ('latent_w', 'latent_h', 'cte_w', 'cte_h', 'target_w', 'target_h', 'crop_w', 'crop_h')
    CATEGORY = 'Mikey/Utils'
    FUNCTION = 'calculate'

    def calculate(self, select_preset, swap_axis, use_preset_seed, seed, unique_id=None, extra_pnginfo=None, prompt=None):
        if use_preset_seed == 'true' and len(self.ratio_presets) > 0:
            len_presets = len(self.ratio_presets)
            offset = seed % (len_presets - 1)
            presets = [p for p in self.ratio_presets if p != 'none']
            select_preset = presets[offset]
        latent_width = self.ratio_config[select_preset]['custom_latent_w']
        latent_height = self.ratio_config[select_preset]['custom_latent_h']
        cte_w = self.ratio_config[select_preset]['cte_w']
        cte_h = self.ratio_config[select_preset]['cte_h']
        target_w = self.ratio_config[select_preset]['target_w']
        target_h = self.ratio_config[select_preset]['target_h']
        crop_w = self.ratio_config[select_preset]['crop_w']
        crop_h = self.ratio_config[select_preset]['crop_h']
        if swap_axis == 'true':
            (latent_width, latent_height) = (latent_height, latent_width)
            (cte_w, cte_h) = (cte_h, cte_w)
            (target_w, target_h) = (target_h, target_w)
            (crop_w, crop_h) = (crop_h, crop_w)
        return (latent_width, latent_height, cte_w, cte_h, target_w, target_h, crop_w, crop_h)
```