# Documentation
- Class name: CR_SDXLAspectRatio
- Category: Comfyroll/Aspect Ratio
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_SDXLAspectRadio node is designed to adjust the size of the image according to the specified vertical ratio. It allows users to select or enter custom dimensions from the predefined vertical ratio list. The node also provides options to exchange dimensions and apply magnification factors to the size of the result image. The main function is to ensure that the output corresponds to the required vertical ratio, thereby facilitating image processing tasks requiring a specific dimension.

# Input types
## Required
- width
    - The `width' parameter sets the width of the image in pixels. This is a key component because it directly affects the vertical ratio and final dimensions of the image. In the image processing workflow, this parameter is essential for achieving the required visual output.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The `height' parameter defines the height of the image in pixels. Together with the `width' parameter, it determines the overall vertical ratio of the image. `height' is essential to align the image size with specific requirements or standards.
    - Comfy dtype: INT
    - Python dtype: int
- aspect_ratio
    - The `aspect_ratio' parameter allows the user to select a predefined vertical ratio or enter a custom vertical ratio. It plays an important role in shaping the image size according to the required format, which is essential for various image processing and display purposes.
    - Comfy dtype: STRING
    - Python dtype: str
- swap_dimensions
    - The'swap_dimensions' parameter provides an option to exchange widths and heights. This function can be useful when the vertical ratio entered is not consistent with the intended direction of the image and allows flexibility in size operations.
    - Comfy dtype: STRING
    - Python dtype: str
- upscale_factor
    - The `upscale_factor' parameter is used to increase the size of the image by specifying the factor. This is an important feature that enhances the resolution of the image without changing the vertical ratio, which is very useful for high-quality image output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_size
    - The `batch_size' parameter determines the number of images processed in a single operation. It is essential to optimize computing resources and improve the efficiency of image-processing tasks, especially when processing large volumes of images.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- width
    - The `width' output provides the range ratio selected for the application and the ultimate width of the image after any dimension exchange or magnification factor. It is the key result of node operations and is essential for subsequent image processing steps.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height'output provides the final height of the image processed after node settings. It is the key information to ensure that the image meets the size required for display or further processing.
    - Comfy dtype: INT
    - Python dtype: int
- upscale_factor
    - The `upscape_factor' output reflects the zoom factor applied to the image. It helps to track the relationship between the original size of the image and the current size.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_size
    - The `batch_size' output indicates the number of images processed. This may be important for downstream tasks that need to know the volume size to be properly aligned or further calculated.
    - Comfy dtype: INT
    - Python dtype: int
- empty_latent
    - `Empty_latet' output is a placeholder for potential expressions that may be used in more advanced image-processing applications. It represents the ability to integrate nodes with complex workflows, although in this context it is returned to an empty structure.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- show_help
    - The'show_help' output provides a URL link to the node document page. It is a useful resource for users seeking more information or help on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SDXLAspectRatio:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        aspect_ratios = ['custom', '1:1 square 1024x1024', '3:4 portrait 896x1152', '5:8 portrait 832x1216', '9:16 portrait 768x1344', '9:21 portrait 640x1536', '4:3 landscape 1152x896', '3:2 landscape 1216x832', '16:9 landscape 1344x768', '21:9 landscape 1536x640']
        return {'required': {'width': ('INT', {'default': 1024, 'min': 64, 'max': 8192}), 'height': ('INT', {'default': 1024, 'min': 64, 'max': 8192}), 'aspect_ratio': (aspect_ratios,), 'swap_dimensions': (['Off', 'On'],), 'upscale_factor': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 100.0, 'step': 0.1}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('INT', 'INT', 'FLOAT', 'INT', 'LATENT', 'STRING')
    RETURN_NAMES = ('width', 'height', 'upscale_factor', 'batch_size', 'empty_latent', 'show_help')
    FUNCTION = 'Aspect_Ratio'
    CATEGORY = icons.get('Comfyroll/Aspect Ratio')

    def Aspect_Ratio(self, width, height, aspect_ratio, swap_dimensions, upscale_factor, batch_size):
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
            (width, height) = (height, width)
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Aspect-Ratio-Nodes#cr-sdxl-aspect-ratio'
        return (width, height, upscale_factor, batch_size, {'samples': latent}, show_help)
```