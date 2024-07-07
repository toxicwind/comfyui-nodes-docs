# Documentation
- Class name: Sharpen
- Category: postprocessing/Filters
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

Sharpening nodes improves image clarity by increasing local contrasts. It applies sharp cores to input images, magnifying edges and fine details, thus producing clearer and clearer visual effects.

# Input types
## Required
- image
    - The image parameter is the main input of the acute node, which is essential for the node. It determines the source material that will be subject to acute treatment, affecting the quality and clarity of the final output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- sharpen_radius
    - A sharper radius parameters control the degree of acute effect. A larger radius leads to a more obvious sharpness, a more active increase in margins and detail, and a smaller radius produces a more subtle effect.
    - Comfy dtype: INT
    - Python dtype: int
- alpha
    - The alpha parameter adjusts the intensity of the sharpening effect. The higher alpha value increases the contrast, leading to a more dramatic sharpening, while the lower value produces a lesser effect.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- result
    - The result parameter is the output of the sharpened node, which represents the image of the sharpened. It reflects the application of the sharpened effect, showing greater clarity and a well-defined edge.
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
        return {'required': {'image': ('IMAGE',), 'sharpen_radius': ('INT', {'default': 1, 'min': 1, 'max': 15, 'step': 1}), 'alpha': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 5.0, 'step': 0.1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'sharpen'
    CATEGORY = 'postprocessing/Filters'

    def sharpen(self, image: torch.Tensor, blur_radius: int, alpha: float):
        if blur_radius == 0:
            return (image,)
        (batch_size, height, width, channels) = image.shape
        kernel_size = blur_radius * 2 + 1
        kernel = torch.ones((kernel_size, kernel_size), dtype=torch.float32) * -1
        center = kernel_size // 2
        kernel[center, center] = kernel_size ** 2
        kernel *= alpha
        kernel = kernel.repeat(channels, 1, 1).unsqueeze(1)
        tensor_image = image.permute(0, 3, 1, 2)
        sharpened = F.conv2d(tensor_image, kernel, padding=center, groups=channels)
        sharpened = sharpened.permute(0, 2, 3, 1)
        result = torch.clamp(sharpened, 0, 1)
        return (result,)
```