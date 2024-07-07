# Documentation
- Class name: VAEEncodeForInpaint
- Category: latent/inpaint
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The `encode'method at the VAE EncodeForInpaint node is designed to convert image pixels to potential spatial expressions suitable for the restoration mission. It encodes the masked area of the image using the VAE, allowing subsequent generation or modification of the masked area. This method is essential for applications such as image editing and restoration, in which maintaining the integrity of the original image outside the mask area is critical.

# Input types
## Required
- pixels
    - The parameter 'pixels' is the input image data processed by the node. It is essential for the encoding process because it is the raw material that VAE will convert to potential expressions. The accuracy and detail of the potential spatial expressions that the quality and resolution of 'pixels' directly influences.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - The parameter 'vae' represents the variable coder model used to encode image data. It is a key component of the node, as it determines the quality and properties of the potential space in which the image is encoded. The selection of the VAE structure can significantly influence the performance of the node and the applicability of the code data to the restoration task.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- mask
    - The parameter'mask' defines the area in which the image needs to be repaired. It is a binary volume to identify which parts of 'pixels' should be masked during the encoding process. 'Mask' is essential for selective encoding of the image area and ensures that only the specified area is converted to potential space.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- grow_mask_by
    - The parameter 'grove_mask_by' allows the masked area to be expanded by the number of pixels specified. This is very useful to ensure that the transition between the masked and unshaded areas is smooth and well defined. This parameter affects the connectivity and consistency of the restored areas in the final image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- samples
    - Output'samples'contains a potential spatial expression for the input of image pixels. This is the core output of the node for further processing or generation of restored images. The quality of'samples' directly influences the end result of the restoration task.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- noise_mask
    - Output 'noise_mask'is a binary volume that indicates that the image is masked and ready for repair. It originates from the input'mask', which is essential to guide the restoration process to ensure that only the desired area is modified.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class VAEEncodeForInpaint:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pixels': ('IMAGE',), 'vae': ('VAE',), 'mask': ('MASK',), 'grow_mask_by': ('INT', {'default': 6, 'min': 0, 'max': 64, 'step': 1})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'encode'
    CATEGORY = 'latent/inpaint'

    def encode(self, vae, pixels, mask, grow_mask_by=6):
        x = pixels.shape[1] // vae.downscale_ratio * vae.downscale_ratio
        y = pixels.shape[2] // vae.downscale_ratio * vae.downscale_ratio
        mask = torch.nn.functional.interpolate(mask.reshape((-1, 1, mask.shape[-2], mask.shape[-1])), size=(pixels.shape[1], pixels.shape[2]), mode='bilinear')
        pixels = pixels.clone()
        if pixels.shape[1] != x or pixels.shape[2] != y:
            x_offset = pixels.shape[1] % vae.downscale_ratio // 2
            y_offset = pixels.shape[2] % vae.downscale_ratio // 2
            pixels = pixels[:, x_offset:x + x_offset, y_offset:y + y_offset, :]
            mask = mask[:, :, x_offset:x + x_offset, y_offset:y + y_offset]
        if grow_mask_by == 0:
            mask_erosion = mask
        else:
            kernel_tensor = torch.ones((1, 1, grow_mask_by, grow_mask_by))
            padding = math.ceil((grow_mask_by - 1) / 2)
            mask_erosion = torch.clamp(torch.nn.functional.conv2d(mask.round(), kernel_tensor, padding=padding), 0, 1)
        m = (1.0 - mask.round()).squeeze(1)
        for i in range(3):
            pixels[:, :, :, i] -= 0.5
            pixels[:, :, :, i] *= m
            pixels[:, :, :, i] += 0.5
        t = vae.encode(pixels)
        return ({'samples': t, 'noise_mask': mask_erosion[:, :, :x, :y].round()},)
```