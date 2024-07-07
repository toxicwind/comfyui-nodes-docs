# Documentation
- Class name: VAEDecode
- Category: latent
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The VAEDecode node is designed to convert potential expressions back to the original data space. Using the decoding power of the VAE, it reconfigures images from the potential vector of its code. This process is essential for generating new data examples similar to the original data set in structure and content.

# Input types
## Required
- samples
    - The `samples' parameter is the key input to the VAEDecode node because it provides a potential indication that the node will be decoded into an image. It is essential to the reconstructing process, because the quality of the decoded image depends to a large extent on the certainty of these potential vectors.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- vae
    - The `vae' parameter specifies a pre-training variable to decode a potential sample. This is a mandatory input, because the node relies on the parameters of the model and the distribution it learns to perform the decoding process.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module

# Output types
- IMAGE
    - The output of the VAEDecode node is a reconstructed image that is generated from the potential expression of decoding. This output is important because it demonstrates the ability of the node to generate consistent images that reflect the input of potential space.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class VAEDecode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'vae': ('VAE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'decode'
    CATEGORY = 'latent'

    def decode(self, vae, samples):
        return (vae.decode(samples['samples']),)
```