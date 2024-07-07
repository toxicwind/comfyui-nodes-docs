# Documentation
- Class name: WAS_Image_Blend_Mask
- Category: WAS Suite/Image
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Blend_Mask node is designed to mix two images seamlessly using the shades and mixing percentages provided. It uses the ability of image synthesis to create a visually consistent result, with one of the masked areas being replaced by the corresponding area of another image according to the specified mix level.

# Input types
## Required
- image_a
    - Image A is the main image that will be mixed with image B. It is a key input because it forms the base layer of the final synthetic image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- image_b
    - Image B is a secondary image whose masked area will be mixed to image A. It contributes to the final appearance by covering a particular part of the image on the base.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- mask
    - Mask is a binary image that defines which parts of image B should be visible in the final mix. It plays a key role in determining the area of image A to be replaced by image B.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
## Optional
- blend_percentage
    - The mixed percentage determines the extent to which the mask area of image B is mixed with image A. It is an optional parameter that allows fine-tuning of the mix effect.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- result_image
    - As a result, the image is the final output of the hybrid process, which combines image A with image B according to the mask and the percentage of the mixture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Blend_Mask:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image_a': ('IMAGE',), 'image_b': ('IMAGE',), 'mask': ('IMAGE',), 'blend_percentage': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_blend_mask'
    CATEGORY = 'WAS Suite/Image'

    def image_blend_mask(self, image_a, image_b, mask, blend_percentage):
        img_a = tensor2pil(image_a)
        img_b = tensor2pil(image_b)
        mask = ImageOps.invert(tensor2pil(mask).convert('L'))
        masked_img = Image.composite(img_a, img_b, mask.resize(img_a.size))
        blend_mask = Image.new(mode='L', size=img_a.size, color=round(blend_percentage * 255))
        blend_mask = ImageOps.invert(blend_mask)
        img_result = Image.composite(img_a, masked_img, blend_mask)
        del img_a, img_b, blend_mask, mask
        return (pil2tensor(img_result),)
```