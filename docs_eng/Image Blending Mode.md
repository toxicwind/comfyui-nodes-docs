# Documentation
- Class name: WAS_Image_Blending_Mode
- Category: WAS Suite/Image
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Blending_Mode node is designed to mix two images using a variety of hybrid models, providing a multifunctional approach to combining visual elements. It emphasizes the creative aspects of image processing and allows for a wide range of effects by selecting different hybrid technologies.

# Input types
## Required
- image_a
    - Image A is the first input image to be mixed with image B. It plays a vital role in determining the final appearance of the mixed result, as it is one of the main visual elements that is combined.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- image_b
    - Image B is the second input image that will be mixed with image A. It is equally important in influencing the final output, and it is a mixture of images that contributes to the overall appearance and senses.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- mode
    - Mixed mode determines how the colours of image A and image B are mixed. Each model provides different visual effects and allows high customization during the mixing process.
    - Comfy dtype: COMBO['add', 'color', 'color_burn', 'color_dodge', 'darken', 'difference', 'exclusion', 'hard_light', 'hue', 'lighten', 'multiply', 'overlay', 'screen', 'soft_light']
    - Python dtype: str
- blend_percentage
    - Mixed percentage controls the strength of the mixed effect. It allows fine-tuning of the mixed effect so that the delicate or significant mixing of the two images can be achieved.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- image
    - The output image is the result of a mix of images A and B using a specified mix mode and a mixed percentage. It encapsulates the combination of visual elements that enter the image, reflecting the creative intent of the hybrid operation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Blending_Mode:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image_a': ('IMAGE',), 'image_b': ('IMAGE',), 'mode': (['add', 'color', 'color_burn', 'color_dodge', 'darken', 'difference', 'exclusion', 'hard_light', 'hue', 'lighten', 'multiply', 'overlay', 'screen', 'soft_light'],), 'blend_percentage': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    FUNCTION = 'image_blending_mode'
    CATEGORY = 'WAS Suite/Image'

    def image_blending_mode(self, image_a, image_b, mode='add', blend_percentage=1.0):
        if 'pilgram' not in packages():
            install_package('pilgram')
        import pilgram
        img_a = tensor2pil(image_a)
        img_b = tensor2pil(image_b)
        if mode:
            if mode == 'color':
                out_image = pilgram.css.blending.color(img_a, img_b)
            elif mode == 'color_burn':
                out_image = pilgram.css.blending.color_burn(img_a, img_b)
            elif mode == 'color_dodge':
                out_image = pilgram.css.blending.color_dodge(img_a, img_b)
            elif mode == 'darken':
                out_image = pilgram.css.blending.darken(img_a, img_b)
            elif mode == 'difference':
                out_image = pilgram.css.blending.difference(img_a, img_b)
            elif mode == 'exclusion':
                out_image = pilgram.css.blending.exclusion(img_a, img_b)
            elif mode == 'hard_light':
                out_image = pilgram.css.blending.hard_light(img_a, img_b)
            elif mode == 'hue':
                out_image = pilgram.css.blending.hue(img_a, img_b)
            elif mode == 'lighten':
                out_image = pilgram.css.blending.lighten(img_a, img_b)
            elif mode == 'multiply':
                out_image = pilgram.css.blending.multiply(img_a, img_b)
            elif mode == 'add':
                out_image = pilgram.css.blending.normal(img_a, img_b)
            elif mode == 'overlay':
                out_image = pilgram.css.blending.overlay(img_a, img_b)
            elif mode == 'screen':
                out_image = pilgram.css.blending.screen(img_a, img_b)
            elif mode == 'soft_light':
                out_image = pilgram.css.blending.soft_light(img_a, img_b)
            else:
                out_image = img_a
        out_image = out_image.convert('RGB')
        blend_mask = Image.new(mode='L', size=img_a.size, color=round(blend_percentage * 255))
        blend_mask = ImageOps.invert(blend_mask)
        out_image = Image.composite(img_a, out_image, blend_mask)
        return (pil2tensor(out_image),)
```