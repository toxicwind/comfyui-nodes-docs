# Documentation
- Class name: WAS_Image_Stitch
- Category: WAS Suite/Image/Transform
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Stitch node is designed to group two images seamlessly according to a given stitching direction. It uses a feather effect to create a smooth transition between images, which is particularly useful for creating landscape images or textures. The node can handle different suture modes, such as 'top', 'left', 'bottom' and 'right', allowing flexible image combinations.

# Input types
## Required
- image_a
    - The first image to be sewn. It serves as the base layer for suture operations and determines the initial part of the final sewn image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- image_b
    - The second image that you want to sew. It aligns it with the first image according to the specified suture mode and mixes it to create a seamless combination.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- stitch
    - The two images should be sewn together. They can be 'top','left', 'bottom' or 'right', defining the direction of the stitches and the way the images are combined.
    - Comfy dtype: COMBO[top, left, bottom, right]
    - Python dtype: str
- feathering
    - The amount of plume applied at the sewn boundary. Higher values create a softer and more gradual transition between images, but also reduce the size of the output images.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- stitched_image
    - The result image after the suture process. It combines the two input images into a single, seamless image according to the specified suture mode and plume.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Stitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image_a': ('IMAGE',), 'image_b': ('IMAGE',), 'stitch': (['top', 'left', 'bottom', 'right'],), 'feathering': ('INT', {'default': 50, 'min': 0, 'max': 2048, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_stitching'
    CATEGORY = 'WAS Suite/Image/Transform'

    def image_stitching(self, image_a, image_b, stitch='right', feathering=50):
        valid_stitches = ['top', 'left', 'bottom', 'right']
        if stitch not in valid_stitches:
            cstr(f"The stitch mode `{stitch}` is not valid. Valid sitch modes are {', '.join(valid_stitches)}").error.print()
        if feathering > 2048:
            cstr(f'The stitch feathering of `{feathering}` is too high. Please choose a value between `0` and `2048`').error.print()
        WTools = WAS_Tools_Class()
        stitched_image = WTools.stitch_image(tensor2pil(image_a), tensor2pil(image_b), stitch, feathering)
        return (pil2tensor(stitched_image),)
```