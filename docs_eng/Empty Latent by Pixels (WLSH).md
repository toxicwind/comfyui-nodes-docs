# Documentation
- Class name: WLSH_Empty_Latent_Image_By_Pixels
- Category: WLSH Nodes/latent
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The WLSH_Empty_Latent_Image_By_Pixels method is designed to create an empty image based on the size and length of the pixels specified. It calculates the width and height of potential images intelligently to adapt to the millions of pixels and directions needed to ensure that the dimensions are optimized for processing efficiency.

# Input types
## Required
- aspect
    - The 'aspct' parameter defines the vertical and vertical ratio of the potential image. It is essential because it directly affects the shape and size of the image generated, and thus the subsequent processing and analysis stage.
    - Comfy dtype: STRING
    - Python dtype: str
- direction
    - The “direction” parameter specifies that the image should be a horizontal or vertical mode. This is important because it determines the direction of the potential image and is essential for certain applications that require a particular direction.
    - Comfy dtype: STRING
    - Python dtype: str
- megapixels
    - The "megapixels" parameter sets the resolution of a potential image in millions of pixels. It is an important factor because it determines the level of detail of the image and the computational resources required.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- batch_size
    - The "batch_size" parameter determines the number of images to be processed in a single iterative process. It is important for optimizing the computational efficiency and can be adjusted according to available resources.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- latent
    - The "latent" output provides the potential image expression generated. It is a key component, as it forms the basis for further image processing and analysis within the system.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- width
    - "width" output represents the width of a potential image calculated in pixels. It is important because it provides the spatial dimension information needed for image operations and displays.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - "Height" output represents the height of a potential image calculated in pixels. Together with width, it is essential to understand the overall size of the image for various applications.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Empty_Latent_Image_By_Pixels:
    aspects = ['1:1', '5:4', '4:3', '3:2', '16:10', '16:9', '19:9', '21:9', '2:1', '3:1', '4:1']
    direction = ['landscape', 'portrait']

    def __init__(self, device='cpu'):
        self.device = device

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'aspect': (s.aspects,), 'direction': (s.direction,), 'megapixels': ('FLOAT', {'default': 1.0, 'min': 0.01, 'max': 16.0, 'step': 0.01}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('LATENT', 'INT', 'INT')
    RETURN_NAMES = ('latent', 'width', 'height')
    FUNCTION = 'generate'
    CATEGORY = 'WLSH Nodes/latent'

    def generate(self, aspect, direction, megapixels, batch_size=1):
        (x, y) = aspect.split(':')
        x = int(x)
        y = int(y)
        ratio = x / y
        total = int(megapixels * 1024 * 1024)
        width = int(np.sqrt(ratio * total))
        width = width + 63 & -64
        height = int(np.sqrt(1 / ratio * total))
        height = height + 63 & -64
        if direction == 'portrait':
            (width, height) = (height, width)
        adj_width = width // 8
        adj_height = height // 8
        latent = torch.zeros([batch_size, 4, adj_height, adj_width])
        return ({'samples': latent}, adj_width * 8, adj_height * 8)
```