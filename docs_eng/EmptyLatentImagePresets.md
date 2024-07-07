# Documentation
- Class name: EmptyLatentImagePresets
- Category: KJNodes
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

The EmptyLatentImagePresets node is designed to generate presets for potential images. It receives parameters such as size, inversion and volume size to produce potential image arrays and corresponding width and height.

# Input types
## Required
- dimensions
    - The dimension parameter specifies the size of the potential image to be generated. It is vital because it determines the spatial resolution of the output image.
    - Comfy dtype: STRING
    - Python dtype: str
- batch_size
    - The batch size parameter defines the number of potential images to be generated in a single batch. It is important to optimize resources when processing a large amount of data.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- invert
    - Reverse parameters allow users to reverse the width and height of potential images. This may be important in some important applications in the image direction.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- Latent
    - Potential parameters represent the array of potential images generated. It is important because it constitutes the core output of the node function.
    - Comfy dtype: ARRAY
    - Python dtype: torch.Tensor
- Width
    - Width parameters indicate the width of the potential image generated. This is an important message for further image processing tasks.
    - Comfy dtype: INT
    - Python dtype: int
- Height
    - Altitude parameters indicate the height of the potential image generated. Together with width, it provides the full size of the potential image.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class EmptyLatentImagePresets:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'dimensions': (['512 x 512', '768 x 512', '960 x 512', '1024 x 512', '1536 x 640', '1344 x 768', '1216 x 832', '1152 x 896', '1024 x 1024'], {'default': '512 x 512'}), 'invert': ('BOOLEAN', {'default': False}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 4096})}}
    RETURN_TYPES = ('LATENT', 'INT', 'INT')
    RETURN_NAMES = ('Latent', 'Width', 'Height')
    FUNCTION = 'generate'
    CATEGORY = 'KJNodes'

    def generate(self, dimensions, invert, batch_size):
        from nodes import EmptyLatentImage
        result = [x.strip() for x in dimensions.split('x')]
        if invert:
            width = int(result[1].split(' ')[0])
            height = int(result[0])
        else:
            width = int(result[0])
            height = int(result[1].split(' ')[0])
        latent = EmptyLatentImage().generate(width, height, batch_size)[0]
        return (latent, int(width), int(height))
```