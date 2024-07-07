# Documentation
- Class name: CR_ColorTint
- Category: Comfyroll/Graphics/Filter
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_ColorTint node is designed to apply colour colours to images and enhance their visual attractiveness by adding the selected colours. The node provides a multifunctional colour operation that allows users to choose or enter custom colour hexadecimal values from predefined colours. It optimizes custom colour applications and batch processing, ensuring the efficiency and consistency of multiple images.

# Input types
## Required
- image
    - The image parameter is necessary because it is the input that the node will process. It is the basis for applying colour palette effects and is a key component of node operations.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- strength
    - The strength parameter controls the strength of the colour tone applied to the image. It allows fine-tuning to achieve the desired visual result. It is an important aspect of the node function.
    - Comfy dtype: FLOAT
    - Python dtype: float
- mode
    - Model parameters determine the type of colour tone that you want to apply. It provides a range of preset options that allow users to select a particular color tone appropriate to their creative vision.
    - Comfy dtype: COMBO['custom', 'white', 'black', 'sepia', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'purple', 'orange', 'warm', 'cool', 'lime', 'navy', 'vintage', 'rose', 'teal', 'maroon', 'peach', 'lavender', 'olive']
    - Python dtype: str
- tint_color_hex
    - When choosing a custom colour, use the tint_collor_hex parameter. It allows the user to specify the exact colour hexadecimal value for the tone, providing a high degree of customization for node operations.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - The IMAGE output is a processed image with colours. It represents the end result of node operations and is the main output for further use or display.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL that points to the node document. It is a useful resource for users seeking to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ColorTint:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        tints = ['custom', 'white', 'black', 'sepia', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'purple', 'orange', 'warm', 'cool', 'lime', 'navy', 'vintage', 'rose', 'teal', 'maroon', 'peach', 'lavender', 'olive']
        return {'required': {'image': ('IMAGE',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 1.0, 'step': 0.1}), 'mode': (tints,)}, 'optional': {'tint_color_hex': ('STRING', {'multiline': False, 'default': '#000000'})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'color_tint'
    CATEGORY = icons.get('Comfyroll/Graphics/Filter')

    def color_tint(self, image: torch.Tensor, strength, mode: str='sepia', tint_color_hex='#000000'):
        if strength == 0:
            return (image,)
        tint_color = get_color_values(mode, tint_color_hex, color_mapping)
        color_rgb = tuple([value / 255 for value in tint_color])
        sepia_weights = torch.tensor([0.2989, 0.587, 0.114]).view(1, 1, 1, 3).to(image.device)
        mode_filters = {'custom': torch.tensor([color_rgb[0], color_rgb[1], color_rgb[2]]), 'white': torch.tensor([1, 1, 1]), 'black': torch.tensor([0, 0, 0]), 'sepia': torch.tensor([1.0, 0.8, 0.6]), 'red': torch.tensor([1.0, 0.6, 0.6]), 'green': torch.tensor([0.6, 1.0, 0.6]), 'blue': torch.tensor([0.6, 0.8, 1.0]), 'cyan': torch.tensor([0.6, 1.0, 1.0]), 'magenta': torch.tensor([1.0, 0.6, 1.0]), 'yellow': torch.tensor([1.0, 1.0, 0.6]), 'purple': torch.tensor([0.8, 0.6, 1.0]), 'orange': torch.tensor([1.0, 0.7, 0.3]), 'warm': torch.tensor([1.0, 0.9, 0.7]), 'cool': torch.tensor([0.7, 0.9, 1.0]), 'lime': torch.tensor([0.7, 1.0, 0.3]), 'navy': torch.tensor([0.3, 0.4, 0.7]), 'vintage': torch.tensor([0.9, 0.85, 0.7]), 'rose': torch.tensor([1.0, 0.8, 0.9]), 'teal': torch.tensor([0.3, 0.8, 0.8]), 'maroon': torch.tensor([0.7, 0.3, 0.5]), 'peach': torch.tensor([1.0, 0.8, 0.6]), 'lavender': torch.tensor([0.8, 0.6, 1.0]), 'olive': torch.tensor([0.6, 0.7, 0.4])}
        scale_filter = mode_filters[mode].view(1, 1, 1, 3).to(image.device)
        grayscale = torch.sum(image * sepia_weights, dim=-1, keepdim=True)
        tinted = grayscale * scale_filter
        result = tinted * strength + image * (1 - strength)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Filter-Nodes#cr-color-tint'
        return (result, show_help)
```