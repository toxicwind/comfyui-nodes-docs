# Documentation
- Class name: WAS_Image_Make_Seamless
- Category: WAS Suite/Image/Process
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The make_seamless method is designed to process a set of images and convert them into seamless textures. It is achieved by applying hybrid techniques to the edges of images, which can be levelled without displaying visible seams. This function is particularly suitable for creating textures that can be used in various graphic applications, such as game development, synthesis and 3D modelling.

# Input types
## Required
- images
    - Enter images that need to be processed into seamless textures. These images are original materials that are to be processed at nodes to create seamless output.
    - Comfy dtype: IMAGE
    - Python dtype: List[PIL.Image.Image]
- blending
    - The mix factor determines the degree of mixing to be applied on the edge of the image. The higher the value, the smoother the transition, but also the smaller the image size.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- tiled
    - Tiled parameters indicate whether the output should be a single seamless image or a 2x2 sheeting version in order to better visualize the seamless effects.
    - Comfy dtype: COMBO[true, false]
    - Python dtype: bool
- tiles
    - The number of floors on each direction (hierarchical and vertical) in the flattening output. Use when the Tiled parameter is set to true.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- images
    - Processed seamless texture images. These images can be levelled without displaying visible seams, making them suitable for use in various graphic applications.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Make_Seamless:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'blending': ('FLOAT', {'default': 0.4, 'max': 1.0, 'min': 0.0, 'step': 0.01}), 'tiled': (['true', 'false'],), 'tiles': ('INT', {'default': 2, 'max': 6, 'min': 2, 'step': 2})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('images',)
    FUNCTION = 'make_seamless'
    CATEGORY = 'WAS Suite/Image/Process'

    def make_seamless(self, images, blending, tiled, tiles):
        WTools = WAS_Tools_Class()
        seamless_images = []
        for image in images:
            seamless_images.append(pil2tensor(WTools.make_seamless(tensor2pil(image), blending, tiled, tiles)))
        seamless_images = torch.cat(seamless_images, dim=0)
        return (seamless_images,)
```