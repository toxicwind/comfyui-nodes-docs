# Documentation
- Class name: IPAdapterFaceID
- Category: ipadapter/faceid
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

IPAdapterFaceID is designed to integrate and process facial recognition data in imaging processes. It uses advanced models to improve the accuracy of facial recognition tasks and to ensure that the system can reliably identify individuals from images.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes because they define machine learning models for facial recognition. They are the backbone of facial recognition processes that enable nodes to analyse and process facial features.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The ipadapter parameter is necessary because it provides nodes with the necessary interface to communicate with other components of the system and facilitates the exchange of facial recognition data.
    - Comfy dtype: IPADAPTER
    - Python dtype: str
- image
    - Image input is essential to the function of the node, providing visual data for facial recognition model analysis. It is a node processing source for identification by extracting facial features.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- weight
    - The weight parameter allows an adjustment of the effect of facial recognition on the overall result. It is an adjustment factor that can be modified to achieve a balance between accuracy and performance.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_faceidv2
    - The weight_faceidv2 parameter is used to fine-tune the contribution of Facid version 2 models in the facial recognition process. It allows the impact of custom models on the final identification results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- combine_embeds
    - The cobine_embeds parameters determine the combination of different embeddings in facial recognition. It is a key factor in integrating facial signature data to enhance identification capabilities.
    - Comfy dtype: COMBO[concat, add, subtract, average, norm average]
    - Python dtype: str
- start_at
    - Start_at parameters specify the starting point of the facial feature extraction process. It is used to control the image snippets used for facial recognition.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at parameters mark the end of the facial feature extraction process. Together with start_at, it defines the image range for analysis.
    - Comfy dtype: FLOAT
    - Python dtype: float
- embeds_scaling
    - The embeds_scaling parameter is responsible for zooming into the mosaic used in facial recognition. It resizes the feature vector to optimize the recognition process.
    - Comfy dtype: COMBO[V only, K+V, K+V w/ C penalty, K+mean(V) w/ C penalty]
    - Python dtype: str

# Output types
- face_id_output
    - Face_id_output provides the final facial recognition after entering the image through model processing. It is the crystallization of node analysis and represents the result of the identification task.
    - Comfy dtype: OUTPUT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterFaceID(IPAdapterAdvanced):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'ipadapter': ('IPADAPTER',), 'image': ('IMAGE',), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05}), 'weight_faceidv2': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 5.0, 'step': 0.05}), 'weight_type': (WEIGHT_TYPES,), 'combine_embeds': (['concat', 'add', 'subtract', 'average', 'norm average'],), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'embeds_scaling': (['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty'],)}, 'optional': {'image_negative': ('IMAGE',), 'attn_mask': ('MASK',), 'clip_vision': ('CLIP_VISION',), 'insightface': ('INSIGHTFACE',)}}
    CATEGORY = 'ipadapter/faceid'
```