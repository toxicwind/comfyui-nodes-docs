# Documentation
- Class name: EnhanceImage
- Category: ♾️Mixlab/Image
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node aims to improve the visual quality of the image by adjusting the contrast level of the image, thereby increasing the clarity and depth of the visual content without changing the basic features of the input image.

# Input types
## Required
- image
    - Image input is essential because it provides the basic visual data that nodes will process. It affects the entire operation by determining the starting point of the enhanced contrast.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or list[PIL.Image]
- contrast
    - The contrast parameter plays an important role in the enhancement process, as it directly affects the dynamic range and visual impact of the output image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- image
    - The output image represents an enhanced version of the input, with better contrast and depth, and provides a richer visual experience.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or list[PIL.Image]

# Usage tips
- Infra type: CPU

# Source code
```
class EnhanceImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'contrast': ('FLOAT', {'default': 0.5, 'min': 0, 'max': 10, 'step': 0.01, 'display': 'slider'})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Image'
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True,)

    def run(self, image, contrast):
        contrast = contrast[0]
        res = []
        for ims in image:
            for im in ims:
                image = tensor2pil(im)
                image = enhance_depth_map(image, contrast)
                image = pil2tensor(image)
                res.append(image)
        return (res,)
```