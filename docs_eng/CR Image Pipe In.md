# Documentation
- Class name: CR_ImagePipeIn
- Category: Comfyroll/Pipe/Image
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ImagePipeIn is designed to facilitate the process of image input to the data pipeline. It plays a key role in preparing image data for use in the subsequent processing phase, ensuring that images are properly formatted and scaled according to the specified parameters.

# Input types
## Optional
- image
    - The image parameter is essential for the node because it defines the input image to be processed. This is the main data source for node operations and affects how the next step is executed.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, bytes, Image.Image]
- width
    - The width parameter specifies the desired width of the post-processed image. It is important to control the size of the output image and to maintain the vertical ratio when the height is also specified.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters set the desired height of the image after processing. It works with the width parameters to determine the ultimate size of the image.
    - Comfy dtype: INT
    - Python dtype: int
- upscale_factor
    - The upscale_factor parameter is used to improve the resolution of the image. During the magnification process, it is important to improve the quality of the image without losing important details.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- pipe
    - Pipe output is a structured data type that encapsifies the processed image and its associated parameters. It serves as a channel for the transmission of image data to the next phase of the pipeline.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple[Any, int, int, float]
- show_help
    - Show_help output provides a document URL link for further help. It is particularly useful for users seeking more information about node functions and usage.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ImagePipeIn:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}, 'optional': {'image': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 64, 'max': 2048}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 2048}), 'upscale_factor': ('FLOAT', {'default': 1, 'min': 1, 'max': 2000})}}
    RETURN_TYPES = ('PIPE_LINE', 'STRING')
    RETURN_NAMES = ('pipe', 'show_help')
    FUNCTION = 'pipe_in'
    CATEGORY = icons.get('Comfyroll/Pipe/Image')

    def pipe_in(self, image=0, width=0, height=0, upscale_factor=0):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pipe-Nodes#cr-image-pipe-in'
        pipe_line = (image, width, height, upscale_factor)
        return (pipe_line, show_help)
```