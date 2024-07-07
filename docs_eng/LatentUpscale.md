# Documentation
- Class name: LatentUpscale
- Category: latent
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The LatentUpscale node is designed to improve the quality and detail of the image creation by increasing the resolution of the input of the potential sample by different magnifying methods. It plays a key role in the image generation process by providing high-resolution outputs that can be further processed or used for downstream tasks.

# Input types
## Required
- samples
    - The “samples” parameter is essential because it provides a potential indication that nodes will be magnified. It directly affects the quality and resolution of the final output and determines the starting point of the magnification process.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- upscale_method
    - The "upscale_method " parameter determines the algorithm to be used to magnify potential samples. It significantly affects the efficiency and visual effects of the magnification process, providing varying degrees of detail and smoothness for the images generated.
    - Comfy dtype: COMBO
    - Python dtype: str
- width
    - The " width " parameter specifies the desired width of the enlarged output. It plays a key role in determining the long-width ratio and dimensions of the final image, thus affecting the aesthetic and architectural landscape as a whole.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The height parameter sets the target height of the magnified image. It works with the width parameter to establish the size of the image, which is essential for achieving the desired visual scale and scale.
    - Comfy dtype: INT
    - Python dtype: int
- crop
    - The 'crop'parameter determines how the node deals with magnifying the image in the centre. It affects the location and configuration of the output and ensures that the image is correctly aligned and focused.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- samples
    - The “samples” output, which contains potential expressions of magnification, now has a higher resolution and detail. This output is important because it serves as the basis for follow-up image processing or analysis steps.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class LatentUpscale:
    upscale_methods = ['nearest-exact', 'bilinear', 'area', 'bicubic', 'bislerp']
    crop_methods = ['disabled', 'center']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'upscale_method': (s.upscale_methods,), 'width': ('INT', {'default': 512, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'height': ('INT', {'default': 512, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'crop': (s.crop_methods,)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'upscale'
    CATEGORY = 'latent'

    def upscale(self, samples, upscale_method, width, height, crop):
        if width == 0 and height == 0:
            s = samples
        else:
            s = samples.copy()
            if width == 0:
                height = max(64, height)
                width = max(64, round(samples['samples'].shape[3] * height / samples['samples'].shape[2]))
            elif height == 0:
                width = max(64, width)
                height = max(64, round(samples['samples'].shape[2] * width / samples['samples'].shape[3]))
            else:
                width = max(64, width)
                height = max(64, height)
            s['samples'] = comfy.utils.common_upscale(samples['samples'], width // 8, height // 8, upscale_method, crop)
        return (s,)
```