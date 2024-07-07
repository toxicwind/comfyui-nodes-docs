# Documentation
- Class name: OffsetImage
- Category: image
- Output node: False
- Repo Ref: https://github.com/spinagon/ComfyUI-seamless-tiling

The OffsetImage node is designed to carry forward the input image, moving pixels according to the percentage values provided for x and y axes. This node is important in creating visual effects and can be used for different image processing tasks such as alignment, combination or data enhancement.

# Input types
## Required
- pixels
    - The `pixels' parameter is the main input of the OffsetImage node, which represents the image data to be operated. It is essential for the operation of the node, because it determines what is to be removed.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- x_percent
    - The 'x_percent' parameter specifies the percentage of the image width that moves pixels along the x axis. It affects the horizontal position of the image after operation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- y_percent
    - The `y_percent' parameter determines the percentage of the image height that moves pixels along the y-axis. It is important for determining the vertical position of the image when it is scaled down.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- offset_image
    - The `offset_image' output is the result of applying migration to input images. It represents a moving image that can be used for further processing or displaying.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class OffsetImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pixels': ('IMAGE',), 'x_percent': ('FLOAT', {'default': 50.0, 'min': 0.0, 'max': 100.0, 'step': 1}), 'y_percent': ('FLOAT', {'default': 50.0, 'min': 0.0, 'max': 100.0, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'run'
    CATEGORY = 'image'

    def run(self, pixels, x_percent, y_percent):
        (n, y, x, c) = pixels.size()
        y = round(y * y_percent / 100)
        x = round(x * x_percent / 100)
        return (pixels.roll((y, x), (1, 2)),)
```