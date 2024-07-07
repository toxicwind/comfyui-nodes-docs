# Documentation
- Class name: CR_AspectRatioSD15
- Category: Comfyroll/Aspect Ratio
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_AspectRadioSD15 is a node for managing and adjusting image width ratios. It allows users to select a predefined width ratio or enter a custom size, and provides options for exchanging sizes and magnifying images. The main function of the node is to ensure that images are properly scaled and directed to meet various display or print needs.

# Input types
## Required
- width
    - Width is a key parameter that defines the horizontal dimensions of the image. It works with the height parameters to determine the width ratio of the image. Node uses this value to calculate the correct scaling and dimensions of the output.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Height is a key parameter, which sets the vertical dimensions of the image. When paired with the width parameter, it is essential to maintain the required width ratio. Node uses this parameter to ensure that the image's vertical scaling is accurate.
    - Comfy dtype: INT
    - Python dtype: int
- aspect_ratio
    - A width ratio parameter is essential because it determines the proportional relationship between image width and height. It provides a predefined ratio selection or a custom input option that allows flexibility in image formatting settings.
    - Comfy dtype: STRING
    - Python dtype: str
- swap_dimensions
    - The swap_dimensions parameter allows the user to switch between width and height. This function is useful when the width ratio requires a different direction or the user needs a manual size switch.
    - Comfy dtype: STRING
    - Python dtype: str
- upscale_factor
    - The upscale_factor parameter is important to control the magnification multipliers of the image. It multiplys the original size to achieve a larger image size without affecting the width ratio.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_size
    - Batch size is an important parameter that determines the number of images that are processed simultaneously. It is particularly useful for optimizing performance when processing large numbers of images.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- width
    - Width output parameters represent the final horizontal dimensions of the image after application of the selected width height ratio and any zoom factor.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - High output parameters represent the final vertical dimensions of the image after considering the width ratio and scaling adjustment.
    - Comfy dtype: INT
    - Python dtype: int
- upscale_factor
    - The upscale_factor output reflects the magnification level applied to the image to increase its size.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_size
    - Batch-size output parameters indicate the number of images processed in a single batch, which is essential for understanding the node's throughput.
    - Comfy dtype: INT
    - Python dtype: int
- empty_latent
    - Empty_late output parameters provide an empty potential space for image batches to be used for further processing or analysis in downstream tasks.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- show_help
    - Show_help output parameters provide a URL linked to the document page to obtain additional guidance and information about the use of this node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_AspectRatioSD15:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        aspect_ratios = ['custom', '1:1 square 512x512', '1:1 square 1024x1024', '2:3 portrait 512x768', '3:4 portrait 512x682', '3:2 landscape 768x512', '4:3 landscape 682x512', '16:9 cinema 910x512', '1.85:1 cinema 952x512', '2:1 cinema 1024x512', '2.39:1 anamorphic 1224x512']
        return {'required': {'width': ('INT', {'default': 512, 'min': 64, 'max': 8192}), 'height': ('INT', {'default': 512, 'min': 64, 'max': 8192}), 'aspect_ratio': (aspect_ratios,), 'swap_dimensions': (['Off', 'On'],), 'upscale_factor': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 100.0, 'step': 0.1}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('INT', 'INT', 'FLOAT', 'INT', 'LATENT', 'STRING')
    RETURN_NAMES = ('width', 'height', 'upscale_factor', 'batch_size', 'empty_latent', 'show_help')
    FUNCTION = 'Aspect_Ratio'
    CATEGORY = icons.get('Comfyroll/Aspect Ratio')

    def Aspect_Ratio(self, width, height, aspect_ratio, swap_dimensions, upscale_factor, batch_size):
        if aspect_ratio == '2:3 portrait 512x768':
            (width, height) = (512, 768)
        elif aspect_ratio == '3:2 landscape 768x512':
            (width, height) = (768, 512)
        elif aspect_ratio == '1:1 square 512x512':
            (width, height) = (512, 512)
        elif aspect_ratio == '1:1 square 1024x1024':
            (width, height) = (1024, 1024)
        elif aspect_ratio == '16:9 cinema 910x512':
            (width, height) = (910, 512)
        elif aspect_ratio == '3:4 portrait 512x682':
            (width, height) = (512, 682)
        elif aspect_ratio == '4:3 landscape 682x512':
            (width, height) = (682, 512)
        elif aspect_ratio == '1.85:1 cinema 952x512':
            (width, height) = (952, 512)
        elif aspect_ratio == '2:1 cinema 1024x512':
            (width, height) = (1024, 512)
        elif aspect_ratio == '2.39:1 anamorphic 1224x512':
            (width, height) = (1224, 512)
        if swap_dimensions == 'On':
            (width, height) = (height, width)
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Aspect-Ratio-Nodes#cr-sd15-aspect-ratio'
        return (width, height, upscale_factor, batch_size, {'samples': latent}, show_help)
```