# Documentation
- Class name: PPFNLatentAdjustment
- Category: Power Noise Suite/Latent/Adjustements
- Output node: False
- Repo Ref: https://github.com/WASasquatch/PowerNoiseSuite

This node class is designed to adjust and enhance the visual features of images expressed in potential vectors. It manipulates image properties, such as brightness, contrast, saturation and sharpness, to achieve desired visual outcomes. The node operates on the basis of the potential expression of modifying images, allowing extensive creative control of images without directly changing pixel data. It is particularly suitable for creating images that meet certain aesthetic standards or fine-tuning the quality of images generated.

# Input types
## Required
- latents
    - The latents parameter is the input load that represents the potential spatial encoding of the image. It is essential because it forms the basis for all image adjustments and enhancements at nodes. The manipulation of this parameter directly influences the final visual output, making it possible to make extensive changes from subtle to drastic.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- brightness
    - Brightness parameters control the overall brightness of the image. By adjusting this parameter, the user can brighten or darken the image, which can significantly change the mood and appearance of the visual content. It plays a key role in setting the tone of the image and the overall look.
    - Comfy dtype: FLOAT
    - Python dtype: float
- contrast
    - The contrast adjustment affects the difference between the brightest and darkest parts of the image. It helps to increase visual depth and detail, making the image more dynamic and attractive. This parameter is essential for creating images with dynamic scope and a sense of reality.
    - Comfy dtype: FLOAT
    - Python dtype: float
- saturation
    - The saturation parameter adjusts the intensity of the colour in the image. Increasing the saturation will make the colours brighter, while reducing the saturation will make the colours more softer. This parameter is important for achieving the desired aesthetic and emotional impact through the use of colours.
    - Comfy dtype: FLOAT
    - Python dtype: float
- exposure
    - Exposure control affects the overall brightness of the image, similar to adjusting the ISO settings on the camera. It is an important parameter for simulating different light conditions and achieving the desired visual effect.
    - Comfy dtype: FLOAT
    - Python dtype: float
- alpha_sharpen
    - The alpha_sharpen parameter is used to apply acute effects to images. It enhances the edge and detail and makes the image look clearer and more visible. This parameter is essential for achieving a high level of detail and clarity in the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- high_pass_radius
    - The high_pass_radius parameters apply high-access filters to images, emphasizing high-frequency details, to make the images clearer. It helps to increase local contrasts and improve the texture of the images.
    - Comfy dtype: FLOAT
    - Python dtype: float
- high_pass_strength
    - The high_pass_strength parameter controls the strength of the high-access filter effect. Adjusting this parameter allows fine-tuning of the filter's impact on the image to ensure that the desired level of detail and clarity is reached.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clamp_min
    - The clamp_min parameter ensures that the adjusted potential values do not fall below a certain threshold and prevent any unintended hypotheses or negative values. This is important to maintain the integrity and quality of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clamp_max
    - The clamp_max parameter limits the potential maximum value to the specified range and ensures that the value remains within the desired range and is not exceeded. This is essential to prevent the image from being over-exposed or saturated.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- latent2rgb_preview
    - The latent2rgb_preview parameter is an optional switch that will generate an RGB image preview of an adjusted potential vector. This feature helps to visualize the effect of the adjustment in real time.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- latents
    - The adjusted potential vector is the output length of the potential space code after the image has been modified. This parameter contains all changes made through node adjustments and is the basis for generating the final image.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- previews
    - The preview parameters provide a visualization of the adjusted potential vector as an RGB image. This output is important for immediate feedback and assessment of the performance of the nodes and the validity of the adjustments made.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class PPFNLatentAdjustment:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'latents': ('LATENT',), 'brightness': ('FLOAT', {'default': 1.0, 'max': 2.0, 'min': -1.0, 'step': 0.001}), 'contrast': ('FLOAT', {'default': 1.0, 'max': 2.0, 'min': -1.0, 'step': 0.001}), 'saturation': ('FLOAT', {'default': 1.0, 'max': 2.0, 'min': 0.0, 'step': 0.001}), 'exposure': ('FLOAT', {'default': 0.0, 'max': 2.0, 'min': -1.0, 'step': 0.001}), 'alpha_sharpen': ('FLOAT', {'default': 0.0, 'max': 10.0, 'min': 0.0, 'step': 0.01}), 'high_pass_radius': ('FLOAT', {'default': 0.0, 'max': 1024, 'min': 0.0, 'step': 0.01}), 'high_pass_strength': ('FLOAT', {'default': 1.0, 'max': 2.0, 'min': 0.0, 'step': 0.01}), 'clamp_min': ('FLOAT', {'default': 0.0, 'max': 10.0, 'min': -10.0, 'step': 0.01}), 'clamp_max': ('FLOAT', {'default': 1.0, 'max': 10.0, 'min': -10.0, 'step': 0.01})}, 'optional': {'latent2rgb_preview': (['false', 'true'],)}}
    RETURN_TYPES = ('LATENT', 'IMAGE')
    RETURN_NAMES = ('latents', 'previews')
    FUNCTION = 'adjust_latent'
    CATEGORY = 'Power Noise Suite/Latent/Adjustements'

    def adjust_latent(self, latents, brightness, contrast, saturation, exposure, alpha_sharpen, high_pass_radius, high_pass_strength, clamp_min, clamp_max, latent2rgb_preview=False):
        original_latents = latents['samples']
        (r, g, b, a) = (original_latents[:, 0:1], original_latents[:, 1:2], original_latents[:, 2:3], original_latents[:, 3:4])
        r = (r - 0.5) * contrast + 0.5 + (brightness - 1.0)
        g = (g - 0.5) * contrast + 0.5 + (brightness - 1.0)
        b = (b - 0.5) * contrast + 0.5 + (brightness - 1.0)
        gray = 0.299 * r + 0.587 * g + 0.114 * b
        r = (r - gray) * saturation + gray
        g = (g - gray) * saturation + gray
        b = (b - gray) * saturation + gray
        r = r * 2 ** exposure
        g = g * 2 ** exposure
        b = b * 2 ** exposure
        latents = torch.cat((r, g, b, a), dim=1)
        if alpha_sharpen > 0:
            latents = sharpen_latents(latents, alpha_sharpen)
        if high_pass_radius > 0:
            latents = high_pass_latents(latents, high_pass_radius, high_pass_strength)
        if clamp_min != 0:
            latents = normalize(latents, target_min=clamp_min)
        if clamp_max != 1:
            latents = normalize(latents, target_max=clamp_max)
        if clamp_min != 0 and clamp_max != 1.0:
            latents = normalize(latents, target_min=clamp_min, target_max=clamp_max)
        tensors = latents_to_images(latents, True if latent2rgb_preview and latent2rgb_preview == 'true' else False)
        return ({'samples': latents}, tensors)
```