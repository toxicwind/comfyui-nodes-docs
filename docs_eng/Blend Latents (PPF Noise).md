# Documentation
- Class name: PPFNBlendLatents
- Category: Power Noise Suite/Latent/Adjustements
- Output node: False
- Repo Ref: https://github.com/WASasquatch/PowerNoiseSuite

The node is designed to enhance the generation process by adjusting two sets of potential visual features by specifying hybrid operations and proportionally, and by allowing for fine control of the final output appearance.

# Input types
## Required
- latent_a
    - The potential expression of the first input, which forms the basis of the mixing process, significantly influences the initial visual characteristics that generate the output.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- latent_b
    - The potential indication of the second input is that it enriches the final visual results and contributes to the hybrid process by introducing changes and nuances.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- operation
    - The hybrid model determines the algorithm approach used to group potential expressions and fundamentally affects the style and consistency of the images generated.
    - Comfy dtype: COMBO
    - Python dtype: str
- blend_ratio
    - The ratio determines the balance between the two potential expressions, giving one greater impact and leading to a more visible visual change in the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- blend_strength
    - Strength adjusts the strength of the blending operation, which has a significant impact on the details and clarity of the final image, and higher values may lead to more significant characteristics changes.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- mask
    - A mask can be applied to selectively mix certain areas of potential expression, allowing for targeted adjustments and greater control over specific visual elements.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- set_noise_mask
    - When this option is enabled, noise will be added to the mask, randomity will be introduced for the mixing process, and diversity may be added for the output.
    - Comfy dtype: COMBO
    - Python dtype: str
- normalize
    - Regulate the range of values within the potential expression to ensure that the mixing process is consistent and that the final output is within a predictable visual range.
    - Comfy dtype: COMBO
    - Python dtype: str
- clamp_min
    - This parameter sets the potential minimum value to be expressed after mixing, prevents any value from being below a certain threshold and maintains the required level of detail.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clamp_max
    - Similar to clamp_min, this parameter limits the maximum value of potential expression, ensures that mixed output does not exceed the specified limit and avoids excessive visual prostheses.
    - Comfy dtype: FLOAT
    - Python dtype: float
- latent2rgb_preview
    - When this option is enabled, the potential expression will be generated as a real-time preview of the RGB image, providing immediate visual feedback for the mixing process.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- latents
    - The potential expression of the output has been commingled according to the specified parameters, representing adjusted and refined visual information to be prepared for further processing or generation.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- previews
    - If enabled, this output provides a visual preview of a mixed potential RGB image, providing a tangible reference for the validity of the hybrid operation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class PPFNBlendLatents:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'latent_a': ('LATENT',), 'latent_b': ('LATENT',), 'operation': (sorted(list(blending_modes.keys())),), 'blend_ratio': ('FLOAT', {'default': 0.5, 'min': 0.01, 'max': 1.0, 'step': 0.01}), 'blend_strength': ('FLOAT', {'default': 1.0, 'min': -100.0, 'max': 100.0, 'step': 0.01})}, 'optional': {'mask': ('MASK',), 'set_noise_mask': (['false', 'true'],), 'normalize': (['false', 'true'],), 'clamp_min': ('FLOAT', {'default': 0.0, 'max': 10.0, 'min': -10.0, 'step': 0.01}), 'clamp_max': ('FLOAT', {'default': 1.0, 'max': 10.0, 'min': -10.0, 'step': 0.01}), 'latent2rgb_preview': (['false', 'true'],)}}
    RETURN_TYPES = ('LATENT', 'IMAGE')
    RETURN_NAMES = ('latents', 'previews')
    FUNCTION = 'latent_blend'
    CATEGORY = 'Power Noise Suite/Latent/Adjustements'

    def latent_blend(self, latent_a, latent_b, operation, blend_ratio, blend_strength, mask=None, set_noise_mask=None, normalize=None, clamp_min=None, clamp_max=None, latent2rgb_preview=None):
        latent_a = latent_a['samples'][:, :-1]
        latent_b = latent_b['samples'][:, :-1]
        assert latent_a.shape == latent_b.shape, f'Input latents must have the same shape, but got: a {latent_a.shape}, b {latent_b.shape}'
        alpha_a = latent_a[:, -1:]
        alpha_b = latent_b[:, -1:]
        blended_rgb = self.blend_latents(latent_a, latent_b, operation, blend_ratio, blend_strength, clamp_min, clamp_max)
        blended_alpha = torch.ones_like(blended_rgb[:, :1])
        blended_latent = torch.cat((blended_rgb, blended_alpha), dim=1)
        tensors = latents_to_images(blended_latent, True if latent2rgb_preview and latent2rgb_preview == 'true' else False)
        if mask is not None:
            blend_mask = self.transform_mask(mask, latent_a['samples'].shape)
            blended_latent = blend_mask * blended_latent + (1 - blend_mask) * latent_a['samples']
            if set_noise_mask == 'true':
                return ({'samples': blended_latent, 'noise_mask': mask.reshape((-1, 1, mask.shape[-2], mask.shape[-1]))}, tensors)
            else:
                return ({'samples': blended_latent}, tensors)
        else:
            return ({'samples': blended_latent}, tensors)

    def blend_latents(self, latent1, latent2, mode='add', blend_percentage=0.5, blend_strength=0.5, mask=None, clamp_min=0.0, clamp_max=1.0):
        blend_func = blending_modes.get(mode)
        if blend_func is None:
            raise ValueError(f"Unsupported blending mode. Please choose from the supported modes: {', '.join(list(blending_modes.keys()))}")
        blend_factor1 = blend_percentage
        blend_factor2 = 1 - blend_percentage
        blended_latent = blend_func(latent1, latent2, blend_strength * blend_factor1)
        if normalize and normalize == 'true':
            blended_latent = normalize(blended_latent, clamp_min, clamp_max)
        return blended_latent

    def transform_mask(self, mask, shape):
        mask = mask.view(-1, 1, mask.shape[-2], mask.shape[-1])
        resized_mask = torch.nn.functional.interpolate(mask, size=(shape[2], shape[3]), mode='bilinear')
        expanded_mask = resized_mask.expand(-1, shape[1], -1, -1)
        if expanded_mask.shape[0] < shape[0]:
            expanded_mask = expanded_mask.repeat((shape[0] - 1) // expanded_mask.shape[0] + 1, 1, 1, 1)[:shape[0]]
        del mask, resized_mask
        return expanded_mask
```