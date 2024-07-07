# Documentation
- Class name: WAS_VAEEncodeForInpaint
- Category: latent/inpaint
- Output node: False
- Repo Ref: https://github.com/WASasquatch/WAS_Extras

The WAS_VAEENcodeForInpaint node is designed to encode image pixels as a potential spatial expression suitable for the image restoration mission. It uses pre-trained VAE (distributive encoder) to achieve this conversion, taking into account a mask that defines the area of image restoration. The function of the node is focused on preparing data for VAE and generating potential expressions that can be used in the follow-up restoration process.

# Input types
## Required
- pixels
    - The `pixels' parameter is the original image data processed by the node. It is essential for the encoded process, as it is an input into VAE. The quality and resolution of the image data directly influences the potential expression generated, which in turn affects the restoration results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - The `vae' parameter represents a pre-training variable from the encoder model used to encode image data to potential space. The selection of the VAE model has a significant impact on the coding process and the quality of the potential expression.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- mask
    - The `mask' parameter is a binary mask used to identify areas in the image that need to be repaired. It is essential to guide the encoding process to focus on the relevant parts of the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- mask_offset
    - The `mask_offset' parameter allows changes to the boundary of the mask, which are useful for controlling the range of restorations. The positive-value extension mask, and the negative-value shrink mask. This parameter indirectly affects the area that VAE considers when encoding.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- samples
    - The `samples' output represents the potential space for encoded images. It is the core result of the encoded process and will be used as input for the follow-up restoration task. This potential expression captures the essential features of the image, removes unnecessary details and optimizes the reconstruction of the restored area.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- noise_mask
    - The `noise_mask' output is a binary mask that indicates the area to be repaired in the image. It is derived from the original mask to ensure that the restoration process is focused only on the specified area. This mask is essential to guide the generation of the restoration content.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class WAS_VAEEncodeForInpaint:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pixels': ('IMAGE',), 'vae': ('VAE',), 'mask': ('MASK',), 'mask_offset': ('INT', {'default': 6, 'min': -128, 'max': 128, 'step': 1})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'encode'
    CATEGORY = 'latent/inpaint'

    def encode(self, vae, pixels, mask, mask_offset=6):
        x = pixels.shape[1] // 8 * 8
        y = pixels.shape[2] // 8 * 8
        mask = torch.nn.functional.interpolate(mask.reshape((-1, 1, mask.shape[-2], mask.shape[-1])), size=(pixels.shape[1], pixels.shape[2]), mode='bilinear')
        pixels = pixels.clone()
        if pixels.shape[1] != x or pixels.shape[2] != y:
            x_offset = pixels.shape[1] % 8 // 2
            y_offset = pixels.shape[2] % 8 // 2
            pixels = pixels[:, x_offset:x + x_offset, y_offset:y + y_offset, :]
            mask = mask[:, :, x_offset:x + x_offset, y_offset:y + y_offset]
        mask_erosion = self.modify_mask(mask, mask_offset)
        m = (1.0 - mask_erosion.round()).squeeze(1)
        for i in range(3):
            pixels[:, :, :, i] -= 0.5
            pixels[:, :, :, i] *= m
            pixels[:, :, :, i] += 0.5
        t = vae.encode(pixels)
        return ({'samples': t, 'noise_mask': mask_erosion[:, :, :x, :y].round()},)

    def modify_mask(self, mask, modify_by):
        if modify_by == 0:
            return mask
        if modify_by > 0:
            kernel_size = 2 * modify_by + 1
            kernel_tensor = torch.ones((1, 1, kernel_size, kernel_size))
            padding = modify_by
            modified_mask = torch.clamp(torch.nn.functional.conv2d(mask.round(), kernel_tensor, padding=padding), 0, 1)
        else:
            kernel_size = 2 * abs(modify_by) + 1
            kernel_tensor = torch.ones((1, 1, kernel_size, kernel_size))
            padding = abs(modify_by)
            eroded_mask = torch.nn.functional.conv2d(1 - mask.round(), kernel_tensor, padding=padding)
            modified_mask = torch.clamp(1 - eroded_mask, 0, 1)
        return modified_mask
```