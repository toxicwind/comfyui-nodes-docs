# Documentation
- Class name: CR_ImagePipeEdit
- Category: Comfyroll/Pipe/Image
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_ImagePipeEdit node is designed to facilitate the editing and enhancement of image data within the pipeline structure. It allows users to modify image properties, such as width, height and magnification factors, to ensure that the output image meets the required specifications. The node plays a key role in the image processing workflow and allows fine-tuning of visual content without disrupting the integrity of the overall pipeline.

# Input types
## Required
- pipe
    - The `pipe' parameter is necessary because it represents an image pipeline to be edited by nodes. This is a key input that determines the starting point for all subsequent image modifications and processing.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple[str, int, int, float]
## Optional
- image
    - The optional `image' parameter allows the user to replace the current image in the conduit. It is particularly useful when a specific image content is needed for further processing or analysis.
    - Comfy dtype: IMAGE
    - Python dtype: str
- width
    - The `width' parameter is used to specify the new width of the image. It is an optional input that can be adjusted to the requirements of different displays or output media.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The `height' parameter determines the new height of the image. Similar to the width, it is optional and can be set up to achieve the required vertical ratio or adapt to specific presentation needs.
    - Comfy dtype: INT
    - Python dtype: int
- upscale_factor
    - The `upscape_factor' parameter is optional and defines the zoom factor for image magnification. It is particularly important for enhancing image quality without compromising the original resolution.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- pipe
    - The `pipe' output represents the modified image conduit, including the updated image and its properties, such as width, height and magnification factors.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple[str, int, int, float]
- show_help
    - The `show_help' output provides a URL linked to the document page to obtain further help or information about the use of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ImagePipeEdit:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pipe': ('PIPE_LINE',)}, 'optional': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 64, 'max': 2048, 'forceInput': True}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 2048, 'forceInput': True}), 'upscale_factor': ('FLOAT', {'default': 1, 'min': 1, 'max': 2000, 'forceInput': True})}}
    RETURN_TYPES = ('PIPE_LINE', 'STRING')
    RETURN_NAMES = ('pipe', 'show_help')
    FUNCTION = 'pipe_edit'
    CATEGORY = icons.get('Comfyroll/Pipe/Image')

    def pipe_edit(self, pipe, image=None, width=None, height=None, upscale_factor=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pipe-Nodes#cr-image-pipe-edit'
        (new_image, new_width, new_height, new_upscale_factor) = pipe
        if image is not None:
            new_image = image
        if width is not None:
            new_width = width
        if height is not None:
            new_height = height
        if upscale_factor is not None:
            new_upscale_factor = upscale_factor
        pipe = (new_image, new_width, new_height, new_upscale_factor)
        return (pipe, show_help)
```