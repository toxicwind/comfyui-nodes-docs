# Documentation
- Class name: WAS_Image_Power_Noise
- Category: WAS Suite/Image/Generate/Noise
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The power_noise method is designed to generate different types of noise patterns that can be used for image processing or as digital texture. It provides the function of creating white, grey, pink, green, blue or mixed noises, and provides a multifunctional tool for customizing noise generation according to different needs, based on specified parameters such as width, height, frequency and decay.

# Input types
## Required
- width
    - The width parameter defines the width of the noise image to be generated. It is vital because it determines the horizontal resolution of the output image and affects the overall detail and vertical ratio.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The header parameter sets the vertical dimensions of the noise image. It is essential for building the vertical resolution of the image and defines the overall shape of the output with width.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- frequency
    - The frequency parameter is used to adjust the scales of noise patterns. It is particularly important for pink, green and blue noise types, affecting the spectrum content of noise, and thus the visual texture.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attenuation
    - The decay affects the contrast between noises by adjusting the standard deviations in the process of producing ash noise. This is an important parameter that controls the visibility and intensity of noise patterns.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise_type
    - Options for the types of noise that you want to generate include grey, white, pink, blue, green, or a mixture of these. Each type produces different visual effects, providing a range of noise properties applicable to different applications.
    - Comfy dtype: COMBO[grey, white, pink, blue, green, mix]
    - Python dtype: str
- seed
    - Seed parameters are used to initialize the random number generator to ensure repeatability of noise patterns. It is an optional parameter that provides control over the randomity of noise in order to achieve consistent results.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - Output image parameters represent the noise mode generated as an image. It is the main result of the power_noise method, and the specified noise properties are enclosed in the visual format.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Power_Noise:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'width': ('INT', {'default': 512, 'max': 4096, 'min': 64, 'step': 1}), 'height': ('INT', {'default': 512, 'max': 4096, 'min': 64, 'step': 1}), 'frequency': ('FLOAT', {'default': 0.5, 'max': 10.0, 'min': 0.0, 'step': 0.01}), 'attenuation': ('FLOAT', {'default': 0.5, 'max': 10.0, 'min': 0.0, 'step': 0.01}), 'noise_type': (['grey', 'white', 'pink', 'blue', 'green', 'mix'],), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    FUNCTION = 'power_noise'
    CATEGORY = 'WAS Suite/Image/Generate/Noise'

    def power_noise(self, width, height, frequency, attenuation, noise_type, seed):
        noise_image = self.generate_power_noise(width, height, frequency, attenuation, noise_type, seed)
        return (pil2tensor(noise_image),)

    def generate_power_noise(self, width, height, frequency=None, attenuation=None, noise_type='white', seed=None):

        def white_noise(width, height):
            noise = np.random.random((height, width))
            return noise

        def grey_noise(width, height, attenuation):
            noise = np.random.normal(0, attenuation, (height, width))
            return noise

        def blue_noise(width, height, frequency, attenuation):
            noise = grey_noise(width, height, attenuation)
            scale = 1.0 / (width * height)
            fy = np.fft.fftfreq(height)[:, np.newaxis] ** 2
            fx = np.fft.fftfreq(width) ** 2
            f = fy + fx
            power = np.sqrt(f)
            power[0, 0] = 1
            noise = np.fft.ifft2(np.fft.fft2(noise) / power)
            noise *= scale / noise.std()
            return np.real(noise)

        def green_noise(width, height, frequency, attenuation):
            noise = grey_noise(width, height, attenuation)
            scale = 1.0 / (width * height)
            fy = np.fft.fftfreq(height)[:, np.newaxis] ** 2
            fx = np.fft.fftfreq(width) ** 2
            f = fy + fx
            power = np.sqrt(f)
            power[0, 0] = 1
            noise = np.fft.ifft2(np.fft.fft2(noise) / np.sqrt(power))
            noise *= scale / noise.std()
            return np.real(noise)

        def pink_noise(width, height, frequency, attenuation):
            noise = grey_noise(width, height, attenuation)
            scale = 1.0 / (width * height)
            fy = np.fft.fftfreq(height)[:, np.newaxis] ** 2
            fx = np.fft.fftfreq(width) ** 2
            f = fy + fx
            power = np.sqrt(f)
            power[0, 0] = 1
            noise = np.fft.ifft2(np.fft.fft2(noise) * power)
            noise *= scale / noise.std()
            return np.real(noise)

        def blue_noise_mask(width, height, frequency, attenuation, seed, num_masks=3):
            masks = []
            for i in range(num_masks):
                mask_seed = seed + i
                np.random.seed(mask_seed)
                mask = blue_noise(width, height, frequency, attenuation)
                masks.append(mask)
            return masks

        def blend_noise(width, height, masks, noise_types, attenuations):
            blended_image = Image.new('L', (width, height), color=0)
            fy = np.fft.fftfreq(height)[:, np.newaxis] ** 2
            fx = np.fft.fftfreq(width) ** 2
            f = fy + fx
            i = 0
            for (mask, noise_type, attenuation) in zip(masks, noise_types, attenuations):
                mask = Image.fromarray((255 * (mask - np.min(mask)) / (np.max(mask) - np.min(mask))).astype(np.uint8).real)
                if noise_type == 'white':
                    noise = white_noise(width, height)
                    noise = Image.fromarray((255 * (noise - np.min(noise)) / (np.max(noise) - np.min(noise))).astype(np.uint8).real)
                elif noise_type == 'grey':
                    noise = grey_noise(width, height, attenuation)
                    noise = Image.fromarray((255 * (noise - np.min(noise)) / (np.max(noise) - np.min(noise))).astype(np.uint8).real)
                elif noise_type == 'pink':
                    noise = pink_noise(width, height, frequency, attenuation)
                    noise = Image.fromarray((255 * (noise - np.min(noise)) / (np.max(noise) - np.min(noise))).astype(np.uint8).real)
                elif noise_type == 'green':
                    noise = green_noise(width, height, frequency, attenuation)
                    noise = Image.fromarray((255 * (noise - np.min(noise)) / (np.max(noise) - np.min(noise))).astype(np.uint8).real)
                elif noise_type == 'blue':
                    noise = blue_noise(width, height, frequency, attenuation)
                    noise = Image.fromarray((255 * (noise - np.min(noise)) / (np.max(noise) - np.min(noise))).astype(np.uint8).real)
                blended_image = Image.composite(blended_image, noise, mask)
                i += 1
            return np.asarray(blended_image)

        def shorten_to_range(value, min_value, max_value):
            range_length = max_value - min_value + 1
            return (value - min_value) % range_length + min_value
        if seed is not None:
            if seed > 4294967294:
                seed = shorten_to_range(seed, 0, 4294967293)
                cstr(f'Seed too large for power noise; rescaled to: {seed}').warning.print()
            np.random.seed(seed)
        if noise_type == 'white':
            noise = white_noise(width, height)
        elif noise_type == 'grey':
            noise = grey_noise(width, height, attenuation)
        elif noise_type == 'pink':
            if frequency is None:
                cstr('Pink noise requires a frequency value.').error.print()
                return None
            noise = pink_noise(width, height, frequency, attenuation)
        elif noise_type == 'green':
            if frequency is None:
                cstr('Green noise requires a frequency value.').error.print()
                return None
            noise = green_noise(width, height, frequency, attenuation)
        elif noise_type == 'blue':
            if frequency is None:
                cstr('Blue noise requires a frequency value.').error.print()
                return None
            noise = blue_noise(width, height, frequency, attenuation)
        elif noise_type == 'mix':
            if frequency is None:
                cstr('Mix noise requires a frequency value.').error.print()
                return None
            if seed is None:
                cstr('Mix noise requires a seed value.').error.print()
                return None
            blue_noise_masks = blue_noise_mask(width, height, frequency, attenuation, seed=seed, num_masks=3)
            noise_types = ['white', 'grey', 'pink', 'green', 'blue']
            attenuations = [attenuation] * len(noise_types)
            noise = blend_noise(width, height, blue_noise_masks, noise_types, attenuations)
        else:
            cstr(f'Unsupported noise type `{noise_type}`').error.print()
            return None
        if noise_type != 'mix':
            noise = 255 * (noise - np.min(noise)) / (np.max(noise) - np.min(noise))
        noise_image = Image.fromarray(noise.astype(np.uint8).real)
        return noise_image.convert('RGB')
```