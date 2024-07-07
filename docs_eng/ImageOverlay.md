# Documentation
- Class name: ImageOverlay
- Category: Mikey/Image
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The Imageoverlay node class integrates the foreground image seamlessly into the background image according to the specified opacity level, creating a composite image combining the visual elements of the two sources.

# Input types
## Required
- background_image
    - Background images are used as base canvass for the application of stacks. They are essential for creating the context and dimensions of the final synthetic images.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- foreground_image
    - The foreground image is designed to add elements to the background. Its visual features and location are essential for achieving the desired effect in a synthetic image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- opacity
    - A lack of transparency determines the extent to which future and background images are integrated. This is a key parameter that affects the overall appearance and transparency of synthetic images.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- result_img
    - Reult_img represents the final synthetic image, in which the foreground image has been superimposed on the background image based on the specified opacity.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageOverlay:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'background_image': ('IMAGE', {'default': None}), 'foreground_image': ('IMAGE', {'default': None}), 'opacity': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('result_img',)
    FUNCTION = 'overlay'
    CATEGORY = 'Mikey/Image'

    def overlay(self, background_image, foreground_image, opacity):
        background_image = tensor2pil(background_image)
        foreground_image = tensor2pil(foreground_image)
        background_image = background_image.convert('RGB')
        foreground_image = foreground_image.convert('RGB')
        cropped_fg = Image.new('RGB', (background_image.size[0], background_image.size[1]))
        cropped_fg.paste(foreground_image, (int((background_image.size[0] - foreground_image.size[0]) / 2), int((background_image.size[1] - foreground_image.size[1]) / 2)))
        bg_array = np.array(background_image, dtype=np.float32) / 255
        fg_array = np.array(cropped_fg, dtype=np.float32) / 255
        mask = bg_array < 0.5
        overlay = np.zeros_like(bg_array)
        overlay[mask] = 2 * bg_array[mask] * fg_array[mask]
        overlay[~mask] = 1 - 2 * (1 - bg_array[~mask]) * (1 - fg_array[~mask])
        result = (1 - opacity) * bg_array + opacity * overlay
        result_img = Image.fromarray((result * 255).astype(np.uint8))
        result_img = pil2tensor(result_img)
        return (result_img,)
```