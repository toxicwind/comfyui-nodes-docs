# Documentation
- Class name: StableCascade_EmptyLatentImage
- Category: latent/stable_cascade
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The StableCascade_EmptyLentImage node is designed to generate the potential representation of images at different stages of the cascade model. It operates by creating zero fills that correspond to the dimensions specified in the input parameters, which are essential for initializing the potential state during the process of stabilizing the cascades.

# Input types
## Required
- width
    - Width parameters define the width of a potential image, which is essential for determining the dimensions of the mass generated. It affects the structure of the potential space and therefore the quality of output of the cascade model.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - High parameters specify the height of the potential image, which is a key factor in the mass shape. It plays an important role in the underlying overall structure and influences the performance of the cascade model.
    - Comfy dtype: INT
    - Python dtype: int
- compression
    - Compression parameter control applies to the compression level of the potential image dimensions. It is essential to manage the balance between the complexity of the model and the computational efficiency, as well as the validity of the output of the cascade model.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- batch_size
    - The catch_size parameter indicates the number of samples to be processed in an iterative manner. It is important to optimize the implementation of nodes and can influence the throughput of cascade models.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- stage_c
    - The stage_c output provides a potential indication of the rough phase of the cascade, which is a key component of the initial phase of image generation.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- stage_b
    - The stage_b output provides a potential indication of the base phase of the cascade, which is essential for the follow-up phase of image refinement.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class StableCascade_EmptyLatentImage:

    def __init__(self, device='cpu'):
        self.device = device

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 1024, 'min': 256, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'height': ('INT', {'default': 1024, 'min': 256, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'compression': ('INT', {'default': 42, 'min': 4, 'max': 128, 'step': 1}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 4096})}}
    RETURN_TYPES = ('LATENT', 'LATENT')
    RETURN_NAMES = ('stage_c', 'stage_b')
    FUNCTION = 'generate'
    CATEGORY = 'latent/stable_cascade'

    def generate(self, width, height, compression, batch_size=1):
        c_latent = torch.zeros([batch_size, 16, height // compression, width // compression])
        b_latent = torch.zeros([batch_size, 4, height // 4, width // 4])
        return ({'samples': c_latent}, {'samples': b_latent})
```