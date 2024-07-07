# Documentation
- Class name: IPAdapterTiledBatch
- Category: Image Processing
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

IPAdapterTiledBatch node is designed to adapt and process image data in bulk format and to use laminative techniques for efficient computing. It is particularly suitable for handling large images or requiring batch processing. The node emphasizes flexibility and performance and allows customization through a variety of parameters that influence the image conversion process.

# Input types
## Required
- model
    - Model parameters are essential for nodes because they define the underlying model for image processing. They directly affect the execution of nodes and post-processing image quality.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The ipadapter parameter is essential for the operation of the node because it has been assigned the appropriate mixer to level image data. It plays a key role in the ability of the node to handle large images effectively.
    - Comfy dtype: IPADAPTER
    - Python dtype: Any
- image
    - The image parameter is the basis of the node function because it represents the input image to be processed. The output of the node depends heavily on the quality and characteristics of the input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- weight
    - The weight parameter allows adjustments to the impact of image processing on the final output. It is important because it provides a method for controlling the intensity of image conversion.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_type
    - The weight type parameter determines the weighted type to be applied to image processing. It is important because it can significantly change the treatment of nodes and the image characteristics generated.
    - Comfy dtype: WEIGHT_TYPES
    - Python dtype: str
- start_at
    - Start_at parameters specify the starting point for image processing. It is important because it determines where the node starts its operations.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at parameters define the end of image processing. It is critical because it sets limits on node processing image data.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sharpening
    - Sharpening parameters are used to enhance the clarity of the post-processing image. It is important because it increases the visual quality of the output by increasing the severity.
    - Comfy dtype: FLOAT
    - Python dtype: float
- embeds_scaling
    - The embeds_scaling parameter is used to zoom in during image processing. It is important because it influences the dimensions and quality of the embedding and affects the performance of nodes.
    - Comfy dtype: COMBO['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty']
    - Python dtype: str
- image_negative
    - The image_negative parameter is used to provide negative examples for image processing. It may be important when applying comparative learning.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- attn_mask
    - The antn_mask parameter is used to shield parts of the image during processing. It is important to focus the attention of nodes on specific areas of the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- clip_vision
    - The clip_vision parameter is used to integrate the CLIP visual model into image processing. It may be important for tasks that need to understand and generate image features.
    - Comfy dtype: CLIP_VISION
    - Python dtype: Any

# Output types
- processed_images
    - Processed_images output contains the results of image processing performed by nodes. It is important because it represents the final output of node operations.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class IPAdapterTiledBatch(IPAdapterTiled):

    def __init__(self):
        self.unfold_batch = True

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'ipadapter': ('IPADAPTER',), 'image': ('IMAGE',), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05}), 'weight_type': (WEIGHT_TYPES,), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'sharpening': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 'embeds_scaling': (['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty'],)}, 'optional': {'image_negative': ('IMAGE',), 'attn_mask': ('MASK',), 'clip_vision': ('CLIP_VISION',)}}
```