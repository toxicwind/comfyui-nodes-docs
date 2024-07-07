# Documentation
- Class name: ipadapterApply
- Category: EasyUse/Adapter
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The ipadapterApply node is designed to simplify the process of applying image processors to the input of images, using models and predefined configurations to achieve desired conversions. It emphasizes adaptability and ease of use, providing structured interfaces for users to use different settings and achieve optimal results without the need for in-depth knowledge of the specific details of complex models.

# Input types
## Required
- model
    - Model parameters are essential because they define the basic image-processing models that will be used to apply conversions to input images. They are the basis for node functions that directly affect the quality and nature of output.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- image
    - Image input is the object of node processing. The content and format are essential to determine how the model interprets and converts it and ultimately shapes the final result.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
- preset
    - Preset parameters determine the specific conversion preset to be applied, and the model guides the image according to the selected style or effect. This is a key factor in achieving the visual effect of the objective.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- lora_strength
    - The lora_strength parameter adjusts the intensity of the style transfer process to allow fine-tuning of visual output to suit user preferences. It plays an important role in the art of image conversion.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- model
    - The output model represents an image-processing model modified after the preset and other parameters selected have been applied. It is the crystallization of node processing and serves as the basis for further image conversion or analysis.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- tiles
    - The tiles output provides a partial view of the post-processed image, allowing for detailed examination and possible use for further image operations. It is an additional layer of output that enhances the usefulness of nodes in image analysis and editing.
    - Comfy dtype: IMAGE
    - Python dtype: List[PIL.Image or torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class ipadapterApply(ipadapter):

    def __init__(self):
        super().__init__()
        pass

    @classmethod
    def INPUT_TYPES(cls):
        presets = cls().presets
        return {'required': {'model': ('MODEL',), 'image': ('IMAGE',), 'preset': (presets,), 'lora_strength': ('FLOAT', {'default': 0.6, 'min': 0, 'max': 1, 'step': 0.01}), 'provider': (['CPU', 'CUDA', 'ROCM', 'DirectML', 'OpenVINO', 'CoreML'],), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05}), 'weight_faceidv2': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 5.0, 'step': 0.05}), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'cache_mode': (['insightface only', 'clip_vision only', 'all', 'none'], {'default': 'insightface only'}), 'use_tiled': ('BOOLEAN', {'default': False})}, 'optional': {'attn_mask': ('MASK',), 'optional_ipadapter': ('IPADAPTER',)}}
    RETURN_TYPES = ('MODEL', 'IMAGE', 'MASK', 'IPADAPTER')
    RETURN_NAMES = ('model', 'tiles', 'masks', 'ipadapter')
    CATEGORY = 'EasyUse/Adapter'
    FUNCTION = 'apply'

    def apply(self, model, image, preset, lora_strength, provider, weight, weight_faceidv2, start_at, end_at, cache_mode, use_tiled, attn_mask=None, optional_ipadapter=None):
        (tiles, masks) = (image, [None])
        (model, ipadapter) = self.load_model(model, preset, lora_strength, provider, clip_vision=None, optional_ipadapter=optional_ipadapter, cache_mode=cache_mode)
        if use_tiled and preset not in self.faceid_presets:
            if 'IPAdapterTiled' not in ALL_NODE_CLASS_MAPPINGS:
                self.error()
            cls = ALL_NODE_CLASS_MAPPINGS['IPAdapterTiled']
            (model, tiles, masks) = cls().apply_tiled(model, ipadapter, image, weight, 'linear', start_at, end_at, sharpening=0.0, combine_embeds='concat', image_negative=None, attn_mask=attn_mask, clip_vision=None, embeds_scaling='V only')
        elif preset in ['FACEID PLUS V2', 'FACEID PORTRAIT (style transfer)']:
            if 'IPAdapterAdvanced' not in ALL_NODE_CLASS_MAPPINGS:
                self.error()
            cls = ALL_NODE_CLASS_MAPPINGS['IPAdapterAdvanced']
            (model,) = cls().apply_ipadapter(model, ipadapter, start_at=start_at, end_at=end_at, weight=weight, weight_type='linear', combine_embeds='concat', weight_faceidv2=weight_faceidv2, image=image, image_negative=None, clip_vision=None, attn_mask=attn_mask, insightface=None, embeds_scaling='V only')
        else:
            if 'IPAdapter' not in ALL_NODE_CLASS_MAPPINGS:
                self.error()
            cls = ALL_NODE_CLASS_MAPPINGS['IPAdapter']
            (model,) = cls().apply_ipadapter(model, ipadapter, image, weight, start_at, end_at, attn_mask)
        return (model, tiles, masks, ipadapter)
```