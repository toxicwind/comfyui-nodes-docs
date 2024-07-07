# Documentation
- Class name: WLSH_Empty_Latent_Image_By_Resolution
- Category: WLSH Nodes/latent
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The `generate' method of WLSH_Empty_Latent_Image_By_Resultion node is designed to create an empty potential image space for the given resolution. It creates the complexity of potential spaces in abstraction by providing a simple interface that accepts width, altitude and volume size as input, and produces a potential length and adjusted dimensions.

# Input types
## Required
- width
    - The `width' parameter specifies the width of the potential image in pixels. It plays a key role in determining the resolution of the potential space generated, which directly affects the quality and detail of the final image.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The `height' parameter determines the height of the potential image, in pixels. Similar to width, it is essential for establishing resolution and for generating the trueness of the potential image.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- batch_size
    - The `batch_size' parameter is optional, which determines the number of potential images generated in a single operation. It can be used to process multiple images in an efficient manner, increasing node throughput.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- latent
    - `latent' output is a volume that represents the potential image space generated. It is a key component of the follow-up image processing and generation tasks and provides the basic data required for these operations.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- width
    - The `width' output reflects the adjusted width of the potential image after the process is generated. It is important to understand the actual dimensions of the potential space generated.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The `height' output provides the adjusted height of the potential image, similar to the width, which is essential for understanding the exact dimensions of the potential space generated.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Empty_Latent_Image_By_Resolution:

    def __init__(self, device='cpu'):
        self.device = device

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 512, 'min': 16, 'max': MAX_RESOLUTION, 'step': 8}), 'height': ('INT', {'default': 512, 'min': 16, 'max': MAX_RESOLUTION, 'step': 8}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 4096})}}
    RETURN_TYPES = ('LATENT', 'INT', 'INT')
    RETURN_NAMES = ('latent', 'width', 'height')
    FUNCTION = 'generate'
    CATEGORY = 'WLSH Nodes/latent'

    def generate(self, width, height, batch_size=1):
        adj_width = width // 8
        adj_height = height // 8
        latent = torch.zeros([batch_size, 4, adj_height, adj_width])
        return ({'samples': latent}, adj_width * 8, adj_height * 8)
```