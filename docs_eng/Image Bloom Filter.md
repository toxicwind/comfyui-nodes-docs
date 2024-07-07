# Documentation
- Class name: WAS_Image_Bloom_Filter
- Category: WAS Suite/Image/Filter
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Image_Bloom_Filter applies a bloom effect to images that enhances their visual attractiveness by simulating the dispersion of light. It adjusts the brightness of images to create luminous effects, which are very useful for a variety of image processing tasks.

# Input types
## Required
- image
    - The input image of the bloom filter will be applied. It is the main object of the node process and directly affects the final output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- radius
    - Radius parameters control the hyperbolic range used to create the bloom effect. It is an important factor in determining the bloom softness.
    - Comfy dtype: FLOAT
    - Python dtype: float
- intensity
    - Strength parameters adjust the brightness of the bloom effect. Higher values lead to more obvious blooms, while lower values produce more subtle effects.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output_image
    - Output_image is a processed image with a bloom filter. It represents the final visual result of node operations.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Bloom_Filter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 10, 'min': 0.0, 'max': 1024, 'step': 0.1}), 'intensity': ('FLOAT', {'default': 1, 'min': 0.0, 'max': 1.0, 'step': 0.1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_bloom'
    CATEGORY = 'WAS Suite/Image/Filter'

    def image_bloom(self, image, radius=0.5, intensity=1.0):
        return (pil2tensor(self.apply_bloom_filter(tensor2pil(image), radius, intensity)),)

    def apply_bloom_filter(self, input_image, radius, bloom_factor):
        blurred_image = input_image.filter(ImageFilter.GaussianBlur(radius=radius))
        high_pass_filter = ImageChops.subtract(input_image, blurred_image)
        bloom_filter = high_pass_filter.filter(ImageFilter.GaussianBlur(radius=radius * 2))
        bloom_filter = ImageEnhance.Brightness(bloom_filter).enhance(2.0)
        bloom_filter = ImageChops.multiply(bloom_filter, Image.new('RGB', input_image.size, (int(255 * bloom_factor), int(255 * bloom_factor), int(255 * bloom_factor))))
        blended_image = ImageChops.screen(input_image, bloom_filter)
        return blended_image
```