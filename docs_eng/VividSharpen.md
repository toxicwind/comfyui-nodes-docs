# Documentation
- Class name: VividSharpen
- Category: image/postprocessing
- Output node: False
- Repo Ref: https://github.com/WASasquatch/WAS_Extras

VividSharpen node is designed to increase the clarity and sharpness of the image by applying sharp algorithms. It adjusts the visual detail to create a more dynamic and clear appearance that applies to later processing tasks in image editing.

# Input types
## Required
- images
    - The `images' parameter is the input of the sharpening process. It is vital because it determines what is to be enhanced. The quality and resolution of the input image directly influences the sharpening effect.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- radius
    - The `radius' parameter controls the range of fuzzy effects applied before sharpening. This is an important adjustment factor that affects the severity of the output image and allows for fine control over the final visual appearance.
    - Comfy dtype: FLOAT
    - Python dtype: float
- strength
    - The `strength' parameter defines the strength of the sharpness effect. It is important because it allows users to control the degree of radicality of the sharpness, thus generating images with different levels of detail and clarity.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- images
    - Output `images' are images with enhanced sharpness and clarity that are processed by sharp algorithms. They are ready for further use or display.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class VividSharpen:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'radius': ('FLOAT', {'default': 1.5, 'min': 0.01, 'max': 64.0, 'step': 0.01}), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('images',)
    FUNCTION = 'sharpen'
    CATEGORY = 'image/postprocessing'

    def sharpen(self, images, radius, strength):
        results = []
        if images.size(0) > 1:
            for image in images:
                image = tensor2pil(image)
                results.append(pil2tensor(vivid_sharpen(image, radius=radius, strength=strength)))
            results = torch.cat(results, dim=0)
        else:
            results = pil2tensor(vivid_sharpen(tensor2pil(images), radius=radius, strength=strength))
        return (results,)
```