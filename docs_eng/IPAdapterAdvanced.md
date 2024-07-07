# Documentation
- Class name: IPAdapterAdvanced
- Category: ipadapter
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

IPAdapterAdvanced nodes are designed to apply advanced image processing techniques using the IPAdapter model. It combines intelligently with different embedded and weights to enhance the performance of the model in tasks such as style and combination transfer. The node plays a key role in adapting the model to specific image processing requirements, ensuring that the output meets the required aesthetic and technical standards.

# Input types
## Required
- model
    - Model parameters are essential for the IPAdapterAdvanced node because it defines the baseline model that will apply image processing techniques. It directly affects the execution of nodes and the quality of post-processing images.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The ipadapter parameter is a key component of the node function that provides the necessary fit and configuration for image processing tasks. It determines how the model interacts with the input image to achieve the desired results.
    - Comfy dtype: IPADAPTER
    - Python dtype: Dict[str, Any]
- image
    - An image parameter is essential because it represents the input image that the node will process. The quality and properties of the image significantly influence the operation and final output of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- weight
    - The weight parameters allow the user to adjust the impact of image processing on the model. This is important for the performance of the microreconciliation point in order to achieve the required balance between the original image and the processed image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- model
    - The output model of the IPAdapterAdvanced node is a processing model that integrates advanced image-processing techniques. It is important because it represents the final state of all conversion applications of the model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterAdvanced:

    def __init__(self):
        self.unfold_batch = False

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'ipadapter': ('IPADAPTER',), 'image': ('IMAGE',), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 5, 'step': 0.05}), 'weight_type': (WEIGHT_TYPES,), 'combine_embeds': (['concat', 'add', 'subtract', 'average', 'norm average'],), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'embeds_scaling': (['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty'],)}, 'optional': {'image_negative': ('IMAGE',), 'attn_mask': ('MASK',), 'clip_vision': ('CLIP_VISION',)}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'apply_ipadapter'
    CATEGORY = 'ipadapter'

    def apply_ipadapter(self, model, ipadapter, start_at, end_at, weight=1.0, weight_style=1.0, weight_composition=1.0, expand_style=False, weight_type='linear', combine_embeds='concat', weight_faceidv2=None, image=None, image_style=None, image_composition=None, image_negative=None, clip_vision=None, attn_mask=None, insightface=None, embeds_scaling='V only', layer_weights=None):
        is_sdxl = isinstance(model.model, (comfy.model_base.SDXL, comfy.model_base.SDXLRefiner, comfy.model_base.SDXL_instructpix2pix))
        if image_style is not None:
            if not is_sdxl:
                raise Exception('Style + Composition transfer is only available for SDXL models at the moment.')
            image = image_style
            weight = weight_style
            if image_composition is None:
                image_composition = image_style
            weight_type = 'strong style and composition' if expand_style else 'style and composition'
        ipa_args = {'image': image, 'image_composition': image_composition, 'image_negative': image_negative, 'weight': weight, 'weight_composition': weight_composition, 'weight_faceidv2': weight_faceidv2, 'weight_type': weight_type, 'combine_embeds': combine_embeds, 'start_at': start_at, 'end_at': end_at, 'attn_mask': attn_mask, 'unfold_batch': self.unfold_batch, 'embeds_scaling': embeds_scaling, 'insightface': insightface if insightface is not None else ipadapter['insightface']['model'] if 'insightface' in ipadapter else None, 'layer_weights': layer_weights}
        if 'ipadapter' in ipadapter:
            ipadapter_model = ipadapter['ipadapter']['model']
            clip_vision = clip_vision if clip_vision is not None else ipadapter['clipvision']['model']
        else:
            ipadapter_model = ipadapter
            clip_vision = clip_vision
        if clip_vision is None:
            raise Exception('Missing CLIPVision model.')
        del ipadapter
        return (ipadapter_execute(model.clone(), ipadapter_model, clip_vision, **ipa_args),)
```