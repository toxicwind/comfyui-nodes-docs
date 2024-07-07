# Documentation
- Class name: WLSH_SDXL_Quick_Image_Scale
- Category: WLSH Nodes/upscaling
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The `upscale' method of the WLSH_SDXL_Quick_Image_Scale node is designed to increase the resolution of the input image efficiently. It provides a wide range of sampling options to ensure that the image is scaled according to the resolution and direction required. The node also provides flexibility to edit the image to obtain a better picture, making it a multifunctional tool for image enhancement tasks.

# Input types
## Required
- original
    - The `origanal' parameter is the input image that needs to be sampled. It is the key element of the whole operation, because the whole operation revolves around the enhancement of the image. The quality and format of the original image directly influences the result of the final sampling.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- upscale_method
    - The `upscale_method' parameter determines the algorithm to be used to take up the image. It significantly affects the quality of the final image and the performance of the sampling process. Users can choose from the `nearest-exact', `bilinear' or `area' methods according to their specific needs.
    - Comfy dtype: COMBO['nearest-exact', 'bilinear', 'area']
    - Python dtype: str
- resolution
    - The `resoltion' parameter specifies the target resolution for the image being sampled. It is vital because it determines the size of the original image to be scaled. The resolution selection affects the level of detail and the final image size.
    - Comfy dtype: COMBO['1024x1024', '1152x896', '1216x832', '1344x768', '1536x640']
    - Python dtype: str
- direction
    - The 'direction' parameter defines the direction of the image as sampled above. It is important to ensure that the image is correctly displayed according to its intended use, whether horizontal or vertical.
    - Comfy dtype: COMBO['landscape', 'portrait']
    - Python dtype: str
- crop
    - The `crop' parameter allows optional cropping of the top sample image. It can be set to `disabled' so that you don't cut it or `center' so that you can cut the image from the centre. This feature improves the design of the final image.
    - Comfy dtype: COMBO['disabled', 'center']
    - Python dtype: str

# Output types
- upscaled_image
    - The `upscaled_image' output is the result of the sampling process. It represents the result of the original image being enhanced to the specified resolution and direction. The quality and appearance of the output directly reflects the ability to enter parameters and nodes.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class WLSH_SDXL_Quick_Image_Scale:
    upscale_methods = ['nearest-exact', 'bilinear', 'area']
    resolution = ['1024x1024', '1152x896', '1216x832', '1344x768', '1536x640']
    direction = ['landscape', 'portrait']
    crop_methods = ['disabled', 'center']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'original': ('IMAGE',), 'upscale_method': (s.upscale_methods,), 'resolution': (s.resolution,), 'direction': (s.direction,), 'crop': (s.crop_methods,)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'upscale'
    CATEGORY = 'WLSH Nodes/upscaling'

    def upscale(self, original, upscale_method, resolution, direction, crop):
        (width, height) = resolution.split('x')
        new_width = int(width)
        new_height = int(height)
        if direction == 'portrait':
            (new_width, new_height) = (new_height, new_width)
        old_width = original.shape[2]
        old_height = original.shape[1]
        samples = original.movedim(-1, 1)
        s = comfy.utils.common_upscale(samples, new_width, new_height, upscale_method, crop)
        s = s.movedim(1, -1)
        return (s,)
```