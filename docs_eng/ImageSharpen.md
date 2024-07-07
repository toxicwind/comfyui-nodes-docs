# Documentation
- Class name: Sharpen
- Category: image/postprocessing
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The Sharpen node is designed to enhance the details of the image by applying a sharp filter. It uses the Gaussian core to generate a sharp mask to highlight the edges and details of the image. In image clarity and defining essential reprocessing tasks, the function of the node is essential.

# Input types
## Required
- image
    - Enter the image as the primary data for the Sharpen node. It is the basis for the application of acute effects, the quality of which directly affects the final output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- sharpen_radius
    - The sharpen_radius parameter determines the range of sharp effects. A larger radius leads to a more obvious sharpness, while a smaller radius provides a more subtle increase.
    - Comfy dtype: INT
    - Python dtype: int
- sigma
    - The sigma parameter controls the standard deviations used to sharpen the Gaussian core. It affects the smoothness of the sharp transition and the spread of nuclear effects.
    - Comfy dtype: FLOAT
    - Python dtype: float
- alpha
    - The alpha parameter adjusts the intensity of the acute effect. The higher the alpha value, the stronger the acute effect, and the lower the value, the milder the effect.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- sharpened_image
    - The sharpened_image output is the result of the application of the sharpening process to the input image. It shows the enhanced detail and edges and provides clearer and clearer visual performance.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class Sharpen:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'sharpen_radius': ('INT', {'default': 1, 'min': 1, 'max': 31, 'step': 1}), 'sigma': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 10.0, 'step': 0.01}), 'alpha': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 5.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'sharpen'
    CATEGORY = 'image/postprocessing'

    def sharpen(self, image: torch.Tensor, sharpen_radius: int, sigma: float, alpha: float):
        if sharpen_radius == 0:
            return (image,)
        (batch_size, height, width, channels) = image.shape
        kernel_size = sharpen_radius * 2 + 1
        kernel = gaussian_kernel(kernel_size, sigma, device=image.device) * -(alpha * 10)
        center = kernel_size // 2
        kernel[center, center] = kernel[center, center] - kernel.sum() + 1.0
        kernel = kernel.repeat(channels, 1, 1).unsqueeze(1)
        tensor_image = image.permute(0, 3, 1, 2)
        tensor_image = F.pad(tensor_image, (sharpen_radius, sharpen_radius, sharpen_radius, sharpen_radius), 'reflect')
        sharpened = F.conv2d(tensor_image, kernel, padding=center, groups=channels)[:, :, sharpen_radius:-sharpen_radius, sharpen_radius:-sharpen_radius]
        sharpened = sharpened.permute(0, 2, 3, 1)
        result = torch.clamp(sharpened, 0, 1)
        return (result,)
```