# Documentation
- Class name: AsciiArt
- Category: postprocessing/Effects
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

AsciiArt node applies the ASCII artistic effect to the input image and converts it into a styled expression using a predefined character set. It uses pixel strength to select the appropriate character, thus creating a text expression for the image content.

# Input types
## Required
- image
    - The input image that you want to use for the ASCII artistic effect. It should be the length of the image data.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- char_size
    - ASCII art indicates the character size to be used. This parameter determines the particle size of the ASCII artistic effect.
    - Comfy dtype: int
    - Python dtype: int
- font_size
    - Font size for ASCII artistic characters. This affects the look of the final ASCII artistic image.
    - Comfy dtype: int
    - Python dtype: int

# Output types
- result
    - Applying the ASCII artistic effect to the result image. This is the volume of the ASCII artistic version that you type.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class AsciiArt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'char_size': ('INT', {'default': 12, 'min': 0, 'max': 64, 'step': 2}), 'font_size': ('INT', {'default': 12, 'min': 0, 'max': 64, 'step': 2})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'apply_ascii_art_effect'
    CATEGORY = 'postprocessing/Effects'

    def apply_ascii_art_effect(self, image: torch.Tensor, char_size: int, font_size: int):
        (batch_size, height, width, channels) = image.shape
        result = torch.zeros_like(image)
        for b in range(batch_size):
            img_b = image[b] * 255.0
            img_b = Image.fromarray(img_b.numpy().astype('uint8'), 'RGB')
            result_b = ascii_art_effect(img_b, char_size, font_size)
            result_b = torch.tensor(np.array(result_b)) / 255.0
            result[b] = result_b
        return (result,)
```