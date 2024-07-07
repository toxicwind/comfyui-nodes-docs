# Documentation
- Class name: ReencodeLatent
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

ReencodeLatent is a node for recoding potential expressions through a variable self-codifier (VAE). It first uses the input VAE to decode samples into pixel space and then uses the output VAE to recode them back into potential space. This node is particularly suitable for tasks that need to manipulate and analyse data in potential and pixel domains.

# Input types
## Required
- samples
    - The “samples” parameter is the key input to the ReencodeLatent node because it represents a potential sign that will be recoded. It is essential for the implementation of the node because it determines the data that will be subjected to decoding and encoding processes.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- tile_mode
    - The tile_mode parameter determines how to decode and encode pixel data. It can be set as `Noone', `Both', `Decode' only' or `Encode (output) only', which determines whether the node is to perform two operations or to perform decoding or encoding steps selectively.
    - Comfy dtype: COMBO[None, Both, Decode(input) only, Encode(output) only]
    - Python dtype: str
- input_vae
    - The " input_vae " parameter is designated as the variable coder for the initial decoding of potential samples into pixel space. It plays an important role in the function of the node, as it determines the model that affects the initial conversion of data.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- output_vae
    - The "output_vae " parameter defines the variable coder that is responsible for recoding pixel data into potential expressions. This parameter is essential because it determines the model that will form the final output of the node.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
## Optional
- tile_size
    - The "tile_size" parameter is an optional input that sets the tile size to be used in decoding and encoding. When the tile_mode is set as 'Both' or 'input' only, it is particularly important to influence the resolution of pixel data processing.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- latent
    - The "latet" output represents a potential sign of recoding after processing the node. It is important because it provides post-conversion data that can be used for further analysis or entered as a follow-up node.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ReencodeLatent:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'tile_mode': (['None', 'Both', 'Decode(input) only', 'Encode(output) only'],), 'input_vae': ('VAE',), 'output_vae': ('VAE',), 'tile_size': ('INT', {'default': 512, 'min': 320, 'max': 4096, 'step': 64})}}
    CATEGORY = 'ImpactPack/Util'
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'doit'

    def doit(self, samples, tile_mode, input_vae, output_vae, tile_size=512):
        if tile_mode in ['Both', 'Decode(input) only']:
            pixels = nodes.VAEDecodeTiled().decode(input_vae, samples, tile_size)[0]
        else:
            pixels = nodes.VAEDecode().decode(input_vae, samples)[0]
        if tile_mode in ['Both', 'Encode(output) only']:
            return nodes.VAEEncodeTiled().encode(output_vae, pixels, tile_size)
        else:
            return nodes.VAEEncode().encode(output_vae, pixels)
```