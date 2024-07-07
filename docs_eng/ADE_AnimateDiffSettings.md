# Documentation
- Class name: AnimateDiffSettingsNode
- Category: Animate Diff 🎭🅐🅓/ad settings
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

AnimatéDiffSettingsNode is designed to generate animation settings for adjusting landscape differences. It encapsulates the logic of repositioning and weighting, which is essential to the animation process. The main function of the node is to provide a structured approach to animation of differences and to ensure that adjustments are applied consistently and efficiently throughout the animation sequence.

# Input types
## Optional
- pe_adjust
    - The p_adjust parameter allows fine-tuning of the position embedded in the animation. This is essential for the spatial distribution and movement required to achieve the animation element. This parameter directly affects the spatial aspects of the animation and affects the overall quality and consistency of the animation landscape.
    - Comfy dtype: PE_ADJUST
    - Python dtype: Union[AdjustGroup, None]
- weight_adjust
    - The weight_adjust parameter is used to modify the weights associated with the animated elements. It plays an important role in controlling the intensity and focus of the animated effects. By adjusting the weight, nodes can enhance or reduce the specific aspects of the animated drawings, thus obtaining more detailed and targeted visual results.
    - Comfy dtype: WEIGHT_ADJUST
    - Python dtype: Union[AdjustGroup, None]

# Output types
- ad_settings
    - The ad_settings output provides a set of comprehensive animation settings adjusted to input parameters. This output is essential for the next steps in animating the waterline, as it determines how animated differences will be reflected in the final rendering scenario.
    - Comfy dtype: AD_SETTINGS
    - Python dtype: AnimateDiffSettings

# Usage tips
- Infra type: CPU

# Source code
```
class AnimateDiffSettingsNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'optional': {'pe_adjust': ('PE_ADJUST',), 'weight_adjust': ('WEIGHT_ADJUST',)}}
    RETURN_TYPES = ('AD_SETTINGS',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/ad settings'
    FUNCTION = 'get_ad_settings'

    def get_ad_settings(self, pe_adjust: AdjustGroup=None, weight_adjust: AdjustGroup=None):
        return (AnimateDiffSettings(adjust_pe=pe_adjust, adjust_weight=weight_adjust),)
```