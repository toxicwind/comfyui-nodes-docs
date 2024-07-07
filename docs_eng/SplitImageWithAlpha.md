# Documentation
- Class name: SplitImageWithAlpha
- Category: mask/compositing
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

SplitImageWith Alpha node is designed to separate the colour information of the image from the alpha channel. It performs a basic function in image processing by dividing the input image into two parts: colour images and alpha masks. This node is essential for tasks that require transparency, such as synthesizing images or creating a mask for visual effects.

# Input types
## Required
- image
    - The 'image'parameter is the input load that contains image data. It is vital because it is the main source of information for node processing. Node relies on this input to extract colours and alpha components, which are then used in subsequent image operations.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Output types
- color_image
    - The 'color_image' output contains colour information extracted from the input image. It is important because it represents visual content that has no transparency layer and can be used directly for displaying or further processing.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- alpha_mask
    - The `alpha_mask' output is the alpha channel for the input image, which represents the transparency information. It is inverted compared to the original alpha to be used in common synthetic operations, with higher values indicating greater lack of transparency.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class SplitImageWithAlpha:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}
    CATEGORY = 'mask/compositing'
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'split_image_with_alpha'

    def split_image_with_alpha(self, image: torch.Tensor):
        out_images = [i[:, :, :3] for i in image]
        out_alphas = [i[:, :, 3] if i.shape[2] > 3 else torch.ones_like(i[:, :, 0]) for i in image]
        result = (torch.stack(out_images), 1.0 - torch.stack(out_alphas))
        return result
```