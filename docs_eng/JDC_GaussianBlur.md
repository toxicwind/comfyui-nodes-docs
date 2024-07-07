# Documentation
- Class name: GaussianBlur
- Category: image/postprocessing
- Output node: False
- Repo Ref: https://github.com/Jordach/comfy-plasma.git

This node applies Gaussian fuzzy to images and is often used to reduce noise or create softness. It emphasizes the role of nodes in improving image quality and preparing for further processing by smoothing image appearances.

# Input types
## Required
- IMAGE
    - The image parameter is necessary because it is the main input for the Gaussian fuzzy operation. It determines the quality and characteristics of the post-processing output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
## Optional
- blur_radius
    - Fuzzy radius parameters control the degree of fuzzy effect. It affects the smoothness of the final image, and a larger radius leads to a more obvious ambiguity.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- IMAGE
    - The output image is the result of an application of Gaussian fuzzy. It represents the conversion of the input image and now has less noise and a softer look.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class GaussianBlur:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'IMAGE': ('IMAGE',), 'blur_radius': ('FLOAT', {'default': 1, 'min': 1, 'max': 1024, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'process_image'
    CATEGORY = 'image/postprocessing'

    def process_image(self, IMAGE, blur_radius):
        img = conv_tensor_pil(IMAGE)
        return conv_pil_tensor(img.filter(ImageFilter.GaussianBlur(blur_radius)))
```