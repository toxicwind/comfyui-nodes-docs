# Documentation
- Class name: PencilSketch
- Category: postprocessing/Effects
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

PencilSketch nodes are designed to convert images into pencil sketches. It uses a range of image-processing techniques to achieve a style expression that imitates hand sketches.

# Input types
## Required
- image
    - Image parameters are essential for PencilSketch nodes because they are inputs that will be converted into pencil sketches. It influences the execution of nodes by determining the content and quality of the output sketches.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- blur_radius
    - Fuzzy radius parameters control the amount of ambiguity applied to the image before applying the sketch effect. It plays an important role in determining the smoothness of the final sketch.
    - Comfy dtype: INT
    - Python dtype: int
- sharpen_alpha
    - The sharpen_alpha parameter adjusts the intensity of the sharpness effect applied to the final image. It is important for fine-tuning the contrast and clarity of pencil sketches.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output_image
    - Output_image is the result of the application of pencil sketching to input images. It represents the final styled image in the form of pencil sketches.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class PencilSketch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'blur_radius': ('INT', {'default': 5, 'min': 1, 'max': 31, 'step': 1}), 'sharpen_alpha': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'apply_sketch'
    CATEGORY = 'postprocessing/Effects'

    def apply_sketch(self, image: torch.Tensor, blur_radius: int=5, sharpen_alpha: float=1):
        image = image.permute(0, 3, 1, 2)
        grayscale = image.mean(dim=1, keepdim=True)
        grayscale = grayscale.repeat(1, 3, 1, 1)
        inverted = 1 - grayscale
        blur_sigma = blur_radius / 3
        blurred = self.gaussian_blur(inverted, blur_radius, blur_sigma)
        final_image = self.dodge(blurred, grayscale)
        if sharpen_alpha != 0.0:
            final_image = self.sharpen(final_image, 1, sharpen_alpha)
        final_image = final_image.permute(0, 2, 3, 1)
        return (final_image,)

    def dodge(self, front: torch.Tensor, back: torch.Tensor) -> torch.Tensor:
        result = back / (1 - front + 1e-07)
        result = torch.clamp(result, 0, 1)
        return result

    def gaussian_blur(self, image: torch.Tensor, blur_radius: int, sigma: float):
        if blur_radius == 0:
            return image
        (batch_size, channels, height, width) = image.shape
        kernel_size = blur_radius * 2 + 1
        kernel = gaussian_kernel(kernel_size, sigma).repeat(channels, 1, 1).unsqueeze(1)
        blurred = F.conv2d(image, kernel, padding=kernel_size // 2, groups=channels)
        return blurred

    def sharpen(self, image: torch.Tensor, blur_radius: int, alpha: float):
        if blur_radius == 0:
            return image
        (batch_size, channels, height, width) = image.shape
        kernel_size = blur_radius * 2 + 1
        kernel = torch.ones((kernel_size, kernel_size), dtype=torch.float32) * -1
        center = kernel_size // 2
        kernel[center, center] = kernel_size ** 2
        kernel *= alpha
        kernel = kernel.repeat(channels, 1, 1).unsqueeze(1)
        sharpened = F.conv2d(image, kernel, padding=center, groups=channels)
        result = torch.clamp(sharpened, 0, 1)
        return result
```