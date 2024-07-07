# Documentation
- Class name: IPAdapterStyleCompositionBatch
- Category: Style Composition
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

The IPAdapterStyleCompositionBatch node is designed to facilitate a combination of image styles and images in bulk processing. It combines style adaptation techniques to integrate different visual elements seamlessly, emphasizing the importance of style consistency in the generation of images.

# Input types
## Required
- model
    - Model parameters are essential to the operation of nodes because they define the underlying neural network structure used for style combinations. They directly affect the ability of nodes to generate images with the required style features.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The ipadapter parameter is essential for adapting the input image to the style of the model. It plays an important role in ensuring that the input image is consistent with the style expectations of the model in order to achieve an effective style mix.
    - Comfy dtype: IPADAPTER
    - Python dtype: torch.Tensor
- image_style
    - The Image_style parameter is the key input that provides a reference to the style of the grouping process. It determines the visual style that the output image should display and influences the aesthetic results as a whole.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image_composition
    - The image_composition parameter is the basis for a combination of node operations. It is an image that will be stymied and converted according to the style provided by the image_style and will form the final output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- weight_style
    - The weight_style parameter allows fine-tuning of the effect of style input on the final combination. It is particularly useful when it needs to be balanced between the original combination and the style of application.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_composition
    - Weight_composition parameters adjust the contribution of the group element to the final output. It is important for harmonious integration in the style and combination of image generation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- expand_style
    - Expand_style parameters determine whether styles should be extended to suit the combination. This may be important to ensure that styles are applied evenly throughout the image.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- start_at
    - Start_at parameters specify the starting point of the group process. It is used to control the initial phase of the style application and to influence the progress of the group.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at parameters mark the end of the grouping process. It determines the final stage of the style application and affects the range of styles applied throughout the group.
    - Comfy dtype: FLOAT
    - Python dtype: float
- embeds_scaling
    - The embeds_scaling parameter is used to select the embedded scaling methods involved in the style combination. It is a key factor in determining the quality and properties of the images in the combination.
    - Comfy dtype: COMBO['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty']
    - Python dtype: str

# Output types
- composed_images
    - Composed_images output represents the end result of the style grouping process. It contains the ability to display nodes based on the synthesizing and grouping of input parameters.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterStyleCompositionBatch(IPAdapterStyleComposition):

    def __init__(self):
        self.unfold_batch = True

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'ipadapter': ('IPADAPTER',), 'image_style': ('IMAGE',), 'image_composition': ('IMAGE',), 'weight_style': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 5, 'step': 0.05}), 'weight_composition': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 5, 'step': 0.05}), 'expand_style': ('BOOLEAN', {'default': False}), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'embeds_scaling': (['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty'],)}, 'optional': {'image_negative': ('IMAGE',), 'attn_mask': ('MASK',), 'clip_vision': ('CLIP_VISION',)}}
```