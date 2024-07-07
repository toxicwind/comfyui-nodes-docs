# Documentation
- Class name: MaskedBlur
- Category: inpaint
- Output node: False
- Repo Ref: https://github.com/Acly/comfyui-inpaint-nodes

The MaskedBlur node is designed to fill missing or unwanted parts of the image with sophisticated image restoration techniques. It applies selective ambiguity to the masked area so that they are seamlessly integrated with the surrounding image content. This node is particularly suitable for content-based image editing and restoration.

# Input types
## Required
- image
    - Enter the image that will be processed at the node. It is the main data source for image restoration operations, the quality of which directly affects the end result.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - Mask defines the area in which the image should be blurred and filled. It is a key parameter that determines which parts of the image will undergo the restoration process.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- blur
    - Fuzzy parameter control applies to the degree of fuzzy effect of the masked area. This is an important setting that affects the smoothness of the transition between the filled area and the rest of the image.
    - Comfy dtype: INT
    - Python dtype: int
- falloff
    - The decay parameter determines the rate at which the fuzzy effect diminishes at the edge of the masked area. It is used to create a more natural and gradual transition from the fuzzy to the unamplified area.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output_image
    - The output image is the result of the image restoration process. It contains the original image, in which the masked area is filled and blurred to match the surrounding area.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class MaskedBlur:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'mask': ('MASK',), 'blur': ('INT', {'default': 255, 'min': 3, 'max': 8191, 'step': 1}), 'falloff': ('INT', {'default': 0, 'min': 0, 'max': 8191, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    CATEGORY = 'inpaint'
    FUNCTION = 'fill'

    def fill(self, image: Tensor, mask: Tensor, blur: int, falloff: int):
        blur = make_odd(blur)
        falloff = min(make_odd(falloff), blur - 2)
        (image, mask) = to_torch(image, mask)
        original = image.clone()
        alpha = mask.floor()
        if falloff > 0:
            erosion = binary_erosion(alpha, falloff)
            alpha = alpha * gaussian_blur(erosion, falloff)
        alpha = alpha.repeat(1, 3, 1, 1)
        image = gaussian_blur(image, blur)
        image = original + (image - original) * alpha
        return (to_comfy(image),)
```