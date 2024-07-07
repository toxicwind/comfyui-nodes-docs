# Documentation
- Class name: IPAdapterStyleComposition
- Category: ipadapter/style_composition
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

The IPAdapterStyleComposition node aims at seamless integration of image styles and configurations, providing a powerful framework for creative image processing. It is cleverly integrating style elements with architecture, enhancing the visual effect and consistency of the final output.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes, as they determine the bottom structure for style and image adaptation. They form the basis for node function construction, making possible the conversion of input images.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The ipadapter parameter is essential for the node because it provides the adaptor mechanism necessary for a style combination with model integration. It plays a key role in the node processing and adaptation style within the framework of the map.
    - Comfy dtype: IPADAPTER
    - Python dtype: torch.Tensor
- image_style
    - The Image_style parameter is essential for the purpose of the node because it represents the style input that will be combined with the art of other elements. It is the main visual style source that the node aims to integrate into the final image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray
- image_composition
    - The image_composition parameter is essential to define the configuration of the structure to which the style element will be integrated. It sets the stage for the node mapping process to ensure that the final image reflects the harmonious integration of style and structure.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray
## Optional
- weight_style
    - The weight_style parameter allows fine-tuning of the style effects in the combination. It is a key factor in the balance between the style of control and the structure, ensuring that the final output is consistent with the required aesthetics.
    - Comfy dtype: FLOAT
    - Python dtype: float
- combine_embeds
    - The cobine_embeds parameter determines the embedded combination method used to integrate style features. It is essential for the ability of nodes to effectively merge different style input, affecting the style consistency of the final image.
    - Comfy dtype: COMBO[concat, add, subtract, average, norm average]
    - Python dtype: str
- start_at
    - The start_at parameter defines the starting point of the construction process and allows control of the initial stages of style integration. It is an important element of the node management style application process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at parameters specify the end of the construction process, allowing control of the final stage of style integration. It is essential for nodes to determine the extent of the influence of style in the structure.
    - Comfy dtype: FLOAT
    - Python dtype: float
- embeds_scaling
    - The embeds_scaling parameter adjusts the embedded scaling used in the map, which is essential for maintaining the integrity and quality of style features throughout the process.
    - Comfy dtype: COMBO[V only, K+V, K+V w/ C penalty, K+mean(V) w/ C penalty]
    - Python dtype: str

# Output types
- composed_image
    - Composed_image output represents the end result of the style grouping process, in which style elements are harmoniously integrated into the architecture. It is evidence of visual pleasure and consistent image capabilities at nodes.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray

# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterStyleComposition(IPAdapterAdvanced):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'ipadapter': ('IPADAPTER',), 'image_style': ('IMAGE',), 'image_composition': ('IMAGE',), 'weight_style': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 5, 'step': 0.05}), 'weight_composition': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 5, 'step': 0.05}), 'expand_style': ('BOOLEAN', {'default': False}), 'combine_embeds': (['concat', 'add', 'subtract', 'average', 'norm average'], {'default': 'average'}), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'embeds_scaling': (['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty'],)}, 'optional': {'image_negative': ('IMAGE',), 'attn_mask': ('MASK',), 'clip_vision': ('CLIP_VISION',)}}
    CATEGORY = 'ipadapter/style_composition'
```