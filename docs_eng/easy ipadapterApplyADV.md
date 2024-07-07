# Documentation
- Class name: ipadapterApplyAdvanced
- Category: EasyUse/Adapter
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node promotes advanced applications of image-processing models, enabling users to integrate seamlessly into presets, weights and other parameters to refine and customize the conversion process. It emphasizes adaptability and control, providing an advanced interface for users to achieve complex image operations without going into the details of bottom algorithms.

# Input types
## Required
- model
    - Model parameters are essential because it defines the core of the image-processing framework. It determines the type of conversion and analysis that will be performed on the input image and significantly affects the quality and characteristics of the final output.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- image
    - Image parameters are the main input for node operations. The content and format are essential in determining how the model is handled and converted, ultimately shaping the results of the image operations.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
- preset
    - Preset parameters allow the user to select the predefined settings and adjust the behaviour of the model to the specific case. By providing optimal configuration, it simplifys the process and ensures that nodes function efficiently for the intended purpose.
    - Comfy dtype: COMBO
    - Python dtype: str
- lora_strength
    - The lora_strength parameter fine-tuning model adapts to the input image and allows fine-tuning to improve the authenticity and consistency of the final output. It plays a key role in achieving a balance between generalization and customization of the model.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- model
    - The output model represents an enhanced or improved version of the model after processing the node. It contains the results of image operations and reflects the effectiveness of the node in achieving the desired conversion.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- tiles
    - The tiles output consists of parts of the input image, each of which is treated by applying models and parameters. It provides a detailed view of image operations at the particle level, showing the ability of nodes to process complex conversions.
    - Comfy dtype: IMAGE
    - Python dtype: List[PIL.Image or torch.Tensor]
- masks
    - Masks output is a series of binary matrices corresponding to processed tiles. It plays an important role in isolating and highlighting specific areas of converted images, demonstrating the accuracy and control of nodes in the editing process.
    - Comfy dtype: MASK
    - Python dtype: List[PIL.Image or torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class ipadapterApplyAdvanced(ipadapter):

    def __init__(self):
        super().__init__()
        pass

    @classmethod
    def INPUT_TYPES(cls):
        ipa_cls = cls()
        presets = ipa_cls.presets
        weight_types = ipa_cls.weight_types
        return {'required': {'model': ('MODEL',), 'image': ('IMAGE',), 'preset': (presets,), 'lora_strength': ('FLOAT', {'default': 0.6, 'min': 0, 'max': 1, 'step': 0.01}), 'provider': (['CPU', 'CUDA', 'ROCM', 'DirectML', 'OpenVINO', 'CoreML'],), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05}), 'weight_faceidv2': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 5.0, 'step': 0.05}), 'weight_type': (weight_types,), 'combine_embeds': (['concat', 'add', 'subtract', 'average', 'norm average'],), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'embeds_scaling': (['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty'],), 'cache_mode': (['insightface only', 'clip_vision only', 'all', 'none'], {'default': 'insightface only'}), 'use_tiled': ('BOOLEAN', {'default': False}), 'use_batch': ('BOOLEAN', {'default': False}), 'sharpening': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.05})}, 'optional': {'image_negative': ('IMAGE',), 'attn_mask': ('MASK',), 'clip_vision': ('CLIP_VISION',), 'optional_ipadapter': ('IPADAPTER',)}}
    RETURN_TYPES = ('MODEL', 'IMAGE', 'MASK', 'IPADAPTER')
    RETURN_NAMES = ('model', 'tiles', 'masks', 'ipadapter')
    CATEGORY = 'EasyUse/Adapter'
    FUNCTION = 'apply'

    def apply(self, model, image, preset, lora_strength, provider, weight, weight_faceidv2, weight_type, combine_embeds, start_at, end_at, embeds_scaling, cache_mode, use_tiled, use_batch, sharpening, image_negative=None, clip_vision=None, attn_mask=None, optional_ipadapter=None):
        (tiles, masks) = (image, [None])
        (model, ipadapter) = self.load_model(model, preset, lora_strength, provider, clip_vision=clip_vision, optional_ipadapter=optional_ipadapter, cache_mode=cache_mode)
        if use_tiled:
            if use_batch:
                if 'IPAdapterTiledBatch' not in ALL_NODE_CLASS_MAPPINGS:
                    self.error()
                cls = ALL_NODE_CLASS_MAPPINGS['IPAdapterTiledBatch']
            else:
                if 'IPAdapterTiled' not in ALL_NODE_CLASS_MAPPINGS:
                    self.error()
                cls = ALL_NODE_CLASS_MAPPINGS['IPAdapterTiled']
            (model, tiles, masks) = cls().apply_tiled(model, ipadapter, image, weight, weight_type, start_at, end_at, sharpening=sharpening, combine_embeds=combine_embeds, image_negative=image_negative, attn_mask=attn_mask, clip_vision=clip_vision, embeds_scaling=embeds_scaling)
        else:
            if use_batch:
                if 'IPAdapterBatch' not in ALL_NODE_CLASS_MAPPINGS:
                    self.error()
                cls = ALL_NODE_CLASS_MAPPINGS['IPAdapterBatch']
            else:
                if 'IPAdapterAdvanced' not in ALL_NODE_CLASS_MAPPINGS:
                    self.error()
                cls = ALL_NODE_CLASS_MAPPINGS['IPAdapterAdvanced']
            (model,) = cls().apply_ipadapter(model, ipadapter, weight=weight, weight_type=weight_type, start_at=start_at, end_at=end_at, combine_embeds=combine_embeds, weight_faceidv2=weight_faceidv2, image=image, image_negative=image_negative, clip_vision=clip_vision, attn_mask=attn_mask, insightface=None, embeds_scaling=embeds_scaling)
        return (model, tiles, masks, ipadapter)
```