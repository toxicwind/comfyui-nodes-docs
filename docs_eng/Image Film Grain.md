# Documentation
- Class name: WAS_Film_Grain
- Category: WAS Suite/Image/Filter
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Film_Grain node is designed to add film particle effects to images, enhance their visual texture, and create aesthetic attractions similar to traditional cinematography. It does so by applying grey-scale noises with adjustable density and intensity that enable users to control the visibility of particles in the final image.

# Input types
## Required
- image
    - The image parameter is the input image that will be applied to the particle effect of the film. It is an essential part of the node operation, because the entire process revolves around the manipulation of the image to achieve the desired visual effect.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- density
    - Density parameter control applies to the noise concentration of the image. It is essential to adjust the intensity of the film particle effect and allows fine-tuning to suit different visual preferences.
    - Comfy dtype: FLOAT
    - Python dtype: float
- intensity
    - The strength parameters determine the power of the film particles to cover the original image. It is an important factor in achieving a balanced effect, ensuring that the particles are visible but not overwhelming the details of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- highlights
    - High-light parameters adjust the brightness of the image, especially for the brighter regions. It plays an important role in increasing contrasts and making film particle effects more visible in the bright parts of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- supersample_factor
    - The supersample_factor parameter increases the resolution of the image before the noise is applied, which can lead to more detailed and high-quality film particle effects. This is an optional setting for users seeking greater control over the final output appearance.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- film_grain_image
    - The filen_grain_image output parameter represents the final image of the particle effect of the film. It is the apex for all nodes, reflecting the user's settings for density, intensity and high light selection.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Film_Grain:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'density': ('FLOAT', {'default': 1.0, 'min': 0.01, 'max': 1.0, 'step': 0.01}), 'intensity': ('FLOAT', {'default': 1.0, 'min': 0.01, 'max': 1.0, 'step': 0.01}), 'highlights': ('FLOAT', {'default': 1.0, 'min': 0.01, 'max': 255.0, 'step': 0.01}), 'supersample_factor': ('INT', {'default': 4, 'min': 1, 'max': 8, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'film_grain'
    CATEGORY = 'WAS Suite/Image/Filter'

    def film_grain(self, image, density, intensity, highlights, supersample_factor):
        return (pil2tensor(self.apply_film_grain(tensor2pil(image), density, intensity, highlights, supersample_factor)),)

    def apply_film_grain(self, img, density=0.1, intensity=1.0, highlights=1.0, supersample_factor=4):
        """
        Apply grayscale noise with specified density, intensity, and highlights to a PIL image.
        """
        img_gray = img.convert('L')
        original_size = img.size
        img_gray = img_gray.resize((img.size[0] * supersample_factor, img.size[1] * supersample_factor), Image.Resampling(2))
        num_pixels = int(density * img_gray.size[0] * img_gray.size[1])
        noise_pixels = []
        for i in range(num_pixels):
            x = random.randint(0, img_gray.size[0] - 1)
            y = random.randint(0, img_gray.size[1] - 1)
            noise_pixels.append((x, y))
        for (x, y) in noise_pixels:
            value = random.randint(0, 255)
            img_gray.putpixel((x, y), value)
        img_noise = img_gray.convert('RGB')
        img_noise = img_noise.filter(ImageFilter.GaussianBlur(radius=0.125))
        img_noise = img_noise.resize(original_size, Image.Resampling(1))
        img_noise = img_noise.filter(ImageFilter.EDGE_ENHANCE_MORE)
        img_final = Image.blend(img, img_noise, intensity)
        enhancer = ImageEnhance.Brightness(img_final)
        img_highlights = enhancer.enhance(highlights)
        return img_highlights
```