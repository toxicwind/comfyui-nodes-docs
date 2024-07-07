# Documentation
- Class name: EmptyLatentImage
- Category: latent
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The EmptyLatentImage node is designed to generate an empty potential spatial expression. As a placeholder for images in potential space, it provides a starting point for a zero-filled structural mass that can be used for further image-generation processes.

# Input types
## Required
- width
    - The width parameter defines the width of the potential image. It is essential to set the horizontal resolution of the potential space generated and plays an important role in determining the overall structure of the image.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters specify the height of the potential image. It is essential for building the vertical resolution of the potential space and is a key factor in the final size of the image.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- batch_size
    - Match_size parameters determine the number of potential images generated at a time. It is important to control the efficiency of the image generation process, especially when processing large amounts of data.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- samples
    - The samples output provides the potential spatial expression to be generated. It is a zero volume that is used as the basis for follow-up image processing or generation tasks.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class EmptyLatentImage:

    def __init__(self):
        self.device = comfy.model_management.intermediate_device()

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 512, 'min': 16, 'max': MAX_RESOLUTION, 'step': 8}), 'height': ('INT', {'default': 512, 'min': 16, 'max': MAX_RESOLUTION, 'step': 8}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 4096})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'generate'
    CATEGORY = 'latent'

    def generate(self, width, height, batch_size=1):
        latent = torch.zeros([batch_size, 4, height // 8, width // 8], device=self.device)
        return ({'samples': latent},)
```