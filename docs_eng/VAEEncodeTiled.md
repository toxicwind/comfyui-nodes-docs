# Documentation
- Class name: VAEEncodeTiled
- Category: _for_testing
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The VAE EncodeTiled node is designed to use a variable self-codifier (VAE) that efficiently and in parallel encodes image data into potential spaces. It operates by dividing large images into smaller, self-processable areas, and then reassemblysing them. This method is particularly appropriate for processing high-resolution images, which may not be able to adapt to memory as a whole. The node is abstractly flattening and coding complex and provides a simplified interface for users to use VAE for encoding tasks.

# Input types
## Required
- pixels
    - The `pixels' parameter is the input image data processed by the node. It is essential because it is the original material of the encoded process. The node expects the data to be available in formats compatible with the coding VAE model, usually involving image pixels.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - The `vae' parameter represents the variable coder model, which is used to encode image data. This model is essential to the function of the node, as it defines the structure and parameters of the encoded process.
    - Comfy dtype: VAE
    - Python dtype: AutoencoderKL
## Optional
- tile_size
    - The `tile_size' parameter determines the size of an input image that is classified as a sheet for processing. This is an optional parameter that allows users to control the particle size of the sheet, which may affect performance and memory use.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- samples
    - The ‘samples’ output contains the coding of the input image in potential space. This is the main result of node operations and is important for any follow-up task that requires a condensed understanding of the image’s bottom structure.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class VAEEncodeTiled:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pixels': ('IMAGE',), 'vae': ('VAE',), 'tile_size': ('INT', {'default': 512, 'min': 320, 'max': 4096, 'step': 64})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'encode'
    CATEGORY = '_for_testing'

    def encode(self, vae, pixels, tile_size):
        t = vae.encode_tiled(pixels[:, :, :, :3], tile_x=tile_size, tile_y=tile_size)
        return ({'samples': t},)
```