# Documentation
- Class name: BlurNode
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The BlurNode class is designed to apply Gaussian fuzzy effects to images and to simulate the flexic effects commonly used in photography and image processing. It uses the Gaussian concept to smooth images, reduce the visibility of details and create more beautiful visual effects.

# Input types
## Required
- image
    - The image parameter is the input image that the node will process. It is vital because it is the primary data for the node operation to achieve the fuzzy effect. The quality and content of the image significantly influences the execution and final outcome of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- radius
    - The radius parameter defines the scope of the fuzzy effect. It is vital because it directly affects the size of the lost Gaussian core, thus affecting the degree of ambiguity applied to the image.
    - Comfy dtype: INT
    - Python dtype: int
- sigma_factor
    - The sigma_factor parameter adjusts the standard deviation of the Gaussian core to allow control of fuzzy smoothness. It plays an important role in fine-tuning the fuzzy effect to meet specific visual requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- blurred_image
    - The blurred_image output parameter represents the application of a processed image with the Gaussian fuzzy effect. It is the result of a node operation and reflects a modified visual appearance of the blurred input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class BlurNode:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'radius': ('INT', {'default': 10, 'min': 0, 'max': 48, 'step': 1}), 'sigma_factor': ('FLOAT', {'default': 1.0, 'min': 0.01, 'max': 3.0, 'step': 0.01})}}

    def gaussian_blur(self, image, kernel_size, sigma):
        kernel = torch.Tensor(kernel_size, kernel_size).to(device=image.device)
        center = kernel_size // 2
        variance = sigma ** 2
        for i in range(kernel_size):
            for j in range(kernel_size):
                x = i - center
                y = j - center
                kernel[i, j] = math.exp(-(x ** 2 + y ** 2) / (2 * variance))
        kernel /= kernel.sum()
        padding = (kernel_size - 1) // 2
        input_pad = torch.nn.functional.pad(image, (padding, padding, padding, padding), mode='reflect')
        (batch_size, num_channels, height, width) = image.shape
        input_reshaped = input_pad.reshape(batch_size * num_channels, 1, height + padding * 2, width + padding * 2)
        output_reshaped = torch.nn.functional.conv2d(input_reshaped, kernel.unsqueeze(0).unsqueeze(0))
        output_tensor = output_reshaped.reshape(batch_size, num_channels, height, width)
        return output_tensor
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'blur'
    CATEGORY = 'Masquerade Nodes'

    def blur(self, image, radius, sigma_factor):
        if len(image.size()) == 3:
            image = image.unsqueeze(3)
        image = image.permute(0, 3, 1, 2)
        kernel_size = radius * 2 + 1
        sigma = sigma_factor * (0.6 * radius - 0.3)
        result = self.gaussian_blur(image, kernel_size, sigma).permute(0, 2, 3, 1)
        if result.size()[3] == 1:
            result = result[:, :, :, 0]
        return (result,)
```