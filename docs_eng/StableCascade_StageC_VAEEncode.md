# Documentation
- Class name: StableCascade_StageC_VAEEncode
- Category: latent/stable_cascade
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The `StableCascade_StageC_VAEENcode'node is designed to encode images as a potential expression using a variable self-codifier (VAE). It will enter the resolution required for sampling the images and then apply VAE to generate potential spatial expressions of compression. This node plays a crucial role in image compression and reconstruction, making the storage and transmission of visual data more efficient.

# Input types
## Required
- image
    - Enter the image parameter is essential for the operation of the node, as it is the node process to generate the original data in a potential expression. The quality and resolution of the image directly influences the output of the node and the subsequent performance of any downstream task.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - VAE parameters represent the variable-to-codator model, which is used by nodes to encode the input image as potential space. VAE model selection and configuration of significant impact nodes are capable of compressing and effectively reconstructing the image.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- compression
    - The compressed parameters determine the lower sampling level of the pre-coding image, which is a key factor in balancing the quality of the reconstructed image with the efficiency of the encoded process. It allows the operation of micro-reconcerting points according to specific needs.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- stage_c
    - The'stage_c' output represents the potential for compression of input images generated by VAE. It is a key component of the cascade in the image processing phase as input for further refinement or analysis during the subsequent phase.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- stage_b
    - The'stage_b' output is a potential sign of a place to supplement the'stage_c' output. It is initially zero and can be used for extension or extra processing in more complex image operations.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class StableCascade_StageC_VAEEncode:

    def __init__(self, device='cpu'):
        self.device = device

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'vae': ('VAE',), 'compression': ('INT', {'default': 42, 'min': 4, 'max': 128, 'step': 1})}}
    RETURN_TYPES = ('LATENT', 'LATENT')
    RETURN_NAMES = ('stage_c', 'stage_b')
    FUNCTION = 'generate'
    CATEGORY = 'latent/stable_cascade'

    def generate(self, image, vae, compression):
        width = image.shape[-2]
        height = image.shape[-3]
        out_width = width // compression * vae.downscale_ratio
        out_height = height // compression * vae.downscale_ratio
        s = comfy.utils.common_upscale(image.movedim(-1, 1), out_width, out_height, 'bicubic', 'center').movedim(1, -1)
        c_latent = vae.encode(s[:, :, :, :3])
        b_latent = torch.zeros([c_latent.shape[0], 4, height // 8 * 2, width // 8 * 2])
        return ({'samples': c_latent}, {'samples': b_latent})
```