# Documentation
- Class name: CR_AspectRatioForPrint
- Category: Comfyroll/Aspect Ratio
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_AspectRadioForPrint is designed to calculate and adjust the size of the image or print according to the specified width ratio. It allows for the exchange of dimensions and the application of the zoom factor to achieve the required output size to meet various printing requirements.

# Input types
## Required
- width
    - The width parameters determine the horizontal dimensions of the image or print. It is essential to maintain the width ratio and to scale the image correctly.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters set the vertical dimensions of the image or print. It works with width to ensure that the width ratio is maintained.
    - Comfy dtype: INT
    - Python dtype: int
- aspect_ratio
    - The width ratio defines the ratio between width and height. It is a key factor in calculating the final size.
    - Comfy dtype: STRING
    - Python dtype: str
- swap_dimensions
    - The swap_dimensions parameters allow users to exchange widths and heights when required to provide flexibility for size adjustments.
    - Comfy dtype: STRING
    - Python dtype: str
- upscale_factor
    - Upscale_factor is used to magnify image sizes. For high-resolution printing or numerical magnification, this is an important parameter.
    - Comfy dtype: FLOAT
    - Python dtype: float
- prescale_factor
    - Prescale_factor parameters are allowed to be initially scaled in image sizes before being used for width adjustment.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_size
    - Match_size parameters specify the number of images to be processed once. This is essential for the efficient processing of a large number of images.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- width
    - The output width is the horizontal size of the image or print after application of the width ratio and the zoom factor.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The output height is the vertical size of the image or print after application of the width ratio and the zoom factor.
    - Comfy dtype: INT
    - Python dtype: int
- upscale_factor
    - Upscale_factor output reflects the zoom factor used to magnify the image size.
    - Comfy dtype: FLOAT
    - Python dtype: float
- prescale_factor
    - The prescale_factor output indicates the initial zoom factor applied prior to the width ratio adjustment.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_size
    - Match_size output shows the number of images processed in the current operation.
    - Comfy dtype: INT
    - Python dtype: int
- empty_latent
    - Empty_latet output provides an empty representation of the post-processing image and can be used for further image-processing tasks.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- show_help
    - Show_help output provides a link to the document for further help and guidance on the use of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_AspectRatioForPrint:

    @classmethod
    def INPUT_TYPES(cls):
        aspect_ratios = list(PRINT_SIZES.keys())
        return {'required': {'width': ('INT', {'default': 1024, 'min': 64, 'max': 8192}), 'height': ('INT', {'default': 1024, 'min': 64, 'max': 8192}), 'aspect_ratio': (aspect_ratios,), 'swap_dimensions': (['Off', 'On'],), 'upscale_factor': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 100.0, 'step': 0.1}), 'prescale_factor': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 100.0, 'step': 0.1}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('INT', 'INT', 'FLOAT', 'FLOAT', 'INT', 'LATENT', 'STRING')
    RETURN_NAMES = ('width', 'height', 'upscale_factor', 'prescale_factor', 'batch_size', 'empty_latent', 'show_help')
    FUNCTION = 'Aspect_Ratio'
    CATEGORY = icons.get('Comfyroll/Aspect Ratio')

    def Aspect_Ratio(self, width, height, aspect_ratio, swap_dimensions, upscale_factor, prescale_factor, batch_size):
        if aspect_ratio in PRINT_SIZES:
            (width, height) = PRINT_SIZES[aspect_ratio]
        if swap_dimensions == 'On':
            (width, height) = (height, width)
        width = int(width * prescale_factor)
        height = int(height * prescale_factor)
        print(f'Width: {width}, Height: {height}')
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Aspect-Ratio-Nodes#cr-aspect-ratio-scial-media'
        return (width, height, upscale_factor, prescale_factor, batch_size, {'samples': latent}, show_help)
```