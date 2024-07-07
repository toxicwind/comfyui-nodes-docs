# Documentation
- Class name: ResizeFactor
- Category: image/postprocessing
- Output node: False
- Repo Ref: https://github.com/Jordach/comfy-plasma.git

ResizeFactor node is designed to resize the image, magnify or narrow it by the specified factor. This process is essential to adapt the image to different display requirements or to input specifications for subsequent image processing tasks.

# Input types
## Required
- IMAGE
    - The IMAGE parameter is necessary because it provides a source image that will resize the node. It directly influences the output and determines the initial resolution and format of the image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- factor
    - The factor parameter is essential to define the zoom ratio of the image. It determines how much the image will be magnified or reduced, thereby changing the ultimate size.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- resampler
    - Resampler parameters are important for selecting the plug-in method to be used in the resizeing process. They affect the image quality and appearance of the resizeed image.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- IMAGE
    - The output IMAGE is the result of a process of resizing, reflecting new dimensions and potential qualitative changes based on the chosen re-sampling method.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class ResizeFactor:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'IMAGE': ('IMAGE',), 'factor': ('FLOAT', {'default': 2, 'min': 0.01, 'max': 10, 'step': 0.01}), 'resampler': (['nearest', 'box', 'bilinear', 'bicubic', 'hamming', 'lanczos'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'process_image'
    CATEGORY = 'image/postprocessing'

    def process_image(self, IMAGE, factor, resampler):
        cimg = conv_tensor_pil(IMAGE)
        (w, h) = (int(cimg.width * factor), int(cimg.height * factor))
        sampler = get_pil_resampler(resampler)
        return conv_pil_tensor(cimg.resize((w, h), resample=sampler))
```