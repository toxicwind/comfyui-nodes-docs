# Documentation
- Class name: CR_ImagePipeOut
- Category: Comfyroll/Pipe/Image
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_ImagePipeOut node is designed to facilitate the output of image data in the current waterline architecture. It plays a key role in the final phase of the image processing workflow to ensure that image data correctly flow out of the system. The node is good at processing the transition of image data from the processing stream to the output interface and provides a seamless integration point for image data dissemination.

# Input types
## Required
- pipe
    - The `pipe' parameter is essential for CR_ImagePipeOut node, as it represents the flow line that carries the image data to be exported. It is through this parameter that the node receives image information and then processes it into output.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple[str, int, int, float]

# Output types
- pipe
    - The ‘pipe’ output parameter represents the complete processing of image data and preparation for the continuation of the flow line after output. It preserves the integrity of the data stream and ensures that the follow-up process can proceed smoothly.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple[str, int, int, float]
- image
    - The `image'output parameter is a processed image from CR_ImagePipeOut node. It represents the result of an image processing stream and is presented as an end-user or end-product of a follow-on system.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- width
    - The `width' output parameter provides the width of the output image in pixels. This information is essential to understand the size of the image and the purpose of any further image operation or display.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height'output parameter indicates the height of the output image in pixels. It defines the overall size of the image with width and is essential for the correct image presentation.
    - Comfy dtype: INT
    - Python dtype: int
- upscale_factor
    - The `upscape_factor' output parameter represents the zoom factor applied to images during processing. It is an important indicator of image quality assessment and can influence subsequent image processing decisions.
    - Comfy dtype: FLOAT
    - Python dtype: float
- show_help
    - The `show_help' output parameter provides a link to the document or URL of the help page associated with the CR_ImagePipeOut node. It is a quick reference for users seeking more information or help in using the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ImagePipeOut:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pipe': ('PIPE_LINE',)}}
    RETURN_TYPES = ('PIPE_LINE', 'IMAGE', 'INT', 'INT', 'FLOAT', 'STRING')
    RETURN_NAMES = ('pipe', 'image', 'width', 'height', 'upscale_factor', 'show_help')
    FUNCTION = 'pipe_out'
    CATEGORY = icons.get('Comfyroll/Pipe/Image')

    def pipe_out(self, pipe):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pipe-Nodes#cr-image-pipe-out'
        (image, width, height, upscale_factor) = pipe
        return (pipe, image, width, height, upscale_factor, show_help)
```