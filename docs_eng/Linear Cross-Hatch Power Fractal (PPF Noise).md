# Documentation
- Class name: PPFNLinearCrossHatchNode
- Category: Power Noise Suite/Noise
- Output node: False
- Repo Ref: https://github.com/WASasquatch/PowerNoiseSuite

The node is designed to generate complex cross-line patterns with power fractal effects and to introduce high-level details and textures for the output image. It controls the frequency, continuity and other properties of noise by operating a variety of parameters to create complex and visually rich images. The function of the node also includes adjusting brightness and contrasts and supporting the selection of the VAE model to further enhance the content generation.

# Input types
## Required
- batch_size
    - This parameter determines the number of images generated in one operation, directly affecting the scale of node processing and the amount of throughput.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The width of the image generated influences the size of the canvas and the detail particle size that can be captured in the output.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters, similar to width, are essential in determining the vertical dimensions and overall resolution of the image.
    - Comfy dtype: INT
    - Python dtype: int
- resampling
    - Re-sampling methods are essential for scaling or adjusting image quality over a large hour of image, as it affects the plug-in value of pixels.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- frequency
    - Frequency parameters control the density of cross-line lines, which is a key factor in defining the complexity and texture for generating patterns.
    - Comfy dtype: FLOAT
    - Python dtype: float
- gain
    - Gains in adjusting the amplitude of noise are essential for determining the visibility of cross-line patterns in the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- octaves
    - The eight-degree influences the complexity and level of detail of the fractal pattern and helps enrich visual output.
    - Comfy dtype: INT
    - Python dtype: int
- persistence
    - Continuity is a key parameter in fractal generation that affects the smoothness and continuity of patterns at different scales.
    - Comfy dtype: FLOAT
    - Python dtype: float
- add_noise
    - Add noise to randomity to the pattern, which creates a more natural and diverse visual texture in the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- linear_range
    - Linear range parameters are important for the mapping of noise values, as they determine the spread and change of cross-lines.
    - Comfy dtype: INT
    - Python dtype: int
- angle_degrees
    - An angle number assigns the direction of the cross line, which is an essential aspect of the overall structure of the pattern.
    - Comfy dtype: FLOAT
    - Python dtype: float
- brightness
    - Brightness adjustments affect the overall brightness of the image, allowing the creation of broader visual effects.
    - Comfy dtype: FLOAT
    - Python dtype: float
- contrast
    - Contrast controls the difference between the brightest and darkest parts of the image and contributes to the vibrancy and depth of visual output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - Seeds are used to generate random numbers to ensure that the randomity of patterns is recreated and consistent.
    - Comfy dtype: INT
    - Python dtype: int
- device
    - The designation of computing equipment is essential to optimize performance and ensure compatibility with bottom hardware.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
## Optional
- optional_vae
    - The optional VAE integration allows for the further enhancement of images generated through the use of the generation model, introducing additional complexities and layers of change.
    - Comfy dtype: VAE
    - Python dtype: VAE

# Output types
- latents
    - Potential variables represent an encoded version of the image generated, which can be used for further processing or analysis.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- previews
    - The preview provides a reduced version of the image generated and is suitable for rapid visualization and review.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class PPFNLinearCrossHatchNode:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'batch_size': ('INT', {'default': 1, 'max': 64, 'min': 1, 'step': 1}), 'width': ('INT', {'default': 512, 'max': 8192, 'min': 64, 'step': 1}), 'height': ('INT', {'default': 512, 'max': 8192, 'min': 64, 'step': 1}), 'resampling': (['nearest-exact', 'bilinear', 'area', 'bicubic', 'bislerp'],), 'frequency': ('FLOAT', {'default': 320.0, 'max': 1024.0, 'min': 0.001, 'step': 0.001}), 'gain': ('FLOAT', {'default': 0.25, 'max': 1.0, 'min': 0.0, 'step': 0.001}), 'octaves': ('INT', {'default': 12, 'max': 32, 'min': 1, 'step': 1}), 'persistence': ('FLOAT', {'default': 1.5, 'max': 2.0, 'min': 0.001, 'step': 0.001}), 'add_noise': ('FLOAT', {'default': 0.0, 'max': 1.0, 'min': 0.0, 'step': 0.001}), 'linear_range': ('INT', {'default': 16, 'max': 256, 'min': 2, 'step': 1}), 'linear_tolerance': ('FLOAT', {'default': 0.05, 'max': 1.0, 'min': 0.001, 'step': 0.001}), 'angle_degrees': ('FLOAT', {'default': 45.0, 'max': 360.0, 'min': 0.0, 'step': 0.01}), 'brightness': ('FLOAT', {'default': 0.0, 'max': 1.0, 'min': -1.0, 'step': 0.001}), 'contrast': ('FLOAT', {'default': 0.0, 'max': 1.0, 'min': -1.0, 'step': 0.001}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'device': (['cpu', 'cuda'],)}, 'optional': {'optional_vae': ('VAE',)}}
    RETURN_TYPES = ('LATENT', 'IMAGE')
    RETURN_NAMES = ('latents', 'previews')
    FUNCTION = 'cross_hatch'
    CATEGORY = 'Power Noise Suite/Noise'

    def cross_hatch(self, batch_size, width, height, resampling, frequency, gain, octaves, persistence, add_noise, linear_range, linear_tolerance, angle_degrees, brightness, contrast, seed, device, optional_vae=None):
        cross_hatch = CrossHatchLinearPowerFractal(width=width, height=height, frequency=frequency, gain=gain, octaves=octaves, persistence=persistence, add_noise_tolerance=add_noise, mapping_range=linear_range, angle_degrees=angle_degrees, brightness=brightness, contrast=contrast)
        tensors = cross_hatch(batch_size, device, seed)
        tensors = torch.cat([tensors, torch.ones(batch_size, height, width, 1, dtype=tensors.dtype, device='cpu')], dim=-1)
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