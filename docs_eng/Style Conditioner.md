# Documentation
- Class name: StyleConditioner
- Category: Mikey/Conditioning
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The StyleConditioner node is designed to manage and apply style conditions to the generation process. It allows for the integration of both positive and negative style tips, allowing the generated content to be fine-tuned to the required style properties. The node plays a key role in guiding the process towards a particular aesthetic or artistic direction.

# Input types
## Required
- style
    - The `style' parameter is essential for determining the style direction of the generation process. It influences the selection of both positive and negative tips that will shape the output results.
    - Comfy dtype: STRING
    - Python dtype: str
- strength
    - The `strength' parameter adjusts the strength of the style to influence the process. It is important when controlling the extent to which style features are reflected in the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- positive_cond_base
    - The `positive_cond_base' parameter represents the basic positive condition element that will be combined with the new positive hint to fine-tune the resulting style.
    - Comfy dtype: CONDITIONING
    - Python dtype: Conditioning
- negative_cond_base
    - The `negative_cond_base' parameter indicates the essential negative condition elements used to balance style effects in the generation process.
    - Comfy dtype: CONDITIONING
    - Python dtype: Conditioning
- positive_cond_refiner
    - The `positive_cond_refiner' parameter is used to further refine the positive aspects of style in the generation process.
    - Comfy dtype: CONDITIONING
    - Python dtype: Conditioning
- negative_cond_refiner
    - The `negative_cond_refiner' parameter is used to ensure that the negative aspects of style are minimized in the final output.
    - Comfy dtype: CONDITIONING
    - Python dtype: Conditioning
- base_clip
    - The `base_clip' parameter is essential for encoding basic positive and negative hints into forms that can be processed by generating models.
    - Comfy dtype: CLIP
    - Python dtype: Clip
- refiner_clip
    - The `refiner_clip' parameter is used to encode refined positive and negative hints to further enhance the impact of style on generation.
    - Comfy dtype: CLIP
    - Python dtype: Clip
- use_seed
    - The `use_seed' parameter decides whether to select a particular style based on the seeds provided, adding a layer of control to the style selection process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- seed
    - The `seed' parameter is used in conjunction with the `use_seed' logo and, when a torrent is used, specifies the starting point of the style selection.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- base_pos_cond
    - The `base_pos_cond' output represents the basic positive condition of the update and reflects the integrated style features.
    - Comfy dtype: CONDITIONING
    - Python dtype: Conditioning
- base_neg_cond
    - The `base_neg_cond' output represents the basic negative condition of the update, which helps to remove unwanted style elements from the generation.
    - Comfy dtype: CONDITIONING
    - Python dtype: Conditioning
- refiner_pos_cond
    - `refiner_pos_cond' output is a refined positive condition element that further shapes the style in which content is generated.
    - Comfy dtype: CONDITIONING
    - Python dtype: Conditioning
- refiner_neg_cond
    - `refiner_neg_cond' output is a refined negative condition element to ensure that negative styles are excluded from generation.
    - Comfy dtype: CONDITIONING
    - Python dtype: Conditioning
- style_str
    - The `style_str' output provides a text expression in the applied style and a descriptive summary of the style's impact on generation.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class StyleConditioner:

    @classmethod
    def INPUT_TYPES(s):
        (s.styles, s.pos_style, s.neg_style) = read_styles()
        return {'required': {'style': (s.styles,), 'strength': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.1}), 'positive_cond_base': ('CONDITIONING',), 'negative_cond_base': ('CONDITIONING',), 'positive_cond_refiner': ('CONDITIONING',), 'negative_cond_refiner': ('CONDITIONING',), 'base_clip': ('CLIP',), 'refiner_clip': ('CLIP',), 'use_seed': (['true', 'false'], {'default': 'false'}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'CONDITIONING', 'CONDITIONING', 'STRING')
    RETURN_NAMES = ('base_pos_cond', 'base_neg_cond', 'refiner_pos_cond', 'refiner_neg_cond', 'style_str')
    FUNCTION = 'add_style'
    CATEGORY = 'Mikey/Conditioning'

    def add_style(self, style, strength, positive_cond_base, negative_cond_base, positive_cond_refiner, negative_cond_refiner, base_clip, refiner_clip, use_seed, seed):
        if use_seed == 'true' and len(self.styles) > 0:
            offset = seed % len(self.styles)
            style = self.styles[offset]
        pos_prompt = self.pos_style[style]
        neg_prompt = self.neg_style[style]
        pos_prompt = pos_prompt.replace('{prompt}', '')
        neg_prompt = neg_prompt.replace('{prompt}', '')
        if style == 'none':
            return (positive_cond_base, negative_cond_base, positive_cond_refiner, negative_cond_refiner, style)
        positive_cond_base_new = CLIPTextEncodeSDXL.encode(self, base_clip, 1024, 1024, 0, 0, 1024, 1024, pos_prompt, pos_prompt)[0]
        negative_cond_base_new = CLIPTextEncodeSDXL.encode(self, base_clip, 1024, 1024, 0, 0, 1024, 1024, neg_prompt, neg_prompt)[0]
        positive_cond_refiner_new = CLIPTextEncodeSDXLRefiner.encode(self, refiner_clip, 6, 4096, 4096, pos_prompt)[0]
        negative_cond_refiner_new = CLIPTextEncodeSDXLRefiner.encode(self, refiner_clip, 2.5, 4096, 4096, neg_prompt)[0]
        positive_cond_base = ConditioningAverage.addWeighted(self, positive_cond_base_new, positive_cond_base, strength)[0]
        negative_cond_base = ConditioningAverage.addWeighted(self, negative_cond_base_new, negative_cond_base, strength)[0]
        positive_cond_refiner = ConditioningAverage.addWeighted(self, positive_cond_refiner_new, positive_cond_refiner, strength)[0]
        negative_cond_refiner = ConditioningAverage.addWeighted(self, negative_cond_refiner_new, negative_cond_refiner, strength)[0]
        return (positive_cond_base, negative_cond_base, positive_cond_refiner, negative_cond_refiner, style)
```