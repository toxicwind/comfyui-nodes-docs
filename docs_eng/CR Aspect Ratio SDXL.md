# Documentation
- Class name: CR_AspectRatio_SDXL
- Category: Comfyroll/Essential/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_AspectRadio_SDXL node is designed to manage and adjust the size of the image according to the specified vertical ratio. It allows for the selection of predefined vertical or custom input and offers options for exchanging dimensions and magnifying the image. The node ensures that the image is properly formatted to accommodate various display purposes and enhances the workflow for media processing tasks.

# Input types
## Required
- width
    - The width parameter defines the horizontal dimensions of the image. It is essential to set the initial size and calculate the correct vertical ratio.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters set the vertical dimensions of the image, working with width to determine the size of the image as a whole.
    - Comfy dtype: INT
    - Python dtype: int
- aspect_ratio
    - The argument_ratio determines the relationship between image sizes. It allows the selection of common scale or custom input to meet specific requirements.
    - Comfy dtype: COMBO['custom', '1:1 square 1024x1024', '3:4 portrait 896x1152', '5:8 portrait 832x1216', '9:16 portrait 768x1344', '9:21 portrait 640x1536', '4:3 landscape 1152x896', '3:2 landscape 1216x832', '16:9 landscape 1344x768', '21:9 landscape 1536x640']
    - Python dtype: str
## Optional
- swap_dimensions
    - The swap_dimensions parameter provides an option to exchange width and height values for scenarios that require inverse image direction.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
- upscale_factor1
    - The upscale_factor1 parameter controls the first level of image magnification and allows the image to be resized without changing the vertical ratio.
    - Comfy dtype: FLOAT
    - Python dtype: float
- upscale_factor2
    - Upscale_factor2 parameters manage the second level of image magnification and provide further control over the final size of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_size
    - Match_size parameters specify how many images are processed at the same time, which optimizes the performance of the batch image processing task.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- width
    - The width output reflects the application of the selected vertical ratio and the adjusted horizontal size of the image after any magnification factor.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - High output corresponds to the vertical size of the image adjusted to take into account vertical ratio and magnification settings.
    - Comfy dtype: INT
    - Python dtype: int
- upscale_factor1
    - The output upscale_factor1 provides a magnifying factor for image width, affecting the final resolution.
    - Comfy dtype: FLOAT
    - Python dtype: float
- upscale_factor2
    - Upscale_factor2 output instructions should be used for submersible magnification factors at image heights to further refine resolution.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_size
    - Match_size output indicates the number of images processed during each cycle, which affects the efficiency of large-scale image processing.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - Show_help output provides a URL link to a document to get further help and information about node functions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_AspectRatio_SDXL:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 1024, 'min': 64, 'max': 2048}), 'height': ('INT', {'default': 1024, 'min': 64, 'max': 2048}), 'aspect_ratio': (['custom', '1:1 square 1024x1024', '3:4 portrait 896x1152', '5:8 portrait 832x1216', '9:16 portrait 768x1344', '9:21 portrait 640x1536', '4:3 landscape 1152x896', '3:2 landscape 1216x832', '16:9 landscape 1344x768', '21:9 landscape 1536x640'],), 'swap_dimensions': (['Off', 'On'],), 'upscale_factor1': ('FLOAT', {'default': 1, 'min': 1, 'max': 2000}), 'upscale_factor2': ('FLOAT', {'default': 1, 'min': 1, 'max': 2000}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('INT', 'INT', 'FLOAT', 'FLOAT', 'INT', 'STRING')
    RETURN_NAMES = ('INT', 'INT', 'FLOAT', 'FLOAT', 'INT', 'show_help')
    FUNCTION = 'Aspect_Ratio'
    CATEGORY = icons.get('Comfyroll/Essential/Legacy')

    def Aspect_Ratio(self, width, height, aspect_ratio, swap_dimensions, upscale_factor1, upscale_factor2, batch_size):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Legacy-Nodes#cr-aspect-ratio-sdxl'
        if aspect_ratio == '1:1 square 1024x1024':
            (width, height) = (1024, 1024)
        elif aspect_ratio == '3:4 portrait 896x1152':
            (width, height) = (896, 1152)
        elif aspect_ratio == '5:8 portrait 832x1216':
            (width, height) = (832, 1216)
        elif aspect_ratio == '9:16 portrait 768x1344':
            (width, height) = (768, 1344)
        elif aspect_ratio == '9:21 portrait 640x1536':
            (width, height) = (640, 1536)
        elif aspect_ratio == '4:3 landscape 1152x896':
            (width, height) = (1152, 896)
        elif aspect_ratio == '3:2 landscape 1216x832':
            (width, height) = (1216, 832)
        elif aspect_ratio == '16:9 landscape 1344x768':
            (width, height) = (1344, 768)
        elif aspect_ratio == '21:9 landscape 1536x640':
            (width, height) = (1536, 640)
        if swap_dimensions == 'On':
            return (height, width, upscale_factor1, upscale_factor2, batch_size, show_help)
        else:
            return (width, height, upscale_factor1, upscale_factor2, batch_size, show_help)
```