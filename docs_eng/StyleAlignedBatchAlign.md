# Documentation
- Class name: StyleAlignedBatchAlign
- Category: style_aligned
- Output node: False
- Repo Ref: https://github.com/brianfitzgerald/style_aligned_comfy

The StyleAlignedBatchAllign class aims to modify the given model by changing the style features of the batch alignment model to enhance its ability to process and produce style alignment outputs. The node focuses on the conceptual integration of style elements, ensuring that model attention and standardization are optimized for style consistency.

# Input types
## Required
- model
    - Model parameters are essential because they define the basic architecture that will be modified to match the style features across batches. It is the main input that determines the behaviour and function of the StyleAlignedBatchAlign node.
    - Comfy dtype: ModelPatcher
    - Python dtype: comfy.model_patcher.ModelPatcher
- share_norm
    - Share_norm parameters are essential to determine how the homogeneity layer within the model should be shared or modified. It affects the efficiency and effectiveness of the style feature alignment within the model.
    - Comfy dtype: str
    - Python dtype: str
- share_attn
    - Share_attn parameters specify which attention mechanisms should be shared or modified to achieve style alignment. It plays an important role in the overall style of the model.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- scale
    - The scale parameter adjustment applies to the degree of style alignment between the attention and the homogeneity layer. It delicately influences the ability of the model to produce a coherent output across batches.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- MODEL
    - The output model is the result of StyleAlignedBatchAlign operation, representing a modified version of the input model that optimizes style alignment. It is the crystallization of node efforts to integrate and align style features within the model structure.
    - Comfy dtype: ModelPatcher
    - Python dtype: comfy.model_patcher.ModelPatcher

# Usage tips
- Infra type: CPU

# Source code
```
class StyleAlignedBatchAlign:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('MODEL',), 'share_norm': (SHARE_NORM_OPTIONS,), 'share_attn': (SHARE_ATTN_OPTIONS,), 'scale': ('FLOAT', {'default': 1, 'min': 0, 'max': 1.0, 'step': 0.1})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = 'style_aligned'

    def patch(self, model: ModelPatcher, share_norm: str, share_attn: str, scale: float):
        m = model.clone()
        share_group_norm = share_norm in ['group', 'both']
        share_layer_norm = share_norm in ['layer', 'both']
        register_shared_norm(model, share_group_norm, share_layer_norm)
        args = StyleAlignedArgs(share_attn)
        m.set_model_attn1_patch(SharedAttentionProcessor(args, scale))
        return (m,)
```