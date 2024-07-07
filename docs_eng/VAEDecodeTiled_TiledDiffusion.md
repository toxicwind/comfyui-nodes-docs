# Documentation
- Class name: VAEDecodeTiled_TiledDiffusion
- Category: _for_testing
- Output node: False
- Repo Ref: https://github.com/shiimizu/ComfyUI-TiledDiffusion

The node is designed to decode and reconstruct images from potential expressions using the VAE model, emphasizing the processing of large images through tiling and diffusion techniques. It is designed to balance the trade-off between computing efficiency and image quality and to provide a sound solution to the image reconstruction task.

# Input types
## Required
- samples
    - Enter the sample to represent the potential spatial vector that the node is used to generate the reconstructed image. These are essential because they form the basis of the image reconstruction process.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- vae
    - The VAE parameter refers to the pre-training decoder model used by nodes to perform decoding processes. It is essential to reconstruct images from potential space.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- tile_size
    - The flatten size parameter determines the size of the tile used to process the image. It is important to optimize memory use and computational efficiency during decoding.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- fast
    - When fast parameters are enabled, nodes are allowed to decode faster at the expense of potential image quality. It affects the balance between speed and accuracy in the reconstruction process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- image
    - The output image is the result of a node decoding process that represents the original reconstruction version entered from the potential space. It is the key output that represents the primary function of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class VAEDecodeTiled_TiledDiffusion(TiledVAE):

    @classmethod
    def INPUT_TYPES(s):
        tile_size = get_rcmd_dec_tsize() * opt_f
        return {'required': {'samples': ('LATENT',), 'vae': ('VAE',), 'tile_size': ('INT', {'default': tile_size, 'min': 48 * opt_f, 'max': 4096, 'step': 16}), 'fast': ('BOOLEAN', {'default': True})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'process'
    CATEGORY = '_for_testing'

    def __init__(self):
        self.is_decoder = True
        super().__init__()
```