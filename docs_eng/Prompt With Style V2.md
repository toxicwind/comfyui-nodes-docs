# Documentation
- Class name: PromptWithStyleV2
- Category: Mikey
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

PromptWithStyleV2 node is designed to generate and fine-tune tips with specified styles, ensuring that the content generated is consistent with the desired artistic or thematic direction. It uses a combination of positive and negative hints and style parameters to guide the creation process, thus generating subtle outputs that reflect input criteria.

# Input types
## Required
- positive_prompt
    - The prompt is the key input that guides content generation, setting the tone of creativity and helping to achieve the desired style and subject matter elements in the output.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt
    - Negative hints are used to exclude elements or features that are not required to generate the content. It refines the output by specifying what should be avoided, thereby enhancing the overall consistency and focus of the result.
    - Comfy dtype: STRING
    - Python dtype: str
- style
    - A style parameter is essential to define the aesthetic or thematic direction of the content generated. It affects the selection of artistic elements and the overall appearance and feeling of the output.
    - Comfy dtype: STRING
    - Python dtype: str
- ratio_selected
    - The ratio_selected parameter determines the width ratio of the content generated, which is essential for maintaining the required visual drawings and layouts.
    - Comfy dtype: STRING
    - Python dtype: str
- clip_base
    - The clip_base parameter is the reference used to encode the texttip and decode the underlying CLIP model as a potential space expression.
    - Comfy dtype: CLIP
    - Python dtype: CLIP
- clip_refiner
    - Clip_refiner parameters represent refined CLIP models used to further improve the quality and specificity of creating tips.
    - Comfy dtype: CLIP
    - Python dtype: CLIP
## Optional
- batch_size
    - Batch size is an optional parameter that allows users to control the number of samples generated in a single operation. It can be adjusted to the specific requirements of the resource and the task at hand.
    - Comfy dtype: INT
    - Python dtype: int
- seed
    - Seeds are optional parameters to ensure that the generation process is replicable. They are particularly useful when consistent results are needed in multiple operations.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- samples
    - The sample output contains the potential expression generated, which can be further processed or used as input to other nodes in the workflow.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- base_pos_cond
    - Base_pos_cond output provides positive reconciliation information based on the base CLIP model, which can be used to guide the generation process towards desired characteristics.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- base_neg_cond
    - Base_neg_cond output provides negative adjustment information based on the base CLIP model, which helps to avoid the generation of unwanted elements in the content.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- refiner_pos_cond
    - Refiner_pos_cond output displays positive reconciliations from refined CLIP models, which enhances the specificity and quality of generating tips.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- refiner_neg_cond
    - Refiner_neg_cond output provides negative reconciliations from refined CLIP models to ensure that the content generated is subject to specified constraints and avoids certain features.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- positive_prompt
    - The positionive_prompt output reflects the final positive hint used during the generation and contains the required quality and subject matter that has been encoded in the output.
    - Comfy dtype: STRING
    - Python dtype: str
- negative_prompt
    - Negative_prompt output represents the last negative hint used in generating the output, specifying the elements and features that should be omitted from the creation content.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class PromptWithStyleV2:

    @classmethod
    def INPUT_TYPES(s):
        (s.ratio_sizes, s.ratio_dict) = read_ratios()
        (s.styles, s.pos_style, s.neg_style) = read_styles()
        return {'required': {'positive_prompt': ('STRING', {'multiline': True, 'default': 'Positive Prompt'}), 'negative_prompt': ('STRING', {'multiline': True, 'default': 'Negative Prompt'}), 'style': (s.styles,), 'ratio_selected': (s.ratio_sizes,), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'clip_base': ('CLIP',), 'clip_refiner': ('CLIP',)}}
    RETURN_TYPES = ('LATENT', 'CONDITIONING', 'CONDITIONING', 'CONDITIONING', 'CONDITIONING', 'STRING', 'STRING')
    RETURN_NAMES = ('samples', 'base_pos_cond', 'base_neg_cond', 'refiner_pos_cond', 'refiner_neg_cond', 'positive_prompt', 'negative_prompt')
    FUNCTION = 'start'
    CATEGORY = 'Mikey'

    def start(self, clip_base, clip_refiner, positive_prompt, negative_prompt, style, ratio_selected, batch_size, seed):
        """ get output from PromptWithStyle.start """
        (latent, pos_prompt, neg_prompt, pos_style, neg_style, width, height, refiner_width, refiner_height) = PromptWithStyle.start(self, positive_prompt, negative_prompt, style, ratio_selected, batch_size, seed)
        ratio = min([width, height]) / max([width, height])
        (target_width, target_height) = (4096, 4096 * ratio // 8 * 8) if width > height else (4096 * ratio // 8 * 8, 4096)
        refiner_width = target_width
        refiner_height = target_height
        sdxl_pos_cond = CLIPTextEncodeSDXL.encode(self, clip_base, width, height, 0, 0, target_width, target_height, pos_prompt, pos_style)[0]
        sdxl_neg_cond = CLIPTextEncodeSDXL.encode(self, clip_base, width, height, 0, 0, target_width, target_height, neg_prompt, neg_style)[0]
        refiner_pos_cond = CLIPTextEncodeSDXLRefiner.encode(self, clip_refiner, 6, refiner_width, refiner_height, pos_prompt)[0]
        refiner_neg_cond = CLIPTextEncodeSDXLRefiner.encode(self, clip_refiner, 2.5, refiner_width, refiner_height, neg_prompt)[0]
        return (latent, sdxl_pos_cond, sdxl_neg_cond, refiner_pos_cond, refiner_neg_cond, pos_prompt, neg_prompt)
```