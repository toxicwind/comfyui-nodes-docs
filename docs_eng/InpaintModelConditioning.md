# Documentation
- Class name: InpaintModelConditioning
- Category: conditioning/inpaint
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The 'encode' method of the InnocentModelConditioning node is designed to process images by encoding them into potential spatial expressions. It uses masking to pixels and adjusts the image size to ensure compatibility with the encoded model. This method is essential for the restoration task, using synthetic content to fill the missing or masked areas of the image.

# Input types
## Required
- positive
    - The " positive " parameter is important for defining the positive conditions in the image coding process. It determines how the contents of the image are affected by the positive conditionalities in the encoding process.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative
    - The “negative” parameter plays an important role in image coding by specifying negative conditions that should be excluded or minimized in the coding process.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- pixels
    - The " pixels " parameter is essential because it represents the input image data that the node will process. It is the core element of the node task.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - The vae parameter is important because it refers to the variable coder model used to encode the image as a potential expression.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- mask
    - The “mask” parameter is essential to the restoration process because it identifies the image area that needs to be filled or synthesized.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- positive
    - The "positive" output is important because it represents the code derived from the input image, which is in the positive direction of the condition information.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[torch.Tensor, Dict[str, torch.Tensor]]
- negative
    - The "negative" output indicates that the model should avoid incorporating negative condition information for the code of the image.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[torch.Tensor, Dict[str, torch.Tensor]]
- latent
    - The “latent” output is a key component because it contains the potential spatial expression of the image, which is the result of the encoded process.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Union[torch.Tensor, torch.Tensor]]

# Usage tips
- Infra type: GPU

# Source code
```
class InpaintModelConditioning:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'vae': ('VAE',), 'pixels': ('IMAGE',), 'mask': ('MASK',)}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'LATENT')
    RETURN_NAMES = ('positive', 'negative', 'latent')
    FUNCTION = 'encode'
    CATEGORY = 'conditioning/inpaint'

    def encode(self, positive, negative, pixels, vae, mask):
        x = pixels.shape[1] // 8 * 8
        y = pixels.shape[2] // 8 * 8
        mask = torch.nn.functional.interpolate(mask.reshape((-1, 1, mask.shape[-2], mask.shape[-1])), size=(pixels.shape[1], pixels.shape[2]), mode='bilinear')
        orig_pixels = pixels
        pixels = orig_pixels.clone()
        if pixels.shape[1] != x or pixels.shape[2] != y:
            x_offset = pixels.shape[1] % 8 // 2
            y_offset = pixels.shape[2] % 8 // 2
            pixels = pixels[:, x_offset:x + x_offset, y_offset:y + y_offset, :]
            mask = mask[:, :, x_offset:x + x_offset, y_offset:y + y_offset]
        m = (1.0 - mask.round()).squeeze(1)
        for i in range(3):
            pixels[:, :, :, i] -= 0.5
            pixels[:, :, :, i] *= m
            pixels[:, :, :, i] += 0.5
        concat_latent = vae.encode(pixels)
        orig_latent = vae.encode(orig_pixels)
        out_latent = {}
        out_latent['samples'] = orig_latent
        out_latent['noise_mask'] = mask
        out = []
        for conditioning in [positive, negative]:
            c = node_helpers.conditioning_set_values(conditioning, {'concat_latent_image': concat_latent, 'concat_mask': mask})
            out.append(c)
        return (out[0], out[1], out_latent)
```