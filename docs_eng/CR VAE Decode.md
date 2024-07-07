# Documentation
- Class name: CR_VAEDecode
- Category: Comfyroll/Essential/Core
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_VAEDecode node is designed to decode potential expressions into images using pre-trained variable coders (VAE). It is the basic component in the model that can rebuild images from the potential vector of compression. This node is particularly suitable for visualizing potential spaces and generating new samples that can be used for further analysis or creative applications.

# Input types
## Required
- samples
    - The'samples' parameter is essential because it contains the potential expression that nodes will decode into images. It directly influences the output and determines the diversity and quality of the images generated.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- vae
    - The ‘vae’ parameter specifies the node that will be used to decode potential samples for pre-training conversion to the encoder model. The selection of the VAE model is essential for the function of the node, as it determines the structure and capability of the code process.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
## Optional
- tiled
    - The `tiled' parameter is an optional boolean symbol, and when set to True, the indicator node decodes the sample in a levelled manner. This may be useful for processing larger images or when a specific decoding mode is required.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- circular
    - `circurlar' is another optional boolean parameter, which, when activated, applies the loop fill mode to the volume layers in the VAE model. This may be important to maintain continuity of image features at the boundary.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- IMAGE
    - The `IMAGE' output contains decoded images from input potential samples. It represents an understanding of the main results of the code process and is important for visual analysis and further image operations.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - The'show_help' output provides a URL link to the document page to obtain further help and detailed information about node operations. This is very useful for users seeking additional guidance or understanding of node capabilities.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: GPU

# Source code
```
class CR_VAEDecode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'vae': ('VAE',), 'tiled': ('BOOLEAN', {'default': False}), 'circular': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'vae_decode'
    CATEGORY = icons.get('Comfyroll/Essential/Core')

    def vae_decode(self, samples, vae, circular=False, tiled=False):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Core-Nodes#cr-vae-decode'
        if circular == True:
            for layer in [layer for layer in vae.first_stage_model.modules() if isinstance(layer, torch.nn.Conv2d)]:
                layer.padding_mode = 'circular'
        if tiled == True:
            c = vae.decode_tiled(samples['samples'], tile_x=512, tile_y=512)
        else:
            c = vae.decode(samples['samples'])
        return (c, show_help)
```