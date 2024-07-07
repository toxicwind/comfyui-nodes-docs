# Documentation
- Class name: ipadapterApplyEmbeds
- Category: EasyUse/Adapter
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node facilitates the application of the location to the model and enhances the model's ability to process spatial information in the data entered. It aims to enhance the model's performance by integrating additional contextual clues, thereby providing a more detailed indication of the input data.

# Input types
## Required
- model
    - Model parameters are essential because they are core components of node modification. It represents a machine learning model to be embedded in the location, which is essential for the operation of node and the subsequent performance of the model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The ipadapter parameter is essential for the node, as it provides the necessary interface between the model and the position embedded. It ensures that the embedding is correctly applied and integrated into the structure of the model, affecting the overall function and output of the node.
    - Comfy dtype: IPADAPTER
    - Python dtype: IPAdapter
- pos_embed
    - The pos_embed parameter is essential to the function of the node, which represents the embedding of the location to be applied to the model. These embeddings provide the spatial information needed for the model to understand and process the input data.
    - Comfy dtype: EMBEDS
    - Python dtype: torch.Tensor
- weight
    - The weight parameter influences the importance of the position embedded in the model. It is an important factor in determining how the embedding will affect the output of the model, and therefore also affects the quality of the results produced by the node.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_type
    - The weight_type parameter determines the type of weight to be applied to the position embedded, which is important for shaping the model's response to input data. It affects the overall adaptability and effectiveness of nodes in modifying model behaviour.
    - Comfy dtype: COMBO[weight_types]
    - Python dtype: str
- start_at
    - The start_at parameter specifies the starting point of the application where the place is embedded, which is essential for the operation of the node. It determines that the model begins to combine the initial context of space information and affects the overall interpretation and processing of the data.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at parameters define the endpoint where the application is embedded and play a key role in the function of the node. It sets the limits to what extent the model integrates spatial information, thus affecting the comprehensiveness of the model's understanding of input data.
    - Comfy dtype: FLOAT
    - Python dtype: float
- embeds_scaling
    - The embeds_scaling parameter adjusts the embedded zoom ratio, which is essential for controlling the impact of position information on models. It directly affects the ability of nodes to balance the contribution of embedding with other features and ensures the best expression of input data.
    - Comfy dtype: COMBO[ ['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty']]
    - Python dtype: str
## Optional
- attn_mask
    - When providing antn_mask parameters, it helps nodes focus on some parts of the input data by ignoring irrelevant information. This increases the ability of models to focus on the most important aspects of the data, thus producing more accurate and relevant results.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- model
    - The model output represents the application of a modified machine learning model embedded in the location. It is the main result of the node, demonstrates the increased capacity of the model to process spatial information and provides a more detailed understanding of input data.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The ipadapter output is an intermediate component that promotes position embedding that is applied to the model. It is used as evidence of successful embedding and ensures that the model is now better able to process space information.
    - Comfy dtype: IPADAPTER
    - Python dtype: IPAdapter

# Usage tips
- Infra type: CPU

# Source code
```
class ipadapterApplyEmbeds(ipadapter):

    def __init__(self):
        super().__init__()
        pass

    @classmethod
    def INPUT_TYPES(cls):
        ipa_cls = cls()
        weight_types = ipa_cls.weight_types
        return {'required': {'model': ('MODEL',), 'ipadapter': ('IPADAPTER',), 'pos_embed': ('EMBEDS',), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05}), 'weight_type': (weight_types,), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'embeds_scaling': (['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty'],)}, 'optional': {'neg_embed': ('EMBEDS',), 'attn_mask': ('MASK',)}}
    RETURN_TYPES = ('MODEL', 'IPADAPTER')
    RETURN_NAMES = ('model', 'ipadapter')
    CATEGORY = 'EasyUse/Adapter'
    FUNCTION = 'apply'

    def apply(self, model, ipadapter, pos_embed, weight, weight_type, start_at, end_at, embeds_scaling, attn_mask=None, neg_embed=None):
        if 'IPAdapterEmbeds' not in ALL_NODE_CLASS_MAPPINGS:
            self.error()
        cls = ALL_NODE_CLASS_MAPPINGS['IPAdapterEmbeds']
        (model,) = cls().apply_ipadapter(model, ipadapter, pos_embed, weight, weight_type, start_at, end_at, neg_embed=neg_embed, attn_mask=attn_mask, clip_vision=None, embeds_scaling=embeds_scaling)
        return (model, ipadapter)
```