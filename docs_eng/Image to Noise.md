# Documentation
- Class name: WAS_Image_To_Noise
- Category: WAS Suite/Image/Generate/Noise
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_To_Noise node is designed to convert input images into noise mode. It can selectively mix with Gaussian fuzzy by quantifying colours, random pixel data, to achieve a noisy aesthetic effect. This node, as an innovative tool for generating noise-based images, can be used for a variety of applications, such as artistic expression or data enhancement.

# Input types
## Required
- images
    - The `images' parameter is essential because it defines the input image of the node that will be treated as a noise mode. This conversion has a significant effect on the final output, making it essential for the execution of the node and for the quality of the image generated.
    - Comfy dtype: IMAGE
    - Python dtype: List[PIL.Image.Image]
## Optional
- num_colors
    - The 'num_colors' parameter determines the number of colours to quantify the image, which affects the complexity of noise patterns. It plays an important role in the operation of nodes by controlling the colour depth and the visual noise effects generated.
    - Comfy dtype: INT
    - Python dtype: int
- black_mix
    - The 'black_mix' parameter controls the black noise volume mixed into the image, adding a layer of complexity to the noise mode. It is important for achieving the required level of noise in the output image.
    - Comfy dtype: INT
    - Python dtype: int
- gaussian_mix
    - The `gaussian_mix' parameter specifies the degree of obscurity to be applied, which can smooth noise and create more subtle noise effects. It is an important factor in fine-tuning the visual appearance of noise.
    - Comfy dtype: FLOAT
    - Python dtype: float
- brightness
    - The 'brightness' parameter adjusts the brightness of the noise image to enhance or reduce the contrast of noise patterns. It is an important factor in controlling the overall appearance of noise effects.
    - Comfy dtype: FLOAT
    - Python dtype: float
- output_mode
    - The 'output_mode'parameter determines the format of the output. Selecting 'batch'will merge the images into a single volume, while 'list' will keep them in a list of individual images. This affects how the results are constructed for downstream tasks.
    - Comfy dtype: COMBO['batch', 'list']
    - Python dtype: Literal['batch', 'list']
- seed
    - The `seed' parameter is used to initialize the random number generator to ensure repeatability of noise patterns. It is important for producing consistent results in different operations.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The 'image'output parameter represents the converted noise image. It is the main result of the node function and contains the noise mode generated from the input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_To_Noise:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'num_colors': ('INT', {'default': 16, 'max': 256, 'min': 2, 'step': 2}), 'black_mix': ('INT', {'default': 0, 'max': 20, 'min': 0, 'step': 1}), 'gaussian_mix': ('FLOAT', {'default': 0.0, 'max': 1024, 'min': 0, 'step': 0.1}), 'brightness': ('FLOAT', {'default': 1.0, 'max': 2.0, 'min': 0.0, 'step': 0.01}), 'output_mode': (['batch', 'list'],), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    OUTPUT_IS_LIST = (False,)
    FUNCTION = 'image_to_noise'
    CATEGORY = 'WAS Suite/Image/Generate/Noise'

    def image_to_noise(self, images, num_colors, black_mix, gaussian_mix, brightness, output_mode, seed):
        noise_images = []
        for image in images:
            noise_images.append(pil2tensor(self.image2noise(tensor2pil(image), num_colors, black_mix, brightness, gaussian_mix, seed)))
        if output_mode == 'list':
            self.OUTPUT_IS_LIST = (True,)
        else:
            noise_images = torch.cat(noise_images, dim=0)
        return (noise_images,)

    def image2noise(self, image, num_colors=16, black_mix=0, brightness=1.0, gaussian_mix=0, seed=0):
        random.seed(int(seed))
        image = image.quantize(colors=num_colors)
        image = image.convert('RGBA')
        pixel_data = list(image.getdata())
        random.shuffle(pixel_data)
        randomized_image = Image.new('RGBA', image.size)
        randomized_image.putdata(pixel_data)
        (width, height) = image.size
        black_noise = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        for _ in range(black_mix):
            for x in range(width):
                for y in range(height):
                    if random.randint(0, 1) == 1:
                        black_noise.putpixel((x, y), (0, 0, 0, 255))
        randomized_image = Image.alpha_composite(randomized_image, black_noise)
        enhancer = ImageEnhance.Brightness(randomized_image)
        randomized_image = enhancer.enhance(brightness)
        if gaussian_mix > 0:
            original_noise = randomized_image.copy()
            randomized_gaussian = randomized_image.filter(ImageFilter.GaussianBlur(radius=gaussian_mix))
            randomized_image = Image.blend(randomized_image, randomized_gaussian, 0.65)
            randomized_image = Image.blend(randomized_image, original_noise, 0.25)
        return randomized_image
```