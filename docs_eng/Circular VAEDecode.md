# Documentation
- Class name: CircularVAEDecode
- Category: latent
- Output node: False
- Repo Ref: https://github.com/FlyingFireCo/tiled_ksampler.git

The CircurarVAEDecode node is designed to decode the potential expression back to the image using a variable self-codifier (VAE). In particular, it changes the fill mode of the volume layer in VAE to `circular', which helps to deal with marginal effects, especially for image generation tasks. The main function of the node is to convert potential spatial data into a visual format that allows interpretation and visualization of coded information.

# Input types
## Required
- samples
    - The'samles' parameter is essential because it preserves the potential expression of the node that will decode the image. It is a mandatory input that directly influences the output of the node and determines the quality and characteristics of the image generated.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- vae
    - The 'vae' parameter represents the variable coder model, which is used by nodes to decode potential samples. This is a necessary input that determines the structure and functional aspects of the code process.
    - Comfy dtype: VAE
    - Python dtype: comfy.sd.VAE

# Output types
- image
    - The 'image' output is the main result of nodes, representing decoded images generated from potential samples. It represents a successful conversion of potential space data into an understandable visual format for humans.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor

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
    CATEGORY = 'latent'

    def decode(self, vae, samples):
        for layer in [layer for layer in vae.first_stage_model.modules() if isinstance(layer, torch.nn.Conv2d)]:
            layer.padding_mode = 'circular'
        return (vae.decode(samples['samples']),)
```