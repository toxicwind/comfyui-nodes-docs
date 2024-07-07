# Documentation
- Class name: PPFNoiseNode
- Category: Power Noise Suite/Noise
- Output node: False
- Repo Ref: https://github.com/WASasquatch/PowerNoiseSuite

PPFNoiseNode is designed to generate fractal noise patterns using Perlin noise, which can control the production process by adjusting parameters to produce complex visual textures. It provides a method for generating a volume of noises, with adjustable parameters to control the generation process, thus generating diverse noise maps.

# Input types
## Required
- batch_size
    - Determine the number of noise maps generated in a single operation, affecting the overall volume and diversity of output.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - Specifies the width of the noise map generated, influencing the resolution and level of detail of the texture.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Defines the height of the noise map, which is directly related to the vertical dimension of the output texture.
    - Comfy dtype: INT
    - Python dtype: int
- X
    - Control of the X-coordinate deviation of noise sampling and movement of patterns along the X-axis contribute to overall changes in noise mapping.
    - Comfy dtype: FLOAT
    - Python dtype: float
- Y
    - Adjust the Y-coordinate deviation of noise sampling to influence the position of the pattern along the Y-axis and contribute to the diversity of output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- Z
    - The Z-coordinate deviation affecting noise sampling increases the depth of noise patterns and introduces temporal evolution.
    - Comfy dtype: FLOAT
    - Python dtype: float
- evolution
    - The timing of the regulation of noise patterns changes as frame sequences create dynamic changes in output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- frame
    - Represents the current frame in the evolutionary sequence, affecting the progress of noise patterns over time.
    - Comfy dtype: INT
    - Python dtype: int
- scale
    - Adjust the frequency scale of noise to influence the particle size and detail level at which the texture is generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- octaves
    - Specifies the eight-degree volume during fractal generation, which determines the complexity and richness of noise patterns.
    - Comfy dtype: INT
    - Python dtype: int
- persistence
    - To influence the continuity of each eight-degree sound in the fractal and to control the overall smoothness of the amplitude and noise.
    - Comfy dtype: FLOAT
    - Python dtype: float
- lacunarity
    - Adjusts the increase in frequency between successive eight degrees of sound, affecting changes and contrasts in noise patterns.
    - Comfy dtype: FLOAT
    - Python dtype: float
- exponent
    - The reconciliation is applied to the index of the noise value and affects the overall strength and contrast of the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- brightness
    - Adjusts the overall brightness of the noise to allow dark-to-light changes in the texture generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- contrast
    - To influence the contrast between noise, increasing or reducing differences between dark and light zones in the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clamp_min
    - Sets the minimum number of noise values to prevent the result from being too bleak or negative.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clamp_max
    - Defines the maximum value of the noise value and ensures that the output does not exceed a certain intensity.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - Seeds are provided for random number generation to ensure the replicability and consistency of noise patterns.
    - Comfy dtype: INT
    - Python dtype: int
- device
    - Computation equipment selected according to performance and resource requirements may be CPU or GPU.
    - Comfy dtype: COMBO['cpu', 'cuda']
    - Python dtype: str

# Output types
- latents
    - Include noise maps in potential form that can be further processed or used as input for other nodes.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- previews
    - The visual representation of generated noise maps allows for rapid assessment of noise patterns and their properties.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class PPFNoiseNode:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'batch_size': ('INT', {'default': 1, 'max': 64, 'min': 1, 'step': 1}), 'width': ('INT', {'default': 512, 'max': 8192, 'min': 64, 'step': 1}), 'height': ('INT', {'default': 512, 'max': 8192, 'min': 64, 'step': 1}), 'resampling': (['nearest-exact', 'bilinear', 'area', 'bicubic', 'bislerp'],), 'X': ('FLOAT', {'default': 0, 'max': 99999999, 'min': -99999999, 'step': 0.01}), 'Y': ('FLOAT', {'default': 0, 'max': 99999999, 'min': -99999999, 'step': 0.01}), 'Z': ('FLOAT', {'default': 0, 'max': 99999999, 'min': -99999999, 'step': 0.01}), 'evolution': ('FLOAT', {'default': 0.0, 'max': 1.0, 'min': 0.0, 'step': 0.01}), 'frame': ('INT', {'default': 0, 'max': 99999999, 'min': 0, 'step': 1}), 'scale': ('FLOAT', {'default': 5, 'max': 2048, 'min': 2, 'step': 0.01}), 'octaves': ('INT', {'default': 8, 'max': 8, 'min': 1, 'step': 1}), 'persistence': ('FLOAT', {'default': 1.5, 'max': 23.0, 'min': 0.01, 'step': 0.01}), 'lacunarity': ('FLOAT', {'default': 2.0, 'max': 99.0, 'min': 0.01, 'step': 0.01}), 'exponent': ('FLOAT', {'default': 4.0, 'max': 38.0, 'min': 0.01, 'step': 0.01}), 'brightness': ('FLOAT', {'default': 0.0, 'max': 1.0, 'min': -1.0, 'step': 0.01}), 'contrast': ('FLOAT', {'default': 0.0, 'max': 1.0, 'min': -1.0, 'step': 0.01}), 'clamp_min': ('FLOAT', {'default': 0.0, 'max': 10.0, 'min': -10.0, 'step': 0.01}), 'clamp_max': ('FLOAT', {'default': 1.0, 'max': 10.0, 'min': -10.0, 'step': 0.01}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'device': (['cpu', 'cuda'],)}, 'optional': {'optional_vae': ('VAE',), 'ppf_settings': ('PPF_SETTINGS',)}}
    RETURN_TYPES = ('LATENT', 'IMAGE')
    RETURN_NAMES = ('latents', 'previews')
    FUNCTION = 'power_fractal_latent'
    CATEGORY = 'Power Noise Suite/Noise'

    def power_fractal_latent(self, batch_size, width, height, resampling, X, Y, Z, evolution, frame, scale, octaves, persistence, lacunarity, exponent, brightness, contrast, clamp_min, clamp_max, seed, device, optional_vae=None, ppf_settings=None):
        if ppf_settings:
            ppf = ppf_settings
            X = ppf['X']
            Y = ppf['Y']
            Z = ppf['Z']
            evolution = ppf['evolution']
            frame = ppf['frame']
            scale = ppf['scale']
            octaves = ppf['octaves']
            persistence = ppf['persistence']
            lacunarity = ppf['lacunarity']
            exponent = ppf['exponent']
            brightness = ppf['brightness']
            contrast = ppf['contrast']
        color_intensity = 1
        masking_intensity = 1
        batch_size = int(batch_size)
        width = int(width)
        height = int(height)
        channel_tensors = []
        for i in range(batch_size):
            nseed = seed + i * 12
            rgb_noise_maps = []
            rgb_image = torch.zeros(4, height, width)
            for j in range(3):
                rgba_noise_map = self.generate_noise_map(width, height, X, Y, Z, frame, device, evolution, octaves, persistence, lacunarity, exponent, scale, brightness, contrast, nseed + j, clamp_min, clamp_max)
                rgb_noise_map = rgba_noise_map.squeeze(-1)
                rgb_noise_map *= color_intensity
                rgb_noise_map *= masking_intensity
                rgb_image[j] = rgb_noise_map
            rgb_image[3] = torch.ones(height, width)
            channel_tensors.append(rgb_image)
        tensors = torch.stack(channel_tensors)
        tensors = normalize(tensors)
        if optional_vae is None:
            latents = F.interpolate(tensors, size=(height // 8, width // 8), mode=resampling)
            return ({'samples': latents}, tensors.permute(0, 2, 3, 1))
        encoder = nodes.VAEEncode()
        latents = []
        for tensor in tensors:
            tensor = tensor.unsqueeze(0)
            tensor = tensor.permute(0, 2, 3, 1)
            latents.append(encoder.encode(optional_vae, tensor)[0]['samples'])
        latents = torch.cat(latents)
        return ({'samples': latents}, tensors.permute(0, 2, 3, 1))

    def generate_noise_map(self, width, height, X, Y, Z, frame, device, evolution, octaves, persistence, lacunarity, exponent, scale, brightness, contrast, seed, clamp_min, clamp_max):
        PPF = PerlinPowerFractal(width, height)
        noise_map = PPF(1, X, Y, Z, frame, device, evolution, octaves, persistence, lacunarity, exponent, scale, brightness, contrast, seed, clamp_min, clamp_max)
        return noise_map
```