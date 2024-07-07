# Documentation
- Class name: Blur
- Category: postprocessing/Filters
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

Fuzzy nodes apply Gaussian fuzzy to images, effectively reducing noise and smoothing edges, which are useful in image analysis and enhanced reprocessing steps.

# Input types
## Required
- image
    - The image parameter is necessary because it is the main input for fuzzy operations. It determines the source data that will be processed by nodes.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- blur_radius
    - Fuzzy radius determines the degree of fuzzy effect. A larger radius can lead to more obvious ambiguity, which may be important for the overall visual effect.
    - Comfy dtype: INT
    - Python dtype: int
- sigma
    - The sigma parameter affects the poor standards of the Gaussian core and directly affects the fuzzy smoothness. This is a key factor in achieving the aesthetic effect required.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- blurred_image
    - The output is a fuzzy image, which is the result of the processing of the image entered after the Gaussian fuzzy application.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class Blur:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'blur_radius': ('INT', {'default': 1, 'min': 1, 'max': 15, 'step': 1}), 'sigma': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 10.0, 'step': 0.1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'blur'
    CATEGORY = 'postprocessing/Filters'

    def blur(self, image: torch.Tensor, blur_radius: int, sigma: float):
        if blur_radius == 0:
            return (image,)
        (batch_size, height, width, channels) = image.shape
        kernel_size = blur_radius * 2 + 1
        kernel = gaussian_kernel(kernel_size, sigma).repeat(channels, 1, 1).unsqueeze(1)
        image = image.permute(0, 3, 1, 2)
        blurred = F.conv2d(image, kernel, padding=kernel_size // 2, groups=channels)
        blurred = blurred.permute(0, 2, 3, 1)
        return (blurred,)
```