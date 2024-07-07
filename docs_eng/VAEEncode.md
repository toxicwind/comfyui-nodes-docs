# Documentation
- Class name: VAEEncode
- Category: latent
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The VAEEncode node is designed to convert input data into potential spatial expressions using the VAE model. It encapsifies the encoded process, which is essential for tasks such as decomposition, feature extraction, and modelling. The node abstractes the complexity of encoding algorithms and provides a simplified interface for users to take advantage of VAE's powerful functionality.

# Input types
## Required
- pixels
    - The `pixels' parameter is the original image data processed by the VAEENcode node, which is used to generate potential expressions. It plays a central role in the function of the node, as it is a direct input into the encoded process. The quality and properties of the `pixels' data directly affect the potential space generated.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - The `vae' parameter indicates that the node is used to encode the input pixels to potential spaces as a model of the variable coder. It is an important part of the node because it defines the structure and parameters of VAE, which in turn affects the encoded results.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module

# Output types
- samples
    - The `samples' output of the VAEncode node contains potential spatial indications for the input of pixels. This is a key output because it captures the essence of the input data in compressed form and applies to various downstream tasks such as classification, clustering or further generation processes.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class VAEEncode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pixels': ('IMAGE',), 'vae': ('VAE',)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'encode'
    CATEGORY = 'latent'

    def encode(self, vae, pixels):
        t = vae.encode(pixels[:, :, :, :3])
        return ({'samples': t},)
```