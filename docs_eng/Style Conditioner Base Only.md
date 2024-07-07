# Documentation
- Class name: StyleConditionerBaseOnly
- Category: Mikey/Conditioning
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The `add_style' method of the StyleConditioner BaseOnly node is designed to integrate user-defined styles into the reconciliation process. It allows the application of style preferences by combining positive and negative hints with underlying adjustment elements. The method intelligently manages the integration of these styles, adjusts their effects to the specified strength factors and supports the use of seeds for style selection. This node plays a vital role in enabling style control during generation, and does not itself directly process generation.

# Input types
## Required
- style
    - The style parameter plays a key role in determining the style direction of the reconciliation process. It determines the particular positive and negative hints that will guide the production. The choice of style has a far-reaching effect on the output of the result, making it an important element in node operations.
    - Comfy dtype: STRING
    - Python dtype: str
- strength
    - The Strength parameter controls the intensity of the style influence that should be applied to the reconciliation process. It is a floating point number that adjusts the weight of style impact and allows fine-tuning of style elements in the output. This parameter is essential for achieving the desired balance between style control and underlying regulation elements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- positive_cond_base
    - The " positionive_cond_base " parameter represents the fundamental positive adjustment element that will be influenced by the style. It is a key component in node operations, as it forms the basis for applying style adjustments. This parameter is essential for creating the initial positive context of the generation process.
    - Comfy dtype: CONDITIONING
    - Python dtype: Conditioning
- negative_cond_base
    - The "negative_cond_base" parameter is the underlying negative adjustment element that will be influenced by the style. It plays an important role in shaping the output, comparing it by providing a positive balance. This parameter is essential to ensure that the content generated meets the required style constraints, while avoiding undesirable elements.
    - Comfy dtype: CONDITIONING
    - Python dtype: Conditioning
- base_clip
    - The " base_clip" parameter is a reference image or clip that serves as a visual basis for the reconciliation process. It is essential to provide a stable visual context where style will be applied. This parameter is essential to ensure style adjustments within a given visual framework.
    - Comfy dtype: CLIP
    - Python dtype: CLIP
## Optional
- use_seed
    - The 'use_seed'parameter determines whether the torrent value should be used to select the style from the available options. When set to 'true', it introduces random elements for the style selection process, which may be useful for diversified output. This parameter is important for increasing the variability of the generation process.
    - Comfy dtype: COMBO['true', 'false']
    - Python dtype: str
- seed
    - The “seed” parameter is used in conjunction with the “use_seed” parameter to control randomity in style selection. It provides a specific reference point for the random number generator and ensures a repeatable selection process. When it comes to randomity, this parameter is important for consistency in the multiple run of nodes.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- base_pos_cond
    - The Base_pos_cond output represents the positive adjustment element updated after applying the style. It is a key component in node operations, as it brings style adjustments into the subsequent stages of the generation process.
    - Comfy dtype: CONDITIONING
    - Python dtype: Conditioning
- base_neg_cond
    - The Base_neg_cond output is an element of negative regulation that is updated after the application of the style. It plays an important role in ensuring that the content is produced in line with style constraints and avoiding undesirable elements.
    - Comfy dtype: CONDITIONING
    - Python dtype: Conditioning
- style_str
    - The " style_str " output provides a text expression for the applied style. It may be useful as a record of the style selection made during the reconciliation process for tracking and recording the parameters for generating the data.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class StyleConditionerBaseOnly:

    @classmethod
    def INPUT_TYPES(s):
        (s.styles, s.pos_style, s.neg_style) = read_styles()
        return {'required': {'style': (s.styles,), 'strength': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'positive_cond_base': ('CONDITIONING',), 'negative_cond_base': ('CONDITIONING',), 'base_clip': ('CLIP',), 'use_seed': (['true', 'false'], {'default': 'false'}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'STRING')
    RETURN_NAMES = ('base_pos_cond', 'base_neg_cond', 'style_str')
    FUNCTION = 'add_style'
    CATEGORY = 'Mikey/Conditioning'

    def add_style(self, style, strength, positive_cond_base, negative_cond_base, base_clip, use_seed, seed):
        if use_seed == 'true' and len(self.styles) > 0:
            offset = seed % len(self.styles)
            style = self.styles[offset]
        pos_prompt = self.pos_style[style]
        neg_prompt = self.neg_style[style]
        pos_prompt = pos_prompt.replace('{prompt}', '')
        neg_prompt = neg_prompt.replace('{prompt}', '')
        if style == 'none':
            return (positive_cond_base, negative_cond_base, style)
        positive_cond_base_new = CLIPTextEncodeSDXL.encode(self, base_clip, 1024, 1024, 0, 0, 1024, 1024, pos_prompt, pos_prompt)[0]
        negative_cond_base_new = CLIPTextEncodeSDXL.encode(self, base_clip, 1024, 1024, 0, 0, 1024, 1024, neg_prompt, neg_prompt)[0]
        positive_cond_base = ConditioningAverage.addWeighted(self, positive_cond_base_new, positive_cond_base, strength)[0]
        negative_cond_base = ConditioningAverage.addWeighted(self, negative_cond_base_new, negative_cond_base, strength)[0]
        return (positive_cond_base, negative_cond_base, style)
```