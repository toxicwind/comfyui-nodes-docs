# Documentation
- Class name: IPAdapterEmbeds
- Category: ipadapter/embeds
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

IPAdapterEmbeds node is designed to adapt IPAdapter to the given model. By using the capabilities of IPAdapter, it customizes the embedded space of the model to allow fine-tuning of model behaviour to suit specific input characteristics. The node abstractly presents the complexity of the embedded operation and provides a simplified interface for model enhancement.

# Input types
## Required
- model
    - Model parameters are necessary because they represent the basic model that will be adapted by IPAdapter. It is the main input parameter that determines the structure and behaviour of the results-adaptation model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The ipadapter parameter specifies the adaptor that will be used to modify the model. It is a key component that can customise the embedded capabilities of the model.
    - Comfy dtype: IPADAPTER
    - Python dtype: Dict[str, Any]
- pos_embed
    - The pos_embed parameter provides a positive-adjection input to guide the fit-out process. It plays an important role in shaping the adaptation model's response to specific characteristics.
    - Comfy dtype: EMBEDS
    - Python dtype: torch.Tensor
- weight
    - The weight parameter determines the impact of the IPAdapter modification on the model. It is a key factor in controlling the suitability.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_type
    - The weight_type parameter defines the way in which the weight is applied in different layers of the model. It is important for pointing the fit focus to the specific area of the model.
    - Comfy dtype: WEIGHT_TYPES
    - Python dtype: str
- start_at
    - The start_at parameter establishes the starting point of the fit-out process. It is essential to define the initial conditions under which the model begins to fit.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at parameters mark the end of the fit-out process. It is essential to specify the conditions at the end of the fit-out.
    - Comfy dtype: FLOAT
    - Python dtype: float
- embeds_scaling
    - The parameters of embeds_scaling determine the scale or combination that is embedded in the model. This is a key setup that can significantly influence the performance of the matching model.
    - Comfy dtype: COMBO['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty']
    - Python dtype: str
## Optional
- neg_embed
    - The neg_embed parameter provides negative embedding input, which can be used during the fit-out period to balance the orientation towards embedding. It helps to fine-tune the model's attention to the desired characteristics.
    - Comfy dtype: EMBEDS
    - Python dtype: torch.Tensor
- attn_mask
    - The antn_mask parameter is used to apply a mask to the attention mechanism during the fit-out period, which is important for controlling the flow of information within the model.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- clip_vision
    - The clip_vision parameter specifies the CLIP Vision model, which can be used in conjunction with IPAdapter to enhance feature extraction.
    - Comfy dtype: CLIP_VISION
    - Python dtype: torch.nn.Module

# Output types
- model
    - The output model is an appropriate version of the input model, modified according to the specifications provided by the IPAdapterEmbeds node. It represents the results of the fit-out process.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterEmbeds:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'ipadapter': ('IPADAPTER',), 'pos_embed': ('EMBEDS',), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05}), 'weight_type': (WEIGHT_TYPES,), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'embeds_scaling': (['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty'],)}, 'optional': {'neg_embed': ('EMBEDS',), 'attn_mask': ('MASK',), 'clip_vision': ('CLIP_VISION',)}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'apply_ipadapter'
    CATEGORY = 'ipadapter/embeds'

    def apply_ipadapter(self, model, ipadapter, pos_embed, weight, weight_type, start_at, end_at, neg_embed=None, attn_mask=None, clip_vision=None, embeds_scaling='V only'):
        ipa_args = {'pos_embed': pos_embed, 'neg_embed': neg_embed, 'weight': weight, 'weight_type': weight_type, 'start_at': start_at, 'end_at': end_at, 'attn_mask': attn_mask, 'embeds_scaling': embeds_scaling}
        if 'ipadapter' in ipadapter:
            ipadapter_model = ipadapter['ipadapter']['model']
            clip_vision = clip_vision if clip_vision is not None else ipadapter['clipvision']['model']
        else:
            ipadapter_model = ipadapter
            clip_vision = clip_vision
        if clip_vision is None and neg_embed is None:
            raise Exception('Missing CLIPVision model.')
        del ipadapter
        return (ipadapter_execute(model.clone(), ipadapter_model, clip_vision, **ipa_args),)
```