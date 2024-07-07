# Documentation
- Class name: LatentSlerp
- Category: latent
- Output node: False
- Repo Ref: https://github.com/BlenderNeko/ComfyUI_Noise.git

This node implements a linear slerp plug between two groups of potential vectors, which can provide a smooth transition between different potential states. This is particularly useful for the generation of intermediates in successive potential spaces.

# Input types
## Required
- latents1
    - The first group of potential vectors serves as the starting point for the plug value.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- factor
    - The plug-in factor determines the location of the path between the two sets of potential collections.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- latents2
    - The second group of potential vectors represents the end point of the plug value.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- mask
    - An optional mask can be used to selectively apply the plug value to certain elements of a potential vector.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- slerped_latents
    - The potential vector result after the plug value represents a smooth transition between the input potential set.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class LatentSlerp:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'latents1': ('LATENT',), 'factor': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01})}, 'optional': {'latents2': ('LATENT',), 'mask': ('MASK',)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'slerp_latents'
    CATEGORY = 'latent'

    def slerp_latents(self, latents1, factor, latents2=None, mask=None):
        s = latents1.copy()
        if latents2 is None:
            return (s,)
        if latents1['samples'].shape != latents2['samples'].shape:
            print('warning, shapes in LatentSlerp not the same, ignoring')
            return (s,)
        slerped = slerp(factor, latents1['samples'].clone(), latents2['samples'].clone())
        if mask is not None:
            mask = prepare_mask(mask, slerped.shape)
            slerped = mask * slerped + (1 - mask) * latents1['samples']
        s['samples'] = slerped
        return (s,)
```