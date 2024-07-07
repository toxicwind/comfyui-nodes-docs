# Documentation
- Class name: IPAdapterSimple
- Category: ipadapter
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

IPAdapterSimple node is designed to integrate image processors seamlessly into the workstream of the model. It applies various conversions and weights to the model based on the image and adaptor configuration provided, increasing the ability of the model to generate or process images according to a particular style or hint.

# Input types
## Required
- model
    - Model parameters are essential because they represent the core structure that will be adapted or modified by the IPAdapterSimple node. This is the main input that determines the follow-up and output of the node.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The ipadapter parameter specifies the formulation configuration that will guide image processing in the node. It is a key component that allows nodes to apply a particular style or conversion.
    - Comfy dtype: IPADAPTER
    - Python dtype: Dict[str, Any]
- image
    - The image parameter is the key input for the IPAdapterSimple node because it is the visual data that will be processed and converted according to the adaptor settings. It directly influences the final output of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- weight
    - The weight parameter adjusts the impact of the image on model output. It is a floating point value that significantly changes the processing of nodes depending on their size.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_at
    - The start_at parameter defines the starting point of the image’s influence on the model. It is a floating point value that helps to control the initial strength of the conversion.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at parameters mark the end point of the image's influence on the model. It works with start_at parameters to determine the range of conversion effects.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_type
    - Weight_type parameters indicate how weight parameters affect models. It can specify styles such as'standard', 'prompt is more important' or'style transfer', each having a different effect on the function of the node.
    - Comfy dtype: COMBO[standard, prompt is more important, style transfer]
    - Python dtype: str
## Optional
- attn_mask
    - The optional antn_mask parameter is used to specify which parts of the model should be concerned with input during the processing period. It is particularly useful for focusing the model's attention on certain areas of the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- model
    - The output model represents an adaptation or modification of the input model using the conversion of the IPAdapterSimple node. It encapsifies the new image processing capabilities assigned by the node.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterSimple:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'ipadapter': ('IPADAPTER',), 'image': ('IMAGE',), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05}), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'weight_type': (['standard', 'prompt is more important', 'style transfer'],)}, 'optional': {'attn_mask': ('MASK',)}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'apply_ipadapter'
    CATEGORY = 'ipadapter'

    def apply_ipadapter(self, model, ipadapter, image, weight, start_at, end_at, weight_type, attn_mask=None):
        if weight_type.startswith('style'):
            weight_type = 'style transfer'
        elif weight_type == 'prompt is more important':
            weight_type = 'ease out'
        else:
            weight_type = 'linear'
        ipa_args = {'image': image, 'weight': weight, 'start_at': start_at, 'end_at': end_at, 'attn_mask': attn_mask, 'weight_type': weight_type, 'insightface': ipadapter['insightface']['model'] if 'insightface' in ipadapter else None}
        if 'ipadapter' not in ipadapter:
            raise Exception('IPAdapter model not present in the pipeline. Please load the models with the IPAdapterUnifiedLoader node.')
        if 'clipvision' not in ipadapter:
            raise Exception('CLIPVision model not present in the pipeline. Please load the models with the IPAdapterUnifiedLoader node.')
        return (ipadapter_execute(model.clone(), ipadapter['ipadapter']['model'], ipadapter['clipvision']['model'], **ipa_args),)
```