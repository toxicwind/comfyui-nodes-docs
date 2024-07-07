# Documentation
- Class name: ChromaticAberration
- Category: postprocessing/Effects
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

This node simulates the colour differential effect of the image, changing the perception colour by moving it horizontally or vertically.

# Input types
## Required
- image
    - The image parameter is necessary because it serves as the basis for the colour differential effect. It is the main input that determines the visual effect of the output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- red_shift
    - Red_Shift parameters adjust the level or vertical position of the red channel to contribute to the overall colour differential effect.
    - Comfy dtype: INT
    - Python dtype: int
- green_shift
    - Green_shift parameters influence the location of the green channel by increasing or modifying the colour differential effect to achieve the desired visual impact.
    - Comfy dtype: INT
    - Python dtype: int
- blue_shift
    - The blue_shift parameter controls the movement of the blue channel, which is essential for creating a convincing colour differential effect.
    - Comfy dtype: INT
    - Python dtype: int
- red_direction
    - Red_direction parameters specify the direction in which the red channel moves, horizontally or vertically, to achieve the desired colour differential effect.
    - Comfy dtype: COMBO
    - Python dtype: str
- green_direction
    - Green_direction parameters determine the direction in which the green channel moves, which is essential for accurate simulation of color differentials.
    - Comfy dtype: COMBO
    - Python dtype: str
- blue_direction
    - The blue_direction parameters specify the direction in which the blue channel moves and contribute to the overall colour differential effect.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- output
    - Output parameters represent the final image using colour differential effects, showing the visual effects of node operations.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ChromaticAberration:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'red_shift': ('INT', {'default': 0, 'min': -20, 'max': 20, 'step': 1}), 'red_direction': (['horizontal', 'vertical'],), 'green_shift': ('INT', {'default': 0, 'min': -20, 'max': 20, 'step': 1}), 'green_direction': (['horizontal', 'vertical'],), 'blue_shift': ('INT', {'default': 0, 'min': -20, 'max': 20, 'step': 1}), 'blue_direction': (['horizontal', 'vertical'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'chromatic_aberration'
    CATEGORY = 'postprocessing/Effects'

    def chromatic_aberration(self, image: torch.Tensor, red_shift: int, green_shift: int, blue_shift: int, red_direction: str, green_direction: str, blue_direction: str):

        def get_shift(direction, shift):
            shift = -shift if direction == 'vertical' else shift
            return (shift, 0) if direction == 'vertical' else (0, shift)
        x = image.permute(0, 3, 1, 2)
        shifts = [get_shift(direction, shift) for (direction, shift) in zip([red_direction, green_direction, blue_direction], [red_shift, green_shift, blue_shift])]
        channels = [torch.roll(x[:, i, :, :], shifts=shifts[i], dims=(1, 2)) for i in range(3)]
        output = torch.stack(channels, dim=1)
        output = output.permute(0, 2, 3, 1)
        return (output,)
```