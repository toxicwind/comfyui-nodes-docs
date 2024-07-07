# Documentation
- Class name: ColorTint
- Category: postprocessing/Color Adjustments
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

The ColorTint node is designed to adjust the colour tone of the image to enhance or change its visual appeal. It applies color fainting to the selected pattern, effectively changing the mood and style of the image. The node applies to post-processing tasks that require colour adjustment to match the aesthetics required or correct the colour imbalance.

# Input types
## Required
- image
    - The image parameter is the primary input of the ColorTint node. It is the source image that will be adjusted for colour. The quality and properties of the image directly influence the final output, making it a key component for achieving the desired visual effect.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- strength
    - Strength parameters control the strength of the color dizziness effect applied to the image. It is a floating number that determines the magnitude of the colour change. Higher values increase the effect, while lower values make it more subtle.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- mode
    - Model parameters determine the particular color dizziness to be applied to the image. It provides a variety of preset options, each of which creates a unique visual style. The selection of models significantly influences the overall mood and aesthetics of the image.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- result
    - The result parameter is the output of the ColorTint node. It is a coloured image that reflects input settings. This output is essential for further processing or eventual presentation and includes creative adjustments made by the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ColorTint:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 1.0, 'step': 0.1}), 'mode': (['sepia', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'purple', 'orange', 'warm', 'cool', 'lime', 'navy', 'vintage', 'rose', 'teal', 'maroon', 'peach', 'lavender', 'olive'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'color_tint'
    CATEGORY = 'postprocessing/Color Adjustments'

    def color_tint(self, image: torch.Tensor, strength: float, mode: str='sepia'):
        if strength == 0:
            return (image,)
        sepia_weights = torch.tensor([0.2989, 0.587, 0.114]).view(1, 1, 1, 3).to(image.device)
        mode_filters = {'sepia': torch.tensor([1.0, 0.8, 0.6]), 'red': torch.tensor([1.0, 0.6, 0.6]), 'green': torch.tensor([0.6, 1.0, 0.6]), 'blue': torch.tensor([0.6, 0.8, 1.0]), 'cyan': torch.tensor([0.6, 1.0, 1.0]), 'magenta': torch.tensor([1.0, 0.6, 1.0]), 'yellow': torch.tensor([1.0, 1.0, 0.6]), 'purple': torch.tensor([0.8, 0.6, 1.0]), 'orange': torch.tensor([1.0, 0.7, 0.3]), 'warm': torch.tensor([1.0, 0.9, 0.7]), 'cool': torch.tensor([0.7, 0.9, 1.0]), 'lime': torch.tensor([0.7, 1.0, 0.3]), 'navy': torch.tensor([0.3, 0.4, 0.7]), 'vintage': torch.tensor([0.9, 0.85, 0.7]), 'rose': torch.tensor([1.0, 0.8, 0.9]), 'teal': torch.tensor([0.3, 0.8, 0.8]), 'maroon': torch.tensor([0.7, 0.3, 0.5]), 'peach': torch.tensor([1.0, 0.8, 0.6]), 'lavender': torch.tensor([0.8, 0.6, 1.0]), 'olive': torch.tensor([0.6, 0.7, 0.4])}
        scale_filter = mode_filters[mode].view(1, 1, 1, 3).to(image.device)
        grayscale = torch.sum(image * sepia_weights, dim=-1, keepdim=True)
        tinted = grayscale * scale_filter
        result = tinted * strength + image * (1 - strength)
        return (result,)
```