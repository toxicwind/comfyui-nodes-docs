# Documentation
- Class name: WLSH_Empty_Latent_Image_By_Ratio
- Category: WLSH Nodes/latent
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The `generate' method of WLSH_Empty_Latent_Image_By_Radio node is designed to create an empty potential image based on the specified width ratio and direction. It calculates the size of the potential image and initially converts it to zero, which can serve as a starting point for further image processing tasks.

# Input types
## Required
- aspect
    - The parameter 'aspect' defines the width ratio of the potential image to be generated. It is essential because it directly affects the size of the output image.
    - Comfy dtype: str
    - Python dtype: str
- direction
    - The parameter'direction' specifies whether the image should be horizontal or vertical, which affects the distribution of width and height.
    - Comfy dtype: str
    - Python dtype: str
- shortside
    - The parameter'shortside' determines the length of the shorter edge of the image, which is used to calculate the full dimensions based on the width ratio.
    - Comfy dtype: int
    - Python dtype: int
## Optional
- batch_size
    - The parameter 'batch_size' indicates the number of images generated in a single operation, which increases the efficiency of processing multiple images at once.
    - Comfy dtype: int
    - Python dtype: int

# Output types
- latent
    - Output 'latent' is a volume that represents an empty potential image of the dimensions calculated on the basis of the input parameters.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- width
    - The output 'width' provides the width of the potential images calculated after considering the width and direction.
    - Comfy dtype: int
    - Python dtype: int
- height
    - The output 'height' provides the height of potential images calculated after considering the width ratio and direction.
    - Comfy dtype: int
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Empty_Latent_Image_By_Ratio:
    aspects = ['1:1', '6:5', '5:4', '4:3', '3:2', '16:10', '16:9', '19:9', '21:9', '2:1', '3:1', '4:1']
    direction = ['landscape', 'portrait']

    def __init__(self, device='cpu'):
        self.device = device

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'aspect': (s.aspects,), 'direction': (s.direction,), 'shortside': ('INT', {'default': 512, 'min': 64, 'max': MAX_RESOLUTION, 'step': 64}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('LATENT', 'INT', 'INT')
    RETURN_NAMES = ('latent', 'width', 'height')
    FUNCTION = 'generate'
    CATEGORY = 'WLSH Nodes/latent'

    def generate(self, aspect, direction, shortside, batch_size=1):
        (x, y) = aspect.split(':')
        x = int(x)
        y = int(y)
        ratio = x / y
        width = int(shortside * ratio)
        width = width + 63 & -64
        height = shortside
        if direction == 'portrait':
            (width, height) = (height, width)
        adj_width = width // 8
        adj_height = height // 8
        latent = torch.zeros([batch_size, 4, adj_height, adj_width])
        return ({'samples': latent}, adj_width * 8, adj_height * 8)
```