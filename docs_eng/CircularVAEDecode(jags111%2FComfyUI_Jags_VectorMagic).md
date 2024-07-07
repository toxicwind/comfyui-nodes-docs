# Documentation
- Class name: CircularVAEDecode
- Category: Jags_vector/latent
- Output node: False
- Repo Ref: https://github.com/jags111/ComfyUI_Jags_VectorMagic

This node ensures consistency in the image generated at the boundary by preparing the volume layers of the model for the decoding process of the VAE.

# Input types
## Required
- samples
    - Enter the sample to represent the potential vector of the VAE encoder, which is essential for generating the image. It drives the entire decoding process and directly affects the quality and characteristics of the output image.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- vae
    - The VAE parameter refers to the variable coder model used to decode a potential sample into an image. It is essential for the function of the node, as it encapsifies the distribution of the data learned.
    - Comfy dtype: VAE
    - Python dtype: comfy.sd.VAE

# Output types
- image
    - The output image is the result of using the VAE model decoding to enter a potential sample. It represents the visual performance of coded data and is a direct product of node operations.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class CircularVAEDecode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'vae': ('VAE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'decode'
    CATEGORY = 'Jags_vector/latent'

    def decode(self, vae, samples):
        for layer in [layer for layer in vae.first_stage_model.modules() if isinstance(layer, torch.nn.Conv2d)]:
            layer.padding_mode = 'circular'
        return (vae.decode(samples['samples']),)
```