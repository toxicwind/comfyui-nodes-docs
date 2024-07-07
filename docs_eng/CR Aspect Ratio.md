# Documentation
- Class name: CR_AspectRatio
- Category: Comfyroll/Aspect Ratio
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_AspectRadio node is designed to operate and define the vertical ratio of the image. It provides various default vertical ratios and allows custom dimensions. The function of the node allows users to select a vertical ratio, choose whether to exchange dimensions and apply the zoom factor to achieve the required output dimensions. It also supports batch processing to improve efficiency.

# Input types
## Required
- width
    - The " width " parameter specifies the desired width of the image. It plays a key role in determining the vertical and final dimensions of the image.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The Height parameter defines the expected height of the image. It works with the Width parameter to create the vertical ratio of the image.
    - Comfy dtype: INT
    - Python dtype: int
- aspect_ratio
    - The 'aspct_ratio'parameter allows the user to select or enter a custom vertical ratio from the predefined vertical ratio list. It is the core of node operations, as it determines the proportion of output images.
    - Comfy dtype: STRING
    - Python dtype: str
- swap_dimensions
    - The " swap_dimensions " parameter provides an option to exchange width and height values. This is very useful in some image operations, where the direction of the image is important.
    - Comfy dtype: STRING
    - Python dtype: str
- upscale_factor
    - The "upscale_factor " parameter is used to increase the size of the image. It multiplys the current size by the specified factor, increasing the resolution.
    - Comfy dtype: FLOAT
    - Python dtype: float
- prescale_factor
    - The " prescale_factor" parameter is used to adjust the initial size before any other conversion. It can be used to optimize processing or achieve specific design requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_size
    - The "batch_size" parameter determines the number of images processed in a single operation. It is essential to manage computing resources and improve workflow efficiency.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- width
    - The "width" output provides the final width of all converted images after application.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height' output gives the final height of the processed image.
    - Comfy dtype: INT
    - Python dtype: int
- upscale_factor
    - The "upscape_factor" output reflects the zoom factor used to magnify the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- prescale_factor
    - The "prescale_factor" output instruction applies to the initial zoom factor of image size.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_size
    - The "batch_size" output indicates the number of images processed during the operation.
    - Comfy dtype: INT
    - Python dtype: int
- empty_latent
    - The "empty_latet" output is a placeholder for potential expressions that may be used in a follow-up image-processing task.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- show_help
    - The Show_help output provides a URL link to the document for further guidance and help.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_AspectRatio:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        aspect_ratios = ['custom', 'SD1.5 - 1:1 square 512x512', 'SD1.5 - 2:3 portrait 512x768', 'SD1.5 - 3:4 portrait 512x682', 'SD1.5 - 3:2 landscape 768x512', 'SD1.5 - 4:3 landscape 682x512', 'SD1.5 - 16:9 cinema 910x512', 'SD1.5 - 1.85:1 cinema 952x512', 'SD1.5 - 2:1 cinema 1024x512', 'SDXL - 1:1 square 1024x1024', 'SDXL - 3:4 portrait 896x1152', 'SDXL - 5:8 portrait 832x1216', 'SDXL - 9:16 portrait 768x1344', 'SDXL - 9:21 portrait 640x1536', 'SDXL - 4:3 landscape 1152x896', 'SDXL - 3:2 landscape 1216x832', 'SDXL - 16:9 landscape 1344x768', 'SDXL - 21:9 landscape 1536x640']
        return {'required': {'width': ('INT', {'default': 1024, 'min': 64, 'max': 8192}), 'height': ('INT', {'default': 1024, 'min': 64, 'max': 8192}), 'aspect_ratio': (aspect_ratios,), 'swap_dimensions': (['Off', 'On'],), 'upscale_factor': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 100.0, 'step': 0.1}), 'prescale_factor': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 100.0, 'step': 0.1}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('INT', 'INT', 'FLOAT', 'FLOAT', 'INT', 'LATENT', 'STRING')
    RETURN_NAMES = ('width', 'height', 'upscale_factor', 'prescale_factor', 'batch_size', 'empty_latent', 'show_help')
    FUNCTION = 'Aspect_Ratio'
    CATEGORY = icons.get('Comfyroll/Aspect Ratio')

    def Aspect_Ratio(self, width, height, aspect_ratio, swap_dimensions, upscale_factor, prescale_factor, batch_size):
        if aspect_ratio == 'SD1.5 - 1:1 square 512x512':
            (width, height) = (512, 512)
        elif aspect_ratio == 'SD1.5 - 2:3 portrait 512x768':
            (width, height) = (512, 768)
        elif aspect_ratio == 'SD1.5 - 16:9 cinema 910x512':
            (width, height) = (910, 512)
        elif aspect_ratio == 'SD1.5 - 3:4 portrait 512x682':
            (width, height) = (512, 682)
        elif aspect_ratio == 'SD1.5 - 3:2 landscape 768x512':
            (width, height) = (768, 512)
        elif aspect_ratio == 'SD1.5 - 4:3 landscape 682x512':
            (width, height) = (682, 512)
        elif aspect_ratio == 'SD1.5 - 1.85:1 cinema 952x512':
            (width, height) = (952, 512)
        elif aspect_ratio == 'SD1.5 - 2:1 cinema 1024x512':
            (width, height) = (1024, 512)
        elif aspect_ratio == 'SD1.5 - 2.39:1 anamorphic 1224x512':
            (width, height) = (1224, 512)
        if aspect_ratio == 'SDXL - 1:1 square 1024x1024':
            (width, height) = (1024, 1024)
        elif aspect_ratio == 'SDXL - 3:4 portrait 896x1152':
            (width, height) = (896, 1152)
        elif aspect_ratio == 'SDXL - 5:8 portrait 832x1216':
            (width, height) = (832, 1216)
        elif aspect_ratio == 'SDXL - 9:16 portrait 768x1344':
            (width, height) = (768, 1344)
        elif aspect_ratio == 'SDXL - 9:21 portrait 640x1536':
            (width, height) = (640, 1536)
        elif aspect_ratio == 'SDXL - 4:3 landscape 1152x896':
            (width, height) = (1152, 896)
        elif aspect_ratio == 'SDXL - 3:2 landscape 1216x832':
            (width, height) = (1216, 832)
        elif aspect_ratio == 'SDXL - 16:9 landscape 1344x768':
            (width, height) = (1344, 768)
        elif aspect_ratio == 'SDXL - 21:9 landscape 1536x640':
            (width, height) = (1536, 640)
        if swap_dimensions == 'On':
            (width, height) = (height, width)
        width = int(width * prescale_factor)
        height = int(height * prescale_factor)
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Aspect-Ratio-Nodes#cr-aspect-ratio'
        return (width, height, upscale_factor, prescale_factor, batch_size, {'samples': latent}, show_help)
```