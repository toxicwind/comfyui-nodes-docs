# Documentation
- Class name: LatentCrop
- Category: latent/transform
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

LatentCrop nodes are designed to operate and extract specific areas from larger potential spatial expressions. It plays a key role in focusing data on relevant areas for further processing or analysis, thereby increasing the efficiency and accuracy of follow-up operations.

# Input types
## Required
- samples
    - The "samples" parameter is the core input of the LatentCrop node, representing the potential spatial data to be cut. It is essential for the operation of the node because it determines the source material of the crop process.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- width
    - The “width” parameter specifies the width required to crop the area in potential space. It is the key determinant of output size and directly affects the range of data extracted.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The “right” parameter defines the height required to crop the area in potential space. Together with the “width”, it forms the size of the final output, concentrating the function of the node on a particular part of the data.
    - Comfy dtype: INT
    - Python dtype: int
- x
    - The " x " parameter sets the horizontal starting point of the potential space tailoring operation. It is critical in defining the exact location where the data extraction begins.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - The " y " parameter determines the vertical starting point of the potential space crop operation. It works with the " x " parameter to determine precisely the starting coordinates of the crop.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- cropped_samples
    - The "cropped_samples" output contains the results of potential space data after cropping. It represents the fine-tuning part of the original data and is adjusted according to the size and location parameters specified.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class LatentCrop:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'width': ('INT', {'default': 512, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'height': ('INT', {'default': 512, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'x': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'y': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'crop'
    CATEGORY = 'latent/transform'

    def crop(self, samples, width, height, x, y):
        s = samples.copy()
        samples = samples['samples']
        x = x // 8
        y = y // 8
        if x > samples.shape[3] - 8:
            x = samples.shape[3] - 8
        if y > samples.shape[2] - 8:
            y = samples.shape[2] - 8
        new_height = height // 8
        new_width = width // 8
        to_x = new_width + x
        to_y = new_height + y
        s['samples'] = samples[:, :, y:to_y, x:to_x]
        return (s,)
```