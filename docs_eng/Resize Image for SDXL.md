# Documentation
- Class name: ResizeImageSDXL
- Category: Mikey/Image
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The ResizeImageSDXL node is designed to adjust and magnify the image size using a variety of methods. It provides the function of adjusting the image size while maintaining its width ratio and applying different magnification techniques to improve quality.

# Input types
## Required
- image
    - The image parameter is essential for the operation of the node, because it is the input that will be adjusted to size and magnified. It directly affects the execution process and the quality and dimensions of the final output image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- upscale_method
    - The upperscale_method parameter determines the algorithm to be used to magnify the image. It is essential for adjusting the image mass and allows the use of different plug-in techniques.
    - Comfy dtype: COMBO['nearest-exact', 'bilinear', 'area', 'bicubic']
    - Python dtype: str
- crop
    - The crop parameter specifies whether and how the image is cropped after the size has been adjusted. It is important to control the final size and width ratio of the output image.
    - Comfy dtype: COMBO['disabled', 'center']
    - Python dtype: str

# Output types
- resized_image
    - Resized_image output represents the adjusted size and magnified processing image. It is the main result of node operations and reflects the impact of the selected method on image size and quality.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ResizeImageSDXL:
    crop_methods = ['disabled', 'center']
    upscale_methods = ['nearest-exact', 'bilinear', 'area', 'bicubic']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'upscale_method': (s.upscale_methods,), 'crop': (s.crop_methods,)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'resize'
    CATEGORY = 'Mikey/Image'

    def upscale(self, image, upscale_method, width, height, crop):
        samples = image.movedim(-1, 1)
        s = comfy.utils.common_upscale(samples, width, height, upscale_method, crop)
        s = s.movedim(1, -1)
        return (s,)

    def resize(self, image, upscale_method, crop):
        (w, h) = find_latent_size(image.shape[2], image.shape[1])
        img = self.upscale(image, upscale_method, w, h, crop)[0]
        return (img,)
```