# Documentation
- Class name: InjectNoise
- Category: latent/noise
- Output node: False
- Repo Ref: https://github.com/BlenderNeko/ComfyUI_Noise.git

The InjectNoise node is designed to introduce noise into a group of potential expressions, thus simulates the impact of noise on the generation process. Its effect is to enhance data through controlled variability, which increases the robustness and diversity of output generation.

# Input types
## Required
- latents
    - The latents parameter is essential because it contains the original potential indication that the noise infuses will take place. It directly affects the results of the noise enhancement process.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- strength
    - The strength parameter determines the intensity of the noise that is to be injected into the lotts. It is essential to control the variation of the data that is to be introduced.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise
    - The optional noise parameter provides the noise source to be applied to latents. It is important because it allows customization of noise properties.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- mask
    - When providing mask parameters, it specifies which areas of latents should be affected by noise. This is important for targeted noise applications.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- latents
    - Output latents are potential indications that the noise has been injected and are prepared for further processing or generation.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class InjectNoise:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'latents': ('LATENT',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 200.0, 'step': 0.01})}, 'optional': {'noise': ('LATENT',), 'mask': ('MASK',)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'inject_noise'
    CATEGORY = 'latent/noise'

    def inject_noise(self, latents, strength, noise=None, mask=None):
        s = latents.copy()
        if noise is None:
            return (s,)
        if latents['samples'].shape != noise['samples'].shape:
            print('warning, shapes in InjectNoise not the same, ignoring')
            return (s,)
        noised = s['samples'].clone() + noise['samples'].clone() * strength
        if mask is not None:
            mask = prepare_mask(mask, noised.shape)
            noised = mask * noised + (1 - mask) * latents['samples']
        s['samples'] = noised
        return (s,)
```