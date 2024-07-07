# Documentation
- Class name: IPAdapterMS
- Category: ipadapter/dev
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

IPAdapterMS nodes are designed to integrate image-processing models into a single framework. It facilitates the operation and enhancement of image data through a set of configured parameters, with the aim of optimizing the performance of integrated models.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes because they define the core image processing models to be used. They directly affect the ability of nodes to process and analyse image data.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The ipadapter parameter is essential for the node because it designates the adaptor that will be used to interface with the model. It plays an important role in the interaction of the node with the model and in enhancing the function of the model.
    - Comfy dtype: IPADAPTER
    - Python dtype: str
- image
    - The image parameter is the basis of the node function, which provides input data for image processing. It is the main source of the visual content that the node will operate and analyse.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- weight
    - The weight parameters allow adjustments to be made to the effect of certain aspects of image processing on the final output. It is a key factor in micro-regulating point operations to achieve the desired results.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- weight_faceidv2
    - The weight_faceidv2 parameter is used to regulate the emphasis on facial characterization in image processing. It is an optional but important factor when processing facial recognition tasks.
    - Comfy dtype: FLOAT
    - Python dtype: float
- combine_embeds
    - The cobine_embeds parameter determines the combination approach that is embedded in the node. This is a key decision point that affects the integration and consistency of node output.
    - Comfy dtype: COMBO[concat, add, subtract, average, norm average]
    - Python dtype: str
- start_at
    - Start_at parameters define the starting point for image processing operations. It is used to specify the node to start the initial phase of analysis and operation of image data.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at parameters set the end point for image processing operations. It determines the final stage of node analysis and operation of image data.
    - Comfy dtype: FLOAT
    - Python dtype: float
- embeds_scaling
    - The embeds_scaling parameter is used for embedding within the zoom node. It is an important factor in controlling the size and impact of the embedded node output.
    - Comfy dtype: COMBO[V only, K+V, K+V w/ C penalty, K+mean(V) w/ C penalty]
    - Python dtype: str
- layer_weights
    - The player_weights parameter allows the weight to be assigned to different layers within the model. It is an optional but powerful tool for customizing nodes to specific needs.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- processed_image
    - Processed_image output represents the results of image processing performed by nodes. It contains the operation and analysis of nodes and provides the final visual content after all operations have been completed.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterMS(IPAdapterAdvanced):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'ipadapter': ('IPADAPTER',), 'image': ('IMAGE',), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 5, 'step': 0.05}), 'weight_faceidv2': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 5.0, 'step': 0.05}), 'weight_type': (WEIGHT_TYPES,), 'combine_embeds': (['concat', 'add', 'subtract', 'average', 'norm average'],), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'embeds_scaling': (['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty'],), 'layer_weights': ('STRING', {'default': '', 'multiline': True})}, 'optional': {'image_negative': ('IMAGE',), 'attn_mask': ('MASK',), 'clip_vision': ('CLIP_VISION',), 'insightface': ('INSIGHTFACE',)}}
    CATEGORY = 'ipadapter/dev'
```