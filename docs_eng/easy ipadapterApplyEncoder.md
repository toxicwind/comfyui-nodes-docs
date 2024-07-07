# Documentation
- Class name: ipadapterApplyEncoder
- Category: EasyUse/Adapter
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The ipadapterApplyEncoder node is designed to process and adapt image data efficiently for the coding purposes in the model. It facilitates the integration of multiple image input and presets, using selected coding methods to generate embedded vectors that can be used for further analysis or model training.

# Input types
## Required
- model
    - Model parameters are essential because they define the core of the encoded process. It is a machine learning model that will process the input of images and generate embedded vectors based on selected preset and encoded methods.
    - Comfy dtype: MODEL
    - Python dtype: comfy.model_management.Model
- image1
    - Image input is essential for the node to perform its encoding function. It provides the raw data that the model will process to extract meaningful features and generate embedded vectors.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray
- preset
    - Preset parameters influence the encoding process by determining the specific settings and parameters of the model to be used. It adjusts the operation of the node to the predefined configuration to achieve the desired result.
    - Comfy dtype: COMBO
    - Python dtype: str
- num_embeds
    - Embedding numerical parameters is important because it determines the number of embedded vectors of images to be generated. This directly affects the complexity and depth of the coding process.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- combine_method
    - The parameters of the consolidation method determine how to aggregate the embedded vectors. By applying operations such as connections, additions, or averages, it can significantly change the embedded vector of the result.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- model
    - The output model is an updated version of the input model and is now equipped with a processed embedded vector. It may be used as a basis for follow-up operations or for downstream tasks.
    - Comfy dtype: MODEL
    - Python dtype: comfy.model_management.Model
- ipadapter
    - The ipadapter output is an encoded part of the node operation that covers the treated embedded vector. It is an important intermediate result that can be further analysed or used in other parts of the system.
    - Comfy dtype: IPADAPTER
    - Python dtype: comfy_ipadapter.ipadapter.IPADAPTER
- pos_embed
    - They play an important role in guiding the learning process of models and improving their predictions.
    - Comfy dtype: EMBEDS
    - Python dtype: List[torch.Tensor]
- neg_embed
    - Negative embeds the input image that does not meet the desired criteria. They help models to distinguish between relevant and unrelated features and improve their ability to make accurate judgements.
    - Comfy dtype: EMBEDS
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class ipadapterApplyEncoder(ipadapter):

    def __init__(self):
        super().__init__()
        pass

    @classmethod
    def INPUT_TYPES(cls):
        ipa_cls = cls()
        normal_presets = ipa_cls.normal_presets
        max_embeds_num = 3
        inputs = {'required': {'model': ('MODEL',), 'image1': ('IMAGE',), 'preset': (normal_presets,), 'num_embeds': ('INT', {'default': 2, 'min': 1, 'max': max_embeds_num})}, 'optional': {}}
        for i in range(1, max_embeds_num + 1):
            if i > 1:
                inputs['optional'][f'image{i}'] = ('IMAGE',)
        for i in range(1, max_embeds_num + 1):
            inputs['optional'][f'mask{i}'] = ('MASK',)
            inputs['optional'][f'weight{i}'] = ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05})
        inputs['optional']['combine_method'] = (['concat', 'add', 'subtract', 'average', 'norm average', 'max', 'min'],)
        inputs['optional']['optional_ipadapter'] = ('IPADAPTER',)
        inputs['optional']['pos_embeds'] = ('EMBEDS',)
        inputs['optional']['neg_embeds'] = ('EMBEDS',)
        return inputs
    RETURN_TYPES = ('MODEL', 'IPADAPTER', 'EMBEDS', 'EMBEDS')
    RETURN_NAMES = ('model', 'ipadapter', 'pos_embed', 'neg_embed')
    CATEGORY = 'EasyUse/Adapter'
    FUNCTION = 'apply'

    def batch(self, embeds, method):
        if method == 'concat' and len(embeds) == 1:
            return (embeds[0],)
        embeds = [embed for embed in embeds if embed is not None]
        embeds = torch.cat(embeds, dim=0)
        if method == 'add':
            embeds = torch.sum(embeds, dim=0).unsqueeze(0)
        elif method == 'subtract':
            embeds = embeds[0] - torch.mean(embeds[1:], dim=0)
            embeds = embeds.unsqueeze(0)
        elif method == 'average':
            embeds = torch.mean(embeds, dim=0).unsqueeze(0)
        elif method == 'norm average':
            embeds = torch.mean(embeds / torch.norm(embeds, dim=0, keepdim=True), dim=0).unsqueeze(0)
        elif method == 'max':
            embeds = torch.max(embeds, dim=0).values.unsqueeze(0)
        elif method == 'min':
            embeds = torch.min(embeds, dim=0).values.unsqueeze(0)
        return embeds

    def apply(self, **kwargs):
        model = kwargs['model']
        preset = kwargs['preset']
        if 'optional_ipadapter' in kwargs:
            ipadapter = kwargs['optional_ipadapter']
        else:
            (model, ipadapter) = self.load_model(model, preset, 0, 'CPU', clip_vision=None, optional_ipadapter=None, cache_mode='none')
        if 'IPAdapterEncoder' not in ALL_NODE_CLASS_MAPPINGS:
            self.error()
        encoder_cls = ALL_NODE_CLASS_MAPPINGS['IPAdapterEncoder']
        pos_embeds = kwargs['pos_embeds'] if 'pos_embeds' in kwargs else []
        neg_embeds = kwargs['neg_embeds'] if 'neg_embeds' in kwargs else []
        for i in range(1, kwargs['num_embeds'] + 1):
            if f'image{i}' not in kwargs:
                raise Exception(f'image{i} is required')
            kwargs[f'mask{i}'] = kwargs[f'mask{i}'] if f'mask{i}' in kwargs else None
            kwargs[f'weight{i}'] = kwargs[f'weight{i}'] if f'weight{i}' in kwargs else 1.0
            (pos, neg) = encoder_cls().encode(ipadapter, kwargs[f'image{i}'], kwargs[f'weight{i}'], kwargs[f'mask{i}'], clip_vision=None)
            pos_embeds.append(pos)
            neg_embeds.append(neg)
        pos_embeds = self.batch(pos_embeds, kwargs['combine_method'])
        neg_embeds = self.batch(neg_embeds, kwargs['combine_method'])
        return (model, ipadapter, pos_embeds, neg_embeds)
```