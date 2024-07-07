# Documentation
- Class name: EmptyImage
- Category: image
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The EmptyImage node is designed to generate blank images with specified dimensions and colours. It serves as the basic component of the image-processing workflow, providing blank canvass for subsequent operations. This node is essential in the context where the start-up image is needed, for example, when creating placeholders or initializing image data structures.

# Input types
## Required
- width
    - The `width' parameter determines the width of the image generated in pixels. It is a key factor in defining the spatial dimensions of the image, directly affecting the overall structure of the image and its possible applications in downstream tasks.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height'parameter specifies the vertical extension of the image in pixels. It determines the resolution of the image with width, which is essential to ensure compatibility with the various display devices and processing requirements.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- batch_size
    - The `batch_size' parameter indicates the number of images generated in a single operation. It is particularly suitable for processing multiple images at the same time and allows for greater efficiency in batch processing scenarios.
    - Comfy dtype: INT
    - Python dtype: int
- color
    - The `color' parameter allows you to specify the colour of the image. It accepts an integer of the colour in the RGB format so that you can create an image with the required uniform background colour.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The `image'output is the main result of the EmptyImage node. It represents the creation of blank images with defined dimensions and colours. This output is very important because it provides the basis for further image operation and analysis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class EmptyImage:

    def __init__(self, device='cpu'):
        self.device = device

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 512, 'min': 1, 'max': MAX_RESOLUTION, 'step': 1}), 'height': ('INT', {'default': 512, 'min': 1, 'max': MAX_RESOLUTION, 'step': 1}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 4096}), 'color': ('INT', {'default': 0, 'min': 0, 'max': 16777215, 'step': 1, 'display': 'color'})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'generate'
    CATEGORY = 'image'

    def generate(self, width, height, batch_size=1, color=0):
        r = torch.full([batch_size, height, width, 1], (color >> 16 & 255) / 255)
        g = torch.full([batch_size, height, width, 1], (color >> 8 & 255) / 255)
        b = torch.full([batch_size, height, width, 1], (color & 255) / 255)
        return (torch.cat((r, g, b), dim=-1),)
```