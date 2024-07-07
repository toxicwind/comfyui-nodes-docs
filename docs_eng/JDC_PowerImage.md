# Documentation
- Class name: PowerImage
- Category: image/postprocessing
- Output node: False
- Repo Ref: https://github.com/Jordach/comfy-plasma.git

The node enhances the image by adjusting the brightness and contrastness of the image to the specified factors and patterns, allowing the manipulation of visual elements to meet specific aesthetic or analytical needs.

# Input types
## Required
- IMAGE
    - Source images that will be processed by nodes as the basic input for all enhancements.
    - Comfy dtype: PIL.Image
    - Python dtype: PIL.Image
- power_of
    - This parameter control is applied to the degree of enhancement of the image, with higher values leading to more visible effects.
    - Comfy dtype: FLOAT
    - Python dtype: float
- mode
    - Determine the type of enhancements to be applied, such as lighting, darkening or highlighting both aspects of the image.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- IMAGE
    - The processed images have been enhanced to prepare for further use or analysis.
    - Comfy dtype: PIL.Image
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class PowerImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'IMAGE': ('IMAGE',), 'power_of': ('FLOAT', {'default': 1, 'min': 1, 'max': 65536, 'step': 0.01}), 'mode': (['darken', 'lighten', 'emphasize both'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'process_image'
    CATEGORY = 'image/postprocessing'

    def process_image(self, IMAGE, power_of, mode):
        cimg = conv_tensor_pil(IMAGE)
        (w, h) = cimg.size
        pbar = comfy.utils.ProgressBar(h)
        step = 0
        for y in range(h):
            for x in range(w):
                (r, g, b) = cimg.getpixel((x, y))
                if mode == 'lighten':
                    r *= 1 + pow(r / 255, power_of)
                    g *= 1 + pow(g / 255, power_of)
                    b *= 1 + pow(b / 255, power_of)
                elif mode == 'emphasize both':
                    r *= 0.5 + pow(r / 255, power_of)
                    g *= 0.5 + pow(g / 255, power_of)
                    b *= 0.5 + pow(b / 255, power_of)
                else:
                    r *= pow(r / 255, power_of)
                    g *= pow(g / 255, power_of)
                    b *= pow(b / 255, power_of)
                r = clamp(r, 0, 255)
                g = clamp(g, 0, 255)
                b = clamp(b, 0, 255)
                cimg.putpixel((x, y), (int(r), int(g), int(b)))
            step += 1
            pbar.update_absolute(step, h)
        return conv_pil_tensor(cimg)
```