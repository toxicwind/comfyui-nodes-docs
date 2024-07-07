# Documentation
- Class name: UpscaleTileCalculator
- Category: Mikey/Image
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The UpscaleTileCalculator node is designed to calculate and manage the surface sheeting of images efficiently. It provides a method for determining the optimal flat size based on image resolution and specified flatten resolution to ensure that the image after sampling remains intact and of quality.

# Input types
## Required
- image
    - The image parameter is essential for the operation of the node, because it represents the input image that will be processed. It is the fundamental element that affects the node execution of the peaceful sheeting of the results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- tile_resolution
    - The tile_resoltion parameter defines the desired resolution for each flat image. It plays a key role in determining the levelling size, thus affecting the efficiency and quality of the sampling process.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The image after the sampling is the main output of the node, which represents the result of the processing of the sampling operation. It marks the success of the node in improving the quality of the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- tile_width
    - tile_width parameters indicate the width calculated by each sheet after the sampling process. It is important because it provides the spatial dimensions of the sheet that are used in the operation.
    - Comfy dtype: INT
    - Python dtype: int
- tile_height
    - The tile_height parameter specifies the height calculated by each sheet after the sampling process. Together with tile_width, it determines the overall structure of the sheet, which is essential to understand the output of the node.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class UpscaleTileCalculator:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'tile_resolution': ('INT', {'default': 512, 'min': 1, 'max': 8192, 'step': 8})}}
    RETURN_TYPES = ('IMAGE', 'INT', 'INT')
    RETURN_NAMES = ('image', 'tile_width', 'tile_height')
    FUNCTION = 'calculate'
    CATEGORY = 'Mikey/Image'

    def upscale(self, image, upscale_method, width, height, crop):
        samples = image.movedim(-1, 1)
        s = comfy.utils.common_upscale(samples, width, height, upscale_method, crop)
        s = s.movedim(1, -1)
        return (s,)

    def resize(self, image, width, height, upscale_method, crop):
        (w, h) = find_latent_size(image.shape[2], image.shape[1])
        img = self.upscale(image, upscale_method, w, h, crop)[0]
        return (img,)

    def calculate(self, image, tile_resolution):
        (width, height) = (image.shape[2], image.shape[1])
        (tile_width, tile_height) = find_tile_dimensions(width, height, 1.0, tile_resolution)
        return (image, tile_width, tile_height)
```