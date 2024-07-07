# Documentation
- Class name: PixelSort
- Category: postprocessing/Effects
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

PixelSort has introduced creative pixel sorting for the image by reorganizing the pixel data to enhance the visual impact of the image according to the specified criteria such as colour, saturation or saturation.

# Input types
## Required
- image
    - The image parameter is necessary because it provides the source data of the pixel sorting process to influence the appearance of the final output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - Mask parameters are essential to define the image area that should be affected by pixel sorting effects, thus controlling the extent of the transformation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- direction
    - The orientation parameters determine the axis direction of the pixel order, which can be either horizontal or vertical, with an overall pattern of effect.
    - Comfy dtype: COMBO['horizontal', 'vertical']
    - Python dtype: str
- sort_by
    - The sort_by parameter determines the criteria for the sorting of pixels, such as colour, saturation or clarity, and shapes the final visual result of the effect.
    - Comfy dtype: COMBO['hue', 'saturation', 'value']
    - Python dtype: str
- order
    - Order parameters specify the direction of the order, whether ascending (forward) or descending (forward) changes the order of pixels.
    - Comfy dtype: COMBO['forward', 'backward']
    - Python dtype: str
## Optional
- span_limit
    - The cross-limitation parameter details the sorting by controlling the number of crosses on each direction, affecting the particle size of the pixel sorting effect.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The output image is the result of a pixel sorting process that reflects the creative changes applied to the input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class PixelSort:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'mask': ('IMAGE',), 'direction': (['horizontal', 'vertical'],), 'span_limit': ('INT', {'default': None, 'min': 0, 'max': 100, 'step': 5}), 'sort_by': (['hue', 'saturation', 'value'],), 'order': (['forward', 'backward'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'sort_pixels'
    CATEGORY = 'postprocessing/Effects'

    def sort_pixels(self, image: torch.Tensor, mask: torch.Tensor, direction: str, span_limit: int, sort_by: str, order: str):
        horizontal_sort = direction == 'horizontal'
        reverse_sorting = order == 'backward'
        sort_by = sort_by[0].upper()
        span_limit = span_limit if span_limit > 0 else None
        batch_size = image.shape[0]
        result = torch.zeros_like(image)
        for b in range(batch_size):
            tensor_img = image[b].numpy()
            tensor_mask = mask[b].numpy()
            sorted_image = pixel_sort(tensor_img, tensor_mask, horizontal_sort, span_limit, sort_by, reverse_sorting)
            result[b] = torch.from_numpy(sorted_image)
        return (result,)
```