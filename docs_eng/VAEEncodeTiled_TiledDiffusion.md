# Documentation
- Class name: VAEEncodeTiled_TiledDiffusion
- Category: _for_testing
- Output node: False
- Repo Ref: https://github.com/shiimizu/ComfyUI-TiledDiffusion

The node covers the process of encoded and diffused data and optimizes memory use and processing efficiency. It is designed to manage large-scale data conversions by dividing input into manageable flats, thereby contributing to efficient computing and resource allocation.

# Input types
## Required
- pixels
    - The image data entered is essential for the encoding and diffusion process because it provides the original material for the node to perform the conversion. Without this input, node cannot generate a potential expression.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - The VAE model is at the heart of the coding process and is responsible for converting input data into potential space and then for further diffusion.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- tile_size
    - Flatten size parameters determine the particle size of the input data, directly affecting the efficiency of the coding and diffusion process. A careful selection is necessary to balance the use of resources and memory.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- fast
    - When fast parameters are enabled, nodes are allowed to perform certain optimizations, thus accelerating the coding and diffusion process, although there may be qualitative trade-offs.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- color_fix
    - When this parameter is activated, apply colour correction steps to input data to ensure that potential space is more robust and less prone to forgery.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- latent
    - The potential expression of the output is a compressed version of the input data that captures the basic features and structure of the low-dimensional space. It is a key component of the next diffusion step.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class VAEEncodeTiled_TiledDiffusion(TiledVAE):

    @classmethod
    def INPUT_TYPES(s):
        fast = True
        tile_size = get_rcmd_enc_tsize()
        return {'required': {'pixels': ('IMAGE',), 'vae': ('VAE',), 'tile_size': ('INT', {'default': tile_size, 'min': 256, 'max': 4096, 'step': 16}), 'fast': ('BOOLEAN', {'default': fast}), 'color_fix': ('BOOLEAN', {'default': fast})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'process'
    CATEGORY = '_for_testing'

    def __init__(self):
        self.is_decoder = False
        super().__init__()
```