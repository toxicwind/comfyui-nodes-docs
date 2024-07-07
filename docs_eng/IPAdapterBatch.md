# Documentation
- Class name: IPAdapterBatch
- Category: Image Processing
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

IPAdapterBatch nodes are designed to efficiently process image data in bulk, using the processing capacity of the bottom IPAdapterAdvanced class. It focuses on integrating images with other models or processing pipes to ensure that image data are formatted correctly and with appropriate weights in order to achieve optimal performance.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes because they define machine learning models that will be used to process image data. They directly affect the execution of nodes and the quality of the results produced.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The ipadapter parameter is essential because it designates the adaptor that will be used to integrate image data with models. It plays an important role in the way the image data are processed and its subsequent results.
    - Comfy dtype: IPADAPTER
    - Python dtype: Any
- image
    - Image input is essential to the function of the node, providing raw data that will be processed and converted by the model. It is the main source of information for node operations.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- weight
    - The weight parameters allow adjustments to the impact of image data on model output. This is particularly important when it comes to microregulating point behaviour for specific applications.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_type
    - The weight_type parameter determines how the weight will be applied to image data, which is critical to controlling the emphasis on different aspects of data during processing.
    - Comfy dtype: WEIGHT_TYPES
    - Python dtype: str
- start_at
    - Start_at parameters define the starting point for processing image data, which is useful for focusing on specific areas or features in the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at parameters mark the end point of image data processing and allow the selection of a subset of image data to be considered.
    - Comfy dtype: FLOAT
    - Python dtype: float
- embeds_scaling
    - The parameters of embeds_scaling are important because it determines the embedded scaling method and influences the expression and use of image characteristics in the model.
    - Comfy dtype: COMBO['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty']
    - Python dtype: str
## Optional
- image_negative
    - The optional Image_negative parameter provides an additional image for comparison or comparison, which enhances the ability of nodes to distinguish between similar images.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- attn_mask
    - When the antn_mask parameters are provided, they can be used to specify which parts of the image data should be noticed or ignored during the processing of the model.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- clip_vision
    - Clip_vision parameters are used to integrate CLIP visual models to enhance image feature extraction, which increases the performance of nodes in some applications.
    - Comfy dtype: CLIP_VISION
    - Python dtype: Any

# Output types

# Usage tips
- Infra type: CPU

# Source code
```
class IPAdapterBatch(IPAdapterAdvanced):

    def __init__(self):
        self.unfold_batch = True

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'ipadapter': ('IPADAPTER',), 'image': ('IMAGE',), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 5, 'step': 0.05}), 'weight_type': (WEIGHT_TYPES,), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'embeds_scaling': (['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty'],)}, 'optional': {'image_negative': ('IMAGE',), 'attn_mask': ('MASK',), 'clip_vision': ('CLIP_VISION',)}}
```