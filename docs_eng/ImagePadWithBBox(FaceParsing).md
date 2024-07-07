# Documentation
- Class name: ImagePadWithBBox
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

This node facilitates accurate filling of images with boundary boxes, ensures that images are properly framed and prepared for further analysis or processing.

# Input types
## Required
- bbox
    - The boundary box parameter is essential for determining the area of interest in the image. It determines from which coordinates the image will be cropped and filled accordingly.
    - Comfy dtype: BBOX
    - Python dtype: torch.Tensor
- width
    - The width parameters specify the desired width of the output image after filling, affecting the overall size and length ratio of the end product.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The height parameter defines the desired height for the output of the image after filling, which directly affects the final presentation and layout of the image.
    - Comfy dtype: INT
    - Python dtype: int
- image
    - The image parameter is the main input, which is operated and filled on the basis of the border box and size provided.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- output_image
    - The output image is the result of the filling process, showing an appropriate frame and size, ready for the subsequent processing phase.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImagePadWithBBox:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'bbox': ('BBOX', {}), 'width': ('INT', {}), 'height': ('INT', {}), 'image': ('IMAGE', {})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, bbox: Tensor, width: int, height: int, image: Tensor):
        image_permuted = image.permute(0, 3, 1, 2)
        bbox_int = bbox.int()
        l = bbox_int[0]
        t = bbox_int[1]
        r = bbox_int[2]
        b = bbox_int[3]
        cropped_image = functional.pad(image_permuted, [l, t, width - r, height - b])
        final = cropped_image.permute(0, 2, 3, 1)
        return (final,)
```