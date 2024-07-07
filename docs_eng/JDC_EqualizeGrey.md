# Documentation
- Class name: Equalize
- Category: image/postprocessing
- Output node: False
- Repo Ref: https://github.com/Jordach/comfy-plasma.git

The node category is designed to enhance the contrast by adjusting the image's histogram, which improves the visual clarity and detail of the image by dispersing pixel intensity values, making it more suitable for further analysis or visualization, and ensuring that the results are clearer and visually attractive.

# Input types
## Required
- IMAGE
    - The IMAGE parameter is essential because it provides input images that will be processed by nodes. It directly influences the output and determines the quality and appearance of the enhanced images. Without this input, nodes cannot perform their intended functions.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Output types
- IMAGE
    - The output IMAGE represents a processing version entered with better contrast and visual clarity. It is a direct result of node functions and is essential for subsequent image analysis or display.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class Equalize:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'IMAGE': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'process_image'
    CATEGORY = 'image/postprocessing'

    def process_image(self, IMAGE):
        cimg = conv_tensor_pil(IMAGE)
        return conv_pil_tensor(ImageOps.equalize(cimg))
```