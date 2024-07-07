# Documentation
- Class name: ArithmeticBlend
- Category: postprocessing/Blends
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

The node synthesizes two images by arithmetic operation, creating visual effects by selecting a hybrid mode (blend_mode) to integrate Image1 and Image2.

# Input types
## Required
- image1
    - The first image to be commingled is critical to the occurrence of arithmetic operations and influences the final output results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image2
    - The second image involved in the hybrid process, which interacts with Image1, determines the characteristics of the composite image generated.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- blend_mode
    - The arithmetic mode of operation determines how the combination of image1 and image2 will significantly influence the final visual result.
    - Comfy dtype: COMBO['add', 'subtract', 'difference']
    - Python dtype: str

# Output types
- blended_image
    - Arithmetic mixing processes generate images that contain the visual effects of the chosen mix mode.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ArithmeticBlend:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image1': ('IMAGE',), 'image2': ('IMAGE',), 'blend_mode': (['add', 'subtract', 'difference'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'arithmetic_blend_images'
    CATEGORY = 'postprocessing/Blends'

    def arithmetic_blend_images(self, image1: torch.Tensor, image2: torch.Tensor, blend_mode: str):
        if blend_mode == 'add':
            blended_image = self.add(image1, image2)
        elif blend_mode == 'subtract':
            blended_image = self.subtract(image1, image2)
        elif blend_mode == 'difference':
            blended_image = self.difference(image1, image2)
        else:
            raise ValueError(f'Unsupported arithmetic blend mode: {blend_mode}')
        blended_image = torch.clamp(blended_image, 0, 1)
        return (blended_image,)

    def add(self, img1, img2):
        return img1 + img2

    def subtract(self, img1, img2):
        return img1 - img2

    def difference(self, img1, img2):
        return torch.abs(img1 - img2)
```