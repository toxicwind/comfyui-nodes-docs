# Documentation
- Class name: WLSH_SDXL_Quick_Empty_Latent
- Category: WLSH Nodes/latent
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The `generate' method of WLSH_SDXL_Quick_Empty_Latent is responsible for creating an empty spatial representation of the image. It operates by accepting image resolution and direction parameters, and then generates a potential load filled with zero. This potential load is used in the image generation stream for further processing or analysis and provides an infrastructure that can be modified to represent image characteristics.

# Input types
## Required
- resolution
    - The `resoltion' parameter defines the size of the image to be created in potential space. It is a key determinant of the potential volume size and structure that directly influences the subsequent image generation process.
    - Comfy dtype: STR
    - Python dtype: str
- direction
    - The `direction' parameter specifies the direction of the image, which can be `landscape' (horizontal) or `portrait' (vertical). This affects the width and altitude of the image, and is therefore essential for the correct generation of potential loads.
    - Comfy dtype: STR
    - Python dtype: str
## Optional
- batch_size
    - The `batch_size' parameter indicates the number of images to be processed in a single operation. It is an optional parameter that can be used to control the efficiency of processing, allowing multiple images to be processed simultaneously.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- latent
    - The 'latent' output provides the potential space mass generated, which is the basis for the image generation. It is a zero-filled load that will be further operated to indicate the required image characteristics.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- width
    - The 'width' output represents the adjusted width of the potential space, which is a multiplier of 8. This value is important for understanding the dimensions of the potential mass generated and is used in the image generation process.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height'output represents the adjusted height of the potential space, which is also a multiplier of 8. It is an important parameter for the dimensions of the potential mass and plays a role in the overall image generation workflow.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_SDXL_Quick_Empty_Latent:
    resolution = ['1024x1024', '1152x896', '1216x832', '1344x768', '1536x640']
    direction = ['landscape', 'portrait']

    def __init__(self, device='cpu'):
        self.device = device

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'resolution': (s.resolution,), 'direction': (s.direction,), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('LATENT', 'INT', 'INT')
    RETURN_NAMES = ('latent', 'width', 'height')
    FUNCTION = 'generate'
    CATEGORY = 'WLSH Nodes/latent'

    def generate(self, resolution, direction, batch_size=1):
        (width, height) = resolution.split('x')
        width = int(width)
        height = int(height)
        if direction == 'portrait':
            (width, height) = (height, width)
        adj_width = width // 8
        adj_height = height // 8
        latent = torch.zeros([batch_size, 4, adj_height, adj_width])
        return ({'samples': latent}, adj_width * 8, adj_height * 8)
```