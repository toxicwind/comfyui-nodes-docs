# Documentation
- Class name: StableCascade_SuperResolutionControlnet
- Category: _for_testing/stable_cascade
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

StableCascade_SuperResultionContronet is designed to improve the resolution of images by means of stable cascades. It encodes the input image using the VAE and generates a control signal for hyper-resolution. This process is designed to magnify the image while maintaining its integrity and detail.

# Input types
## Required
- image
    - The input image is a basic parameter of the node because it is the original data used for ultra-resolution processing. Its quality and resolution directly influence the output of the node, determining the ultimate increase in the clarity and detail of the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - The VAE parameter is essential for the operation of the node, as it provides the encoding mechanism needed to generate the control signal. The selection and configuration of VAE can significantly influence the ability of the node to zoom effectively in the image.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module

# Output types
- controlnet_input
    - Contronet_input, a processing version of the input image, has been coded and is ready for hyper-resolution control networks. This is a key intermediate step that helps generate high-quality magnifying images.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- stage_c
    - The stage_c output represents a potential expression of a rough level, which is a key component of the ultra-resolution process. It captures broader features of the image and is used to guide the upward extension to a higher resolution.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- stage_b
    - The stage_b output represents a potential indication of a more finer particle size, which is essential to add details to the magnified image. It ensures that the final image retains complex details and textures after the ultra-resolution process.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class StableCascade_SuperResolutionControlnet:

    def __init__(self, device='cpu'):
        self.device = device

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'vae': ('VAE',)}}
    RETURN_TYPES = ('IMAGE', 'LATENT', 'LATENT')
    RETURN_NAMES = ('controlnet_input', 'stage_c', 'stage_b')
    FUNCTION = 'generate'
    CATEGORY = '_for_testing/stable_cascade'

    def generate(self, image, vae):
        width = image.shape[-2]
        height = image.shape[-3]
        batch_size = image.shape[0]
        controlnet_input = vae.encode(image[:, :, :, :3]).movedim(1, -1)
        c_latent = torch.zeros([batch_size, 16, height // 16, width // 16])
        b_latent = torch.zeros([batch_size, 4, height // 2, width // 2])
        return (controlnet_input, {'samples': c_latent}, {'samples': b_latent})
```