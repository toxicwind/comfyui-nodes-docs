# Documentation
- Class name: CR_AspectRatioSocialMedia
- Category: icons.get('Comfyroll/Aspect Ratio')
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The node is designed to process and adjust image sizes to the requirements of specific social media platforms to ensure optimal demonstration effectiveness and user participation.

# Input types
## Required
- width
    - Width is the basic parameter for determining the horizontal dimensions of the image, affecting its length ratio and overall appearance on different social media platforms.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Height is the key parameter for defining vertical dimensions of images and working with width to meet the long-width ratio requirements of social media platforms.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- aspect_ratio
    - The width ratio preset allows quick selection of optimal sizes for various social media platforms, simplifying the image preparation process.
    - Comfy dtype: COMBO
    - Python dtype: str
- swap_dimensions
    - The exchange dimension option allows for the interchangeability of width and height and provides flexibility to meet the specific requirements of certain social media platforms.
    - Comfy dtype: COMBO
    - Python dtype: str
- upscale_factor
    - The magnification factor is used to expand image size and improve image quality and visibility when presented on social media platforms.
    - Comfy dtype: FLOAT
    - Python dtype: float
- prescale_factor
    - The prescaling factor is used to adjust the initial image size before further processing, affecting the resolution of the final output and performance on social media.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_size
    - The volume of images processed simultaneously is determined by the size of batch processing, which can increase efficiency and throughput in the processing of multiple social media images.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- width
    - Adjusted image width, optimized for selected social media platforms to ensure correct display and participation.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The adjusted image height is customized to meet the requirements of the selected social media platform in order to achieve the best demonstration effect.
    - Comfy dtype: INT
    - Python dtype: int
- upscale_factor
    - The original magnification factor used for the image is used to indicate the size of the magnification to achieve the best display of social media.
    - Comfy dtype: FLOAT
    - Python dtype: float
- prescale_factor
    - The original pre-scaling factor used for the image represents the initial size adjustment prior to further processing in order to optimize social media.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_size
    - The number of images processed during batch processing reflects the efficiency of processing image adjustments to multiple social media platforms.
    - Comfy dtype: INT
    - Python dtype: int
- empty_latent
    - The potential location of images is used for potential further processing or analysis of social media optimization workflows.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- show_help
    - A link to the document is used to further guide and understand how nodes can be used to optimize social media length.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_AspectRatioSocialMedia:

    @classmethod
    def INPUT_TYPES(s):
        aspect_ratios = ['custom', 'Instagram Portrait - 1080x1350', 'Instagram Square - 1080x1080', 'Instagram Landscape - 1080x608', 'Instagram Stories/Reels - 1080x1920', 'Facebook Landscape - 1080x1350', 'Facebook Marketplace - 1200x1200', 'Facebook Stories - 1080x1920', 'TikTok - 1080x1920', 'YouTube Banner - 2560×1440', 'LinkedIn Profile Banner - 1584x396', 'LinkedIn Page Cover - 1128x191', 'LinkedIn Post - 1200x627', 'Pinterest Pin Image - 1000x1500', 'CivitAI Cover - 1600x400', 'OpenArt App - 1500x1000']
        return {'required': {'width': ('INT', {'default': 1024, 'min': 64, 'max': 8192}), 'height': ('INT', {'default': 1024, 'min': 64, 'max': 8192}), 'aspect_ratio': (aspect_ratios,), 'swap_dimensions': (['Off', 'On'],), 'upscale_factor': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 100.0, 'step': 0.1}), 'prescale_factor': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 100.0, 'step': 0.1}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('INT', 'INT', 'FLOAT', 'FLOAT', 'INT', 'LATENT', 'STRING')
    RETURN_NAMES = ('width', 'height', 'upscale_factor', 'prescale_factor', 'batch_size', 'empty_latent', 'show_help')
    FUNCTION = 'Aspect_Ratio'
    CATEGORY = icons.get('Comfyroll/Aspect Ratio')

    def Aspect_Ratio(self, width, height, aspect_ratio, swap_dimensions, upscale_factor, prescale_factor, batch_size):
        if aspect_ratio == 'Instagram Portrait - 1080x1350':
            (width, height) = (1080, 1350)
        elif aspect_ratio == 'Instagram Square - 1080x1080':
            (width, height) = (1080, 1080)
        elif aspect_ratio == 'Instagram Landscape - 1080x608':
            (width, height) = (1080, 608)
        elif aspect_ratio == 'Instagram Stories/Reels - 1080x1920':
            (width, height) = (1080, 1920)
        elif aspect_ratio == 'Facebook Landscape - 1080x1350':
            (width, height) = (1080, 1350)
        elif aspect_ratio == 'Facebook Marketplace - 1200x1200':
            (width, height) = (1200, 1200)
        elif aspect_ratio == 'Facebook Stories - 1080x1920':
            (width, height) = (1080, 1920)
        elif aspect_ratio == 'TikTok - 1080x1920':
            (width, height) = (1080, 1920)
        elif aspect_ratio == 'YouTube Banner - 2560×1440':
            (width, height) = (2560, 1440)
        elif aspect_ratio == 'LinkedIn Profile Banner - 1584x396':
            (width, height) = (1584, 396)
        elif aspect_ratio == 'LinkedIn Page Cover - 1128x191':
            (width, height) = (1584, 396)
        elif aspect_ratio == 'LinkedIn Post - 1200x627':
            (width, height) = (1200, 627)
        elif aspect_ratio == 'Pinterest Pin Image - 1000x1500':
            (width, height) = (1000, 1500)
        elif aspect_ratio == 'Pinterest Cover Image - 1920x1080':
            (width, height) = (1920, 1080)
        elif aspect_ratio == 'CivitAI Cover - 1600x400':
            (width, height) = (1600, 400)
        elif aspect_ratio == 'OpenArt App - 1500x1000':
            (width, height) = (1500, 1000)
        if swap_dimensions == 'On':
            (width, height) = (height, width)
        width = int(width * prescale_factor)
        height = int(height * prescale_factor)
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Aspect-Ratio-Nodes#cr-aspect-ratio-scial-media'
        return (width, height, upscale_factor, prescale_factor, batch_size, {'samples': latent}, show_help)
```