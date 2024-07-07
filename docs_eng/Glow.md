# Documentation
- Class name: Glow
- Category: postprocessing/Effects
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

The node uses light for images to enhance their visual appeal by adding vague image versions of adjustable strength. It aims to improve the beauty of images at the reprocessing stage, providing a thematic light that attracts attention to certain features or creates a fantastic atmosphere.

# Input types
## Required
- image
    - The image parameter is essential because it is the basic input for the application of the luminous effect. It determines the content and structure of the final output, and the luminous effect is directly influenced by image characteristics and quality.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- intensity
    - The strength parameter controls the visibility of the luminous effect, and the higher the value, the more the luminous it is. It is critical in adjusting the visual impact of the effect, allowing for fine-tuning the intensity of the luminous to achieve the aesthetic effect required.
    - Comfy dtype: FLOAT
    - Python dtype: float
- blur_radius
    - Fuzzy radius parameters specify the degree of fuzzy application of the light to the image. It affects the diffusion and smoothness of the light, and a larger radius leads to a more dispersed and extensive brightness.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- glowing_image
    - The resulting luminous image is the main output of the node, representing the original image that enhances the luminous effect. It contains a comprehensive visual modification of the input parameters and provides a visually attractive representation of the input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class Glow:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'intensity': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 5.0, 'step': 0.01}), 'blur_radius': ('INT', {'default': 5, 'min': 1, 'max': 50, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'apply_glow'
    CATEGORY = 'postprocessing/Effects'

    def apply_glow(self, image: torch.Tensor, intensity: float, blur_radius: int):
        blurred_image = self.gaussian_blur(image, 2 * blur_radius + 1)
        glowing_image = self.add_glow(image, blurred_image, intensity)
        glowing_image = torch.clamp(glowing_image, 0, 1)
        return (glowing_image,)

    def gaussian_blur(self, image: torch.Tensor, kernel_size: int):
        (batch_size, height, width, channels) = image.shape
        sigma = (kernel_size - 1) / 6
        kernel = gaussian_kernel(kernel_size, sigma).repeat(channels, 1, 1).unsqueeze(1)
        image = image.permute(0, 3, 1, 2)
        blurred = F.conv2d(image, kernel, padding=kernel_size // 2, groups=channels)
        blurred = blurred.permute(0, 2, 3, 1)
        return blurred

    def add_glow(self, img, blurred_img, intensity):
        return img + blurred_img * intensity
```