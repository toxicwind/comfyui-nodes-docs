# Documentation
- Class name: WAS_Image_Blend
- Category: WAS Suite/Image
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Blend' method is designed to integrate two images seamlessly. It controls the degree of integration by using the blend_percentage parameter to create a composite image of visual harmony that reflects the balance between the input pictures.

# Input types
## Required
- image_a
    - The first picture that you want to mix. It plays a vital role in determining the initial visual context of the picture.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- image_b
    - The second picture that you want to mix with the first picture. It contributes to the final look by folding the visual elements on the basic picture.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- blend_percentage
    - The blend_percentage parameter determines the visibility of the image_b in the final mix. It is a floating point value from 0.0 to 1.0, of which 0.0 indicates that only the image_a is visible, while 1.0 indicates that only the image_b is visible.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- image
    - Output is a mixed image that visualizes the two elements that enter the image according to the specified blend_percentage.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Blend:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image_a': ('IMAGE',), 'image_b': ('IMAGE',), 'blend_percentage': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    FUNCTION = 'image_blend'
    CATEGORY = 'WAS Suite/Image'

    def image_blend(self, image_a, image_b, blend_percentage):
        img_a = tensor2pil(image_a)
        img_b = tensor2pil(image_b)
        blend_mask = Image.new(mode='L', size=img_a.size, color=round(blend_percentage * 255))
        blend_mask = ImageOps.invert(blend_mask)
        img_result = Image.composite(img_a, img_b, blend_mask)
        del img_a, img_b, blend_mask
        return (pil2tensor(img_result),)
```