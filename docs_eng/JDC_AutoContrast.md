# Documentation
- Class name: AutoContrast
- Category: image/postprocessing
- Output node: False
- Repo Ref: https://github.com/Jordach/comfy-plasma.git

The node enhances the contrast of the image by stretching out the intensity range of the image, stretching it across a desired range, increasing the visual appeal and clarity of the image without changing its basic features.

# Input types
## Required
- IMAGE
    - Enter the image, the contrast of which will be adjusted by the node as the basis for the enhancement process.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
## Optional
- cutoff
    - This parameter control applies to the degree of relative enhancement of the image, with higher values leading to a more marked change in the contrast.
    - Comfy dtype: FLOAT
    - Python dtype: float
- min_value
    - This parameter sets the minimum value in the image that is not affected by contrast adjustments and retains the details of the shadow.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - Output is an image with a higher degree of contrast and is suitable for further processing or display.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class AutoContrast:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'IMAGE': ('IMAGE',), 'cutoff': ('FLOAT', {'default': 2, 'min': 0, 'max': 100, 'step': 0.01}), 'min_value': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'process_image'
    CATEGORY = 'image/postprocessing'

    def process_image(self, IMAGE, cutoff, min_value):
        cimg = conv_tensor_pil(IMAGE)
        if min_value >= 0:
            return conv_pil_tensor(ImageOps.autocontrast(cimg, cutoff=cutoff, ignore=min_value))
        else:
            return conv_pil_tensor(ImageOps.autocontrast(cimg, cutoff=cutoff))
```