# Documentation
- Class name: PPFNPowerLawNoise
- Category: Power Noise Suite/Noise
- Output node: False
- Repo Ref: https://github.com/WASasquatch/PowerNoiseSuite

The node is designed to generate various types of noise that can be used in a variety of applications, such as texture generation, random processes and noise-based art. It provides a flexible interface to specify parameters such as noise types, sizes and alpha indices, allowing users to customize outputs according to their particular needs.

# Input types
## Required
- batch_size
    - This parameter determines the number of noise images generated in a single batch, which affects the efficiency of the calculation and the applicability of the results.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The width of the noise image determines the horizontal resolution and affects the level of detail and the overall size of the output.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Similar to width, height parameters set the vertical resolution of the noise image to influence the size and detail of the output.
    - Comfy dtype: INT
    - Python dtype: int
- noise_type
    - The type of noise chosen will determine the statistical properties that generate noise, which is essential for the application that relies on specific noise properties.
    - Comfy dtype: COMBO
    - Python dtype: str
- scale
    - Scale parameters adjust the overall amplitude of noise to control the visibility and intensity of noise patterns.
    - Comfy dtype: FLOAT
    - Python dtype: float
- alpha_exponent
    - The Alpha Index shapes the distribution of noise, influencing the “colour” of frequency content and noise (for example, from white to Brown noise).
    - Comfy dtype: FLOAT
    - Python dtype: float
- device
    - The specified device (`cpu' or 'cuda') determines the hardware that will be calculated to affect performance and compatibility.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- resampling
    - Re-sampling parameters affect the way in which sound images are plugged in and the quality and appearance of the final output are adjusted.
    - Comfy dtype: COMBO
    - Python dtype: str
- modulator
    - The modem parameters add a modem to the noise to create more complex patterns and changes in the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - By setting up seeds, users can ensure the replicability of the noise generation process, which is important for experimental and research purposes.
    - Comfy dtype: INT
    - Python dtype: int
- optional_vae
    - When provided, the optional_vae parameter allows for the integration of VAEs, thus achieving more complex noise operations and generation.
    - Comfy dtype: VAE
    - Python dtype: VAE

# Output types
- latents
    - Potential output contains noise images in potential space expressions that can be further processed or used as input for other nodes.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- previews
    - The preview output provides a visual expression for generating noise, allowing users to quickly assess and compare different noise settings and parameters.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class PPFNPowerLawNoise:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        pln = PowerLawNoise('cpu')
        return {'required': {'batch_size': ('INT', {'default': 1, 'max': 64, 'min': 1, 'step': 1}), 'width': ('INT', {'default': 512, 'max': 8192, 'min': 64, 'step': 1}), 'height': ('INT', {'default': 512, 'max': 8192, 'min': 64, 'step': 1}), 'resampling': (['nearest-exact', 'bilinear', 'area', 'bicubic', 'bislerp'],), 'noise_type': (pln.get_noise_types(),), 'scale': ('FLOAT', {'default': 1.0, 'max': 1024.0, 'min': 0.01, 'step': 0.001}), 'alpha_exponent': ('FLOAT', {'default': 1.0, 'max': 12.0, 'min': -12.0, 'step': 0.001}), 'modulator': ('FLOAT', {'default': 1.0, 'max': 2.0, 'min': 0.1, 'step': 0.01}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'device': (['cpu', 'cuda'],)}, 'optional': {'optional_vae': ('VAE',)}}
    RETURN_TYPES = ('LATENT', 'IMAGE')
    RETURN_NAMES = ('latents', 'previews')
    FUNCTION = 'power_noise'
    CATEGORY = 'Power Noise Suite/Noise'

    def power_noise(self, batch_size, width, height, resampling, noise_type, scale, alpha_exponent, modulator, seed, device, optional_vae=None):
        power_law = PowerLawNoise(device=device)
        tensors = power_law(batch_size, width, height, scale=scale, alpha=alpha_exponent, modulator=modulator, noise_type=noise_type, seed=seed)
        alpha_channel = torch.ones((batch_size, height, width, 1), dtype=tensors.dtype, device='cpu')
        tensors = torch.cat((tensors, alpha_channel), dim=3)
        if optional_vae is None:
            latents = tensors.permute(0, 3, 1, 2)
            latents = F.interpolate(latents, size=(height // 8, width // 8), mode=resampling)
            return ({'samples': latents}, tensors)
        encoder = nodes.VAEEncode()
        latents = []
        for tensor in tensors:
            tensor = tensor.unsqueeze(0)
            latents.append(encoder.encode(optional_vae, tensor)[0]['samples'])
        latents = torch.cat(latents)
        return ({'samples': latents}, tensors)
```