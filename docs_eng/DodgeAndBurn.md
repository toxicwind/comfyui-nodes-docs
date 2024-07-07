# Documentation
- Class name: DodgeAndBurn
- Category: postprocessing/Blends
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

DodgeAndBurn nodes are designed to enhance images by applying dodge and burn techniques that can manipulate the brightness and contrast of a given area in the image. By using masks and adjusting strength, this node can selectively brighten or darken an area, create depth and attract attention to a particular area.

# Input types
## Required
- image
    - The image parameter is the main input of the DodgeAnd Burn node, which will be the base layer modified by dodging and burning technology. Its quality and content directly influence the final output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - The mask parameters determine which areas of the image will be affected by the dodge and burn processes. It plays a vital role in controlling the accuracy of the adjustments made to the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- intensity
    - Strength is a key parameter that controls the level of brightening or darkening applied to the image. Adjusting this value affects the overall impact of dodge and burn technology.
    - Comfy dtype: FLOAT
    - Python dtype: float
- mode
    - Model parameters determine the specific dodge and burn technologies to be applied. It affects the way the image is adjusted and meets different creative or style preferences.
    - Comfy dtype: COMBO[ ['dodge', 'burn', 'dodge_and_burn', 'burn_and_dodge', 'color_dodge', 'color_burn', 'linear_dodge', 'linear_burn'],]
    - Python dtype: str

# Output types
- output_image
    - The output image represents the final result of the dodge and burn processes and reflects the adjustments made to the original image based on input parameters.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class DodgeAndBurn:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'mask': ('IMAGE',), 'intensity': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'mode': (['dodge', 'burn', 'dodge_and_burn', 'burn_and_dodge', 'color_dodge', 'color_burn', 'linear_dodge', 'linear_burn'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'dodge_and_burn'
    CATEGORY = 'postprocessing/Blends'

    def dodge_and_burn(self, image: torch.Tensor, mask: torch.Tensor, intensity: float, mode: str):
        if mode in ['dodge', 'color_dodge', 'linear_dodge']:
            dodged_image = self.dodge(image, mask, intensity, mode)
            return (dodged_image,)
        elif mode in ['burn', 'color_burn', 'linear_burn']:
            burned_image = self.burn(image, mask, intensity, mode)
            return (burned_image,)
        elif mode == 'dodge_and_burn':
            dodged_image = self.dodge(image, mask, intensity, 'dodge')
            burned_image = self.burn(dodged_image, mask, intensity, 'burn')
            return (burned_image,)
        elif mode == 'burn_and_dodge':
            burned_image = self.burn(image, mask, intensity, 'burn')
            dodged_image = self.dodge(burned_image, mask, intensity, 'dodge')
            return (dodged_image,)
        else:
            raise ValueError(f'Unsupported dodge and burn mode: {mode}')

    def dodge(self, img, mask, intensity, mode):
        if mode == 'dodge':
            return img / (1 - mask * intensity + 1e-07)
        elif mode == 'color_dodge':
            return torch.where(mask < 1, img / (1 - mask * intensity), img)
        elif mode == 'linear_dodge':
            return torch.clamp(img + mask * intensity, 0, 1)
        else:
            raise ValueError(f'Unsupported dodge mode: {mode}')

    def burn(self, img, mask, intensity, mode):
        if mode == 'burn':
            return 1 - (1 - img) / (mask * intensity + 1e-07)
        elif mode == 'color_burn':
            return torch.where(mask > 0, 1 - (1 - img) / (mask * intensity), img)
        elif mode == 'linear_burn':
            return torch.clamp(img - mask * intensity, 0, 1)
        else:
            raise ValueError(f'Unsupported burn mode: {mode}')
```