# Documentation
- Class name: WLSH_VAE_Encode_For_Inpaint_Padding
- Category: WLSH Nodes/inpainting
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The node is designed to encode image data using the VAE model in order to carry out image restoration tasks when filling is considered. It processes the input image and the mask to generate potential expressions that can be used for further images to complete or generate.

# Input types
## Required
- pixels
    - Entering image pixels is essential for the encoding process because they provide the raw data needed for VAE to generate potential expressions. The image size is adjusted to the model’s input requirements.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - The VAE model is the core component of this node, which encodes the input image into potential space. Its configuration and weight directly influences the quality of the code.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- mask
    - The mask parameter is essential to define the areas of interest in the image that need to be repaired. It works with image pixels to guide the coding process for VAE.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- mask_padding
    - This parameter defines the filling size around the mask for erosion operations, which helps to fine-tune the noise mask used in the encoding process. It indirectly affects the quality of the potential expression.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- samples
    - The output sample represents a potential representation of the code of the image entered and is the main output of this node, which can be used for various restoration or generation tasks.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- noise_mask
    - Noise mask is an auxiliary output that provides information about the area covered in the image. It is used to assist in restoring the process of reconstruction or generation in the mission.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class WLSH_VAE_Encode_For_Inpaint_Padding:

    def __init__(self, device='cpu'):
        self.device = device

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pixels': ('IMAGE',), 'vae': ('VAE',), 'mask': ('MASK',), 'mask_padding': ('INT', {'default': 24, 'min': 6, 'max': 128, 'step': 2})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'encode'
    CATEGORY = 'WLSH Nodes/inpainting'

    def encode(self, vae, pixels, mask, mask_padding=3):
        x = pixels.shape[1] // 64 * 64
        y = pixels.shape[2] // 64 * 64
        mask = torch.nn.functional.interpolate(mask[None, None], size=(pixels.shape[1], pixels.shape[2]), mode='bilinear')[0][0]
        pixels = pixels.clone()
        if pixels.shape[1] != x or pixels.shape[2] != y:
            pixels = pixels[:, :x, :y, :]
            mask = mask[:x, :y]
        kernel_tensor = torch.ones((1, 1, mask_padding, mask_padding))
        mask_erosion = torch.clamp(torch.nn.functional.conv2d(mask.round()[None], kernel_tensor, padding=3), 0, 1)
        m = 1.0 - mask.round()
        for i in range(3):
            pixels[:, :, :, i] -= 0.5
            pixels[:, :, :, i] *= m
            pixels[:, :, :, i] += 0.5
        t = vae.encode(pixels)
        return ({'samples': t, 'noise_mask': mask_erosion[0][:x, :y].round()},)
```