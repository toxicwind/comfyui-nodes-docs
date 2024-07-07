# Documentation
- Class name: Blur
- Category: image/postprocessing
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

Fuzzy nodes are designed to apply Gaussian blurry to images, increase their smoothness and reduce noise. This is achieved by volumeing images with Gaussian cores based on the vague radius and consideration values provided. This node is particularly applicable to reprocessing tasks when image clarity is not critical or needs softness.

# Input types
## Required
- image
    - An image parameter is the input image that blurs the node that will be processed. It is the basis for node operations, because the entire conversion is organized around this input. The quality and resolution of the image directly influences the appearance of the output after application of the fuzzy effect.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- blur_radius
    - Fuzzy radius parameters determine the degree of fuzzy effect that should be applied to the image. Larger values lead to greater ambiguity, while smaller values produce more subtle effects. It plays a key role in controlling the visual results of node operations.
    - Comfy dtype: INT
    - Python dtype: int
- sigma
    - It controls the sharpness of the transition between blurred and non-inflammated areas in the image. Higher values lead to greater ambiguity, while lower values produce more localized effects.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- blurred_image
    - Fuzzy image output is the result of the use of Gaussian fuzzy to input images. It represents the main result of the blurring nodes and is essential for subsequent image processing steps or visualization.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class Blur:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'blur_radius': ('INT', {'default': 1, 'min': 1, 'max': 31, 'step': 1}), 'sigma': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 10.0, 'step': 0.1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'blur'
    CATEGORY = 'image/postprocessing'

    def blur(self, image: torch.Tensor, blur_radius: int, sigma: float):
        if blur_radius == 0:
            return (image,)
        (batch_size, height, width, channels) = image.shape
        kernel_size = blur_radius * 2 + 1
        kernel = gaussian_kernel(kernel_size, sigma, device=image.device).repeat(channels, 1, 1).unsqueeze(1)
        image = image.permute(0, 3, 1, 2)
        padded_image = F.pad(image, (blur_radius, blur_radius, blur_radius, blur_radius), 'reflect')
        blurred = F.conv2d(padded_image, kernel, padding=kernel_size // 2, groups=channels)[:, :, blur_radius:-blur_radius, blur_radius:-blur_radius]
        blurred = blurred.permute(0, 2, 3, 1)
        return (blurred,)
```